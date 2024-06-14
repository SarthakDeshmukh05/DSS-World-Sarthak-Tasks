import logging

class MCUDevice:
    def __init__(self, storage_capacity):
        self.storage_capacity = storage_capacity
        self.sensor_data = []
        self.tamper_threshold = 0.2
        self.weight_change_threshold = 50
        self.logger = logging.getLogger('MCUDevice')
        self.logger.setLevel(logging.INFO)
        self.total_weight = 0

    def collect_data(self, data):
        if len(self.sensor_data) < self.storage_capacity:
            self.sensor_data.append(data)
            self.total_weight += data.weight
            self.logger.info(f"Data collected: Height={data.height}, Weight={data.weight}, Movement={data.movement}")
        else:
            self.logger.warning("Storage full. Data not collected.")

    def detect_tampering(self):
        if len(self.sensor_data) < 2:
            self.logger.warning("Insufficient data for tamper detection.")
            return False

        avg_movement = sum(data_point.movement for data_point in self.sensor_data) / len(self.sensor_data)

        if abs(self.sensor_data[-1].movement - avg_movement) > self.tamper_threshold:
            self.logger.warning("Tampering detected based on movement!")
            return True

        return False

    def detect_weight_tampering(self, weight_change):
        if abs(weight_change) > self.weight_change_threshold:
            self.logger.warning("Tampering detected based on weight change!")
            return True
        return False
