from abc import ABC, abstractmethod
from typing import List, final


class Tick_action(ABC):

    @abstractmethod
    def msg(self) -> str:
        pass

    @abstractmethod
    def execute(self):
        pass


class Delay(Tick_action):

    def __init__(self, msg):
        self.msg = msg

    def msg(self) -> str:
        return self.msg

    def execute(self):
        pass


class Tick_subjected(ABC):

    def __init__(self):
        self.actions: List[List[Tick_action]] = []

    def add_action(self, action: List[Tick_action], duration: int = 1):
        for a in range(duration-1):
            self.actions.append([Delay(action[0].msg())])
        self.actions.append(action)

    def rem_action(self, action: Tick_action):
        pass

    @abstractmethod
    def begin_tick(self):
        pass

    # Final impedisce che un metodo sia sovrascritto
    @final
    def tick(self):
        self.begin_tick()
        action = self.actions.pop(0)
        for a in action:
            try:
                a.execute()
            except Exception as err:
                print("Errore:", err)
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
