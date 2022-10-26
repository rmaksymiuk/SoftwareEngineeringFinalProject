class Client:
    def __init__(self, budget, tasks):
        self.budget = budget
        self.tasks = tasks

    def showBudget(self):
        print(f'Budget: {self.budget}')
    def negotiate(self):
        return