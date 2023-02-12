

import json
import pandas as pd
import os
from stock_data import *


loc = os.path.join(os.getcwd())



def API_conv_csv(JSON_NAME, CSV_NAME):

	data = json.load(open(f'{loc}\\{JSON_NAME}'))
	df = pd.DataFrame(data['response'])
	df.to_csv(f'{loc}\\{CSV_NAME}')
	print("CSV file has completed!")

	print(df)




