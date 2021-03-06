import busio
import board
import digitalio
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from w1thermsensor import W1ThermSensor
from pyHS100 import SmartPlug

VOLTAGE_AT_2_INCH = 2.41
VOLTAGE_AT_6_INCH = 2.04

PUMP_IP = "192.168.1.88"
PUMP_CUTOFF_INCHES = 4.0

HEATER_IP = "192.168.1.88"
HEATER_CUTOFF_CELSIUS = 22


def get_water_level_inches(voltage):
    """
    observational approximation assuming voltage to water level relationship is linear
    use two reference points to find slope and y-intercept of a line
    y = mx + b
    Set VOLTAGE_AT_2_IN and VOLTAGE_AT_6_INCH global variables

    y = Voltage
    x = water level
    m = slope

    VOLTAGE_AT_2_INCH = m(2) + b
    VOLTAGE_AT_6_INCH = m(6) + b
    VOLTAGE_AT_2_INCH - m(2) = VOLTAGE_AT_6_INCH - m(6)
    m(4) = 4m = VOLTAGE_AT_6_INCH - VOLTAGE_AT_2_INCH
    m = (VOLTAGE_AT_6_INCH - VOLTAGE_AT_2_INCH) / 4

    :param voltage:
    :return:
    """
    slope = (VOLTAGE_AT_6_INCH - VOLTAGE_AT_2_INCH) / 4.0
    y_intercept = VOLTAGE_AT_6_INCH - ( 6 * slope)
    water_level_inches = (voltage - y_intercept) / slope
    return round(water_level_inches, 2)


def celsius_to_fahrenheit(celsius):
    return round(celsius * 1.8 + 32, 1)


def main():
    """
    Print the water level and temperature every second
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

    pump = SmartPlug(PUMP_IP)
    heater = SmartPlug(HEATER_IP)

    while True:
        temperature = temp_sensor.get_temperature()
        print(f"The temperature is {temperature} C, {celsius_to_fahrenheit(temperature)} F")
        print(f"ADC Voltage: {round(water_level_sensor.voltage, 2)}V")
        water_level = get_water_level_inches(water_level_sensor.voltage)
        print(f"Water Level: {water_level} inches")
        print("\n")

        if temperature < HEATER_CUTOFF_CELSIUS:
            print("Turning heater on")
            heater.turn_on()
        else:
            print("Turning heater off")
            heater.turn_off()

        if water_level < PUMP_CUTOFF_INCHES:
            print("Turning pump on")
            pump.turn_on()
        else:
            print("Turning pump off")
            pump.turn_off()
        time.sleep(1)


if __name__ == '__main__':
    main()
