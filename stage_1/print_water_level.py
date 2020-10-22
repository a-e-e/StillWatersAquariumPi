import busio
import board
import digitalio
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


def get_water_level_inches(voltage):
    """
    v-b / m
    b = 2.49
    m = -.097
    :param voltage:
    :return:
    """
    slope = -0.0978
    y_intercept = 2.49
    water_level_inches = (voltage - y_intercept) / slope
    return round(water_level_inches, 2)


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

    while True:
        print('ADC Voltage: ' + str(round(water_level_sensor.voltage, 2)) + 'V')
        print('Water Level: ' + str(get_water_level_inches(water_level_sensor.voltage)) + ' inches')
        time.sleep(.5)


if __name__ == '__main__':
    main()
