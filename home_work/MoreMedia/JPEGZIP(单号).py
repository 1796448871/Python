import numpy as np

# 亮度量化表
luminance_quantization_table = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])

# 色度量化表
chrominance_quantization_table = np.array([
    [17, 18, 24, 47, 99, 99, 99, 99],
    [18, 21, 26, 66, 99, 99, 99, 99],
    [24, 26, 56, 99, 99, 99, 99, 99],
    [47, 66, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99]
])


def generate_random_matrix():
    # 随机生成一个8x8的矩阵，表示DCT变换后的结果
    return np.random.randint(0, 256, size=(8, 8))


def quantize(matrix, student_id):
    # 根据学号选择相应的量化表
    if student_id % 2 == 1:  # 奇数学号，使用亮度量化表
        quantization_table = luminance_quantization_table
    else:  # 偶数学号，使用色度量化表
        quantization_table = chrominance_quantization_table

    # 进行量化
    return np.round(matrix / quantization_table)


def zigzag_encode(matrix):
    # Z字形扫描编码
    encoded = []
    i, j = 0, 0
    direction = 1  # 1为向右上，-1为向左下

    for _ in range(8):
        encoded.append(matrix[i, j])

        # 更新下一个元素的坐标
        if direction == 1:
            if i == 0 or j == 7:
                direction = -1
                if j == 7:
                    i += 1
                else:
                    j += 1
            elif j == 0 or i == 7:
                direction = -1
                if i == 7:
                    j += 1
                else:
                    i += 1
            else:
                i -= 1
                j += 1
        else:
            if i == 7 or j == 0:
                direction = 1
                if i == 7:
                    j += 1
                else:
                    i += 1
            elif i == 0 or j == 7:
                direction = 1
                if j == 7:
                    i += 1
                else:
                    j += 1
            else:
                i += 1
                j -= 1

    return encoded


def zigzag_decode(encoded):
    # Z字形扫描解码
    matrix = np.zeros((8, 8))
    i, j = 0, 0
    direction = 1  # 1为向右上，-1为向左下

    for value in encoded:
        matrix[i, j] = value

        # 更新下一个元素的坐标
        if direction == 1:
            if i == 0 or j == 7:
                direction = -1
                if j == 7:
                    i += 1
                else:
                    j += 1
            elif j == 0 or i == 7:
                direction = -1
                if i == 7:
                    j += 1
                else:
                    i += 1
            else:
                i -= 1
                j += 1
        else:
            if i == 7 or j == 0:
                direction = 1
                if i == 7:
                    j += 1
                else:
                    i += 1
            elif i == 0 or j == 7:
                direction = 1
                if j == 7:
                    i += 1
                else:
                    j += 1
            else:
                i += 1
                j -= 1

    return matrix


# 步骤1：随机生成一个矩阵
random_matrix = generate_random_matrix()
print("随机矩阵：")
print(random_matrix)

# 步骤2：对矩阵进行量化
student_id = int(input("请输入你的学号："))
quantized_matrix = quantize(random_matrix, student_id)
print("量化后的矩阵：")
print(quantized_matrix)

# 步骤3：Z字形行程编码
encoded_matrix = zigzag_encode(quantized_matrix)
print("Z字形行程编码后的结果：")
print(encoded_matrix)

# 步骤4：将Z字形行程编码结果恢复成随机矩阵
decoded_matrix = zigzag_decode(encoded_matrix)
print("解码后的矩阵：")
print(decoded_matrix)