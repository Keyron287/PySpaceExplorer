from abc import ABC, abstractmethod
from typing import List, final


class Tick_action:
    def execute(self):
        pass


class Tick_subjected(ABC):

    def __init__(self):
        self.actions: List[Tick_action] = []

    def add_action(self, action: Tick_action, duration: int = 1, priority: int = -1):
        pass

    def rem_action(self, action: Tick_action):
        pass

    @abstractmethod
    def begin_tick(self):
        pass

    @final
    def tick(self):
        self.begin_tick()
        action = self.actions.pop(0)
        action.execute()
        self.end_tick()

    @abstractmethod
    def end_tick(self):
        pass

    @abstractmethod
    def on_born(self):
        pass

    @abstractmethod
    def on_death(self):
        pass