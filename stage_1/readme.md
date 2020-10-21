Stage 1: Print water level on screen using raspberry pi and eTape sensor

Directions borrowed heavily from 

https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi/connecting-the-cobbler-to-a-mcp3008

# To get started
We will need the following:
- Raspberry pi 4
- 8in eTape
https://www.adafruit.com/product/463
- MCP3008 ADC (or similar)
https://www.adafruit.com/product/856

# Wiring

### Why we need an ADC
The Raspberry Pi computer does not have a way to read analog inputs. It's a digital-only computer. 
Compare this to the Arduino, AVR or PIC microcontrollers that often have 6 or more analog inputs! 
Analog inputs are handy because many sensors are analog outputs, so we need a way to make the Pi analog-friendly.

We'll do that by wiring up an MCP3008 chip to it. 
The MCP3008 acts like a "bridge" between digital and analog. 
It has 8 analog inputs and the Pi can query it using 4 digital pins. 
That makes it a perfect addition to the Pi for integrating simple sensors like photocells, FSRs or potentiometers, thermistors, etc.!

Let's check the datasheet of the MCP3008 chip.
 On the first page in the lower right corner there's a pinout diagram showing the names of the pins:
 
 ![MCP3008](https://learn.adafruit.com/assets/1222.png)


# Installing required packages

Assuming a new raspberry pi,

`sudo apt-get update -y`

`sudo apt-get upgrade -y`

Enable SPI

`sudo pip 3 install adafruit-circuitpython-mp3xxx`