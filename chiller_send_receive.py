# バイト列をASCII文字列に変換する関数
def bytes_to_ascii(byte_data):
    try:
        ascii_string = byte_data.decode("ascii")
        return ascii_string
    except UnicodeDecodeError:
        return "Invalid ASCII"

# バイト列をASCII文字列に変換
byte_code1 = b'\x4D\x31'
byte_code2 = b'\x53\x31'

ascii_value1 = bytes_to_ascii(byte_code1)
ascii_value2 = bytes_to_ascii(byte_code2)
ascii_value3 = bytes_to_ascii(byte_code1+byte_code2)

print(f"ASCII変換結果1: {ascii_value1}")
print(f"ASCII変換結果2: {ascii_value2}")

print(f"ASCII変換結果2: {ascii_value3}")
