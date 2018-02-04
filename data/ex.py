import json

with open("meta.txt") as df:
	lines = df.readlines()

questions = []
content = {}
content["title"] = "Gynaecology"

lines = [line.strip() for line in lines]

for i in range(10):
    question = {}
    question["question"] = lines[i * 6]
    question["options"] = [lines[i * 6 + 1], lines[i * 6 + 2], lines[i * 6 + 3], lines[i * 6 + 4], lines[i * 6 + 5]]
    question["answer"] = ""
    questions.append(question)
 
content["questions"] = questions

json.dump(content, open("data.json", "w"))
