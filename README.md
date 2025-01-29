# Python I2C Driver for Sensirion SCD4X

This repository contains the Python driver to communicate with a Sensirion sensor of the SCD4X family over I2C.

<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-scd4x/master/images/SCD41.png"
    width="300px" alt="SCD4X picture">


Click [here](https://sensirion.com/products/catalog/SEK-SCD41) to learn more about the Sensirion SCD4X sensor family.


Not all sensors of this driver family support all measurements.
In case a measurement is not supported by all sensors, the products that
support it are listed in the API description.



## Supported sensor types

| Sensor name   | I²C Addresses  |
| ------------- | -------------- |
|[SCD40](https://sensirion.com/products/catalog/SCD40)| **0x62**|
|[SCD41](https://sensirion.com/products/catalog/SCD41)| **0x62**|

The following instructions and examples use a *SCD41*.



## Connect the sensor

You can connect your sensor over a [SEK-SensorBridge](https://developer.sensirion.com/sensirion-products/sek-sensorbridge/).
For special setups you find the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-scd4x/master/images/SCD41_pinout.png"
     width="300px" alt="sensor wiring picture">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | yellow | SCL | I2C: Serial clock input |
| 2 | black | GND | Ground |
| 3 | red | VDD | Supply Voltage | 2.4V to 5.5V
| 4 | green | SDA | I2C: Serial data input / output |


</p>
</details>


## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-i2c-scd4x) for an API description and a
[quickstart](https://sensirion.github.io/python-i2c-scd4x/execute-measurements.html) example.


## Contributing

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

In addition, we check the formatting of files with
[`editorconfig-checker`](https://editorconfig-checker.github.io/):

```bash
pip install editorconfig-checker==2.0.3   # Install requirements
editorconfig-checker                      # Run check
```

## License

See [LICENSE](LICENSE).