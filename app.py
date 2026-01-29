from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

DATA_FILE = "tasks.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_tasks():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f)

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    subject = request.form["subject"]
    task = request.form["task"]
    date = request.form["date"]
    time = request.form["time"]
    hours = request.form["hours"]

    tasks = load_tasks()
    tasks.append({
        "subject": subject,
        "task": task,
        "date": date,
        "time": time,
        "hours": hours
    })
    save_tasks(tasks)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
