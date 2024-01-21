def print_student_name(name):
    print("Student Name:", name)

def print_student_id(id_number):
    print("Student ID:", id_number)

def get_value_size(value):
    return len(value)

def print_name_characters(name):
    for ch in name:
        print(ch, end=' ')
    print()

def print_id_characters(id_number):
    for num in id_number:
        print(num, end=' ')
    print()

def main():
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    print_student_name(student_name)
    print_student_id(student_id)

    name_size = get_value_size(student_name)
    id_size = get_value_size(student_id)

    print("Name size:", name_size)
    print("ID size:", id_size)

    print_name_characters(student_name)
    print_id_characters(student_id)

if __name__ == "__main__":
    main()
