import sys


class ModuleFindChanger():
    @property
    def paths(self):
        for priority, path in enumerate(sys.path, 1):
            print(priority, path)

    @paths.setter
    def paths(self, path: str):
        sys.path.append(path)

    def delete_path_by_priority(self, priority: int):
        sys.path.pop(priority)

    def insert_path_by_priority(self, priority: int, path: str):
        sys.path.insert(priority, path)


changer = ModuleFindChanger()
changer.paths
changer.paths = 'F:\\BTT'
changer.paths
changer.insert_path_by_priority(0, 'F:\\BTT')
changer.paths
changer.delete_path_by_priority(0)
changer.paths
