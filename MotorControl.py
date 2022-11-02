#!/usr/bin/env python3
 # -*- coding: utf-8 -*-
import time
from Serial.serialPi import SerialU

class MotorControl():
  def __init__(self):
        super().__init__()
        self.ser = SerialU('/dev/ttyAMA0', 115200)
        

  def CRC8(self, mas):
        st_byt = 0
        crc = 0
        while st_byt < len(mas):
            dat = mas[st_byt]
            for i in range(8):
                fb = crc ^ dat
                fb &= 1
                crc >>= 1
                dat >>= 1
                if fb == 1:
                    crc ^= 0x8c
            st_byt += 1
        return crc

  def MotionManage(self, MotorID, FrontMotorSpeed, BackMotorSpeed):
        if 1:
            
            FrontMotorSpeed = 65534 - abs(FrontMotorSpeed) if FrontMotorSpeed < 0 else abs(FrontMotorSpeed)
            BackMotorSpeed = 65534 - abs(BackMotorSpeed) if BackMotorSpeed < 0 else abs(BackMotorSpeed)

            data = [18, MotorID, FrontMotorSpeed >> 8, FrontMotorSpeed & 0xff, BackMotorSpeed >> 8, BackMotorSpeed & 0xff, 0]

            data.append(self.CRC8(data[1:]))
            data.append(36)            
            self.ser.write(data, len(data))
            return data


