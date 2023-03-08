from abc import ABC, abstractmethod


class Validator(ABC):
    def __set__(self, instance, value):
        self.validate(value)
        super().__set__(instance, value)

    @abstractmethod
    def validate(self, value):
        pass
