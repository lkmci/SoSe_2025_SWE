import datetime
from my_functions import estimate_max_hr
from my_functions import calculate_and_show_heartrate


class Person():
    def __init__(self, name, sex, date_of_birth):
        self.name = name
        self.sex = sex
        self.__date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()  
    def get_age_years(self):
        today = datetime.date.today()
        age_years = datetime.datetime.now().year - self.__date_of_birth.year
        
        
class Subject(Person):
    def __init__(self, name, sex, date_of_birth):
        super().__init__(name, sex, date_of_birth)  
        self.sex = sex
        self.__date_of_birth = date_of_birth
    

    def get_subject_age(self):
        return self.get_age_years()
    
    def estimate_subject_max_hr(self):
        from my_functions import estimate_max_hr, calculate_and_show_heartrate
        """ Berechnet die maximale Herzfrequenz für das Subject """
        age_years = self.get_subject_age()
        return estimate_max_hr(age_years, self.sex)
    
    def get_subject_info(self): 
        return {
            "first_name": self.name,
            "date_of_birth": self.__date_of_birth,
            "sex": self.sex, 
              "estimate_max_hr": self.estimate_subject_max_hr()
}

class Supervisor():
    def __init__(self, name, sex, date_of_birth):
        self.first_name = name 
        self.date_of_birth = date_of_birth

    def get_supervisor_age(self):
        return self.get_age_years()


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
    
    def get_experiment_info(self):
        return {
            "experiment_name": self.name,
            "experiment_date": self.date,
            "subject": self.subject.get_subject_info(),
            "supervisor": self.supervisor.get_supervisor_age()
        }


# Testen der Klassen
#p = Subject("Lena", "female", "2006-03-16")
#print(f"Alter: {p.get_age_years()} Jahre")
#print(f"Maximale Herzfrequenz: {p.estimate_subject_max_hr()} bpm")