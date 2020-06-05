#OOP Test

class Students:

    num_students = 0

    #class index variables
    class_index_dict = {1 : 'math', 2 : 'english', 3 : 'science', 4 : 'gym'}

    def __init__(self, first, last, grade, num_class):
        self.first = first
        self.last = last
        self.grade = grade
        self.email = first + last + '@utschools.ca'
        self.num_class = num_class
        self.class_list = []

        Students.num_students += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def class_select(self):
        print('Math: 1\nEnglish: 2\nScience: 3\nGym: 4')
        class_choice_index = input('Enter the ' + str(self.num_class) + ' classes you want to take (seperated by spaces): ')
        class_index_list = class_choice_index.split()
        for i in range(len(class_index_list)):
            if class_index_list[i] == '1':
                self.class_list.append('math')
            elif class_index_list[i] == '2':
                self.class_list.append('english')
            elif class_index_list[i] == '3':
                self.class_list.append('science')
            else:
                self.class_list.append('gym')




student_1 = Students('Adam','Taback',10, 2)
student_2 = Students('Oli','Taback',7, 3)

student_1.class_select()
student_2.class_select()

print(student_1.class_list)
print(student_2.class_list)