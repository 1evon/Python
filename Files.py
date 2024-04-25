import json
with open('js.json', encoding = 'UTF-8') as file:
    data = json.load(file)
print(data['name'])
string = '{"number":123456789}'
data = json.loads(string)
print(data["number"])