# This one's really simple, so I'll just use a classic example. 
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        print(f"Hello. My name is {self.first_name} {self.last_name}.")
        if (self.first_name == "Inigo" and self.last_name == "Montoya"): 
            print("You killed my father. Prepare to die.")

# Class Junior_Dev inherits from class Person
class Junior_Dev(Person):
    def __init__(self):
        Person.__init__(self, "Code", "Monkey")
    
    # Method override
    def greeting(self):
        # Calling method from parent class
        Person.greeting(self)
        print("Halp.")

# Instantiating the Junior_Dev class. 
jd = Junior_Dev()
# Why yes, I did initially write
# Junior_Dev jd = new Junior_Dev();
# How did you know? 
jd.greeting()
