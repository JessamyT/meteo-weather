"""
This file registers the model with the Python SDK.
"""

from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .meteo_PM import meteo_PM

Registry.register_resource_creator(Sensor.SUBTYPE, meteo_PM.MODEL, ResourceCreatorRegistration(meteo_PM.new, meteo_PM.validate))
