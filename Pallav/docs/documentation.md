# Documentation

## Overview
This documentation provides a detailed description of the data collection and storage system for an MCU-enabled device that detects and counts passengers and infants. The system utilizes EEPROM for data storage, UART for communication, MQTT for data transmission, and an SQLite database for storing and exporting data.

## Components

### 1. Passenger Counter
- **Class:** `PassengerCounter`
- **Description:** Simulates the detection of passengers and infants.
- **Methods:**
  - `detect_passenger`: Simulates passenger detection.
  - `detect_infant`: Simulates infant detection.
  - `update_counts`: Updates and returns the current counts of passengers and infants.

### 2. EEPROM Storage with CRC
- **Class:** `EEPROMStorageWithCRC`
- **Description:** Simulates EEPROM storage with CRC for data integrity.
- **Methods:**
  - `calculate_crc`: Calculates CRC for given data.
  - `write_data_with_crc`: Writes data to EEPROM with CRC.
  - `read_data_with_crc`: Reads data from EEPROM and verifies CRC.
  - `save_to_file`: Saves EEPROM data to a file.
  - `load_from_file`: Loads EEPROM data from a file.

### 3. UART Communication
- **Class:** `UARTCommunication`
- **Description:** Handles UART communication for data transmission.
- **Methods:**
  - `send_data`: Sends data via UART.
  - `receive_data`: Receives data via UART.

### 4. MQTT Communication
- **Class:** `MQTTClient`
- **Description:** Handles MQTT communication for data transmission.
- **Methods:**
  - `connect`: Connects to the MQTT broker.
  - `publish`: Publishes a message to the MQTT broker.
  - `disconnect`: Disconnects from the MQTT broker.

### 5. SQLite Database
- **Class:** `SQLDatabase`
- **Description:** Manages SQLite database operations for storing and exporting data.
- **Methods:**
  - `create_table`: Creates the database table if it does not exist.
  - `insert_data`: Inserts collected data into the database.
  - `export_data_to_csv`: Exports data from the database to a CSV file.
  - `close`: Closes the database connection.

## Data Flow

1. **Data Collection:**
   - The `PassengerCounter` class simulates the detection of passengers and infants, updating the counts.

2. **Data Storage in EEPROM:**
   - The `EEPROMStorageWithCRC` class stores the collected data in EEPROM, ensuring data integrity using CRC.

3. **Data Transmission:**
   - The `UARTCommunication` class sends the data via UART.
   - The `MQTTClient` class publishes the data to an MQTT broker.

4. **Database Storage:**
   - The `SQLDatabase` class inserts the collected data into an SQLite database.

5. **Data Export:**
   - The `SQLDatabase` class exports the stored data to a CSV file for further analysis and verification.

## Libraries and Tools Used

- **Python Standard Libraries:**
  - `random`: For simulating data collection.
  - `time`: For simulating time delays.
  - `struct`: For packing/unpacking binary data.
  - `binascii`: For CRC calculations.
  - `sqlite3`: For database operations.
  - `csv`: For exporting data to CSV.

- **Third-Party Libraries:**
  - `pyserial`: For UART communication.
  - `paho-mqtt`: For MQTT communication.

## Troubleshooting and Support

- Ensure all required libraries are installed and configured correctly.
- Verify file permissions and UART port availability.
- Check MQTT broker connectivity and configuration.

For additional support and inquiries, contact the development team or refer to the usage guide (`usage.md`).
