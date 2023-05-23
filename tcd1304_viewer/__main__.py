#!/usr/bin/env python3

import numpy as np
import serial
import struct
import sys

from tcd1304_viewer.viewer import Viewer

viewer = Viewer()
cfg = [1680, 8400000]

if len(sys.argv) > 2:
    cfg = [int(i) for i in sys.argv[1:]]

msg = struct.pack("<HBII", 0x1304, 0, *cfg)

viewer.show()

# Open the serial port
ser = serial.Serial('/dev/serial0', baudrate=921600)

ser.write(msg)

# Now read and print data from the serial port forever
while True:
    m = ser.read(1)[0] << 8

    while m != 0x1304:
        m >>= 8
        m |= ser.read(1)[0] << 8

    t, l = struct.unpack("<BI", ser.read(5))
    c = ser.read(l)
    print(f"msg t={t:#02x}, l={l}")

    if t == 0x00:
        print(f"content {c}")
    if t == 0x01:
        data = np.array()

        while len(c):
            d, c = c[:2], c[2:]
            (r, ) = struct.unpack("<H", d)
            data.append(r * 3.3 / 4096)

        viewer.update_data(data)
