from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def print_(self):
        pass


class HighResPrintDriver(Document):
    def print_(self):
        print('Printing document with HighResPrintDriver')


class LowResPrintDriver(Document):
    def print_(self):
        print('Printing document with LowResPrintDriver')


class Widget(ABC):
    @abstractmethod
    def draw(self):
        pass


class HighResDisplayDriver(Widget):
    def draw(self):
        print('Drawing widget with HighResDisplayDriver')


class LowResDisplayDriver(Widget):
    def draw(self):
        print('Drawing widget with LowResDisplayDriver')


class DriverFactory(ABC):
    @abstractmethod
    def get_driver(self, type):
        pass


class HighResFactory(DriverFactory):
    def get_driver(self, type):
        if type == 'Widget': return HighResDisplayDriver()
        if type == 'Document': return HighResPrintDriver()


class LowResFactory(DriverFactory):
   def get_driver(self, type):
        if type == 'Widget': return LowResDisplayDriver()
        if type == 'Document': return LowResPrintDriver()


def main():
    # res = 'MedRes'
    # res = 'LowRes'
    res = 'HighRes'

    if res == 'HighRes':
        factory = HighResFactory()
    elif res == 'LowRes':
        factory = LowResFactory()
    else:
        raise NotImplementedError(f"Not implemented for {res}")
    
    printDriver = factory.get_driver('Document')
    displayDriver = factory.get_driver('Widget')

    printDriver.print_()
    displayDriver.draw()


if __name__ == "__main__":
    main()
