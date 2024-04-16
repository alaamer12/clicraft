from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    class Docker:
        pass

    @classmethod
    def create_docker_instance(cls):
        return cls.Docker()

class Create(ICommand):
    class Docker:
        def __init__(self):
            pass

        def dockerize(self):
            print("dockerized")
            pass

    def __init__(self, package_manager, docker_it):
        self.__package_manager = package_manager
        self.__docker_it = docker_it
        self.docker_instance = self.create_docker_instance()

    @property
    def package_manager(self):
        return self.__package_manager

    @package_manager.setter
    def package_manager(self, value):
        self.__package_manager = value

    def execute(self):
        pass

class AnotherCommand(ICommand):




    def __init__(self, some_arg):
        self.some_arg = some_arg
        self.docker_instance = self.create_docker_instance()

    def execute(self):
        pass

c = Create("poetry", None)
c.docker_instance.dockerize()
b = AnotherCommand("some_arg")