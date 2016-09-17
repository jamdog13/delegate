from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route("/")
def hello():
	mydict = dict()
	mydict["meow"] = 2
	mydict["woof"] = 3
	mydict["task"] = task(owner=["matt","sean"],users=["james"],title="my task",description="do stuff").to_dict()

	return render_template('home.html', text=json.dumps(mydict))


@app.route("/echo", methods=['POST'])
def echo():
    return render_template('echo.html', text="meow")


class task:
	def __init__(self, owner = [], users = [], title = "", description="", subtasks = [], resources = [], state = "To Do"):
		self.owner = owner  # pretty confident I don't need these other than the dict...
		self.users = users
		self.title = title
		self.description = description
		self.subtasks = subtasks
		self.resources = resources
		self.state = state
		self.task_dict = {"owner":self.owner, "users":self.users, "title":self.title, "description":self.description, "subtasks":self.subtasks, "resources":self.resources, "state":self.state}

	def update_self(self, new_dict):
		self.task_dict = new_dict

	def to_dict(self):
		return self.task_dict


class subtask(task): #figure out proper method of subclassing. Needs a parent task. Doesn't have subtasks.
	def __init__(self, owner=[], users=[], title="", description="", subtasks=[], resources=[], state="To Do", parent=""):
		task.__init__(self, owner, users, title, description, subtasks, resources, state)
		self.parent = parent

class user:
	def __init__(self):
		self.username = ""
		self.email = ""
		self.tasks = []
		self.current_task = [] # only one per project
		self.projects = []
		


if __name__ == "__main__":
    app.run(debug=True)
