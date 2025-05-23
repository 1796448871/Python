import numpy as np

# 随机生成一个 8x8 的矩阵，模拟JPEG图像块DCT变换后的结果
matrix = np.random.randint(0, 255, size=(8, 8))

# 使用色度量化表进行量化
color_table = np.array([
    [17, 18, 24, 47, 99, 99, 99, 99],
    [18, 21, 26, 66, 99, 99, 99, 99],
    [24, 26, 56, 99, 99, 99, 99, 99],
    [47, 66, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99]
])

quantized_matrix = np.round(matrix / color_table)


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

dequantized_matrix = decoded_matrix * color_table


print("原始矩阵:")
print(matrix)
print("---------------------------------")
print("量化后的矩阵:")
print(quantized_matrix)
print("---------------------------------")
print("Z字形行程编码后的结果:")
print(encoded_matrix)
print("---------------------------------")
print(decoded_matrix)