import busio
import board
import digitalio
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from w1thermsensor import W1ThermSensor


VOLTAGE_AT_2_INCH = 2.41
VOLTAGE_AT_6_INCH = 2.04


def get_water_level_inches(voltage):
    """
    v-b / m
    b = 2.49
    m = -.097
    :param voltage:
    :return:
    """
    slope = (VOLTAGE_AT_6_INCH - VOLTAGE_AT_2_INCH) / 4.0
    y_intercept = VOLTAGE_AT_6_INCH - ( 6 * slope)
    water_level_inches = (voltage - y_intercept) / slope
    return round(water_level_inches, 2)


def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32


def main():
    """
    Print the water level every .5 seconds
    :return:
    """
    # create the spi bus
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    # create the cs (chip select)
    cs = digitalio.DigitalInOut(board.D22)

    # create the mcp object
    mcp = MCP.MCP3008(spi, cs)

    # create an analog input channel on pin 0
    water_level_sensor = AnalogIn(mcp, MCP.P0)

    # create temperature sensor
    temp_sensor = W1ThermSensor()

    while True:
        temperature = temp_sensor.get_temperature()
        print(f"The temperature is {temperature} C, {celsius_to_fahrenheit(temperature)} F")
        print('ADC Voltage: ' + str(round(water_level_sensor.voltage, 2)) + 'V')
        print('Water Level: ' + str(get_water_level_inches(water_level_sensor.voltage)) + ' inches')
        time.sleep(1)


if __name__ == '__main__':
    main()
