import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

""" Preprocessing 预处理 """


# 加载数据集
data = pd.read_csv('user_behavior_dataset.csv')

# 数据清洗：处理缺失值
data.dropna(inplace=True)  
#输出所有None值 对应其列的占比(mean)
print(data.isna().mean())
# 输出重复值得到占比
print(data.duplicated().mean())
# 一些基本信息输出
print(data.info())
# 描述显示:计数（count）：每列非空值的数量 平均值 标准差 最小值……
print(data.describe())




""" EDA 数据探索性分析 """

# 删掉与目标变量无关的列
data.drop(columns=['User ID'], axis=1, inplace=True)

# 展示Behavior Class各值分别的总数
sns.set_style(style='dark')
plt.figure(figsize=(9,6))   #设置窗口大小
plt.title('Distribtution of User Behavior Class ', fontsize=14)
sns.countplot(x=data['User Behavior Class'], palette='magma')   #统计每个类别的出现次数,重要
plt.show()

# 对两个操作系统的各类使用时长的人群进行分类.
plt.figure(figsize=(9,6))
plt.title('Distribtution of Operating System (User Behavior Class) ', fontsize=14)
sns.countplot(x=data['Operating System'], palette='magma', hue=data['User Behavior Class'])
plt.show()

""" 热力图：相关系数为 1 表示完全正相关。
相关系数为 -1 表示完全负相关。
相关系数为 0 表示无相关性。 """
numeric_df = data.select_dtypes(include=['number']) #仅选择原来是数值列,到新的数据框中 
plt.figure(figsize=(9,6))
sns.heatmap(numeric_df.corr(), annot=True)
plt.show()





""" Label Encoding 分类编码处理"""

# 分类变量编码object转化成number
le = LabelEncoder()
for col in data.columns[data.dtypes=='object']:
    data[col] = le.fit_transform(data[col])
print(data,data.shape)

# 数据规范化(只能对number进行处理)
scaler = StandardScaler()
numeric_df = data.select_dtypes(include=['number'])
features_scaled = scaler.fit_transform(numeric_df)

# 对目标变量编码,目标变量不用规范化(虽然原来的目标变量已经很清晰了)
target = data['User Behavior Class']
target_encoded = le.fit_transform(target)

# 使用SMOTE进行过采样
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(features_scaled, target_encoded)

# 从左到右分别表示：训练集测试数据、测试集数据、训练集目标、测试集目标
# train_test_split的参数分别是：输入的特征数据、输入的目标数据、二八分、随机种子
X_train, X_test, y_train, y_test = train_test_split(X_train_resampled, y_train_resampled, test_size=0.2, random_state=42)
print("训练集特征：\n", X_train)






""" Model Buliding 模型训练 """

# 训练SVM模型
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)
svm_report = classification_report(y_test, svm_pred)
svm_cm = confusion_matrix(y_test, svm_pred)

# 训练随机森林模型
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_report = classification_report(y_test, rf_pred)
rf_cm = confusion_matrix(y_test, rf_pred)

# 训练朴素贝叶斯模型
gnb = GaussianNB()
gnb.fit(X_train, y_train)
gnb_pred = gnb.predict(X_test)
gnb_report = classification_report(y_test, gnb_pred)
gnb_cm = confusion_matrix(y_test, gnb_pred)

# 训练逻辑回归模型
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)
logreg_pred = logreg.predict(X_test)
logreg_report = classification_report(y_test, logreg_pred)
logreg_cm = confusion_matrix(y_test, logreg_pred)

# 训练决策树模型
dtree = DecisionTreeClassifier(random_state=42)
dtree.fit(X_train, y_train)
dtree_pred = dtree.predict(X_test)
dtree_report = classification_report(y_test, dtree_pred)
dtree_cm = confusion_matrix(y_test, dtree_pred)


# 创建一个大图，包含多个子图
plt.figure(figsize=(20, 10))

# SVM 混淆矩阵
plt.subplot(2, 3, 1)
sns.heatmap(svm_cm, annot=True, fmt='d')
plt.title('SVM Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')

# 随机森林混淆矩阵
plt.subplot(2, 3, 2)
sns.heatmap(rf_cm, annot=True, fmt='d', cmap='Blues')
plt.title('Random Forest Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')

# 朴素贝叶斯混淆矩阵
plt.subplot(2, 3, 3)
sns.heatmap(gnb_cm, annot=True, fmt='d', cmap='Reds')
plt.title('Naive Bayes Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')

# 逻辑回归混淆矩阵
plt.subplot(2, 3, 4)
sns.heatmap(logreg_cm, annot=True, fmt='d', cmap='Greens')
plt.title('Logistic Regression Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')

# 决策树混淆矩阵
plt.subplot(2, 3, 5)
sns.heatmap(dtree_cm, annot=True, fmt='d', cmap='coolwarm')
plt.title('Decision Tree Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')

# 调整布局并显示
plt.tight_layout()
plt.show()

""" 
 精确率（Precision）：预测为正类的样本中实际为正类的比例，计算公式为 Precision = TP / (TP + FP)
 召回率（Recall）：实际为正类的样本中被预测为正类的比例，计算公式为 Recall = TP / (TP + FN)
 F1分数（F1 Score）：精确率和召回率的调和平均值，计算公式为 F1 = 2 * (Precision * Recall) / (Precision + Recall)
 支持度（Support）：每个类别的样本数量，表示该类别在数据集中的样本数 
""" 
print('\nSVM Classifier\n', svm_report)
print()
print('\nRandom Forest Classifier\n', rf_report)
print()
print('\nNaive Bayes Classifier\n', gnb_report)
print()
print('\nLogistic Regression Classifier\n', logreg_report)
print()
print('\nDecision Tree Classifier\n', dtree_report)