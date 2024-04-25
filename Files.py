import json
with open('js.json', encoding = 'UTF-8') as file:
    data = json.load(file)
print(data['name'])
for i in range(1, 10): 
    string = '{"number":'+str(i)+'}'
    data = json.loads(string)
print(data["number"])