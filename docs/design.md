# Design Details

## Overview

The system simulates an MCU device that collects sensor data, detects tampering, and identifies infants. It consists of multiple components, each handling specific functionalities.

## Components

### MCUDevice
- **Purpose**: Collects sensor data, detects tampering based on movement and weight changes.
- **Attributes**:
  - `storage_capacity`: Maximum number of data points it can store.
  - `tamper_threshold`: Threshold for detecting tampering based on movement.
  - `weight_change_threshold`: Threshold for detecting significant weight changes.
  - `total_weight`: Tracks the total weight of passengers.

### SensorData
- **Purpose**: Represents individual sensor readings.
- **Attributes**:
  - `height`: Height of the passenger.
  - `weight`: Weight of the passenger.
  - `movement`: Movement reading.

### InfantIdentifier
- **Purpose**: Identifies infants based on height, weight, and movement thresholds.
- **Attributes**:
  - `height_threshold`: Threshold for identifying infants by height.
  - `weight_threshold`: Threshold for identifying infants by weight.
  - `movement_threshold`: Threshold for identifying infants by movement.

## Simulation

### Data Collection
- Simulates the collection of sensor data points with random values for height, weight, and movement.

### Stop Events
- Simulates passengers entering and exiting, updating the total weight and detecting tampering based on significant weight changes.
