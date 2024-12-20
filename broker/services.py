from abc import ABC, abstractmethod
from .models import Broker

class BrokerServiceI(ABC):
    @abstractmethod
    def save(self, email: str) -> Broker:
        pass

    @abstractmethod
    def find_all(self) -> list:
        pass


class BrokerService(BrokerServiceI):
    @staticmethod
    def save(email: str) -> Broker:
        broker = Broker.create(email)
        broker.save()
        return broker

    def find_all(self) -> list:
        return list(Broker.objects.all())