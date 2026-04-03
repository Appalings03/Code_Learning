welcome_prompt = """Welcome doctor, what would you like to do today?\n
- To list all patients, press 1\n
- To run a new diagnosis, press 2\n
- To quit, press q\n"""

name_prompt = "What is the patient's name?\n"
appearance_prompt = "How is the patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"
eye_prompt = """How are the patient's eyes?\n
- 1: Eyes normal or slightly sunken\n
- 2: Eyes very sunken\n"""
skin_prompt = """How is the patient's skin when you pinch it?\n
- 1: Normal skin pinch\n
- 2: Slow skin pinch\n"""
severe_dehydratation = "Severe dehydratation"
some_dehydratation = "Some dehydratation"
no_dehydratation = "Severe dehydratation"

patients_and_diagnosis = [
    "Mike: Severe dehydratation",
    "Sally: No dehydratation",
    "Kate: Some dehydratation"
]


def list_patients():
    for patient in patients_and_diagnosis:
        print(patient)

def save_new_diagnosis(name, diagnosis):
    if name == "" or diagnosis =="":
        print("Could not save patient and diagnosis due to invalide input")
        return
    final_diagnosis = name + ": " + diagnosis
    patients_and_diagnosis.append(final_diagnosis)
    print("Final Diagnosis:", final_diagnosis, "\n")
    

# Try calling the 2 functions below according to the appearance_prompt input!
def assess_skin(skin):
    if skin == "1":
        return some_dehydratation
    elif skin == "2":
        return severe_dehydratation
    else:
        return ""

def assess_eyes(eyes):
    if eyes == "1":
        return no_dehydratation
    elif eyes == "2":
        return severe_dehydratation
    else:
        return ""
    
def assess_apperance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        eyes = input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_skin(skin)
    else:
        return ""


def start_new_diagnosis():
    # Asks user to enter the patient's name
    name = input(name_prompt)
    # Asks user to enter how the general appearance of the patient is
    diagnosis = assess_apperance()
    save_new_diagnosis(name, diagnosis)

def main():
    # Executes the code within the while loop until user presses 'q'
    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            # Exits the program
            return

main()

# Assessing all if-then-else cases for both skin and eyes
def test_assess_skin():
    print(assess_skin("1") == some_dehydratation)
    print(assess_skin("2") == severe_dehydratation)
    print(assess_skin("3") == "")

def test_assess_eyes():
    print(assess_eyes("1") == no_dehydratation)
    print(assess_eyes("2") == severe_dehydratation)
    print(assess_eyes("3") == "")

def test_assess_appearance():
    print(assess_apperance())

# Assessing all possible cases of entries for name and diagnosis
def test_save_new_diagnosis():
    save_new_diagnosis("", "")
    print(patients_and_diagnosis == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration"
    ])
    save_new_diagnosis("Nimish", "")
    print(patients_and_diagnosis == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration"
    ])
    save_new_diagnosis("", "No dehydration")
    print(patients_and_diagnosis == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration"
    ])
    save_new_diagnosis("Nimish", "Some dehydration")
    print(patients_and_diagnosis == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration",
        "Nimish - Some dehydration"
    ])


#test_assess_skin()
#test_assess_eyes()
#test_assess_appearance()
#test_save_new_diagnosis()