import requests
import json

# RAPID API LINK : https://rapidapi.com/principalapis/api/currency-conversion-and-exchange-rates/playground/endpoint_01c2f371-2ab0-4e56-98f4-e4f4149e9cfc
url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/timeseries"

start_date = "2025-05-01" #may = 5
end_date = "2025-05-30"
base_currency = "USD"
symbols = "TRY"

querystring = {"start_date":{start_date},"end_date":{end_date},"base":{base_currency},"symbols":{symbols}}

headers = {
    "x-rapidapi-key": "11c830c25emshf8289b2a0f0cecep1a192fjsna96600ee8ec1",
    "x-rapidapi-host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

output = response.json()
output = json.dumps(output, indent=4)
try_file = "/Users/hermann/Documents/Python Course/python_course/data/try.json"
with open (try_file, "w") as try_file:
    try_file.write(output)
    try_file.flush()