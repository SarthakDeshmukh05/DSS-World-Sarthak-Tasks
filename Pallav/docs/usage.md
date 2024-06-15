# Usage Instructions

This document provides step-by-step instructions on how to use the data collection and storage system for the MCU-enabled device.

## Prerequisites

1. **Hardware:**
   - MCU-enabled device with UART capability.
   - EEPROM module.
   - Sensors for passenger and infant detection.
   - UART to USB converter (if connecting to a PC).

2. **Software:**
   - Python 3.x
   - Required Python libraries: `sqlite3`, `paho-mqtt`, `serial`, `random`, `struct`, `time`, `binascii`, `csv`

## Setup

1. **Install Python:**
   Make sure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries:**
   Run the following command to install the required Python libraries:
   ```bash
   pip install pyserial paho-mqtt
