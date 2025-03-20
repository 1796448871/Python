import numpy as np
import matplotlib.pyplot as plt

# 1. 随机生成20个学生的成绩
np.random.seed(0)  # 设置随机种子以便结果可复现
num_students = 20
num_subjects = 7
scores = np.random.randint(0, 101, size=(num_students, num_subjects))

# 2. 获取每一门课程的单科成绩排名和最高分
subject_ranks = np.argsort(scores, axis=0) + 1  # 排名
subject_max_scores = np.max(scores, axis=0)  # 最高分

# 3. 获取每个学生的平均分排名以及平均分最高分学生的序号
average_scores = np.mean(scores, axis=1)
average_ranks = np.argsort(average_scores) + 1  # 平均分排名
highest_average_index = np.argmax(average_scores)  # 平均分最高分学生序号

# 打印结果
print("Ranking for each subject:")
print(subject_ranks)
print("\nHighest score for each subject:")
print(subject_max_scores)
print("\nAverage score ranking for each student:")
print(average_ranks)
print("\nIndex of the student with the highest average score:", highest_average_index)

# 4. 可视化
# a) 每一门课程的及格率和不及格率（饼状图）
pass_threshold = 60
pass_rates = np.sum(scores >= pass_threshold, axis=0) / num_students
fail_rates = 1 - pass_rates
subjects = ["Chinese", "Math", "English", "Physics", "Chemistry", "Biology", "PE"]
fig, ax = plt.subplots(1, 7, figsize=(20, 5))
for i in range(num_subjects):
    ax[i].pie([pass_rates[i], fail_rates[i]], labels=["Pass", "Fail"], autopct='%1.1f%%')
    ax[i].set_title(subjects[i])
plt.show()

# b) 不同课程的平均分比较（柱状图）
subject_averages = np.mean(scores, axis=0)
plt.bar(subjects, subject_averages, color='skyblue')
plt.xlabel("Subjects")
plt.ylabel("Average Score")
plt.title("Comparison of Average Scores Across Subjects")
plt.show()