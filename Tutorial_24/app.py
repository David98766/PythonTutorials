from dao.TaskDao import TaskDao
from flask import (Flask, render_template, request,
                   redirect,
                   url_for)
app = Flask(__name__)

taskDao = TaskDao()

@app.route('/')
def index():
    # Example here showing we can make TaskDao object anywhere will call the original created on top
    task_Dao = TaskDao()
    # using Dao to get all tasks from the object
    tasks = task_Dao.get_all_tasks()
    return render_template('index.html',
                           tasks=tasks)


@app.route('/create', methods=['GET', 'POST'])
def create_task():
    # handling for when the request type is post
    if request.method == 'POST':
        #getting data from the form
        taskName = request.form['taskName']
        taskCategory = request.form['taskCategory']
        # calling the crated method for the TaskDao
        taskDao.create_task(taskName, taskCategory)
        # redirecting back to index endpoint
        return redirect(url_for('index'))

# this part is separate just for get requests when retrieving page
    return render_template('create.html')

# taking url argument of Task ID
@app.route('/mark_completed/<int:task_id>', methods=['POST'])
def mark_completed(task_id):
    # calling method from TaskDao to set boolean to true
    taskDao.mark_task_done(task_id)
    # redirecting back to index endpoint
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)