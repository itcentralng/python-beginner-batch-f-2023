# def lists_to_dict(list1, list2):
    
#     result_dict = {}

    
#     for i in range(len(list1)):

#         result_dict[list1[i]] = list2[i]

#     return result_dict


# list1 = ["name", "age", "height"]
# list2 = ["Ahmad Sani", 15, 1.6]
# result = lists_to_dict(list1, list2)
# print(result)

def get_student_info(students):
    result = {}
    for student in students:
        if student['name'] in ['Ahmad', 'Muhammad', 'Omale',"divid",'Sarah',"aisha"]:
            result[student['name']] = {
                'score': student['score'],
                'performance': student['performance'],
                'subject': student['subject']
            }
    return result


students = [
    {'name': 'Ahmad', 'score': 90, 'performance': 'Excellent', 'subject': 'Math'},
    {'name': 'Muhammad', 'score': 85, 'performance': 'Good', 'subject': 'Science'},
    {'name': 'Omale', 'score': 78, 'performance': 'Average', 'subject': 'English'},
     {'name': 'Sarah', 'score': 92, 'performance': 'Excellent', 'subject': 'Math'},
     {'name': 'Aisha', 'score': 88, 'performance': 'Good', 'subject': 'Science'},
     {'name': 'David', 'score': 75, 'performance': 'Average', 'subject': 'English'},
]


result = get_student_info(students)
print(result)

#write function that take a list of student   and return 3 dic 
# there socre and there preformsce subjet there namrs ahamad
#  muhammad omale