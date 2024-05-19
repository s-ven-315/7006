def get_step_label():
	return {
		"step1" : "Accident details",
		"step2" : "Driver Details",
		"step3" : "Policy Details",
		"step4" : "Claim Processing Details",
		"step5" : "Summary",
		"step6" : "Result",
	}

def get_question_label():
	return {
		"accidentDate" : "When did the accident happen?",
		"claimedDate" : "When was the claim reported?",
		"AccidentArea" : "What is the classification of the area where the accident occurred?",
		"Make" : "Who is the manufacturer of the vehicle involved in the claim?",
		"Sex" : "What is the gender of the claimant?",
		"MaritalStatus" : "What is the marital status of the claimant?",
		"Age" : "What is the age of the claimant?",
		"Fault" : "Who was found to be at fault in the accident?",
		"VehicleCategory" : "What type of vehicle was involved in the accident?",
		"VehiclePrice" : "What was the original cost new of the vehicle involved in the accident?",
		"RepNumber" : "What is the unique identifier of the claims adjuster who handled this claim?",
		"Deductible" : "What is the amount the insured must pay before the insurer begins paying for repairs?",
		"DriverRating" : "Provide the driver's rating.",
		"Days_Policy_Accident" : "How many days were there between policy inception and the reported date of the accident?",
		"Days_Policy_Claim" : "How many days were there between policy inception and the date the claim was reported?",
		"PastNumberOfClaims" : "How many prior claims are there on the insured's policy?",
		"AgeOfVehicle" : "How old is the vehicle involved in the accident?",
		"AgeOfPolicyHolder" : "What is the age group of the policyholder?",
		"PoliceReportFiled" : "Was a police report filed at the time of the accident?",
		"WitnessPresent" : "Were any witnesses present at the time of the accident?",
		"AgentType" : "What type of agent is handling the claim?",
		"NumberOfSuppliments" : "How many additional payments were issued on the claim?",
		"AddressChange_Claim" : "How many days were there between the most recent policyholder change of address and the date the claim was reported?",
		"NumberOfCars" : "How many vehicles are on the policy?",
		"BasePolicy" : "What type of base policy does the policyholder have?",
	}

def get_options_set():
	return {
		"AccidentArea": {
			"Rural": 0,
			"Urban": 1
		},
		"Make": {
			"Accura": 0,
			"BMW": 1,
			"Chevrolet": 2,
			"Dodge": 3,
			"Ferrari": 4,
			"Ford": 5,
			"Honda": 6,
			"Jaguar": 7,
			"Lexus": 8,
			"Mazda": 9,
			"Mecedes": 10,
			"Mercury": 11,
			"Nisson": 12,
			"Pontiac": 13,
			"Porche": 14,
			"Saab": 15,
			"Saturn": 16,
			"Toyota": 17,
			"VW": 18
		},
		"Sex" : {
			"Male": 1,
			"Female": 0
		},
		"MaritalStatus": {
			"Single": 2,
			"Married": 1,
			"Divorced": 0,
			"Widow": 3
		},
		"Fault": {
			"Policy Holder": 0,
			"Third Party": 1
		},
		"VehicleCategory": {
			"Sedan" : 0,
			"Sport" : 1,
			"Utility" : 2
		},
		"VehiclePrice" : {
			"less than 20000" : 4,
			"20000 to 29000" : 0,
			"30000 to 39000" : 1,
			"40000 to 59000" : 2,
			"60000 to 69000" : 3,
			"More than 69000" : 5
		},
		"Days_Policy_Accident" : {
			"None": 4,
			"1 to 7": 0,
			"8 to 15": 2,
			"15 to 30": 1,
			"More than 30": 3,
		},
		"Days_Policy_Claim" : {
			"None": 3,
			"8 to 15": 1,
			"15 to 30": 0,
			"More than 30": 2,
		},
		"PastNumberOfClaims" : {
			"None": 3,
			"1": 0,
			"2 to 4": 1,
			"More than 4": 2,
		},
		"AgeOfVehicle" : {
			"New": 7,
			"2 years": 0,
			"3 years": 1,
			"4 years": 2,
			"5 years": 3,
			"6 years": 4,
			"7 years": 5,
			"More than 7": 6,
		},
		"AgeOfPolicyHolder" : {
			"16 to 17" : 0,
			"18 to 20" : 1,
			"21 to 25" : 2,
			"26 to 30" : 3,
			"31 to 35" : 4,
			"36 to 40" : 5,
			"41 to 50" : 6,
			"51 to 65" : 7,
			"over 65" : 8,
		},
		"PoliceReportFiled" : {
			"No": 0,
			"Yes": 1,
		},
		"WitnessPresent" : {
			"No": 0,
			"Yes": 1,
		},
		"AgentType" : {
			"External": 0,
			"Internal": 1,
		},
		"NumberOfSuppliments" : {
			"None" : 3,
			"1 to 2" : 0,
			"3 to 5" : 1,
			"More than 5" : 2,
		},
		"AddressChange_Claim" : {
			"No change" : 3,
			"1 year" : 0,
			"2 to 3 years" : 1,
			"4 to 8 years" : 2,
			"Under 6 months" : 4,
		},
		"NumberOfCars" : {
			"1 vehicle": 0,
			"2 vehicles": 1,
			"3 to 4": 2,
			"5 to 8": 3,
			"More than 8": 4,
		},
		"BasePolicy" : {
			"All Perils" : 0,
			"Collision" : 1,
			"Liability" : 2,
		}
	}