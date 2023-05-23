import serial


class SerialHandler:

    def __init__(self) -> None:
        self.ser = serial.Serial()
        self.ser.baudrate = 921600
        self.ser.port = "/dev/serial0"

    def start(self) -> None:
        self.ser.open()