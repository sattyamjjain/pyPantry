from pyPantry.DesignPatterns import PyDesignPatterns


class PyModelViewViewModelPattern(PyDesignPatterns):
    # Model
    class TaskModel:
        def __init__(self):
            self.tasks = []

        def add_task(self, task):
            self.tasks.append(task)

        def remove_task(self, task):
            self.tasks.remove(task)

        def get_tasks(self):
            return self.tasks

    # View
    class TaskView:
        @staticmethod
        def display_tasks(tasks):
            print("Task List:")
            for task in tasks:
                print(f"- {task}")

    # ViewModel
    class TaskViewModel:
        def __init__(self, model):
            self.model = model
            self.tasks = []

        def add_task(self, task):
            self.model.add_task(task)
            self.update_tasks()

        def remove_task(self, task):
            self.model.remove_task(task)
            self.update_tasks()

        def update_tasks(self):
            self.tasks = self.model.get_tasks()

        def get_tasks(self):
            return self.tasks

    def example(self):
        # Initialize the model, view, and viewmodel
        model = PyModelViewViewModelPattern.TaskModel()
        view = PyModelViewViewModelPattern.TaskView()
        viewmodel = PyModelViewViewModelPattern.TaskViewModel(model)

        # Add and remove tasks using the ViewModel
        viewmodel.add_task("Task 1")
        viewmodel.add_task("Task 2")
        viewmodel.remove_task("Task 1")

        # Display tasks using the View
        view.display_tasks(viewmodel.get_tasks())
