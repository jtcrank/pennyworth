import json, os.path, re

import logging
logger = logging.getLogger(__name__)

class ListManager(): 
    def __init__(self, active_list='default'):
        str_path = f'~/.pennyworth/lists/{active_list}.json'
        self.list_path = str_path.replace('~', os.path.expanduser('~'), 1)

        self.task_list = {}
        if not os.path.isfile(self.list_path):
            with open(self.list_path, 'w') as f:
                json.dump({}, f, indent=4)

        with open(self.list_path) as f:
            self.task_list = json.load(f)

    def get_tasks(self):
        return list(self.task_list.keys())

    def is_complete(self, task, parent_task=None):
        if parent_task:
            task = self.task_list[parent_task]['subtasks'][task]
        else:
            task = self.task_list[task]

        return task['complete']

    def get_subtasks(self, task):
        return list(self.task_list[task]['subtasks'].keys())

    def get_task_description(self, task, parent_task=None):
        if parent_task:
            return self.task_list[parent_task]['subtasks'][task]
        else:
            return self.task_list[task]['description']

    def save(self):
        with open(self.list_path) as f:
            json.dump(self.task_list, f, indent=4)

    def toggle_task(self, task, parent_task=None):
        if parent_task:
            task = self.task_list[parent_task]['subtasks'][task]
        else:
            task = self.task_list[task]

        task['complete'] = not task['complete']
        
