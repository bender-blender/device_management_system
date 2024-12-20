from system import (
    Thermostat,
    Lamp,
    System
)
from control import Control


class Switch(Control):
    """Включатель

    Args:
        Control (_type_): _description_
    """

    def __init__(self, device: System):
        self.device = device
        super().__init__(device)

    def func(self):
        """Включить устройство
        """

        print(f"Устройство {self.device.__class__.__name__} включено")
        self.device._func()


class SwitchTwo(Control):
    """Выключатель

    Args:
        Control (_type_): _description_
    """

    def __init__(self, device: System):
        self.device = device
        super().__init__(device)

    def func(self):
        """Выключить устройство
        """
        print(f"Устройство {self.device.__class__.__name__} отключено")
        print(self.device.__dict__)
        for key in self.device.__dict__.keys():
            self.device.__dict__[key] = 0
        print(self.device.__dict__)


lamp = Lamp()
termo = Thermostat()
lst = [lamp, termo]

for device in lst:
    print(device)
    switch = Switch(device)
    switch.func()
    switch_two = SwitchTwo(device)
    switch_two.func()
