# meteo_PM.py
from typing import ClassVar, Mapping, Any, Optional
from typing_extensions import Self

from viam.utils import SensorReading, struct_to_dict
from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily
from viam.components.sensor import Sensor
from viam.logging import getLogger

import openmeteo_requests
import requests_cache
from retry_requests import retry

LOGGER = getLogger(__name__)


class meteo_PM(Sensor, Reconfigurable):

    """
    Sensor represents a sensing device that can provide measurement readings.
    """

    MODEL: ClassVar[Model] = Model(
      ModelFamily("jessamy", "weather"), "meteo_PM")

    # Class parameters
    latitude: float  # Latitude at which to get data
    longitude: float  # Longitude at which to get data

    # Constructor
    @classmethod
    def new(
      cls, config: ComponentConfig,
      dependencies: Mapping[ResourceName, ResourceBase]
      ) -> Self:
        my_class = cls(config.name)
        my_class.reconfigure(config, dependencies)
        return my_class

    # Validates JSON Configuration
    @classmethod
    def validate(cls, config: ComponentConfig):
        fields = config.attributes.fields
        # Check that configured fields are floats
        if "latitude" in fields:
            if not fields["latitude"].HasField("number_value"):
                raise Exception("Latitude must be a float.")

        if "longitude" in fields:
            if not fields["longitude"].HasField("number_value"):
                raise Exception("Longitude must be a float.")
        return

    # Handles attribute reconfiguration
    def reconfigure(
      self, config: ComponentConfig,
      dependencies: Mapping[ResourceName, ResourceBase]
      ):
        attrs = struct_to_dict(config.attributes)

        self.latitude = float(attrs.get("latitude", 45))
        LOGGER.debug("Using latitude: " + str(self.latitude))

        self.longitude = float(attrs.get("longitude", -121))
        LOGGER.debug("Using longitude: " + str(self.longitude))

        return

    async def get_readings(
        self, *, extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, SensorReading]:

        # Set up the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession(
          '.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        openmeteo = openmeteo_requests.Client(session=retry_session)

        # The order of variables in hourly or daily is
        # important to assign them correctly below
        url = "https://air-quality-api.open-meteo.com/v1/air-quality"
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "current": ["pm10", "pm2_5"],
            "timezone": "America/Los_Angeles"
        }
        responses = openmeteo.weather_api(url, params=params)

        # Process location
        response = responses[0]

        # Current values. The order of variables needs
        # to be the same as requested.
        current = response.Current()
        current_pm10 = current.Variables(0).Value()
        current_pm2_5 = current.Variables(1).Value()

        LOGGER.info(current_pm2_5)

        # Return a dictionary of the readings
        return {
            "pm2_5": current_pm2_5,
            "pm10": current_pm10
        }
