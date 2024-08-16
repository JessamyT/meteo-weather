# meteo_PM modular component

This module implements the [Viam sensor API](https://github.com/rdk/sensor-api) in a jessamy:weather:meteo_PM model.
With this model, you can gather [Open-Meteo](https://open-meteo.com/en/docs/air-quality-api) PM2.5 and PM10 air quality data from anywhere in the world, at the coordinates you specify.

## Build and Run

To use this module, follow these instructions to [add a module from the Viam Registry](https://docs.viam.com/registry/configure/#add-a-modular-resource-from-the-viam-registry) and select the `rdk:sensor:jessamy:weather:meteo_PM` model from the [`jessamy:weather:meteo_PM` module](https://app.viam.com/module/rdk/jessamy:weather:_PM).

## Configure your meteo_PM sensor

Navigate to the **CONFIGURE** tab of your robot’s page in [the Viam app](https://app.viam.com/).
Add a component.
Select the `sensor` type, then select the `jessamy:weather:meteo_PM` model.
Enter a name for your sensor and click **Create**.

On the new component panel, copy and paste the following attribute template into your sensor’s **Attributes** box:

```json
{
  "latitude": <float>,
  "longitude": <float>
}
```

### Attributes

The following attributes are available for `rdk:sensor:jessamy:weather:meteo_PM` sensors:

| Name | Type | Inclusion | Description |
| ---- | ---- | --------- | ----------- |
| `latitude` | float | Optional |  Latitude at which to get the readings. Defaults to 45. |
| `longitude` | float | Optional |  Longitude at which to get the readings. Defaults to -121. |

### Example Configuration

```json
{
  "latitude": -40.6,
  "longitude": 93.125
}
```
