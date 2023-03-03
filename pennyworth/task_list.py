import curses, npyscreen

import logging
logger = logging.getLogger(__name__)

class TaskList(npyscreen.MultiSelectAction):
    def __init__(self, *args, **kwargs):
        super(TaskList, self).__init__(*args, **kwargs)
        # attrs
        self.allow_filtering = None
        self.list_type = 'task_list'

        # keybindings
        # TODO set up custom handler for 'L' inside MainList
        new_handlers = {
            curses.KEY_RIGHT: self.h_exit_right,
            ord('l'): self.h_exit_right,
            curses.KEY_LEFT: self.h_exit_left,
            ord('h'): self.h_exit_left,
            ord(';'): self.h_exit_escape
        }
        self.add_handlers(new_handlers)

    def when_cursor_moved(self):
        self.parent.dispatch(
            'hover_task',
            list_type=self.list_type,
            task=self.values[self.cursor_line]
        )
    
    def actionHighlighted(self, act_on_this, keypress):
        self.parent.dispatch(
            'select_task',
            list_type=self.list_type, 
            task=act_on_this
        )

class MainList(npyscreen.BoxTitle):
    _contained_widget = TaskList

    def create(self, **kwargs):
        self.entry_widget.list_type = 'main_tasks'
        self.values = kwargs.get('values', [])

        # Check the box for completed items
        self.value = []
        for i, v in enumerate(self.values):
            self.entry_widget.cursor_line = i
            if self.parent.list_manager.is_complete(task=v):
                self.value.append(v)
                self.entry_widget.h_select_toggle(None)

        self.entry_widget.cursor_line = 0

        self.parent.dispatch(
            'hover_task',
            self.entry_widget.list_type,
            self.entry_widget.values[self.entry_widget.cursor_line]
        )

class SubList(npyscreen.BoxTitle):
    _contained_widget = TaskList

    def create(self, **kwargs):
        self.entry_widget.list_type = 'subtasks'
        self.values = kwargs.get('values', [])


class MainDetails(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

class SubDetails(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit
