import time
from data_collection import counter

class DataStorage:
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, data):
        try:
            with open(self.filename, 'a') as file:
                file.write(f"{data}\n")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return file.readlines()
        except Exception as e:
            print(f"Error loading data: {e}")
            return []

storage = DataStorage('passenger_count.txt')

# Save the passenger count data
for _ in range(100):  # Simulate 100 detection attempts
    count = counter.update_counts()
    storage.save_data(count)
    time.sleep(0.1)  # Simulate time delay between detections

# Load and print the stored data
stored_data = storage.load_data()
print("Stored Data:")
print(stored_data)