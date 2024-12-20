from abc import ABC, abstractmethod

# Абстракция


class Control(ABC):
    """Устройство

    Args:
        ABC (_type_): _description_
    """

    def __init__(self, device):
        self.device = device

    @abstractmethod
    def func(self):
        raise NotImplementedError
