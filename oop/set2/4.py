#lex_auth_012751124968554496166
#Start writing your code here

class Classroom:
    classroom_list = ["a", "b", "c", "d"]

    @staticmethod
    def search_classroom(class_room):
        for classroom in Classroom.classroom_list:
            if classroom.lower() == class_room.lower():
                return "FOUND"
        return -1


x = Classroom()
if Classroom.search_classroom("a") == "FOUND":
    print("Classroon found in left wing")
else:
    print("Classroom not found in left wing")
