from abc import ABC, abstractmethod

class AbstractKeyValueStore(ABC):
    """
    Interface / Abstract Base Class for storing key-value pairs.
    """

    @abstractmethod
    def get(self, key):
        """
        Retrieves key-value pair at the given key.
        :param key:
        :return:
        """
        pass

    @abstractmethod
    def put(self, key, value):
        """
        Stores key-value pair at the given key.
        :param key:
        :param value:
        :return:
        """
        pass
