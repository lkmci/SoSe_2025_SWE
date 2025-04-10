def build_person(first_name: str, last_name: str, age_years : int, sex) -> dict:
    """Builds a dictionary representing a person."""
    person_dict = { "first_name": first_name, 
                   "age": age_years,
                    "estimate_max_hr": calculate_and_show_heartrate( age_years, sex) }
    return {
        "first_name": first_name,
        "last_name": last_name
    }

def ask_name() -> str:
    """Asks the user for their name."""
    try :
        name = input("What is your name? ")
        return name
    except Exception as e:
        print("Please enter a valid name")
        ask_name()

def ask_number() -> int:
    """Asks the user for a number."""
    try:
        number = int(input("Enter a number: "))
        return number
    except Exception as e:
        print("Please enter a valid number")
        ask_number()

def ask_sex() -> str:
    """Ask the user for the sex"""
    sex_string = input("Enter sex (w/m): ")
    if sex_string == "w":
        return "female"
    elif sex_string == "m":
        return "male"
    else:
        print("Please enter 'w' or 'm'")
        ask_sex() 

def estimate_max_hr(age_years, sex: str = None) -> int:
    """
    Schätzt die maximale Herzfrequenz basierend auf Alter und optional Geschlecht.
    """
    if sex == "female":
        return 226 - 1.0 * age_years
    elif sex == "male":
        return 223 - 0.9 * age_years
    else:
        max_hr = input("Enter your maximum heart rate: ")
    return int(max_hr)


def calculate_and_show_heartrate(date_of_birth):
    """Fragt Nutzerdaten ab und zeigt die geschätzte maximale Herzfrequenz an."""
    print("🫀 Maximaler Herzfrequenz-Rechner 🫀")
    from datetime import datetime
    today = datetime.today()
    year_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").year
    name = ask_name()
    age_years = today.year - year_of_birth - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))  # Berechnung des Alters
    return age_years 
   

   # max_hr = estimate_max_hr(age, sex)