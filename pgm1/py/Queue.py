class Queue:
    def __init__(self, strat) -> None:
        self.strat = strat

    def add(self, input):
        self.strat.add(input)

    def get(self):
        pass

    def remove(self):
        pass

    def size(self):
        pass

    def clear(self):
        pass

    def change_strats(self, new_strat):
        pass
