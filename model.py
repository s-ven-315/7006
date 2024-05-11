import pickle
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from static import get_question_label,get_options_set
from imblearn.combine import SMOTEENN

from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, confusion_matrix

model_filename = 'model/best_KNN_model.pkl'

with open(model_filename, 'rb') as file:
	model = pickle.load(file)

print(model)
# Load data
@st.cache_data
def load_and_preprocess_data():
	df = pd.read_csv("encoded_df.csv")

	X_ml = df.drop(columns=['FraudFound_P', 'matchPolicy'], axis=1)
	y_ml = df['FraudFound_P']

	smote_enn = SMOTEENN(random_state=42)
	X_ml, y_ml = smote_enn.fit_resample(X_ml, y_ml)

	X_train_ml, X_val_test_ml, y_train_ml, y_val_test_ml = train_test_split(X_ml, y_ml, test_size=0.2, random_state=42)

	scaler = StandardScaler()
	X_train_scaled_ml = scaler.fit_transform(X_train_ml)

	pca = PCA(n_components=10)
	X_train_ml_pca = pca.fit_transform(X_train_scaled_ml)

	knn_clf = model
	knn_clf.fit(X_train_ml_pca, y_train_ml)

	return scaler, pca, knn_clf

scaler, pca, knn_clf = load_and_preprocess_data()

# Display prediction
def display_prediction(prediction):
	if prediction[0] == 0:
		st.write("Prediction: This is not a fraud case.")
	else:
		st.write("Prediction: This is a fraud case.")

# Run prediction
def fraud_prediction(input_data, scaler, pca):
	input_data_array = np.array(input_data)
	input_data_array = input_data_array.reshape(1, -1)

	X_scaled = scaler.transform(input_data_array)

	X_pca = pca.transform(X_scaled)
	y_pred = knn_clf.predict(X_pca)
	display_prediction(y_pred)

# Form
def main():
	st.title("Fraud prediction web app")

	questions_label = get_question_label()
	options_set = get_options_set()

	inputs = {}
	radio_fields = ["AccidentArea","Sex","MaritalStatus","Fault","VehicleCategory","DriverRating","PoliceReportFiled","WitnessPresent","AgentType","BasePolicy"]
	for field, options in questions_label.items():
		if field in ["accidentDate", "claimedDate"]:
			inputs[field] = st.date_input(options)
		elif field in ["Age"]:
			inputs[field] = st.number_input(options, min_value=16, max_value=99, step=1)
		elif field in ["RepNumber"]:
			inputs[field] = st.number_input(options, min_value=1, max_value=16, step=1)
		elif field in ["Deductible"]:
			inputs[field] = st.radio( options, (300,400,500,700))
		elif field in ["DriverRating"]:
			inputs[field] = st.radio( options, (1,2,3,4))
		elif field in radio_fields:
			inputs[field] = st.radio( options, list(options_set[field].keys() ))
		else:
			inputs[field] = st.selectbox(options, options_set[field].keys())

	if st.button("Predict"):
		user_input = [
			inputs["accidentDate"].month, inputs["accidentDate"].weekday(), week_of_month(inputs["accidentDate"]),
			options_set["Make"][inputs["Make"]], options_set["AccidentArea"][inputs["AccidentArea"]],
			inputs["claimedDate"].weekday(), inputs["claimedDate"].month, week_of_month(inputs["claimedDate"]),
			options_set["Sex"][inputs["Sex"]], options_set["MaritalStatus"][inputs["MaritalStatus"]],
			inputs["Age"], options_set["Fault"][inputs["Fault"]], options_set["VehicleCategory"][inputs["VehicleCategory"]],
			options_set["VehiclePrice"][inputs["VehiclePrice"]], inputs["RepNumber"], inputs["Deductible"],
			inputs["DriverRating"], options_set["Days_Policy_Accident"][inputs["Days_Policy_Accident"]],
			options_set["Days_Policy_Claim"][inputs["Days_Policy_Claim"]], options_set["PastNumberOfClaims"][inputs["PastNumberOfClaims"]],
			options_set["AgeOfVehicle"][inputs["AgeOfVehicle"]], options_set["AgeOfPolicyHolder"][inputs["AgeOfPolicyHolder"]],
			options_set["PoliceReportFiled"][inputs["PoliceReportFiled"]], options_set["WitnessPresent"][inputs["WitnessPresent"]],
			options_set["AgentType"][inputs["AgentType"]], options_set["NumberOfSuppliments"][inputs["NumberOfSuppliments"]],
			options_set["AddressChange_Claim"][inputs["AddressChange_Claim"]], options_set["NumberOfCars"][inputs["NumberOfCars"]],
			inputs["accidentDate"].year, options_set["BasePolicy"][inputs["BasePolicy"]],
		]

		fraud_prediction(user_input, scaler, pca)

# return the week of the month
def week_of_month(date):
	first_day = date.replace(day=1)
	dom = date.day
	adjusted_dom = dom + first_day.weekday()
	return (adjusted_dom - 1) // 7 + 1

if __name__ == '__main__':
	main()