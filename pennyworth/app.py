import curses, npyscreen
from pennyworth.event_manager import EventManager
from pennyworth.list_manager import ListManager
from pennyworth.task_list import MainList, MainDetails, SubList, SubDetails

class App(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Pennyworth")

class MainForm(npyscreen.FormBaseNew):
    def create(self):

        # Custom Keybindings
        custom_handlers = {
            ord('q'): exit,
        }

        self.add_handlers(custom_handlers)

        # List Manager
        self.list_manager = ListManager()

        # Event Manager
        self.event_manager = EventManager(form=self)

        # Form UI
        y, x = self.useable_space()

        self.main_list = self.add(
            MainList, name="Tasks",
            relx=1, 
            max_width=x // 4,
            rely=2, 
            max_height=-5 )

        self.sub_list = self.add(
            SubList,
            name='Subtasks',
            relx=self.main_list.max_width + 1, 
            max_width=self.main_list.max_width,
            rely=2, 
            max_height=-5 )
        
        self.main_details = self.add(
            MainDetails,
            name='Task Details',
            editable=False,
            values=[str(i) for i in range(500)],
            relx=self.main_list.max_width + self.sub_list.max_width + 1,
            rely=2, 
            max_height=(y // 2) - 5 )
        
        self.sub_details = self.add(
            SubDetails,
            name='Subtask Details',
            editable=False,
            relx=self.main_list.max_width + self.sub_list.max_width + 1,
            rely=self.main_details.max_height + 2,
            max_height=-5)

        self.sub_list.create(values=[])
        self.main_list.create(values=self.list_manager.get_tasks())

    # Events
    def dispatch(self, event, *args, **kwargs):
        self.event_manager.manage_event(event, *args, **kwargs)
