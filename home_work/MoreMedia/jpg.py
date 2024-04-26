import numpy as np

# 随机生成一个矩阵，模拟JPEG图像块DCT变换后的结果
random_matrix = np.random.randint(0, 256, (8, 8))

# 色度量化表
quantization_table = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                                [12, 12, 14, 19, 26, 58, 60, 55],
                                [14, 13, 16, 24, 40, 57, 69, 56],
                                [14, 17, 22, 29, 51, 87, 80, 62],
                                [18, 22, 37, 56, 68, 109, 103, 77],
                                [24, 35, 55, 64, 81, 104, 113, 92],
                                [49, 64, 78, 87, 103, 121, 120, 101],
                                [72, 92, 95, 98, 112, 100, 103, 99]])

# 量化
quantized_matrix = np.round(random_matrix / quantization_table)

# Z字形行程编码
def run_length_encoding(matrix):
    encoded = []
    run_length = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] != 0:
                encoded.append((run_length, matrix[i, j]))
                run_length = 0
            else:
                run_length += 1
    if run_length != 0:
        encoded.append((run_length, 0))  # 终止标记
    return encoded

# 反Z字形行程编码
def run_length_decoding(encoded):
    matrix = np.zeros((8, 8))
    i = 0
    j = 0
    for run_length, value in encoded:
        for _ in range(run_length):
            if j < 8:
                matrix[i, j] = 0
                j += 1
            if j == 8:
                j = 0
                i += 1
            if i == 8:
                break
        if i == 8:
            break
        matrix[i, j] = value
        j += 1
        if j == 8:
            j = 0
            i += 1
            if i == 8:
                break
    return matrix

# Z字形行程编码
encoded_matrix = run_length_encoding(quantized_matrix)

# 反Z字形行程编码
decoded_matrix = run_length_decoding(encoded_matrix)

dequantized_matrix = decoded_matrix * quantization_table


print("原始矩阵:")
print(random_matrix)
print("\n量化后矩阵:")
print(quantized_matrix)
print("\nZ字形行程编码后:")
print(encoded_matrix)
print("\n恢复后的矩阵:")
print(dequantized_matrix)