import controller as c

class Dictionary:
    def __init__(self, dict=[], language = ""):
        self._dict = dict
        self._language = language

    def loadDictionary(self,path):
        file_path = path
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                line_changed = ""
                for char in line:
                    if char == '/':
                        break
                    else:
                        line_changed += char
                value = line_changed.strip()
                self._dict.append(value.lower())

    def printAll(self):
        for value in self._dict:

            print(f" {value}")


    @property
    def dict(self):
        return self._dict