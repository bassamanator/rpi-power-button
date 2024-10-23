# Orange Pi Power Button With LED Indicator

# Expected Behaviour

- The Orange Pi will shutdown if the power button is held for 3 seconds.
- The LED will blink while the power button is held.

# Notes

- _Should_ work on any Orange Pi.
- Make sure [https://github.com/orangepi-xunlong/wiringOP-Python](wiringOP-Python) is installed (it should be with an official Orange Pi image).
- Connect the LED and BUTTON as follows:

```Python
# listen-for-shutdown.py
LED = 3 # NOTE wPI: 3; Physical: 8
BUTTON = 27 # NOTE wPI: 27; Physical: 40
# ⚠️ In case this get's outdated, check `listen-for-shutdown.py` for actual pins
```

- Any pins can be used, however, **you can only shutdown the OPi via the button, not turn it on**.

# Installation

1. `SSH` into your OPi.
1. Clone this repo: `git clone -b opiz2w https://github.com/bassamanator/rpi-power-button.git`
1. Edit `listen-for-shutdown.py` to your preferred pin.
1. Run the setup script: `./rpi-power-button/script/install.systemd`

# Uninstallation

1. Run the uninstall script: `./rpi-power-button/script/uninstall.systemd`

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

# Inspired By

[Raspberry Pi power button guide](https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi).
