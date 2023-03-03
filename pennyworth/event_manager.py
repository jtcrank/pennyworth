import logging
logger = logging.getLogger(__name__)

class EventManager():
    def __init__(self, *args, **kwargs):
        self.form = kwargs['form']
        self.EVENT_MAP = {
            'hover_task': self.hover_task,
            'select_task': self.select_task,
        }

    def select_task(self, list_type, task):
        if list_type == 'main_tasks':
            self.form.main_list.entry_widget.h_select_toggle(None)
            # TODO mark item complete
            # TODO find out how to mark multiple complete on load

    def hover_task(self, list_type, task):
        if list_type == 'main_tasks':
            # Get description and load sublist for task
            self.form.main_details.value = self.form.list_manager.get_task_description(task)
            self.form.sub_list.values = self.form.list_manager.get_subtasks(task)
            # check the box for completed subtasks
            self.form.sub_list.value = []
            for i, v in enumerate(self.form.sub_list.values):
                self.form.sub_list.entry_widget.cursor_line = i
                if self.form.list_manager.is_complete(task=v, parent_task=task):
                    self.form.sub_list.value.append(v)
                    self.form.sub_list.entry_widget.h_select_toggle(None)
            self.form.sub_list.entry_widget.cursor_line = 0

        if list_type == 'subtasks':
            #  logger.info(self.form.main_list.values[self.form.main_list.entry_widget.cursor_line])
            #  self.form.sub_details.value = self.form.list_manager.get_task_description(task=task, parent_task=self.form.main_list.values[self.form.main_list.entry_widget.cursor_line])
            pass

        self.form.display()
        self.form.main_list.display()
        self.form.main_details.display()
        self.form.sub_list.display()
        self.form.sub_details.display()

    def manage_event(self, event, *args, **kwargs):
        #  logger.info(f'\nevent: {event}\nargs: {args}\nkwargs: {kwargs}\n===')
        func = self.EVENT_MAP.get(event)
        if func:
            func(*args, **kwargs)
        else:
            logger.warn(f'Received unbound event "{event}"')
