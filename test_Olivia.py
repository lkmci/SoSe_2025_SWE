from my_classes_Olivia import Subject, Supervisor, Experiment

if __name__ == "__main__":

    # Erstellen eines Leistungstests
    supervisor = Supervisor("Olivia", "Kiechl", "date of birth")
    subject = Subject("Olivia", "Kiechl", "2005-01-18")
    subject.estimate_subject_max_hr()

    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment)
   