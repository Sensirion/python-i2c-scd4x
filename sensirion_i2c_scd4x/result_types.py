#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2025 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:     sensirion-driver-generator 1.1.2
# Product:       scd4x
# Model-Version: 1.0
#
"""
The signal classes specify transformations of the raw sensor signals into a meaningful units.
The generated signal types are used by the driver class and not intended for direct use.
"""

from sensirion_driver_support_types.signals import AbstractSignal


class SignalTemperature(AbstractSignal):
    """Temperature in °C"""

    def __init__(self, raw_temperature):
        self._temperature = -45.0 + ((175.0 * raw_temperature) / 65535.0)

    @property
    def value(self):
        return self._temperature

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalRelativeHumidity(AbstractSignal):
    """Relative humidity in %RH"""

    def __init__(self, raw_relative_humidity):
        self._relative_humidity = (100.0 * raw_relative_humidity) / 65535.0

    @property
    def value(self):
        return self._relative_humidity

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalCo2Concentration(AbstractSignal):
    """CO₂ concentration in ppm"""

    def __init__(self, raw_co2_concentration):
        self._co2_concentration = raw_co2_concentration

    @property
    def value(self):
        return self._co2_concentration

    def __str__(self):
        return '{0}'.format(self.value)


class SignalTemperatureOffset(AbstractSignal):
    """Temperature in °C"""

    def __init__(self, raw_temperature_offset):
        self._temperature_offset = (175 * raw_temperature_offset) / 65535.0

    @property
    def value(self):
        return self._temperature_offset

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalAmbientPressure(AbstractSignal):
    """Pressure in Pa"""

    def __init__(self, raw_ambient_pressure):
        self._ambient_pressure = raw_ambient_pressure * 100

    @property
    def value(self):
        return self._ambient_pressure

    def __str__(self):
        return '{0}'.format(self.value)

