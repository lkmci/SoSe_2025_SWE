from datetime import date
import numpy as np

 

def Leistungstest(first_experiment_id: int): 

    # first_experiment_id ist ein integer?

    try:

        first_experiment_id = int(first_experiment_id)

    except ValueError:

        print("Error: first_experiment_id ist ein integer")

        return[]

   

    # Liste für Experiment erstellen
    experiments = []
    

    # Schleife mit 10 Experimente
    for i in range(10):

        experiment = {

            "id" : first_experiment_id + i,  # id soll sich um i erhöhen

            "Erstellungsdatum" : date.today(),
            
            "Versuchsleiter:in" : "Lena Kurzthaler"

        }

        # Überschriften für Experiment hinzufügen
        experiments.append(experiment)
       

 

    # Schleife, um die ersten 5 Experimente anzuzeigen
    for experiment in experiments[:5]:

        print(experiment)

 

    # ist id eine gerade zahl oder ungerade? 
    # alle geraden id-zahlen zusammenzählen

    even_id = 0

    for experiment in experiments:

        if experiment["id"] % 2 == 0:

            even_id += 1

            print("gerade: ", even_id)

        else:

            print("first_experiment_id ist ungerade")
            

print(Leistungstest(10))

