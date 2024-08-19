from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
from modules import Todo
from connection import session, database
from sqlalchemy import func, desc
app = Flask(__name__)


@app.route('/')
def index():
    # Display todos
    # get tasks current dates from db to display in  todays, upcoming, and due tasks in their respective sessions
    todos = session.query(Todo).order_by(desc(Todo.id)).all()
    current_date = datetime.utcnow().date()
    today_todos = session.query(Todo).filter(func.date(Todo.date) == current_date).all()
    upcoming_todos = session.query(Todo).filter(func.date(Todo.date) > current_date).all()
    due_tasks = session.query(Todo).filter(Todo.date <= current_date, Todo.complete == False).all()
    
    return render_template('index.html', todos=todos, today_todos=today_todos, date=current_date, upcoming_todos=upcoming_todos, due_tasks=due_tasks) 
    
#This is a route to create and add tasks to the database
@app.route("/add", methods=["GET","POST"])
def add():
    title = request.form.get("title")
    desc = request.form.get("desc")
    time = request.form.get("time")
    date = request.form.get("date")
    priority = request.form.get("priority")
    category = request.form.get("category")

    new_todo =Todo(task=title, desc=desc, complete=False, date=date, time=time, priority=priority, category=category)
    session.add(new_todo)
    session.commit()
    return redirect(url_for("index"))

# This updates the tasks to 'Completed' when clicked, if task is not complete 
@app.route("/update/<int:todo_id>", methods=["GET"])
def update(todo_id):
    todo = session.query(Todo).get(todo_id)
    todo.complete = True
    session.commit()
    return redirect(url_for("index"))

# This is to delete the tasks
@app.route("/delete/<int:todo_id>", methods=["GET"])
def delete(todo_id):
    todo = session.query(Todo).get(todo_id)
    session.delete(todo)
    session.commit()
    return redirect(url_for("index"))

# This is a route created to edit each task
@app.route("/edit/<int:todo_id>", methods=["GET", "POST"])
def edit(todo_id):
    todo = session.query(Todo).get(todo_id)

    #if it is a POST request
    if request.method == "POST":
        todo.task = request.form.get("task-title")
        todo.desc = request.form.get("task-desc")
        session.commit()
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo)
    
#search function



@app.route("/Searched", methods=["GET"])
def Searched():
    Searched_arg = request.args.get('Searched')
     # set a loop to filter the task and dispaly empty if todo is not in the index
    if Searched_arg:
        #convert task to lower case
        Searched_lower = Searched_arg.lower()
        #can search with titile, desc, date
        filtered_todos = session.query(Todo).filter(
            func.lower(Todo.task).contains(Searched_lower)  |
            func.lower(Todo.desc).contains(Searched_lower)  |
            func.lower(Todo.date).contains(Searched_lower)  
        ).all()
        return render_template('Searched.html', Searched=Searched_lower, filtered_todos=filtered_todos)
    else:
        return render_template('Searched.html')
    

# order_by(asc(Todo.id)).all
if __name__ == "__main__":
    app.run(debug=True)