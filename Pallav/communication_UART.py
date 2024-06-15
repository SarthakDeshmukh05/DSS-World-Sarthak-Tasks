import serial


class UARTCommunication:
    def __init__(self, port, baudrate=9600):
        self.ser = serial.Serial(port, baudrate)

    def send_data(self, data):
        self.ser.write(data)

    def receive_data(self):
        return self.ser.read()


# Example usage
uart = UARTCommunication("/dev/ttyUSB0")
uart.send_data(data)  # Send passenger and infant counts in binary format
