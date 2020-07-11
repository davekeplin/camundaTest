import requests
import json

URL = "http://localhost:8080/engine-rest/"
TASK = "findPiece"

def complete_some_task(key):
	print("Started")
	tasks = []
	try: 
		response = requests.get(URL +"task/", params={"taskDefinitionKey": key})
	except requests.exceptions.RequestException:
		pass
	for t in json.loads(response.text):
		tasks.append(t)

	for i, t in enumerate(tasks):
		if t["taskDefinitionKey"] != key:
			del tasks[i]
	
	for task in tasks:
		try:
			requests.post(URL+"task/{}/complete".format(task["id"]))
		except requests.exceptions.RequestException:
			pass

	print("Completed tasks.")

	
complete_some_task(TASK)

