from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def get_driver(self):
        pass


class HighResFactory(AbstractFactory):
    def get_driver(self, type):
        if type == 'Widget': return HighResDisplayDriver()
        if type == 'Document': return HighResPrintDriver()


class LowResFactory(AbstractFactory):
   def get_driver(self, type):
        if type == 'Widget': return LowResDisplayDriver()
        if type == 'Document': return LowResPrintDriver()
    

class FactoryProducer:
    def get_factory(self, type):
        if type == 'HighRes': return HighResFactory()
        if type == 'LowRes': return LowResFactory()


## Drivers ##

   
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
