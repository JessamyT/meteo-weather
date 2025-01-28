# `meteo_PM` modular component

This module implements the [Viam sensor API](https://docs.viam.com/dev/reference/apis/components/sensor/) in a `jessamy:weather:meteo_PM` model.
With this model, you can gather [Open-Meteo](https://open-meteo.com/en/docs/air-quality-api) PM2.5 and PM10 air quality data from anywhere in the world, at the coordinates you specify.

## Configure your `meteo_PM` sensor

Navigate to the **CONFIGURE** tab of your machine’s page in the [Viam app](https://app.viam.com/).
Click the **+** button, select **Component**, then select the `sensor / weather:meteo_PM` model provided by the [`weather` module](https://app.viam.com/module/rdk/jessamy/weather).
Click **Add module**, enter a name for your sensor, and click **Create**.

On the new component panel, copy and paste the following attribute template into your sensor’s **Attributes** box:

```json
{
  "latitude": <float>,
  "longitude": <float>
}
```

### Attributes

The following attributes are available for `rdk:sensor:jessamy:weather:meteo_PM` sensors:

| Name        | Type  | Inclusion | Description                            |
| ----------- | ----- | --------- | -------------------------------------- |
| `latitude`  | float | Optional  | Latitude at which to get the readings  |
| `longitude` | float | Optional  | Longitude at which to get the readings |

### Example Configuration

```json
{
  "latitude": -40.6,
  "longitude": 93.125
}
```
