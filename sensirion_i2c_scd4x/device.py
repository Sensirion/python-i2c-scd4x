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
The class Scd4xDeviceBase implements the low level interface of the sensor.
The class Scd4xDevice extends the Scd4xDeviceBase. It provides additional functions to ease the use of the
sensor.
"""

import time
from sensirion_driver_adapters.transfer import execute_transfer
from sensirion_driver_support_types.mixin_access import MixinAccess
from sensirion_i2c_scd4x.commands import (GetAmbientPressureRaw, GetAutomaticSelfCalibrationEnabled,
                                          GetAutomaticSelfCalibrationInitialPeriod,
                                          GetAutomaticSelfCalibrationStandardPeriod, GetAutomaticSelfCalibrationTarget,
                                          GetDataReadyStatusRaw, GetSensorAltitude, GetSensorVariantRaw,
                                          GetSerialNumber, GetTemperatureOffsetRaw, MeasureSingleShot,
                                          MeasureSingleShotRhtOnly, PerformFactoryReset, PerformForcedRecalibration,
                                          PerformSelfTest, PersistSettings, PowerDown, ReadMeasurementRaw, Reinit,
                                          SensorVariant, SetAmbientPressureRaw, SetAutomaticSelfCalibrationEnabled,
                                          SetAutomaticSelfCalibrationInitialPeriod,
                                          SetAutomaticSelfCalibrationStandardPeriod, SetAutomaticSelfCalibrationTarget,
                                          SetSensorAltitude, SetTemperatureOffsetRaw, StartLowPowerPeriodicMeasurement,
                                          StartPeriodicMeasurement, StopPeriodicMeasurement, WakeUp)

from sensirion_i2c_scd4x.result_types import (SignalAmbientPressure, SignalCo2Concentration, SignalRelativeHumidity,
                                              SignalTemperature, SignalTemperatureOffset)


class Scd4xDeviceBase:
    """Low level API implementation of SCD4X"""

    def __init__(self, channel):
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    def start_periodic_measurement(self):
        """
        Starts the periodic measurement mode.
        The signal update interval is 5 seconds.

        .. note::
            This command is only available in idle mode.
        """
        transfer = StartPeriodicMeasurement()
        return execute_transfer(self._channel, transfer)

    def read_measurement_raw(self):
        """
        Reads the sensor output. The measurement data can only be read out once per signal update interval as the buffer
        is emptied upon read-out. If no data is available in the buffer, the sensor returns a NACK. To avoid a NACK response, the
        get_data_ready_status can be issued to check data status. The I2C master can abort the read transfer with a NACK
        followed by a STOP condition after any data byte if the user is not interested in subsequent data.

        :return co2_concentration:
            CO₂ concentration in ppm
        :return temperature:
            Convert to degrees celsius by (175 * value / 65535) - 45
        :return relative_humidity:
            Convert to relative humidity in % by (100 * value / 65535)
        """
        transfer = ReadMeasurementRaw()
        return execute_transfer(self._channel, transfer)

    def stop_periodic_measurement(self):
        """
        Command returns a sensor running in periodic measurement mode or low power periodic measurement mode
        back to the idle state, e.g. to then allow changing the sensor configuration or to save power.
        """
        transfer = StopPeriodicMeasurement()
        return execute_transfer(self._channel, transfer)

    def set_temperature_offset_raw(self, offset_temperature):
        """
        Setting the temperature offset of the SCD4x inside the customer device allows the user to optimize the RH and T
        output signal. The temperature offset can depend on several factors such as the SCD4x measurement mode, self-heating of
        close components, the ambient temperature and air flow. Thus, the SCD4x temperature offset should be determined after
        integration into the final device and under its typical operating conditions (including the operation mode to be used in the
        application) in thermal equilibrium. By default, the temperature offset is set to 4 °C. To save the setting to the EEPROM, the
        persist_settings command may be issued. Equation (1) details how the characteristic temperature offset
        can be calculated using the current temperature output of the sensor (TSCD4x), a reference temperature value (TReference),
        and the previous temperature offset (Toffset_pervious) obtained using the get_temperature_offset_raw command:

        Toffset_actual = TSCD4x - TReference + Toffset_pervious.

        Recommended temperature offset values are between 0 °C and 20 °C.
        The temperature offset does not impact the accuracy of the CO2 output.

        :param offset_temperature:
            Temperature offset. Convert Toffset in °C to value by: (Toffset * 65535 / 175)

        .. note::
            This command is only available in idle mode.

        :Example:
            .. code-block:: python

                sensor.set_temperature_offset_raw(1498)

        """
        transfer = SetTemperatureOffsetRaw(offset_temperature)
        return execute_transfer(self._channel, transfer)

    def get_temperature_offset_raw(self):
        """
        Get the raw temperature compensation offset used by the sensor.

        :return offset_temperature:
            Convert to °C by (175 * value / 65535)

        .. note::
            This command is only available in idle mode.
        """
        transfer = GetTemperatureOffsetRaw()
        return execute_transfer(self._channel, transfer)[0]

    def set_sensor_altitude(self, sensor_altitude):
        """
        Typically, the sensor altitude is set once after device installation.
        To save the setting to the EEPROM, the persist_settings command must be issued.
        The default sensor altitude value is set to 0 meters above sea level.
        Note that setting a sensor altitude to the sensor overrides any pressure
        compensation based on a previously set ambient pressure.

        :param sensor_altitude:
            Sensor altitude in meters above sea level. Valid input values are between 0 - 3000 m.

        .. note::
            This command is only available in idle mode.

        :Example:
            .. code-block:: python

                sensor.set_sensor_altitude(0)

        """
        transfer = SetSensorAltitude(sensor_altitude)
        return execute_transfer(self._channel, transfer)

    def get_sensor_altitude(self):
        """
        Get the sensor altitude used by the sensor.

        :return sensor_altitude:
            Sensor altitude used by the sensor in meters above sea level.

        .. note::
            This command is only available in idle mode.
        """
        transfer = GetSensorAltitude()
        return execute_transfer(self._channel, transfer)[0]

    def set_ambient_pressure_raw(self, ambient_pressure):
        """
        The set_ambient_pressure command can be sent during periodic measurements to enable continuous pressure
        compensation. Note that setting an ambient pressure overrides any pressure compensation based on a previously set sensor
        altitude. Use of this command is highly recommended for applications experiencing significant ambient pressure changes to
        ensure sensor accuracy. Valid input values are between 70000 - 120000 Pa. The default value is 101300 Pa.

        :param ambient_pressure:
            Convert ambient_pressure in hPa to Pa by ambient_pressure / 100.

        .. note::
            Available during measurements.

        :Example:
            .. code-block:: python

                sensor.set_ambient_pressure_raw(1013)

        """
        transfer = SetAmbientPressureRaw(ambient_pressure)
        return execute_transfer(self._channel, transfer)

    def get_ambient_pressure_raw(self):
        """
        Get the ambient pressure around the sensor.

        :return ambient_pressure:
            Convert to Pa by value = ambient_pressure * 100.
        """
        transfer = GetAmbientPressureRaw()
        return execute_transfer(self._channel, transfer)[0]

    def perform_forced_recalibration(self, target_CO2_concentration):
        """
        To successfully conduct an accurate FRC, the following steps need to be carried out:

        1. Operate the SCD4x in the operation mode later used for normal sensor operation (e.g. periodic measurement)
        for at least 3 minutes in an environment with a homogenous and constant CO2 concentration.
        The sensor must be operated at the voltage desired for the application when performing the FRC sequence.
        2. Issue the stop_periodic_measurement command.
        3. Issue the perform_forced_recalibration command.

        A return value of 0xffff indicates that the FRC has failed because the sensor was not operated before sending the command.

        :param target_co2_concentration:
            Target CO₂ concentration in ppm CO₂.

        :return frc_correction:
            Convert to FRC correction in ppm CO₂ by frc_correction - 0x8000.
            A return value of 0xFFFF indicates that the FRC has failed because the sensor was not operated before sending the command.

        .. note::
            This command is only available in idle mode.
        """
        transfer = PerformForcedRecalibration(target_CO2_concentration)
        return execute_transfer(self._channel, transfer)[0]

    def set_automatic_self_calibration_enabled(self, asc_enabled):
        """
        Sets the current state (enabled / disabled) of the ASC. By default, ASC is enabled. To save the setting to the
        EEPROM, the persist_settings command must be issued.
        The ASC enables excellent long-term stability of SCD4x without the need for regular user intervention. The algorithm leverages
        the sensor's measurement history and the assumption of exposure of the sensor to a known minimum background CO₂
        concentration at least once over a period of cumulative operation. By default, the ASC algorithm assumes that the sensor is
        exposed to outdoor fresh air at 400 ppm CO₂ concentration at least once per week of accumulated operation using one of the
        following measurement modes for at least 4 hours without interruption at a time: periodic measurement mode, low
        power periodic measurement mode or single shot mode with a measurement interval of 5 minutes (SCD41 only).

        :param asc_enabled:
            1 enables ASC, 0 disables ASC.

        .. note::
            This command is only available in idle mode.

        :Example:
            .. code-block:: python

                sensor.set_automatic_self_calibration_enabled(1)

        """
        transfer = SetAutomaticSelfCalibrationEnabled(asc_enabled)
        return execute_transfer(self._channel, transfer)

    def get_automatic_self_calibration_enabled(self):
        """
        Check if automatic self calibration (ASC) is enabled.

        :return asc_enabled:
            1 if ASC is enabled, 0 if ASC is disabled.

        .. note::
            This command is only available in idle mode.
        """
        transfer = GetAutomaticSelfCalibrationEnabled()
        return execute_transfer(self._channel, transfer)[0]

    def set_automatic_self_calibration_target(self, asc_target):
        """
        Sets the value of the ASC baseline target, i.e. the CO₂ concentration in ppm which the ASC algorithm will assume
        as lower-bound background to which the SCD4x is exposed to regularly within one ASC period of operation. To save the setting
        to the EEPROM, the persist_settings command must be issued subsequently. The factory default value is 400 ppm.

        :param asc_target:
            ASC baseline value in ppm CO₂

        .. note::
            This command is only available in idle mode.

        :Example:
            .. code-block:: python

                sensor.set_automatic_self_calibration_target(400)

        """
        transfer = SetAutomaticSelfCalibrationTarget(asc_target)
        return execute_transfer(self._channel, transfer)

    def get_automatic_self_calibration_target(self):
        """
        Reads out the ASC baseline target concentration parameter.

        :return asc_target:
            ASC baseline target concentration parameter in ppm CO₂.

        .. note::
            This command is only available in idle mode.
        """
        transfer = GetAutomaticSelfCalibrationTarget()
        return execute_transfer(self._channel, transfer)[0]

    def start_low_power_periodic_measurement(self):
        """
        To enable use-cases with a constrained power budget, the SCD4x features a low power periodic measurement mode with a
        signal update interval of approximately 30 seconds. The low power periodic measurement mode is initiated using the
        start_low_power_periodic_measurement command and read-out in a similar manner as the periodic measurement mode using
        the read_measurement command.
        To periodically check whether a new measurement result is available for read out, the get_data_ready_status command
        can be used to synchronize to the sensor's internal measurement interval as an alternative to relying on the ACK/NACK
        status of the read_measurement_command.
        """
        transfer = StartLowPowerPeriodicMeasurement()
        return execute_transfer(self._channel, transfer)

    def get_data_ready_status_raw(self):
        """
        Polls the sensor for whether data from a periodic or single shot measurement is ready to be read out.

        :return data_ready_status:
            If one or more of the 11 least significant bits are 1, then the data is ready.
        """
        transfer = GetDataReadyStatusRaw()
        return execute_transfer(self._channel, transfer)[0]

    def persist_settings(self):
        """
        Configuration settings such as the temperature offset, sensor altitude and the ASC enabled/disabled parameters
        are by default stored in the volatile memory (RAM) only. The persist_settings command stores the current configuration in the
        EEPROM of the SCD4x, ensuring the current settings persist after power-cycling. To avoid unnecessary wear of the EEPROM,
        the persist_settings command should only be sent following configuration changes whose persistence is required. The EEPROM
        is guaranteed to withstand at least 2000 write cycles. Note that field calibration history (i.e. FRC and ASC) is
        automatically stored in a separate EEPROM dimensioned for the specified sensor lifetime when operated continuously in either
        periodic measurement mode, low power periodic measurement mode or single shot mode with 5 minute measurement interval (SCD41 only).

        .. note::
            This command is only available in idle mode.
        """
        transfer = PersistSettings()
        return execute_transfer(self._channel, transfer)

    def get_serial_number(self):
        """
        Reading out the serial number can be used to identify the chip and to verify the presence of the sensor.
        The get_serial_number command returns 3 words, and every word is followed by an 8-bit CRC checksum. Together, the 3 words
        constitute a unique serial number with a length of 48 bits (in big endian format).

        :return serial_number:
            48-bit unique serial number of the sensor.

        .. note::
            This command is only available in idle mode.
        """
        transfer = GetSerialNumber()
        return execute_transfer(self._channel, transfer)[0]

    def perform_self_test(self):
        """
        Can be used as an end-of-line test to check the sensor functionality.

        :return sensor_status:
            If sensor status is equal to 0, no malfunction has been detected.

        .. note::
            This command is only available in idle mode.
        """
        transfer = PerformSelfTest()
        return execute_transfer(self._channel, transfer)[0]

    def perform_factory_reset(self):
        """
        The perform_factory_reset command resets all configuration settings stored in the EEPROM and erases the
        FRC and ASC algorithm history.

        .. note::
            This command is only available in idle mode.
        """
        transfer = PerformFactoryReset()
        return execute_transfer(self._channel, transfer)

    def reinit(self):
        """
        The reinit command reinitialize the sensor by reloading user settings from EEPROM. The sensor must be in the
        idle state before sending the reinit command. If the reinit command does not trigger the desired re-initialization,
        a power-cycle should be applied to the SCD4x.

        .. note::
            This command is only available in idle mode.
        """
        transfer = Reinit()
        return execute_transfer(self._channel, transfer)

    def get_sensor_variant_raw(self):
        """
        Reads out the SCD4x sensor variant.

        :return sensor_variant:
            Bits[15…12] = 0000 → SCD40
            Bits[15…12] = 0001 → SCD41

        .. note::
            This command is only available in idle mode.
        """
        transfer = GetSensorVariantRaw()
        return execute_transfer(self._channel, transfer)[0]

    def measure_single_shot(self):
        """
        The sensor output is read out by using the read_measurement command.
        The fastest possible sampling interval for single shot measurements is 5 seconds.
        The ASC is enabled by default in single shot operation and optimized for single shot measurements performed every 5 minutes.
        For more details about single shot measurements and optimization of power consumption please refer to the datasheet.

        .. note::
            This command is only available for SCD41.
        """
        transfer = MeasureSingleShot()
        return execute_transfer(self._channel, transfer)

    def measure_single_shot_rht_only(self):
        """
        For more details about single shot measurements and optimization of power consumption please refer to the datasheet.

        .. note::
            This command is only available for SCD41.
        """
        transfer = MeasureSingleShotRhtOnly()
        return execute_transfer(self._channel, transfer)

    def power_down(self):
        """
        Put the sensor from idle to sleep to reduce power consumption. Can be used to power down when operating the
        sensor in power-cycled single shot mode.

        .. note::
            This command is only available in idle mode. Only for SCD41.
        """
        transfer = PowerDown()
        return execute_transfer(self._channel, transfer)

    def wake_up(self):
        """
        Wake up the sensor from sleep mode into idle mode. Note that the SCD4x does not acknowledge the wake_up
        command. The sensor's idle state after wake up can be verified by reading out the serial number.

        .. note::
            This command is only available for SCD41.
        """
        transfer = WakeUp()
        return execute_transfer(self._channel, transfer)

    def set_automatic_self_calibration_initial_period(self, asc_initial_period):
        """
        Sets the duration of the initial period for ASC correction (in hours). By default, the initial period for ASC correction
        is 44 hours. Allowed values are integer multiples of 4 hours. A value of 0 results in an immediate correction.
        To save the setting to the EEPROM, the persist_settings command must be issued.

        For single shot operation, this parameter always assumes a measurement interval of 5 minutes, counting the number of
        single shots to calculate elapsed time. If single shot measurements are taken more / less frequently than once every 5 minutes,
        this parameter must be scaled accordingly to achieve the intended period in hours (e.g. for a 10-minute measurement interval,
        the scaled parameter value is obtained by multiplying the intended period in hours by 0.5).

        :param asc_initial_period:
            ASC initial period in hours

        .. note::
            This command is available for SCD41 and only in idle mode.

        :Example:
            .. code-block:: python

                sensor.set_automatic_self_calibration_initial_period(44)

        """
        transfer = SetAutomaticSelfCalibrationInitialPeriod(asc_initial_period)
        return execute_transfer(self._channel, transfer)

    def get_automatic_self_calibration_initial_period(self):
        """
        Read out the initial period for ASC correction

        :return asc_initial_period:
            ASC initial period in hours

        .. note::
            This command is only available for SCD41 and only in idle mode.
        """
        transfer = GetAutomaticSelfCalibrationInitialPeriod()
        return execute_transfer(self._channel, transfer)[0]

    def set_automatic_self_calibration_standard_period(self, asc_standard_period):
        """
        Sets the standard period for ASC correction (in hours). By default, the standard period for ASC correction is 156
        hours. Allowed values are integer multiples of 4 hours. Note: a value of 0 results in an immediate correction. To save the
        setting to the EEPROM, the persist_settings (see Section 3.10.1) command must be issued.

        For single shot operation, this parameter always assumes a measurement interval of 5 minutes, counting the number of
        single shots to calculate elapsed time. If single shot measurements are taken more / less frequently than once every 5 minutes,
        this parameter must be scaled accordingly to achieve the intended period in hours (e.g. for a 10-minute measurement interval,
        the scaled parameter value is obtained by multiplying the intended period in hours by 0.5).

        :param asc_standard_period:
            ASC standard period in hours

        .. note::
            This command is only available for SCD41 and only in idle mode.

        :Example:
            .. code-block:: python

                sensor.set_automatic_self_calibration_standard_period(156)

        """
        transfer = SetAutomaticSelfCalibrationStandardPeriod(asc_standard_period)
        return execute_transfer(self._channel, transfer)

    def get_automatic_self_calibration_standard_period(self):
        """
        Get the standard period for ASC correction.

        :return asc_standard_period:
            ASC standard period in hours

        .. note::
            This command is only available for SCD41 and only in idle mode.
        """
        transfer = GetAutomaticSelfCalibrationStandardPeriod()
        return execute_transfer(self._channel, transfer)[0]


class Scd4xDevice(Scd4xDeviceBase):
    """Driver class implementation of SCD4X"""

    #: Access to base class
    scd4x = MixinAccess()

    def __init__(self, channel):
        super().__init__(channel)

    def read_measurement(self):
        """
        Reads the sensor output. The measurement data can only be read out once per signal update interval as the buffer
        is emptied upon read-out. If no data is available in the buffer, the sensor returns a NACK. To avoid a NACK response, the
        get_data_ready_status can be issued to check data status. The I2C master can abort the read transfer with a NACK
        followed by a STOP condition after any data byte if the user is not interested in subsequent data.

        :return a_co2_concentration:
            CO₂ concentration in ppm
        :return a_temperature:
            Temperature in °C
        :return a_relative_humidity:
            Relative humidity in %RH
        """
        (raw_co2_concentration, raw_temperature, raw_relative_humidity
         ) = self.scd4x.read_measurement_raw()
        return (SignalCo2Concentration(raw_co2_concentration), SignalTemperature(raw_temperature),
                SignalRelativeHumidity(raw_relative_humidity))

    def set_temperature_offset(self, temperature_offset):
        """
        Setting the temperature offset of the SCD4x inside the customer device allows the user to optimize the RH and T
        output signal. The temperature offset can depend on several factors such as the SCD4x measurement mode, self-heating of
        close components, the ambient temperature and air flow. Thus, the SCD4x temperature offset should be determined after
        integration into the final device and under its typical operating conditions (including the operation mode to be used in the
        application) in thermal equilibrium. By default, the temperature offset is set to 4 °C. To save the setting to the EEPROM, the
        persist_settings command may be issued. Equation (1) details how the characteristic temperature offset
        can be calculated using the current temperature output of the sensor (TSCD4x), a reference temperature value (TReference),
        and the previous temperature offset (Toffset_pervious) obtained using the get_temperature_offset_raw command:

        Toffset_actual = TSCD4x - TReference + Toffset_pervious.

        Recommended temperature offset values are between 0 °C and 20 °C.
        The temperature offset does not impact the accuracy of the CO2 output.

        :param temperature_offset:
            Temperature offset value in °C

        .. note::
            This command is only available in idle mode.
        """
        raw_temperature_offset = round((temperature_offset * 65535.0) / 175.0)
        self.scd4x.set_temperature_offset_raw(raw_temperature_offset)

    def get_temperature_offset(self):
        """
        Get the temperature compensation offset used by the sensor in °C.

        :return a_temperature_offset:
            Temperature in °C

        .. note::
            This command is only available in idle mode.
        """
        raw_temperature_offset = self.scd4x.get_temperature_offset_raw()
        return SignalTemperatureOffset(raw_temperature_offset)

    def set_ambient_pressure(self, ambient_pressure):
        """
        The set_ambient_pressure command can be sent during periodic measurements to enable continuous pressure
        compensation. Note that setting an ambient pressure overrides any pressure compensation based on a previously set sensor
        altitude. Use of this command is highly recommended for applications experiencing significant ambient pressure changes to
        ensure sensor accuracy. Valid input values are between 70000 - 120000 Pa. The default value is 101300 Pa.

        :param ambient_pressure:
            Ambient pressure around the sensor in Pa
        """
        raw_ambient_pressure = round(ambient_pressure / 100.0)
        self.scd4x.set_ambient_pressure_raw(raw_ambient_pressure)

    def get_ambient_pressure(self):
        """
        Get the ambient pressure around the sensor.

        :return a_ambient_pressure:
            Pressure in Pa
        """
        raw_ambient_pressure = self.scd4x.get_ambient_pressure_raw()
        return SignalAmbientPressure(raw_ambient_pressure)

    def get_data_ready_status(self):
        """
        Polls the sensor for whether data from a periodic or single shot measurement is ready to be read out.

        :return arg_0:

        """
        data_ready_status = self.scd4x.get_data_ready_status_raw()
        return (data_ready_status & 2047) != 0

    def get_sensor_variant(self):
        """
        Reads out the SCD4x sensor variant.

        :return a_sensor_variant:


        .. note::
            This command is only available in idle mode.
        """
        raw_sensor_variant = self.scd4x.get_sensor_variant_raw()
        variant = raw_sensor_variant & 4
        if variant == 0:
            return SensorVariant.SCD40
        elif variant == 1:
            return SensorVariant.SCD41
        return SensorVariant.UNKNOWN

    def measure_and_read_single_shot(self):
        """
        Start a single shot measurement and read out the data when ready

        :return a_co2_concentration:
            CO₂ concentration in ppm
        :return a_temperature:
            Temperature in °C
        :return a_relative_humidity:
            Relative humidity in %RH
        """
        self.scd4x.measure_single_shot()
        data_ready = self.get_data_ready_status()
        while not data_ready:
            time.sleep(0.1)
            data_ready = self.get_data_ready_status()
        return self.read_measurement()
