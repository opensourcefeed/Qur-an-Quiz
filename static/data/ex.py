import json

with open("meta.txt") as df:
	lines = df.readlines()

questions = []
content = {}
content["title"] = "48. മൂഹമ്മദ്"

lines = [line.strip() for line in lines]
print(len(lines))
for i in range(int(len(lines) / 5)):
    print(i)
    question = {}
    question["question"] = lines[i * 5]
    question["options"] = [lines[i * 5 + 1], lines[i * 5 + 2], lines[i * 5 + 3], lines[i * 5 + 4]]
    question["answer"] = ""
    questions.append(question)
 
content["questions"] = questions

json.dump(content, open("hollywood-2.json", "w"))
