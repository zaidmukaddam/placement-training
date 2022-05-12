# lex_auth_0127384900074618882679
# Start writing your code here

from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    def __init__(self, job_band, employee_name, basic_salary, qualification):
        self.__job_band = job_band
        self.__employee_name = employee_name
        self.__basic_salary = basic_salary
        self.__qualification = qualification

    def validate_basic_salary(self):
        if self.__basic_salary > 3000:
            return True
        return False

    def validate_qualification(self):
        if self.__qualification == "Masters" or self.__qualification == "Bachelors":
            return True
        return False

    @abstractmethod
    def calculate_gross_salary(self):
        pass

    @abstractmethod
    def validate_job_band(self):
        pass

    def get_basic_salary(self):
        return self.__basic_salary

    def get_qualification(self):
        return self.__qualification

    def get_employee_name(self):
        return self.__employee_name

    def get_job_band(self):
        return self.__job_band


class Graduate(Employee):
    def __init__(self, job_band, basic_salary, qualification, cgpa, employee_name):
        super().__init__(job_band, employee_name, basic_salary, qualification)

        self.__cgpa = cgpa

    def validate_job_band(self):
        job_bands = ["A", "B", "C"]
        if self.get_job_band() in job_bands:
            return True
        return False

    def calculate_gross_salary(self):
        incentive = {"A": 4, "B": 6, "C": 10}
        if (
            self.validate_basic_salary()
            and self.validate_qualification()
            and self.validate_job_band()
        ):
            salary = self.get_basic_salary() * (
                1.12 + incentive[self.get_job_band()] / 100
            )
            if 4 <= self.__cgpa <= 4.25:
                salary += 1000
            elif 4.26 <= self.__cgpa <= 4.5:
                salary += 1700
            elif 4.51 <= self.__cgpa <= 4.75:
                salary += 3200
            elif 4.76 <= self.__cgpa <= 5:
                salary += 5000
            return salary
        return -1

    def get_cgpa(self):
        return self.__cgpa


class Lateral(Employee):
    def __init__(self, job_band, basic_salary, qualification, skill_set, employee_name):
        super().__init__(job_band, employee_name, basic_salary, qualification)

        self.__skill_set = skill_set

    def validate_job_band(self):
        job_bands = ["D", "E", "F"]
        if self.get_job_band() in job_bands:
            return True
        else:
            return False

    def calculate_gross_salary(self):
        incentive = {"D": 13, "E": 16, "F": 20}
        if (
            self.validate_basic_salary()
            and self.validate_qualification()
            and self.validate_job_band()
        ):
            sme_bonus = {"AGP": 6500, "AGPT": 8200, "AGDEV": 11500}
            salary = (
                self.get_basic_salary() *
                (1.12 + incentive[self.get_job_band()] / 100)
                + sme_bonus[self.__skill_set]
            )
            return salary
        return -1

    def get_skill_set(self):
        return self.__skill_set


emp2 = Lateral("D", 4000, "Bachelors", "AGP", "emp1")
print(emp2.calculate_gross_salary())
emp1 = Graduate("A", 4000, "Bachelors", 4.5, "emp2")
print(emp1.calculate_gross_salary())
