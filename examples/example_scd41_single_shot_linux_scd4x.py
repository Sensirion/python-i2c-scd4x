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

import argparse
import time
from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection, CrcCalculator
from sensirion_driver_adapters.i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_scd4x.device import Scd4xDevice

parser = argparse.ArgumentParser()
parser.add_argument('--i2c-port', '-p', default='/dev/i2c-1')
args = parser.parse_args()

with LinuxI2cTransceiver(args.i2c_port) as i2c_transceiver:
    channel = I2cChannel(I2cConnection(i2c_transceiver),
                         slave_address=0x62,
                         crc=CrcCalculator(8, 0x31, 0xff, 0x0))
    sensor = Scd4xDevice(channel)
    time.sleep(0.03)

    # Ensure sensor is in clean state
    sensor.wake_up()
    sensor.stop_periodic_measurement()
    sensor.reinit()

    # Read out information about the sensor
    serial_number = sensor.get_serial_number()
    print(f"serial number: {serial_number}"
          )

    #     If temperature offset and/or sensor altitude compensation
    #     is required, you should call the respective functions here.
    #     Check out the header file for the function definitions.
    for i in range(5):

        #     Wake the sensor up from sleep mode.
        sensor.wake_up()

        #     Ignore first measurement after wake up.
        sensor.measure_single_shot()

        #     Perform single shot measurement and read data.
        (co2_concentration, temperature, relative_humidity
         ) = sensor.measure_and_read_single_shot()

        #     Print results in physical units.
        print(f"CO2 concentration [ppm]: {co2_concentration}"
              )
        print(f"Temperature [°C]: {temperature}"
              )
        print(f"Relative Humidity [RH]: {relative_humidity}"
              )
        print("sleep for 5 minutes until next measurement is due"
              )
        time.sleep(300.0)
