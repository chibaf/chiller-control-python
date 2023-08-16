#!/usr/bin/env python3
# -*- coding: utf-8 -*-"
""" HNGN001 Created on Tue Jun 11 08:34:11 2019
(two days before 190613) (1month before 190711), work till 1000 codes"""


import serial

# シリアルポートの設定
ser = serial.Serial(
    port='/dev/ttyUSB0',  # ポート名は環境に合わせて変更
    baudrate=9600,
    timeout=1  # タイムアウトの設定
)

# M1 = 温度の計測値を要求するコマンド
# x04  EOT, 開始
# x05  ENQ, 終了
# x30\x30\  Chiller のアドレス（00）

# 00M1,   00=アドレス、M1=識別子 

# b'\x04\x30\x30\x4D\x31\x05'
# b`\x04' + "00M1" +  b`\x05`

EOT= b'\x04'
ENQ= b'\x05'

STX= b'\x02'
ETX= b'\x03'

BCC= b'\x70'

M1 = b'\x4D\x31'
S1 = b'\x53\x31'

input=

request_00M1 = b'\x04\x30\x30\x4D\x31\x05'    
ser.write(request_00M1)

# データ受信
line = ser.readline()  
line2 = line.strip().decode("utf-8")
print(line2)


ser.close()



""" This code is private property of MSLab inc. and it is strictly not permitted to copy any of algorisms in this code without written permission of MSLab inc., copy_right May 2023"""