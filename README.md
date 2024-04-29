\* _This README is a work in progress_.

# Orange Pi Zero 2W

Make sure [https://github.com/orangepi-xunlong/wiringOP-Python](wiringOP-Python) is installed (it should be with an official Orange Pi image).

Connect the LED and BUTTON as follows:

```Python
# listen-for-shutdown.py
LED = 3 # NOTE wPI: 3; Physical: 8
BUTTON = 27 # NOTE wPI: 27; Physical: 40
```

Differences between this branch and the others:

- Any pins can be used, however, you can only shutdown the OPi via the button, not turn it on.

# Directory Structure

```BASH
├── diagrams
│   ├── pinout.fzz
│   └── pinout.png
├── LICENSE
├── listen-for-shutdown.py ✏️ To adjust PINs and press delay
├── listen-for-shutdown.service
├── listen-for-shutdown.sh
├── README.md
└── script
    ├── install
    ├── install.systemd
    ├── uninstall
    └── uninstall.systemd
```

# pi-power-button

Scripts used in our official [Raspberry Pi power button guide](https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi).

## Installation

1. [Connect to your Orange Pi via SSH](https://howchoo.com/g/mgi3mdnlnjq/how-to-log-in-to-a-raspberry-pi-via-ssh)
1. Clone this repo: `git clone -b opiz2w https://github.com/bassamanator/pi-power-button`
1. Optional: Edit line 9/10 in listen-for-shutdown.py to your preferred pin (Please see "Is it possible to use another pin other than Pin 5 (GPIO 3/SCL)?" below!)
1. Run the setup script: `./pi-power-button/script/install.systemd`

## Uninstallation

If you need to uninstall the power button script in order to use GPIO3 for another project or something:

1. Run the uninstall script: `./pi-power-button/script/uninstall.systemd`

## Hardware

A full list of what you'll need can be found [here](https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi#parts-list). At a minimum, you'll need a normally-open (NO) power button, some jumper wires, and a soldering iron. If you _don't_ have a soldering iron or don't feel like breaking it out, you can use [this prebuilt button](https://howchoo.com/shop/product/prebuilt-raspberry-pi-power-button?utm_source=github&utm_medium=referral&utm_campaign=git-repo-readme) instead.

Connect the power button to Pin 5 (GPIO 3/SCL) and Pin 6 (GND) as shown in this diagram:

![Connection Diagram](https://raw.githubusercontent.com/Howchoo/pi-power-button/master/diagrams/pinout.png)

### Is it possible to use any unused pin?

Yes.
