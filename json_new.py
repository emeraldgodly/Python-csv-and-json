import json
with open('test_data.json') as f:
  data = json.load(f)




for i in range(len(data)):

  print(i,data[i]['name'],' => ',type(data[i]['name']))



