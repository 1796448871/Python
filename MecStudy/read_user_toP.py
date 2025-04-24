import pandas as pd
from joblib import load
import os

# 指定保存模型和预处理工具的文件夹路径
joblib_folder = 'joblib'

# 加载新数据
new_data = pd.read_csv('Ourselves.csv')

# 数据预处理
# 1. 处理缺失值
new_data.dropna(inplace=True)

# 2. 删除与目标变量无关的列（如果有）
new_data.drop(columns=['User ID'], axis=1, inplace=True)

# 3. 加载保存的标签编码器
le_path = os.path.join(joblib_folder, 'label_encoder.joblib')
le = load(le_path)

# 4. 对分类变量进行编码 所用方法：fit_transform
for col in new_data.columns[new_data.dtypes == 'object']:
    new_data[col] = le.fit_transform(new_data[col])

# 5. 加载保存的标准化器
scaler_path = os.path.join(joblib_folder, 'scaler.joblib')
scaler = load(scaler_path)

# 6. 对数值特征进行规范化 所用方法：fit_transform
numeric_df = new_data.select_dtypes(include=['number'])
features_scaled_new = scaler.fit_transform(numeric_df)

# 7. 加载保存的模型
svm_path = os.path.join(joblib_folder, 'svm_model.joblib')
svm = load(svm_path)

rf_path = os.path.join(joblib_folder, 'random_forest_model.joblib')
rf = load(rf_path)

gnb_path = os.path.join(joblib_folder, 'naive_bayes_model.joblib')
gnb = load(gnb_path)

logreg_path = os.path.join(joblib_folder, 'logistic_regression_model.joblib')
logreg = load(logreg_path)

dtree_path = os.path.join(joblib_folder, 'decision_tree_model.joblib')
dtree = load(dtree_path)

# 8. 对新数据进行预测
svm_predictions = svm.predict(features_scaled_new)
rf_predictions = rf.predict(features_scaled_new)
gnb_predictions = gnb.predict(features_scaled_new)
logreg_predictions = logreg.predict(features_scaled_new)
dtree_predictions = dtree.predict(features_scaled_new)

# 9. 输出预测结果
print("SVM Predictions:", svm_predictions)
print("Random Forest Predictions:", rf_predictions)
print("Naive Bayes Predictions:", gnb_predictions)
print("Logistic Regression Predictions:", logreg_predictions)
print("Decision Tree Predictions:", dtree_predictions)