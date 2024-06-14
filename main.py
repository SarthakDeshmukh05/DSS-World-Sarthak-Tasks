
import logging
import random
import time
from mcu_device import MCUDevice
from infant_identifier import InfantIdentifier
from sensor_data import SensorData
from simulate import simulate_data_collection, simulate_stop

def main():
    logging.basicConfig(filename='logs/mcu_device.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    
    storage_capacity = 100
    device = MCUDevice(storage_capacity)
    infant_detector = InfantIdentifier()

    num_data_points = 1000
    simulate_data_collection(device, num_data_points)

    entering = [SensorData(random.uniform(0.6, 1.4), random.uniform(3, 20), random.uniform(0, 0.5)) for _ in range(10)]
    exiting = [device.sensor_data[random.randint(0, len(device.sensor_data)-1)] for _ in range(5)]

    simulate_stop(device, entering, exiting)

    if device.detect_tampering():
        print("Tampering detected based on movement!")
    else:
        print("No tampering detected based on movement.")

    infants = infant_detector.identify_infants(device.sensor_data)
    total_infants = len(infants)
    print("Total infants identified (without duplicates):", total_infants)

if __name__ == "__main__":
    main()
