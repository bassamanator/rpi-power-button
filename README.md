# Power Button with Indicator

[Source article](https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi).

\*_This fork implements the use of a power LED indicator as well._
\*\*_Should work without an LED._

# Pin Definitions

```python
PIN_LED = 4 # GPIO4 / physical pin #7
PIN_BUTTON = 3 # GPIO3 / physical pin #5
```

# Installation

1. [Connect to your Raspberry Pi via SSH](https://howchoo.com/g/mgi3mdnlnjq/how-to-log-in-to-a-raspberry-pi-via-ssh)
2. Clone this repo: `git clone https://github.com/bassamanator/rpi-power-button.git`
3. Run the setup script: `./rpi-power-button/script/install.systemd`

# Uninstallation

1. Run the uninstall script: `./rpi-power-button/script/uninstall.systemd`

# Physical Connections

Connect the power button to Pin 5 (GPIO 3/SCL) and Pin 6 (GND) as shown in this diagram:

![Connection Diagram](https://raw.githubusercontent.com/Howchoo/pi-power-button/master/diagrams/pinout.png)

_Power LED connection is not shown in this diagram._

# Is it possible to use another pin other than Pin 5 (GPIO 3/SCL)?

Not for full functionality, no. There are two main features of the power button:

1. **Shutdown functionality:** Shut the Pi down safely when the button is pressed. The Pi now consumes zero power.
1. **Wake functionality:** Turn the Pi back on when the button is pressed again.

The **wake functionality** requires the SCL pin, Pin 5 (GPIO 3). There's simply no other pin that can "hardware" wake the Pi from a zero-power state. If you don't care about turning the Pi back _on_ using the power button, you could use a different GPIO pin for the **shutdown functionality** and still have a working shutdown button. Then, to turn the Pi back on, you'll just need to disconnect and reconnect power (or use a cord with a physical switch in it) to "wake" the Pi.

Of course, for the GND connection, you can use [any other ground pin you want](https://pinout.xyz/).
