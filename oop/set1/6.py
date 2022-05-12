class Instructor:
    def __init__(self):
        self.__instructor_name = ""
        self.__experience = 0
        self.__avg_feedback = 0
        self.__technology_skill = []

    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill

    def set_experience(self, experience):
        self.__experience = experience

    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback

    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name

    def get_technology_skill(self):
        return self.__technology_skill

    def get_experience(self):
        return self.__experience

    def get_avg_feedback(self):
        return self.__avg_feedback

    def get_instructor_name(self):
        return self.__instructor_name

    def check_eligibility(self):
        if (
            self.__experience > 3
            and self.__avg_feedback >= 4.5
            or self.__experience <= 3
            and self.__avg_feedback >= 4
        ):
            return True
        else:
            return False

    def allocate_course(self, technology):
        if technology in self.__technology_skill and self.check_eligibility():
            return True
        else:
            return False


instructor1 = Instructor()
instructor1._Instructor__instructor_name = "demo1"
instructor1._Instructor__experience = 3
instructor1._Instructor__avg_feedback = 4.5
instructor1._Instructor__technology_skill = ["java", "python"]
print(instructor1.check_eligibility())
print(instructor1.allocate_course("java"))
