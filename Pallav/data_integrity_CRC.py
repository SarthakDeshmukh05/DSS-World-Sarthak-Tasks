import binascii
import struct
from data_storage_system import EEPROMStorage
from data_collection import counter

class EEPROMStorageWithCRC(EEPROMStorage):
    def calculate_crc(self, data):
        return binascii.crc32(data) & 0xFFFFFFFF

    def write_data_with_crc(self, address, data):
        crc = self.calculate_crc(data)
        full_data = data + struct.pack("I", crc)
        self.write_data(address, full_data)

    def read_data_with_crc(self, address, length):
        full_data = self.read_data(address, length + 4)
        data, crc_stored = full_data[:-4], struct.unpack("I", full_data[-4:])[0]
        crc_calculated = self.calculate_crc(data)
        if crc_stored != crc_calculated:
            raise ValueError("Data corruption detected")
        return data


eeprom_crc = EEPROMStorageWithCRC("eeprom_crc.bin")

# Convert counts to binary and store in EEPROM with CRC
passenger_count, infant_count = counter.update_counts()
data = struct.pack("HH", passenger_count, infant_count)
eeprom_crc.write_data_with_crc(0, data)
eeprom_crc.save_to_file()

# Read data from EEPROM with CRC
eeprom_crc.load_from_file()
stored_data = eeprom_crc.read_data_with_crc(0, struct.calcsize("HH"))
stored_passenger_count, stored_infant_count = struct.unpack("HH", stored_data)
print(
    f"Stored Passenger count with CRC: {stored_passenger_count}, Stored Infant count with CRC: {stored_infant_count}"
)
