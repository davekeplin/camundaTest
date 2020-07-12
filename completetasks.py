import requests
import json
import pycamunda.task
import pycamunda

URL = "http://localhost:8080/engine-rest/"
TASK = "findPiece"

def complete_some_task(key):
	print("Started")
	tasks = []
	try: 
		tasks = pycamunda.task.GetList(url=URL, task_definition_key=key)()
	except pycamunda.PyCamundaException:
		pass
	for t in json.loads(response.text):
		tasks.append(t)

	for i, t in enumerate(tasks):
		if t.task_definition_key != key:
			del tasks[i]
	
	for task in tasks:
		try:
			pycamunda.task.Complete(url=URL, id_=task.id_)()
		except pycamunda.PyCamundaException:
			pass

	print("Completed tasks.")


if __name__ == "__main__":

	complete_some_task(TASK)

