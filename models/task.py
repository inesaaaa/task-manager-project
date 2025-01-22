class Task:
    def __init__(self, task_id, description, is_done=False):
        self.id = task_id
        self.description = description
        self.is_done = is_done

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "is_done": self.is_done,
        }
