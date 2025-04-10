from my_classes_lena import Subject, Supervisor, Experiment

if __name__ == "__main__":

    # Erstellen eines Leistungstests
    supervisor = Supervisor("Lena", "Kurzthaler","date_of_birth")
    subject = Subject("Lena", "Kurzthaer", "2006-03-16")
    subject.estimate_subject_max_hr()

    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)


    print(experiment)
