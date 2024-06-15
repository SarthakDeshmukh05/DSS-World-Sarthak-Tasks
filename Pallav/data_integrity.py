import hashlib
import time
from data_collection import counter
from data_storage_system import DataStorage

class DataStorageWithIntegrity(DataStorage):
    def calculate_checksum(self, data):
        return hashlib.md5(data.encode()).hexdigest()

    def save_data(self, data):
        try:
            checksum = self.calculate_checksum(str(data))
            with open(self.filename, "a") as file:
                file.write(f"{data},{checksum}\n")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                data_lines = file.readlines()
                valid_data = []
                for line in data_lines:
                    data, checksum = line.strip().split(",")
                    if self.calculate_checksum(data) == checksum:
                        valid_data.append(data)
                    else:
                        print(f"Data corruption detected: {line}")
                return valid_data
        except Exception as e:
            print(f"Error loading data: {e}")
            return []


storage_with_integrity = DataStorageWithIntegrity("passenger_count_with_integrity.txt")

# Save the passenger count data with integrity check
for _ in range(100):  # Simulate 100 detection attempts
    count = counter.update_count()
    storage_with_integrity.save_data(count)
    time.sleep(0.1)  # Simulate time delay between detections

# Load and print the stored data
stored_data_with_integrity = storage_with_integrity.load_data()
print("Stored Data with Integrity Check:")
print(stored_data_with_integrity)
