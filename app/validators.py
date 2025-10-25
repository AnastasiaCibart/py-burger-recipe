from abc import ABC, abstractmethod


class Validator(ABC):

    def __set_name__(self, owner: type, name: str) -> None:
        self.protected_name = f"_{name}"

    def __get__(self, instance: object, owner: type) -> None:
        if instance is None:
            return self
        return getattr(instance, self.protected_name)

    def __set__(self, instance: object, value: int) -> None:
        setattr(instance, self.protected_name, value)

    @abstractmethod
    def validate(self, value: int) -> None:
        """Validate the given value."""
        pass


class Number(Validator):
    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Quantity should be integer.")

        if not self.min_value <= value <= self.max_value:
            raise ValueError(
                f"Quantity should not be less than {self.min_value} "
                f"and greater than {self.max_value}."
            )

        self.__set__(self, value)


class OneOf(Validator):
    def __init__(self, options: list[str]) -> None:
        self.options = tuple(options)
        self.value = None

    def validate(self, value: str) -> None:
        if value not in self.options:
            raise ValueError(f"Expected {value} to be one of {self.options}.")
        self.__set__(self, value)

    def __repr__(self) -> str:
        return f"'{self.__get__(self, type(self))}'"
