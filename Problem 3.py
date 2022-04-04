class Member:
    def __init__(self, name):
        self.full_name = name

    def intro(self):
        print(f'Hi, I am {self.full_name}!')


class Student(Member):
    def __init__(self, name, reason):
        super().__init__(name)
        self.reason = reason



class Instructor(Member):
    def __init__(self, name, bio, skills):
        super().__init__(name)
        self.bio = bio
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)

#Ous
class Workshop:
    def __init__(self, date, subject, instructors, students):
        self.date = date
        self.subject = subject
        self.instructors = instructors
        self.students = students

    def add_participant(self, participant):
        if participant.__class__.__name__ == 'Instructor':
            self.instructors.append(participant)
        elif participant.__class__.__name__ == 'Student':
            self.students.append(participant)

    def print_details(self):
        print(f'Program Date: {self.date}\nSubject: {self.subject}\n')
        print('Instructors:')
        for ins in self.instructors:
            print(f'\n{ins.full_name}\n{ins.bio}')
            print('Skills:')
            for s in ins.skills:
                print(s)

        print('\nStudents:')
        for s in self.students:
            print(f'\n{s.full_name}\n{s.reason}\n')


workshop = Workshop('12/03/2021 ', 'Programming in Python ',[],[])
jane = Student('Jane Doe', "I'm trying to learn programming and need some help")
lena = Student('Lena Smith', "I'm really excited about learning to program!")
vicky = Instructor('Vicky Python ', "I want to help people learn coding",[])
vicky.add_skill('Python ')
vicky.add_skill('HTML')
vicky.add_skill('JavaScript ')
nicole = Instructor('Nicole McMillan ', "I've been coding in Python for 5 years",[])
nicole.add_skill('Python ')
workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details ()
# workshop = Workshop('12/03/21', 'Programming in Python', [], [])
# workshop.add_participant(jane)
# workshop.add_participant(lena)
# workshop.add_participant(vicky)
# workshop.add_participant(nicole)
# workshop.print_details()
#
#
# jane = Student('Jane Doe', "I'm trying to learn programming and need some help")
# lena = Student('Lena Smith', "I'm really excited about learning to program!")
# vicky = Instructor('Vicky Python ', "I want to help people learn coding", [])
# vicky.add_skill('Python ')
# vicky.add_skill('HTML')
# vicky.add_skill('JavaScript ')
# nicole = Instructor('Nicole McMillan ', "I've been coding in Python for 5 years", [])
# nicole.add_skill('Python ')