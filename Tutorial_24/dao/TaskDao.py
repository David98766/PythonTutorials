from datetime import datetime
from Tutorial_24.model.Task import  Task
# Making the class a singleton so it has only one instance
class TaskDao:
    _instance = None  # Class-level variable to hold the single instance
    # the cls key word here refers to the TaskDao itself
    # __new__ is a keyword that is called for us to create object.
    # because it's a singleton we need to override the logic to make sure it's not made twice
    def __new__(cls, *args, **kwargs):
        # if TaskDao hasn't been created yet
        if cls._instance is None:
            # create an object of TaskDao using parent object
            # using super here to use the parent class object to create child
            cls._instance = super(TaskDao, cls).__new__(cls)
            cls._instance.__initialized = False  # Prevent re-initialization
            # return the instance of TaskDao
        return cls._instance

    def __init__(self):
        # Initialising data in the constructor
        self.list = [
            Task(1, "Clean Room",
                 datetime(2024, 2, 1),
                 "Home", False),
            Task(2, "Do Homework",
                 datetime(2024, 2, 2),
                 "School", True),
            Task(3, "Buy Groceries", datetime(2024, 2, 3), "Home", False),
            Task(4, "Workout", datetime(2024, 2, 4), "Personal", True),
            Task(5, "Read a Book", datetime(2024, 2, 5), "Personal", False),
        ]

    def get_all_tasks(self):
        return self.list


    def create_task(self, taskName, taskCategory):
        # grabbing the largest ID so we can increment the id ourselves
        new_id = (max(task.taskId for task in self.list)
                  + 1) if self.list else 1
        new_task = Task(new_id, taskName, datetime.now(), taskCategory,
                        False)
        self.list.append(new_task)
        return new_task

    def mark_task_done(self, task_id):
        # Find the task by task_id and mark it as completed
        for task in self.list:
            if task.taskId == task_id:
                task.isCompleted = True
                return True  # Successfully marked as completed
        return False  # Task not found
