import random
import time
from sensor_data import SensorData

def simulate_data_collection(device, num_data_points):
    for _ in range(num_data_points):
        height = random.uniform(0.6, 1.4)
        weight = random.uniform(3, 20)
        movement = random.uniform(0, 0.5)
        data_point = SensorData(height, weight, movement)
        device.collect_data(data_point)
        time.sleep(0.1)

def simulate_stop(device, entering, exiting):
    entering_weight = sum(data.weight for data in entering)
    exiting_weight = sum(data.weight for data in exiting)
    weight_change = entering_weight - exiting_weight

    device.total_weight += weight_change

    if device.detect_weight_tampering(weight_change):
        print("Tampering detected based on weight change!")

    for data in exiting:
        device.sensor_data.remove(data)

    for data in entering:
        device.collect_data(data)
