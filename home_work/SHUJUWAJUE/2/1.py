import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 适用于 Windows
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
sns.set(font="SimHei", style="whitegrid")  # 适用于 Seaborn 画图


# 读取数据
athlete_data_path = "athlete_events.csv"
noc_data_path = "noc_regions.csv"

athletes = pd.read_csv(athlete_data_path)
noc_regions = pd.read_csv(noc_data_path)

# 处理缺失值（身高、体重缺失值用均值填充，其他删除）
athletes["Height"].fillna(athletes["Height"].mean(), inplace=True)
athletes["Weight"].fillna(athletes["Weight"].mean(), inplace=True)
athletes.dropna(subset=["Sex", "Team", "NOC", "Sport"], inplace=True)

# 关联 NOC 国家数据
athletes = athletes.merge(noc_regions, on="NOC", how="left")

# 田径运动员分析
athletics = athletes[athletes["Sport"] == "Athletics"]

# 1) 田径运动员国籍分布
plt.figure(figsize=(12, 6))
top_countries = athletics["region"].value_counts().head(10)
sns.barplot(x=top_countries.index, y=top_countries.values, palette="viridis")
plt.xticks(rotation=45)
plt.xlabel("国家")
plt.ylabel("运动员数量")
plt.title("田径运动员前10大国籍分布")
plt.show()

# 2) 田径运动员男女比例
plt.figure(figsize=(6, 6))
athletics["Sex"].value_counts().plot.pie(autopct="%1.1f%%", colors=["skyblue", "lightcoral"])
plt.title("田径运动员男女比例")
plt.ylabel("")
plt.show()

# 3) 田径运动员身高和体重分布（按性别）
plt.figure(figsize=(12, 5))
sns.histplot(athletics[athletics["Sex"] == "M"]["Height"], kde=True, color="blue", label="男性")
sns.histplot(athletics[athletics["Sex"] == "F"]["Height"], kde=True, color="red", label="女性")
plt.xlabel("身高 (cm)")
plt.ylabel("频数")
plt.title("田径运动员身高分布")
plt.legend()
plt.show()

plt.figure(figsize=(12, 5))
sns.histplot(athletics[athletics["Sex"] == "M"]["Weight"], kde=True, color="blue", label="男性")
sns.histplot(athletics[athletics["Sex"] == "F"]["Weight"], kde=True, color="red", label="女性")
plt.xlabel("体重 (kg)")
plt.ylabel("频数")
plt.title("田径运动员体重分布")
plt.legend()
plt.show()

# 乒乓球 vs. 网球对比分析
ping_pong = athletes[athletes["Sport"] == "Table Tennis"]
tennis = athletes[athletes["Sport"] == "Tennis"]

# 1) 乒乓球 vs. 网球运动员 身高对比（按性别）
plt.figure(figsize=(12, 5))
sns.kdeplot(ping_pong[ping_pong["Sex"] == "M"]["Height"], label="乒乓球（男）", shade=True, color="blue")
sns.kdeplot(tennis[tennis["Sex"] == "M"]["Height"], label="网球（男）", shade=True, color="red")
plt.xlabel("身高 (cm)")
plt.ylabel("密度")
plt.title("乒乓球 vs. 网球 男运动员身高对比")
plt.legend()
plt.show()

plt.figure(figsize=(12, 5))
sns.kdeplot(ping_pong[ping_pong["Sex"] == "F"]["Height"], label="乒乓球（女）", shade=True, color="blue")
sns.kdeplot(tennis[tennis["Sex"] == "F"]["Height"], label="网球（女）", shade=True, color="red")
plt.xlabel("身高 (cm)")
plt.ylabel("密度")
plt.title("乒乓球 vs. 网球 女运动员身高对比")
plt.legend()
plt.show()

# 2) 乒乓球 vs. 网球运动员 体重对比（按性别）
plt.figure(figsize=(12, 5))
sns.kdeplot(ping_pong[ping_pong["Sex"] == "M"]["Weight"], label="乒乓球（男）", shade=True, color="blue")
sns.kdeplot(tennis[tennis["Sex"] == "M"]["Weight"], label="网球（男）", shade=True, color="red")
plt.xlabel("体重 (kg)")
plt.ylabel("密度")
plt.title("乒乓球 vs. 网球 男运动员体重对比")
plt.legend()
plt.show()

plt.figure(figsize=(12, 5))
sns.kdeplot(ping_pong[ping_pong["Sex"] == "F"]["Weight"], label="乒乓球（女）", shade=True, color="blue")
sns.kdeplot(tennis[tennis["Sex"] == "F"]["Weight"], label="网球（女）", shade=True, color="red")
plt.xlabel("体重 (kg)")
plt.ylabel("密度")
plt.title("乒乓球 vs. 网球 女运动员体重对比")
plt.legend()
plt.show()

# 3) 乒乓球 vs. 网球 国籍分布
plt.figure(figsize=(12, 6))
top_pingpong_countries = ping_pong["region"].value_counts().head(10)
sns.barplot(x=top_pingpong_countries.index, y=top_pingpong_countries.values, palette="Blues_d")
plt.xticks(rotation=45)
plt.xlabel("国家")
plt.ylabel("运动员数量")
plt.title("乒乓球运动员前10大国籍分布")
plt.show()

plt.figure(figsize=(12, 6))
top_tennis_countries = tennis["region"].value_counts().head(10)
sns.barplot(x=top_tennis_countries.index, y=top_tennis_countries.values, palette="Reds_d")
plt.xticks(rotation=45)
plt.xlabel("国家")
plt.ylabel("运动员数量")
plt.title("网球运动员前10大国籍分布")
plt.show()
