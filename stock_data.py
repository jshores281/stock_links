

# take raw API json data and convert to json and csv



import requests
import json
import pandas as pd
import os
from pj_data import *



def INPT():
	URL = input("Enter API URL: ") 
	HEADERS_inp = input("Enter API key: ") 
	QSTRING_inp = input("Enter Company Symbol: ") 

	HEADERS = {"access_key": HEADERS_inp}
	QUERYSTRING = {"symbol": QSTRING_inp}

	JSON_NAME = input("Enter json output file name: ")
	CSV_NAME = input("Enter csv output file name: ")

	API_CALL(URL, HEADERS, QUERYSTRING, JSON_NAME, CSV_NAME)



def API_CALL(URL, HEADERS, QUERYSTRING, JSON_NAME, CSV_NAME):
	r = requests.request('GET', URL, headers=HEADERS, params=QUERYSTRING)
	stock_data = r.content
	
	json_apidata(stock_data, JSON_NAME, CSV_NAME)




def json_apidata(apicall, JSON_NAME, CSV_NAME):
	stock_data_json = json.loads(apicall)
	print(stock_data_json)

	ser_json_data = json.dumps(stock_data_json, indent=4)

	with open(f"{loc}\\{JSON_NAME}", "w") as json_write:
		json_write.write(ser_json_data)
		print("JSON file has completed!")

	API_conv_csv(JSON_NAME, CSV_NAME)




if __name__ == "__main__":
	INPT()


