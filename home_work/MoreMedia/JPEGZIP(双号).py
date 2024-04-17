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

# 对量化的结果进行Z字形行程编码
def encode(matrix):
    result = []
    rows, cols = matrix.shape
    i, j = 0, 0
    forward = True  # Flag indicating whether we are currently moving forward in the zigzag pattern
    while i < rows and j < cols:
        result.append(matrix[i, j])
        if forward:  # Moving up-right
            if i == 0 or j == cols - 1:
                forward = False
                if j == cols - 1:
                    i += 1
                else:
                    j += 1
            else:
                i -= 1
                j += 1
        else:  # Moving down-left
            if i == rows - 1 or j == 0:
                forward = True
                if i == rows - 1:
                    j += 1
                else:
                    i += 1
            else:
                i += 1
                j -= 1
    return result

# 恢复Z字形行程编码结果为原始矩阵
def zigzag_decode(encoded_data):
    matrix = np.zeros((8, 8))
    i, j = 0, 0
    forward = True
    for num in encoded_data:
        matrix[i, j] = num
        if forward:
            if i == 0 or j == 8 - 1:
                forward = False
                if j == 8 - 1:
                    i += 1
                else:
                    j += 1
            else:
                i -= 1
                j += 1
        else:
            if i == 8 - 1 or j == 0:
                forward = True
                if i == 8 - 1:
                    j += 1
                else:
                    i += 1
            else:
                i += 1
                j -= 1
    return matrix

# 对量化的结果进行Z字形行程编码
encoded_data = encode(quantized_matrix)

# 将Z字形行程编码结果恢复成原始矩阵
decoded_matrix = zigzag_decode(encoded_data)

# 打印结果
print("原始矩阵:")
print(matrix)
print("---------------------------------")
print("量化后的矩阵:")
print(quantized_matrix)
print("---------------------------------")
print("Z字形行程编码后的结果:")
print(encoded_data)
print("---------------------------------")
print(" :")
print(decoded_matrix)