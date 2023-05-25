#!/usr/bin/env python3

import numpy as np
import serial
import struct
import sys

from tcd1304_viewer.viewer import Viewer

viewer = Viewer()
sh = 84 * 20
icg = 84 * 1000 * 200
cfg = [sh, icg]

if len(sys.argv) > 2:
    cfg = [int(i) for i in sys.argv[1:]]

msg = struct.pack("<HBIIIx", 0x1304, 0, 8, *cfg)

# viewer.show()

# Open the serial port
print("Opening serial")
ser = serial.Serial('/dev/ttyUSB0', baudrate=2457600)

ser.write(msg)

# Now read and print data from the serial port forever
while True:
    # viewer.pause()
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
        data = []

        while len(c):
            d, c = c[:2], c[2:]
            (r, ) = struct.unpack("<H", d)
            data.append(r * 3.3 / 4096)

        viewer.update_data(np.array(data) * -1 + 3.3)
