#AirHijacker

AirHijacker is a wireless security research tool designed to perform active Wi-Fi authentication attack simulations in authorized environments.
It focuses on real-time connection attempts rather than traditional offline WPA handshake cracking.

Features

Active Wi-Fi authentication testing.

No monitor mode required.

No handshake capture dependency.

Real-time brute-force simulation.

Simple interactive CLI.

Designed for security research & labs.

Requirements
```bash
pip install -r requirements.txt
```
OR 
```bash 
pip3 install pywifi requirements.txt
```
Installation
```bash
git clone https://github.com/yourusername/AirHijacker.git
cd AirHijacker
python airhijacker.py
```
usages
```bash
python AirHijacker.py
```
Or
```bash
python3 AirHijacker.py
```
Once launched, you will interact with AirHijacker using the following commands.
help ---- Show available commands
scan  --- Scan for nearby Wi-Fi networks
attack --- Start active authentication testing

First of all scan for the available networks.
```bash
scan
```
```bash
attack
```
In the attack menu, select the Wi-Fi network you want to brute-force by typing the associated number (for example: 1, 2, or 3).

#Disclaimer

AirHijacker is developed strictly for authorized security research, educational use, and ethical penetration testing.
It must only be used on Wi-Fi networks you own or have explicit written permission to test.

Any unauthorized or illegal use is strictly prohibited.
The author assumes no liability for misuse.

Author

BlackHatRihaan
Offensive Security • Wireless Security Research
Tooling • Attack Simulation • Ethical Hacking

License

This project is released for educational and research purposes only.

Use responsibly.


