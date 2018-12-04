from abc import ABC, abstractmethod


class BaseParser(ABC):
    def __init__(self, **kwargs):
        self.init(**kwargs)
        super().__init__()

    @abstractmethod
    def init(self, **kwargs):
        pass

    @abstractmethod
    def parse(self, **kwargs):
        pass
