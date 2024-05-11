def get_question_label():
	return {
		"accidentDate" : "Date of Accident",
		"claimedDate" : "Date of claimed happen",
		"AccidentArea" : "Area of accident",
		"Make" : "Manufacturer",
		"Sex" : "Gender",
		"MaritalStatus" : "Marital status",
		"Age" : "Age",
		"Fault" : "Fault",
		"VehicleCategory" : "Category",
		"VehiclePrice" : "Price",
		"RepNumber" : "Representative number",
		"Deductible" : "a",
		"DriverRating" : "Rating",
		"Days_Policy_Accident" : "a",
		"Days_Policy_Claim" : "a",
		"PastNumberOfClaims" : "a",
		"AgeOfVehicle" : "Age",
		"AgeOfPolicyHolder" : "a",
		"PoliceReportFiled" : "a",
		"WitnessPresent" : "ac",
		"AgentType" : "Agent type",
		"NumberOfSuppliments" : "a",
		"AddressChange_Claim" : "a",
		"NumberOfCars" : "Number of cars",
		"BasePolicy" : "a",
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
			"Female": 0,
			"Male": 1
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
			"more than 69000" : 5
		},
		"Days_Policy_Accident" : {
			"none": 4,
			"1 to 7": 0,
			"8 to 15": 2,
			"15 to 30": 1,
			"more than 30": 3,
		},
		"Days_Policy_Claim" : {
			"none": 3,
			"8 to 15": 1,
			"15 to 30": 0,
			"more than 30": 2,
		},
		"PastNumberOfClaims" : {
			"none": 3,
			"1": 0,
			"2 to 4": 1,
			"more than 4": 2,
		},
		"AgeOfVehicle" : {
			"new": 7,
			"2 years": 0,
			"3 years": 1,
			"4 years": 2,
			"5 years": 3,
			"6 years": 4,
			"7 years": 5,
			"more than 7": 6,
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
			"none" : 3,
			"1 to 2" : 0,
			"3 to 5" : 1,
			"more than 5" : 2,
		},
		"AddressChange_Claim" : {
			"no change" : 3,
			"1 year" : 0,
			"2 to 3 years" : 1,
			"4 to 8 years" : 2,
			"under 6 months" : 4,
		},
		"NumberOfCars" : {
			"1 vehicle": 0,
			"2 vehicles": 1,
			"3 to 4": 2,
			"5 to 8": 3,
			"more than 8": 4,
		},
		"BasePolicy" : {
			"All Perils" : 0,
			"Collision" : 1,
			"Liability" : 2,
		}
	}