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

# 通信の開始
# ser.open()

# データ送信

# M1 = 温度の計測値を要求するコマンド
# x04  開始
# x05  終了
request_00M1 = b'\x04\x30\x30\x4D\x31\x05'    
ser.write(request_00M1)

# データ受信
received_data = ser.read(26)  # 最大26バイト（）のデータを受信

# 受信データを16進数に戻して表示
received_hex_string = int.from_bytes(
            received_data, 
            byteorder='big'
            )

print(f"Received data: {received_hex_string}")

print(f"Received data in hex: {hex(received_hex_string)}")

# 例えばこんなのが帰ってきます、   
# 0x24d312020202033342e330365
 
exit()

# バイト列を16進数文字列に変換
hex_string = received_hex_string

hex_string = received_data.hex()

hex_data = b'\x24\xd3\x12\x02\x02\x02\x03\x33\x42\xe3\x30\x36\x35'
# バイト列を16進数文字列に変換
hex_string = hex_data.hex()

# 必要な部分を切り出して解釈
value_hex = hex_string[8:12]  # '3342'
fraction_hex = hex_string[12:14]  # 'e3'
fraction_after_dot_hex = hex_string[14:16]  # '30'

# 16進数を10進数に変換
value = int(value_hex, 16)  # 13346
fraction = int(fraction_hex, 16)  # 227
fraction_after_dot = int(fraction_after_dot_hex, 16)  # 48

# 小数点を挿入して小数点形式に変換
result = f'{value}.{fraction}{fraction_after_dot}'  # '13346.348'
print(result)  # 結果を表示


# 通信の終了
ser.close()



""" This code is private property of MSLab inc. and it is strictly not permitted to copy any of algorisms in this code without written permission of MSLab inc., copy_right May 2023"""