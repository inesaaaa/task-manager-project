import uuid
from utils.file_utils import read_file, write_file
from models.task import Task

class TaskService:
    def __init__(self, file_path="data/tasks.json"):
        self.file_path = file_path

    def get_tasks(self):
        return read_file(self.file_path)

    def add_task(self, description):
        tasks = self.get_tasks()
        task_id = str(uuid.uuid4())
        new_task = Task(task_id, description)
        tasks.append(new_task.to_dict())
        write_file(self.file_path, tasks)

    def mark_task_done(self, task_id):
        tasks = self.get_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["is_done"] = True
                break
        write_file(self.file_path, tasks)
