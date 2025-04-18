# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 11:20:41 2025

@author: asus
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import numpy as np

# 加载数据集
data = pd.read_csv('WineQT.csv')

# 查看数据集的前几行
print(data.head())

# 计算不同quality的占比
quality_counts = data['quality'].value_counts(normalize=True)

# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(quality_counts, labels=quality_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Quality Distribution')
plt.show()

# 提取特征和目标变量
X = data.drop(columns=['Id', 'quality'])
y = data['quality']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 使用SMOTE对少数类进行过采样
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# 标准化特征
scaler = StandardScaler()
X_train_resampled = scaler.fit_transform(X_train_resampled)
X_test = scaler.transform(X_test)

# 使用支持向量机进行分类
svm = SVC()

# 使用GridSearchCV进行参数调优
#param_grid = {
 #   'C': [0.1, 1, 10, 100],
  #  'gamma': [0.001, 0.01, 0.1, 1],
   # 'kernel': ['rbf', 'linear']
#}


    #'C': np.arange(0.1, 100.1, 10,  # 从0.1到100，步长为10
    #'gamma': np.arange(0.001, 1, 0.1),
#{'C': 10.1, 'gamma': 0.6010000000000001, 'kernel': 'rbf'}
#0.8600380051909529
#Model Accuracy: 0.65

    #'C': np.arange(0.1, 100.1, 5),  # 从0.1到100，步长为5
    #'gamma': np.arange(0.001, 1.001, 0.05),
    #{'C': 5.1, 'gamma': 0.651, 'kernel': 'rbf'}
    #0.8639089729328884
    #Model Accuracy: 0.64
param_grid = {
    'C': np.arange(0.1, 100.1, 20),  # 从0.1到100，步长为20
    'gamma': np.arange(0.001, 1.001, 0.25),
    'kernel': ['rbf', 'linear']
}

grid_search = GridSearchCV(svm, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train_resampled, y_train_resampled)

# 输出最佳参数
print("Best parameters found: ", grid_search.best_params_)
print("Best cross-validation accuracy: ", grid_search.best_score_)
# 使用最佳参数的模型进行预测
best_svm = grid_search.best_estimator_
y_pred = best_svm.predict(X_test)

# 输出分类报告
print(classification_report(y_test, y_pred))

# 计算准确度
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# 绘制混淆矩阵
cm = confusion_matrix(y_test, y_pred)
# 确保display_labels的长度与混淆矩阵的维度一致
display_labels = sorted(y_test.unique())
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=display_labels)
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()