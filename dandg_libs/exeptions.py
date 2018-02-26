class ApolloEx(Exception):
    pass

class ApolloOpenFileEx(ApolloEx):
    def __init__(self, filename):
        self.args = ('Ошибка загрузки файла "{}"'.format(filename),)

class ApolloConvertToIntEx(ApolloEx):
    def __init__(self, value, name):
        self.args = ('Значение параметра "{}" не является целым числом: {}'.format(name, value),)

class ApolloCalculateEx(ApolloEx):
    def __init__(self, value):
        self.args = ('Расчетный параметр имеет отрицательное значение: "{}"'.format(value),)

class ApolloPasreTubeEx(ApolloEx):
    def __init__(self, tube):
        self.args = ('Неверное обозначение профильной трубы в файле конфигурации: "{}"'.format(tube),)

class ApolloEmptyValueEx(ApolloEx):
    def __init__(self, name):
        self.args = ('Значение параметра "{}" не должно быть пустым'.format(name),)

class ApolloNotFoundType(ApolloEx):
    def __init__(self):
        self.args = ('Не удалось определить тип шаблона изделия',)