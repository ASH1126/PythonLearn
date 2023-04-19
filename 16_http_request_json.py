import requests
import json
import pprint

r = requests.get(
    "https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple"
)
# print(r.status_code)
# print(r.text)

question = json.loads(r.text)
# print(question, type(question))

# pprint.pprint(question)

print(question["results"][0]["category"])
print(question["results"][0]["incorrect_answers"])

person = {"Name": "John", "Age": 35}
person_json = json.dumps(person)
print(type(person_json), person_json)
