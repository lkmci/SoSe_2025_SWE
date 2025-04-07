class Subject():
    def __init__(self, firstname, last, sex, age):
      self.firstname = firstname
      self.last = last
      self.sex = sex
      self.age = age
    
    def __str__(self):
       return f"First: {self.firstname}, Last: {self.last}, Sex: {self.sex}, Age: {self.age}"
    
    def estimate_max_hr(self):
      """A function that estimates the maximum heart rate of a subject"""
      pass

class Supervisor():
    def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name
    def __str__(self):
       return f"Vorname: {self.first_name}, Nachname: {self.last_name}"

class Experiment():
    def __init__(self, name, date):
      self.name = name
      self.date = date

    def add_subject(self, subject):
      self.subject = subject

    def add_supervisor(self, supervisor):
      self.supervisor = supervisor

    def __str__(self):
       return f"Name: {self.name}, Date:{self.date}, Subject:{self.subject}, Supervisor:{self.supervisor}"