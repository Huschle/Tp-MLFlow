# importing the requests library
import requests

# api-endpoint
TEST1 = "http://0.0.0.0:8000/predict"
TEST2 = "http://0.0.0.0:8000/update-model"
TEST3 = "http://0.0.0.0:8000/accept-next-model"

# defining a params dict for the parameters to be sent to the API
data_predict = {"X_pred": [5.7,3.8,1.7,0.3]}
data_update1 = {"version" : 1}
data_update2 = {"version" : 2}


# sending get request and saving the response as response object
request1 = requests.post(url= TEST1, json = data_predict)
request2 = requests.post(url= TEST2, json = data_update1)
request3 = requests.post(url= TEST1, json = data_predict) # Tjr le meme modèle
request4 = requests.post(url=TEST3, json='') # On change le modèle
request5 = requests.post(url= TEST1, json = data_predict) # On predict sur le nouveau modèle
request6 = requests.post(url= TEST2, json = data_update2)
request7 = requests.post(url=TEST3, json='') # On change le modèle





# extracting data in json format
data1 = request1.text
data2 = request2.text
data3 = request3.text
data4 = request4.text
data5 = request5.text
data6 = request6.text
data7 = request7.text

print(data1)
print(data2)
print(data3)
print(data4)
print(data5)
print(data6)
print(data7)
