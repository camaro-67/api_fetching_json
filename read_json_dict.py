# Python program to demonstrate
# Conversion of JSON data to
# dictionary
import urllib.request
url = "http://127.0.0.1:8000/dishes"

response = urllib.request.urlopen(url)

# importing the module
import json
data = json.loads(response.read())
print("Print at first")
for i in data['data']:
    print(i['relationships']['restaurant']['links']['related'])
print(type(data))
print("data :")
print(data)
# Opening JSON file
print("data['data']:")
print(data['data'])
print(type(data['data']))
print("Attributes : ")
for i in data['data']:
    print(i['attributes']['name'],",",i['attributes']['rating'])
print("\n")
print("Relationships : ")
for i in data['data']:
    print(i['relationships']['restaurant'])

print("\n")
print("Links : ")
for i in data['data']:
    print(i['relationships']['restaurant']['links']['related'])