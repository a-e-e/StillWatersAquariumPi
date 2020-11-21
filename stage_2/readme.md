# Stage 2: Print water temperature on screen using raspberry pi and DS18B20 temperature sensor

Referencing https://docs.micropython.org/en/latest/esp8266/tutorial/onewire.html

# To get started
Stage 2 builds off of staging 1.

We will need the following:
- Everything from stage 1
- DS18B20 Waterproof temperature sensor
- 4.7k ohm resistor (included with temperature sensor)
- Electrical Tape
https://www.adafruit.com/product/381

## Enable 1 wire interface
https://www.raspberrypi-spy.co.uk/2018/02/enable-1-wire-interface-raspberry-pi/

Unlike the analog water level sensor, the DS18B20 has a built in Analog to Digital converter and features a Dallas 1-wire connection. This allows us to skip the MCP3008 ADC we used for the water level senor.

## Install required library
- `sudo pip3 install w1thermsensor`

# Wiring
The temperature sensor has 3 wires: Blue (GND), Orange (3.3V), Yellow (Data).
- Find matching color male to female wires and use electrical tape to attachem them to the end of the sensor wires.
<img src="resources/images/IMG_3020.jpeg" height=400>
<img src="resources/images/IMG_3024.jpeg" height=400>
<img src="resources/images/IMG_3025.jpeg" height=400>
- Connect the blue wire to GND
- Connect the red wire to 3.3V
- Connect the yellow wire to GPIO 4 with the 4.7k ohm resistor inbetween it that is connected to 3.3V

# Running code

- Open Thornny Python IDE
- Load -> Code/StillWatersAquariumPi/stage_2/print_water_level_and_temperature.py
- Click 'Run'
