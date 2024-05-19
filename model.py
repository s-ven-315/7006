import pickle
import numpy as np
import pandas as pd
import streamlit as st
from streamlit.components.v1 import html
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from static import get_step_label, get_question_label, get_options_set
from imblearn.combine import SMOTEENN

model_filename = 'model/best_KNN_model.pkl'

with open(model_filename, 'rb') as file:
	model = pickle.load(file)

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
		st.write("This claim is legitimate.")
	else:
		st.write("Please proceed further investigation on this case.")

# Run prediction
def fraud_prediction(input_data, scaler, pca):
	input_data_array = np.array(input_data)
	input_data_array = input_data_array.reshape(1, -1)

	X_scaled = scaler.transform(input_data_array)
	X_pca = pca.transform(X_scaled)
	y_pred = knn_clf.predict(X_pca)
	display_prediction(y_pred)


def display_prev_next_button( prev_button="Previous", next_button="Next", hide_prev=False ):
	col1, col2 = st.columns([6, 6])
	with col1:
		if not hide_prev:
			if st.form_submit_button(prev_button, use_container_width=True):
				st.session_state.step -= 1
				st.experimental_rerun()

	with col2:
		if st.form_submit_button(next_button, use_container_width=True):
			st.session_state.step += 1
			st.experimental_rerun()

def main():
	st.title("Fraud Prediction")

	steps_label = get_step_label()
	questions_label = get_question_label()
	options_set = get_options_set()

	def collect_inputs(fields):
		for field in fields:
			options = questions_label[field]
			if field in ["accidentDate", "claimedDate"]:
				st.session_state.inputs[field] = st.date_input(options)
			elif field in ["Age"]:
				st.session_state.inputs[field] = st.number_input(options, min_value=16, max_value=99, step=1)
			elif field in ["RepNumber"]:
				st.session_state.inputs[field] = st.number_input(options, min_value=1, max_value=16, step=1)
			elif field in ["Deductible"]:
				st.session_state.inputs[field] = st.radio(options, (300, 400, 500, 700))
			elif field in ["DriverRating"]:
				st.session_state.inputs[field] = st.radio(options, (1, 2, 3, 4))
			elif field in radio_fields:
				st.session_state.inputs[field] = st.radio(options, list(options_set[field].keys()))
			else:
				st.session_state.inputs[field] = st.selectbox(options, options_set[field].keys())

	radio_fields = ["AccidentArea", "Sex", "MaritalStatus", "Fault", "VehicleCategory", "DriverRating", "PoliceReportFiled", "WitnessPresent", "AgentType", "BasePolicy"]

	step1_fields = ["accidentDate", "claimedDate", "AccidentArea", "VehicleCategory", "VehiclePrice", "Make" ]
	step2_fields = ["Sex", "MaritalStatus", "Age" ]
	step3_fields = ["Days_Policy_Accident", "Days_Policy_Claim", "PastNumberOfClaims", "AgeOfVehicle", "AgeOfPolicyHolder", "BasePolicy"]
	step4_fields = ["RepNumber", "Deductible", "DriverRating", "AddressChange_Claim", "PoliceReportFiled", "WitnessPresent", "AgentType", "NumberOfSuppliments", "NumberOfCars", "Fault" ]
	
	# Initialize session state
	if 'step' not in st.session_state:
		st.session_state.step = 1
		st.session_state.inputs = {}

	step_key = f"step{st.session_state.step}"

	# Step 1: Accident Details
	if st.session_state.step == 1:
		st.header(f"Step {st.session_state.step}: {steps_label[step_key]}")
		with st.form(key='accident_form'):
			collect_inputs(step1_fields)			
			display_prev_next_button(hide_prev=True)

	# Step 2: Driver Details
	elif st.session_state.step == 2:
		st.header(f"Step {st.session_state.step}: {steps_label[step_key]}")
		with st.form(key='driver_form'):
			collect_inputs(step2_fields)
			display_prev_next_button()

	# Step 3: Policy Details
	elif st.session_state.step == 3:
		st.header(f"Step {st.session_state.step}: {steps_label[step_key]}")
		with st.form(key='policy_form'):
			collect_inputs(step3_fields)
			display_prev_next_button()

	# Step 4: Claim Processing Details
	elif st.session_state.step == 4:
		st.header(f"Step {st.session_state.step}: {steps_label[step_key]}")
		with st.form(key='claim_processing_form'):
			collect_inputs(step4_fields)
			display_prev_next_button(next_button="View summary")
	
	# Step 5: Summary
	elif st.session_state.step == 5:
		st.header(f"Step {st.session_state.step}: {steps_label[step_key]}")
		st.write("Please review the information below before submitting:")
		def create_summary_table(step_fields):
			summary_data = {questions_label[field]: st.session_state.inputs.get(field, 'N/A') for field in step_fields}
			df = pd.DataFrame(list(summary_data.items()), columns=["Field", "Value"])
			return df

		st.subheader(steps_label['step1'])
		st.table(create_summary_table(step1_fields))

		st.subheader(steps_label['step2'])
		st.table(create_summary_table(step2_fields))

		st.subheader(steps_label['step3'])
		st.table(create_summary_table(step3_fields))

		st.subheader(steps_label['step4'])
		st.table(create_summary_table(step4_fields))
	
		with st.form(key='summary'):
			display_prev_next_button(next_button="Submit")
	
	# Step 6: Result
	elif st.session_state.step == 6:
		st.header(f"Step {st.session_state.step}: {steps_label[step_key]}")

		inputs = st.session_state.inputs
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

	# Start Over button
	if st.button("Start Over", type="primary"):
		st.session_state.step = 1
		st.session_state.inputs = {}
		st.experimental_rerun()

# Return the week of the month
def week_of_month(date):
	first_day = date.replace(day=1)
	dom = date.day
	adjusted_dom = dom + first_day.weekday()
	return (adjusted_dom - 1) // 7 + 1

if __name__ == '__main__':
	main()