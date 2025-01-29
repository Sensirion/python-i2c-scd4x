#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2025 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:     sensirion-driver-generator 1.1.2
# Product:       scd4x
# Model-Version: 2.0
#

import pytest
from sensirion_i2c_scd4x.device import Scd4xDevice


@pytest.fixture
def sensor(channel_provider):
    channel_provider.i2c_frequency = 100e3
    channel_provider.supply_voltage = 3.3
    with channel_provider:
        channel = channel_provider.get_channel(slave_address=0x62,
                                               crc_parameters=(8, 0x31, 0xff, 0x0))
        yield Scd4xDevice(channel)


def test_set_temperature_offset1(sensor):
    sensor.set_temperature_offset(4)


def test_get_temperature_offset1(sensor):
    a_temperature_offset = sensor.get_temperature_offset()
    print(f"a_temperature_offset: {a_temperature_offset}; "
          )


def test_set_temperature_offset_raw1(sensor):
    sensor.set_temperature_offset_raw(1498)


def test_get_temperature_offset_raw1(sensor):
    offset_temperature = sensor.get_temperature_offset_raw()
    print(f"offset_temperature: {offset_temperature}; "
          )


def test_set_sensor_altitude1(sensor):
    sensor.set_sensor_altitude(0)


def test_get_sensor_altitude1(sensor):
    sensor_altitude = sensor.get_sensor_altitude()
    print(f"sensor_altitude: {sensor_altitude}; "
          )


def test_get_serial_number1(sensor):
    serial_number = sensor.get_serial_number()
    print(f"serial_number: {serial_number}; "
          )


def test_perform_forced_recalibration1(sensor):
    frc_correction = sensor.perform_forced_recalibration(400)
    print(f"frc_correction: {frc_correction}; "
          )


def test_set_automatic_self_calibration_enabled1(sensor):
    sensor.set_automatic_self_calibration_enabled(1)


def test_get_automatic_self_calibration_enabled1(sensor):
    asc_enabled = sensor.get_automatic_self_calibration_enabled()
    print(f"asc_enabled: {asc_enabled}; "
          )


def test_set_automatic_self_calibration_target1(sensor):
    sensor.set_automatic_self_calibration_target(400)


def test_get_automatic_self_calibration_target1(sensor):
    asc_target = sensor.get_automatic_self_calibration_target()
    print(f"asc_target: {asc_target}; "
          )


def test_persist_settings1(sensor):
    sensor.persist_settings()


def test_perform_self_test1(sensor):
    sensor_status = sensor.perform_self_test()
    print(f"sensor_status: {sensor_status}; "
          )


def test_perform_factory_reset1(sensor):
    sensor.perform_factory_reset()


def test_reinit1(sensor):
    sensor.reinit()


def test_get_sensor_variant_raw1(sensor):
    sensor_variant = sensor.get_sensor_variant_raw()
    print(f"sensor_variant: {sensor_variant}; "
          )


def test_get_sensor_variant1(sensor):
    a_sensor_variant = sensor.get_sensor_variant()
    print(f"a_sensor_variant: {a_sensor_variant}; "
          )


def test_set_automatic_self_calibration_initial_period1(sensor):
    sensor.set_automatic_self_calibration_initial_period(44)


def test_get_automatic_self_calibration_initial_period1(sensor):
    asc_initial_period = sensor.get_automatic_self_calibration_initial_period()
    print(f"asc_initial_period: {asc_initial_period}; "
          )


def test_set_automatic_self_calibration_standard_period1(sensor):
    sensor.set_automatic_self_calibration_standard_period(156)


def test_get_automatic_self_calibration_standard_period1(sensor):
    asc_standard_period = sensor.get_automatic_self_calibration_standard_period()
    print(f"asc_standard_period: {asc_standard_period}; "
          )


def test_measure_and_read_single_shot1(sensor):
    (a_co2_concentration, a_temperature, a_relative_humidity
     ) = sensor.measure_and_read_single_shot()
    print(f"a_co2_concentration: {a_co2_concentration}; "
          f"a_temperature: {a_temperature}; "
          f"a_relative_humidity: {a_relative_humidity}; "
          )


def test_measure_single_shot_rht_only1(sensor):
    sensor.measure_single_shot_rht_only()


def test_measure_single_shot1(sensor):
    sensor.measure_single_shot()


def test_start_periodic_measurement1(sensor):
    sensor.start_periodic_measurement()
    (a_co2_concentration, a_temperature, a_relative_humidity
     ) = sensor.read_measurement()
    print(f"a_co2_concentration: {a_co2_concentration}; "
          f"a_temperature: {a_temperature}; "
          f"a_relative_humidity: {a_relative_humidity}; "
          )
    (co2_concentration, temperature, relative_humidity
     ) = sensor.read_measurement_raw()
    print(f"co2_concentration: {co2_concentration}; "
          f"temperature: {temperature}; "
          f"relative_humidity: {relative_humidity}; "
          )
    sensor.set_ambient_pressure(101300)
    a_ambient_pressure = sensor.get_ambient_pressure()
    print(f"a_ambient_pressure: {a_ambient_pressure}; "
          )
    sensor.set_ambient_pressure_raw(1013)
    ambient_pressure = sensor.get_ambient_pressure_raw()
    print(f"ambient_pressure: {ambient_pressure}; "
          )
    arg_0 = sensor.get_data_ready_status()
    print(f"arg_0: {arg_0}; "
          )
    data_ready_status = sensor.get_data_ready_status_raw()
    print(f"data_ready_status: {data_ready_status}; "
          )
    sensor.stop_periodic_measurement()


def test_start_low_power_periodic_measurement1(sensor):
    sensor.start_low_power_periodic_measurement()
    (a_co2_concentration, a_temperature, a_relative_humidity
     ) = sensor.read_measurement()
    print(f"a_co2_concentration: {a_co2_concentration}; "
          f"a_temperature: {a_temperature}; "
          f"a_relative_humidity: {a_relative_humidity}; "
          )
    (co2_concentration, temperature, relative_humidity
     ) = sensor.read_measurement_raw()
    print(f"co2_concentration: {co2_concentration}; "
          f"temperature: {temperature}; "
          f"relative_humidity: {relative_humidity}; "
          )
    sensor.set_ambient_pressure(101300)
    a_ambient_pressure = sensor.get_ambient_pressure()
    print(f"a_ambient_pressure: {a_ambient_pressure}; "
          )
    sensor.set_ambient_pressure_raw(1013)
    ambient_pressure = sensor.get_ambient_pressure_raw()
    print(f"ambient_pressure: {ambient_pressure}; "
          )
    arg_0 = sensor.get_data_ready_status()
    print(f"arg_0: {arg_0}; "
          )
    data_ready_status = sensor.get_data_ready_status_raw()
    print(f"data_ready_status: {data_ready_status}; "
          )
    sensor.stop_periodic_measurement()

