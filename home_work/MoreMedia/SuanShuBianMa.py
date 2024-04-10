import random

class ArithmeticEncoder:
    def __init__(self):
        pass

    def encode(self, data):
        a_count = data.count('a')
        b_count = data.count('b')

        total_count = a_count + b_count
        a_range = (0, a_count / total_count)
        b_range = (a_range[1], 1)

        low, high = 0.0, 1.0
        for symbol in data:
            if symbol == 'a':
                low, high = low + (high - low) * a_range[0], low + (high - low) * a_range[1]
            elif symbol == 'b':
                low, high = low + (high - low) * b_range[0], low + (high - low) * b_range[1]
            else:
                raise ValueError("Invalid symbol")
        return low, high

    def decode(self, encoded_value, length, a_count, b_count):
        decoded_data = ""
        total_count = a_count + b_count
        a_range = (0, a_count / total_count)
        b_range = (a_range[1], 1)

        for _ in range(length):
            if a_range[0] <= encoded_value < a_range[1]:
                decoded_data += 'a'
                encoded_value = (encoded_value - a_range[0]) / (a_range[1] - a_range[0])
            elif b_range[0] <= encoded_value < b_range[1]:
                decoded_data += 'b'
                encoded_value = (encoded_value - b_range[0]) / (b_range[1] - b_range[0])
            else:
                raise ValueError("Invalid encoded value")
        return decoded_data

# 创建算术编码器
arithmetic_encoder = ArithmeticEncoder()

# 生成随机字符串
random_string = ''.join(random.choices(['a', 'b'], k=30))
print("随机生成的字符串:", random_string)

# 编码
low, high = arithmetic_encoder.encode(random_string)
print("编码后的范围:", (low, high))

# 计算编码后数据的长度
encoded_length = -1 * (low - high).as_integer_ratio()[1].bit_length()
print("编码后数据的长度:", encoded_length)

# 计算压缩比
compression_ratio = len(random_string) / encoded_length
print("压缩比:", compression_ratio)

# 解码
decoded_string = arithmetic_encoder.decode((low + high) / 2, len(random_string), random_string.count('a'), random_string.count('b'))
print("解码后的字符串:", decoded_string)