# using dictionary argument to print out student detail according to data given.
def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")

    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: {kwargs['student_name']}")
            print(f"Student Class: {kwargs['student_class']}")


# Calling function and giving only student name
student_data(student_id='21107003', student_name='Aditya Kundu')

# Calling function and giving both student name and class
student_data(student_id='21107005', student_name='Harshvardhan', student_class ='21-25')
