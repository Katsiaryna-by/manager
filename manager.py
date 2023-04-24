class Task:
    # A class representing a task with a name and a description.

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def __str__(self):
        # A string representation of the task.

        status = "✔" if self.completed else " "
        return f"{[status]} {self.name}: {self.description}"


class TaskManager:
    # A class that represents a task manager with the ability to add, delete, mark completion and edit tasks.
    # Also, the ability to view the current list of tasks.

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                return True
        return False

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return True
        return False

    def edit_task(self, task_name, new_name=None, new_description=None):
        for task in self.tasks:
            if task.name == task_name:
                if new_name is not None:
                    task.name = new_name
                if new_description is not None:
                    task.description = new_description
                return True
        return False

    def view_tasks(self):
        for task in self.tasks:
            print(task)
