from pyPantry.DesignPatterns import PyDesignPatterns


class PyModelViewControllerPattern(PyDesignPatterns):
    # Model
    class TaskModel:
        def __init__(self):
            self.tasks = []
            self.observers = []

        def add_task(self, task):
            self.tasks.append(task)
            self.notify_observers()

        def remove_task(self, task):
            self.tasks.remove(task)
            self.notify_observers()

        def get_tasks(self):
            return self.tasks

        def add_observer(self, observer):
            self.observers.append(observer)

        def notify_observers(self):
            for observer in self.observers:
                observer.update()

    # View
    class TaskView:
        @staticmethod
        def display_tasks(tasks):
            print("Task List:")
            for task in tasks:
                print(f"- {task}")

    # Controller
    class TaskController:
        def __init__(self, model, view):
            self.model = model
            self.view = view
            self.model.add_observer(self)

        def add_task(self, task):
            self.model.add_task(task)

        def remove_task(self, task):
            self.model.remove_task(task)

        def update(self):
            tasks = self.model.get_tasks()
            self.view.display_tasks(tasks)

    def example(self):
        # Initialize the model, view, and controller
        model = PyModelViewControllerPattern.TaskModel()
        view = PyModelViewControllerPattern.TaskView()
        controller = PyModelViewControllerPattern.TaskController(model, view)

        # Add and remove tasks
        controller.add_task("Task 1")
        controller.add_task("Task 2")
        controller.remove_task("Task 1")
