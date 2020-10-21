import busio
import board
import digitalio
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)


def get_water_level_inches(voltage):
    """
    v-b / m
    b = 2.49
    m = -.097
    :param voltage:
    :return:
    """
    water_level_inches = (voltage - 2.49) / -0.0978
    return water_level_inches


while True:
    print('Raw ADC Value: ', chan.value)
    print('ADC Voltage: ' + str(chan.voltage) + 'V')
    print('Water Level: ' + str(get_water_level_inches(chan.voltage)))
    time.sleep(.5)
