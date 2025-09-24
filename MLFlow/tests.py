# importing the requests library
import requests

# api-endpoint
TEST1 = "http://0.0.0.0:8000/predict"
TEST2 = "http://0.0.0.0:8000/update-model"

# defining a params dict for the parameters to be sent to the API
data_predict = {"X_pred": [5.7,3.8,1.7,0.3]}
data_update = {"version" : 2}

# sending get request and saving the response as response object
request2 = requests.post(url= TEST2, json = data_update)
request3 = requests.post(url = TEST1, json = data_predict)

# extracting data in json format
data2 = request2.text
data3 = request3.text

print(data2)
print(data3)