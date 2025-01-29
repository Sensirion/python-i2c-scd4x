# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

import pytest
from sensirion_shdlc_sensorbridge import SensorBridgePort
from sensirion_driver_adapters.i2c_adapter.sensor_bridge_i2c_channel_provider import SensorBridgeI2cChannelProvider
from sensirion_driver_adapters.mocks.mock_i2c_channel_provider import MockI2cChannelProvider
from sensirion_i2c_scd4x.response_provider import Scd4xResponseProvider


def pytest_addoption(parser):
    """
    Register command line options
    """
    parser.addoption("--serial-port", action="store", type=str)
    parser.addoption("--serial-bitrate", action="store", type=int, default=460800)


def _get_serial_port(config, validate=False):
    """
    Get the serial port to be used for the tests.
    """
    port = config.getoption("--serial-port")
    if (validate is True) and (port is None):
        raise ValueError("Please specify the serial port to be used with "
                         "the '--serial-port' argument.")
    return port


def _get_serial_bitrate(config):
    """
    Get the serial port bitrate to be used for the tests.
    """
    return config.getoption("--serial-bitrate")


def pytest_report_header(config):
    """
    Add extra information to test report header
    """
    lines = [
        "SensorBridge serial port: " + str(_get_serial_port(config)),
        "SensorBridge serial bitrate: " + str(_get_serial_bitrate(config))
    ]
    return '\n'.join(lines)


@pytest.fixture(scope="session")
def channel_provider(request):
    serial_port = _get_serial_port(request.config)

    serial_bitrate = _get_serial_bitrate(request.config)
    if serial_port is not None:
        yield SensorBridgeI2cChannelProvider(sensor_bridge_port=SensorBridgePort.ONE,
                                             serial_baud_rate=serial_bitrate,
                                             serial_port=serial_port)
    else:
        yield MockI2cChannelProvider(command_width=2,
                                     response_provider=Scd4xResponseProvider())