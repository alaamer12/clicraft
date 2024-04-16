from base_command import ICommand

class Package(ICommand):

    def __init__(self, package_manager, docker_it):
        super().__init__(docker_it)
        self.__package_manager = package_manager

    @property
    def package_manager(self):
        return self.__package_manager

    @package_manager.setter
    def package_manager(self, value):
        self.__package_manager = value

    def __del__(self):
        pass

    def vcs(self):
        pass

    def set_package_manager(self):
        pass

    def execute(self):
        pass