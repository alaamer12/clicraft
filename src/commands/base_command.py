from abc import ABCMeta, abstractmethod
from docker import Docker


class ICommand(metaclass=ABCMeta):


    def __init__(self, docker_it):
        if docker_it:
            self.docker = docker_it
    @abstractmethod
    def execute(self):
        pass