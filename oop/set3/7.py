#lex_auth_012751878508396544244
#Start writing your code here

class Applicant:
    __applicant_id_count = 1000
    __application_dict = {"A": 0, "B": 0, "C": 0}

    def __init__(self, applicant_name):
        self.__applicant_id = None
        self.__applicant_name = applicant_name
        self.__job_band = None

    def generate_applicant_id(self):
        if Applicant.__applicant_id_count == None:
            Applicant.__applicant_id_count = 1000
        Applicant.__applicant_id_count += 1
        self.__applicant_id = Applicant.__applicant_id_count

    def apply_for_job(self, job_band):
        if Applicant.__application_dict[job_band] < 5:
            Applicant.__application_dict[job_band] += 1
            self.generate_applicant_id()
            self.__job_band = job_band
            return

        return -1

    def get_applicant_id(self):
        return self.__applicant_id

    def get_job_band(self):
        return self.__job_band

    def get_applicant_name(self):
        return self.__applicant_name

    @staticmethod
    def get_application_dict():
        return Applicant.application_dict


app1 = Applicant("app1")
app2 = Applicant("app2")
app1.apply_for_job("A")
app2.apply_for_job("B")
print(
    "Applicant 1:",
    app1.get_applicant_name(),
    app1.get_applicant_id(),
    app1.get_job_band(),
)
print(
    "Applicant 2:",
    app2.get_applicant_name(),
    app2.get_applicant_id(),
    app2.get_job_band(),
)
