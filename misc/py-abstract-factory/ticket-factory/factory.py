from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_ticket(self):
        pass


class JiraFactory(AbstractFactory):
    def create_ticket(self, type):
        if type == 'incident': return IncidentTicket()
        if type == 'problem': return ProblemTicket()


class SnowFactory(AbstractFactory):
    def create_ticket(self, type):
        if type == 'incident': return IncidentTicket()


class FactoryProducer:
    def get_factory(self, type):
        if type == 'jira': return JiraFactory()
        if type == 'snow': return SnowFactory()


# Abstract ticket

class Ticket(ABC):
    @abstractmethod
    def info(self):
        pass


class IncidentTicket(Ticket):
    def info(self):
        return self.__class__.__name__


class ProblemTicket(Ticket):
    def info(self):
        return self.__class__.__name__