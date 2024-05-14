import random
import logging
import time

class SensorData:
    def __init__(self, height, weight, movement):
        self.height = height
        self.weight = weight
        self.movement = movement

class MCUDevice:
    def __init__(self, storage_capacity):
        self.storage_capacity = storage_capacity
        self.sensor_data = []
        self.tamper_threshold = 0.2  # Adjusted threshold for tamper detection
        self.logger = logging.getLogger('MCUDevice')
        self.logger.setLevel(logging.INFO)
        self.total_count = 0  # Initialize total count of individuals

    def collect_data(self, data):
        if len(self.sensor_data) < self.storage_capacity:
            self.sensor_data.append(data)
            self.logger.info(f"Data collected: Height={data.height}, Weight={data.weight}, Movement={data.movement}")
        else:
            self.logger.warning("Storage full. Data not collected.")

    def detect_tampering(self):
        if len(self.sensor_data) < 2:
            self.logger.warning("Insufficient data for tamper detection.")
            return False  # Not enough data points for comparison

        # Calculate average movement
        avg_movement = sum(data_point.movement for data_point in self.sensor_data) / len(self.sensor_data)

        # Check for tampering based on threshold
        if abs(self.sensor_data[-1].movement - avg_movement) > self.tamper_threshold:
            self.logger.warning("Tampering detected!")
            return True  # Tampering detected
        else:
            return False

class InfantIdentifier:
    def __init__(self):
        self.height_threshold = 1.2  # Adjusted threshold for infant height
        self.weight_threshold = 15  # Adjusted threshold for infant weight
        self.movement_threshold = 0.1  # Adjusted threshold for infant movement
        self.identifiers = set()  # Set to store unique identifiers

    def identify_infants(self, sensor_data):
        infants = []
        for data_point in sensor_data:
            identifier = f"{data_point.height}-{data_point.weight}-{data_point.movement}"
            if identifier not in self.identifiers:
                self.identifiers.add(identifier)
                if (data_point.height < self.height_threshold and
                        data_point.weight < self.weight_threshold and
                        data_point.movement < self.movement_threshold):
                    infants.append(data_point)
        return infants

def simulate_data_collection(device, num_data_points):
    for _ in range(num_data_points):
        height = random.uniform(0.6, 1.4)  # Adjusted range for height
        weight = random.uniform(3, 20)  # Adjusted range for weight
        movement = random.uniform(0, 0.5)  # Adjusted range for movement
        data_point = SensorData(height, weight, movement)
        device.collect_data(data_point)
        time.sleep(0.1)  # Simulate data collection delay

def main():
    logging.basicConfig(filename='mcu_device.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    
    storage_capacity = 100  # Increased storage capacity
    device = MCUDevice(storage_capacity)
    infant_detector = InfantIdentifier()

    num_data_points = 1000  # Increased number of data points for accuracy
    simulate_data_collection(device, num_data_points)

    # Detect tampering
    if device.detect_tampering():
        print("Tampering detected!")
    else:
        print("No tampering detected.")

    # Identify infants
    infants = infant_detector.identify_infants(device.sensor_data)
    total_infants = len(infants)
    print("Total infants identified (without duplicates):", total_infants)

if __name__ == "__main__":
    main()
