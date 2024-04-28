import pickle
import numpy as np

with open('model/best_XGBoost_model.pkl', 'rb') as f:
    model = pickle.load(f)

array_30_ones = np.ones(30)

X_test_ml_pca = array_30_ones
print(len(X_test_ml_pca))

# y_pred = model.predict(X_test_ml_pca)
# print(y_pred)