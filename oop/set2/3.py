#lex_auth_012727139457941504148
#Start writing your code here
class Bill:
    def __init__(self, bill_id, patient_name):
        self.__bill_id = bill_id
        self.__patient_name = patient_name
        self.__bill_amount = None

    def get_bill_id(self):
        return self.__bill_id

    def get_bill_amount(self):
        return self.__bill_amount

    def get_patient_name(self):
        return self.__patient_name

    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        bill_amount = consultation_fees
        for i in range(len(quantity_list)):
            bill_amount += quantity_list[i] * price_list[i]
        self.__bill_amount = bill_amount

patient = Bill(2343, "patient1")
patient.calculate_bill_amount(250, [2, 4, 3, 4], [34, 56, 12, 5])
print(patient.get_bill_id(), patient.get_patient_name(), patient.get_bill_amount())
