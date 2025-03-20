import pandas as pd



# 读取 Excel 文件
file_path = "my_data.xlsx"  # 替换为你的文件路径
data = pd.read_excel(file_path)

# 显示数据的前几行
print("数据的前几行：")
print(data.head())

# 查看数据的类型和格式
print("\n数据的类型和格式：")
print(data.info())

print("列名：")
print(data.columns)


d_column_data = data.iloc[:, 3]  # 第 4 列（索引从 0 开始）
print("D 列数据：")
print(d_column_data)