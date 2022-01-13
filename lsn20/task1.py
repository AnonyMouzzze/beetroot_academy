from datetime import datetime

class OpenFile:
    counter = 0

    def __init__(self, file_directory, mode='r'):
        self.__file_directory = file_directory
        self.__mode = mode
        self.__file = open(file_directory, mode)
        self.__logger = open('logger.txt', 'a')

    def __enter__(self):
        self.__logger.writelines(f'[Open file] Filename: {self.__file_directory}; Mode: {self.__mode}; Time: {datetime.now().time()}\n')
        OpenFile.counter += 1
        return self.__file

    def __exit__(self, type, value, traceback):
        self.__logger.writelines(f'[Close file] Filename: {self.__file_directory}; Time: {datetime.now().time()}\n')
        self.__logger.close()
        return None

    @property
    def closed(self):
        return self.__logger.closed

    @classmethod
    def get_usage_count(cls):
        return cls.counter


