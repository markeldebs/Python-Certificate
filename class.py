class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def full_name(self):
        return person.name +": " +person.age
    
e = person("mike", "11")

print(e.full_name())