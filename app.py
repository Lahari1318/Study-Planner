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
        json.dump(tasks, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    tasks = load_tasks()

    if request.method == "POST":
        subject = request.form["subject"]
        task = request.form["task"]
        date = request.form["date"]
        time = request.form["time"]
        hours = request.form["hours"]

        tasks.append({
            "subject": subject,
            "task": task,
            "date": date,
            "time": time,
            "hours": hours,
            "completed": False
        })

        save_tasks(tasks)
        return redirect("/")

    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:index>")
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect("/")

@app.route("/complete/<int:index>")
def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


