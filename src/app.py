import os
from flask import Flask, render_template, request, redirect
from db import InMemoryDatabase
from common.task import Task

app = Flask(__name__)
tasks = InMemoryDatabase()

@app.route("/")
def root():
    return render_template('index.html', tasks=tasks.load_all())

@app.post("/tasks/")
def add_task():
    tasks.store(Task(request.form['task_name'], False))
    return redirect('/')

@app.post("/finish/")
def finish_task():
    tasks.load(request.form['task_name']).is_completed = True
    return redirect('/')


PORT = os.environ["PORT"]
HOST = os.environ["HOST"]

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
