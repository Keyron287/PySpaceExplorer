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
        self.actions = []
        self.current_action = None

    def add_action(self, action: List[Tick_action], duration: int = 1):
        for a in range(duration - 1):
            self.actions.append([Delay(action[0].msg())])
        self.actions.append(action)

    def rem_action(self, action: Tick_action):
        pass

    def begin_tick(self):
        pass

    # Final impedisce che un metodo sia sovrascritto
    @final
    def tick(self):
        self.begin_tick()
        if len(self.actions) > 0:
            action = self.actions.pop(0)
            for a in action:
                try:
                    self.current_action = a
                    a.execute()
                except Exception as err:
                    print("Error:", err)
            self.end_tick()

    def end_tick(self):
        pass