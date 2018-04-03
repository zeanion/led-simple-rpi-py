# Simple Raspberry Pi LED - Python

A simple example of how to blink an LED using a Raspberry Pi via Python 2.x

## Getting Started

These instructions will provide you a component list and steps to get up and running. I'm assuming you have already have everything needed to power / boot up the Raspberry Pi board.

### Components

* 1 Raspberry Pi B+ or Newer
* 1 3mm or 5mm LED - Any Color
* 1 220 Ohms Resistor (Color Bands - Red, Red, Brown)
* 1 Solder-less Prototype Breadboard
* 2 Pin Jumper Wires (Male to Female)

### Wiring

![alt text][simpledwiring]

* [Board pin 6 - Ground](https://pinout.xyz/pinout/ground)
* [Board pin 11 - BCM 17](https://pinout.xyz/pinout/pin11_gpio17)


### Running the code

* Open the cmd
* Navigate to the project directory (example, Enter: cd Downloads)
* Enter: sudo python led.py

### Demo

![alt text][demo]

### Stopping the code

* Press: CTRL+C in the cmd window

[simpledwiring]: https://github.com/zeanion/led-simple-rpi-py/raw/master/images/led-simple-breadboard.png "Breadboard wiring"
[demo]: https://github.com/zeanion/led-simple-rpi-py/raw/master/images/led-simple-demo.png "Demo"
