
# Реализация


class System:
    """Прибор
    """

    def _func(self):
        raise NotImplementedError


class Lamp(System):
    """Лампа
    Args:
        System (_type_): _description_
    """

    def __init__(self):
        self.brightness = 0  # Яркость

    def __str__(self):
        return f"Яркость: {self.brightness}"

    def _func(self):
        """Включить свет
        """
        self.brightness = 100
        return "Лампа включена!"

    


class Thermostat(System):
    """Термостат

    Args:
        System (_type_): _description_
    """

    def __init__(self):
        self.temperature = 25  # Температура

    def __str__(self):
        return f"Температура: {self.temperature}"

    def _func(self):
        """Изменить температуру

        Args:
            temperature (int): _description_

        Returns:
            _type_: _description_
        """
        inlet = int(input("Введите нужную температуру:"))
        self.temperature = inlet
        return f"Температура изменена! {self.temperature} *C"
