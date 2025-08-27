# multi level inheritance

class Person:
    name = "PPP"
    email = "ppp@mail.com"
    city = "Pune"


class Teacher(Person):
    subject = "maths"


class GuestFaculty(Teacher):
    hours = 8
    renumeration = 1000
    salary = hours * renumeration

    def show(self):
        print(self.name, self.email, self.city, self.subject, self.hours, self.salary)


c1 = GuestFaculty()
c1.show()
