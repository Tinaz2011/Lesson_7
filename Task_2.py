class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'All material is: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Smth vary abstract'


class Coat(Clothes):
    def consumption(self):
        return f'For coat: {self.param / 6.5 + 0.5 :.2f} of material'

    def abstract(self):
        return 'Smth vary abstract second'


class Costume(Clothes):
    def consumption(self):
        return f'For suit: {2 * self.param + 0.3 :.2f} of material'

    def abstract(self):
        pass


coat = Coat(400)
costume = Costume(55)
print(coat.consumption)
print(costume.consumption())
print(coat.abstract())
