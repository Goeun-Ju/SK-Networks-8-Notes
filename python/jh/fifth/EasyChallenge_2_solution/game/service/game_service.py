from abc import ABC, abstractmethod


class GameService(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def getState(self):
        pass

    @abstractmethod
    def convertState(self, currentState, userInputNumber):
        pass

    @abstractmethod
    def updateState(self, state):
        pass
