def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    # write your logic here
    patient_count = {"P": 0, "O": 0, "E": 0}
    for i in range(1, len(patient_medical_speciality_list), 2):
        patient_count[patient_medical_speciality_list[i]] += 1
    max_key = ""
    max_value = 0
    for speciality, frequency in patient_count.items():
        if frequency > max_value:
            max_value = frequency
            max_key = speciality
    return medical_speciality[max_key]


# provide different values in the list and test your program
patient_medical_speciality_list = [
    301, 'P', 302, 'P', 305, 'P', 401, 'E', 656, 'E']
medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality(
    patient_medical_speciality_list, medical_speciality)
print(speciality)
