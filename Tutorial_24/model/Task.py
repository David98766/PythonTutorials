
# Creating model to hold data related to task
class Task:
    def __init__(self, taskId, taskName, taskCreationDate,
                 taskCategory, isCompleted):
        self.taskId = taskId
        self.taskName = taskName
        self.taskCreationDate = taskCreationDate
        self.taskCategory = taskCategory
        self.isCompleted = isCompleted


