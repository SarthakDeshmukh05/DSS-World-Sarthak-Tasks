import random
import time

class PassengerCounter:
    def __init__(self):
        self.passenger_count = 0
        self.infant_count = 0

    def detect_passenger(self):
        # Simulate passenger detection (1 means passenger detected, 0 means no passenger)
        return random.choice([0, 1])

    def detect_infant(self):
        # Simulate infant detection (1 means infant detected, 0 means no infant)
        return random.choice([0, 1])

    def update_counts(self):
        if self.detect_passenger():
            self.passenger_count += 1
        if self.detect_infant():
            self.infant_count += 1
        return self.passenger_count, self.infant_count

counter = PassengerCounter()

# Simulate data collection
for _ in range(100):  # Simulate 100 detection attempts
    passenger_count, infant_count = counter.update_counts()
    print(f"Passenger count: {passenger_count}, Infant count: {infant_count}")
    time.sleep(0.1)  # Simulate time delay between detections
