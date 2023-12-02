def test_get_student(test_list):
    student_list = StudentList()

    # Додаємо студентів до списку
    for data in test_list:
        student_list.add_student(Student(**data))

    # Тест на отримання студента за іменем
    retrieved_student = student_list.get_student('Bob')
    assert retrieved_student is not None
    assert retrieved_student.name == 'Bob'
    assert retrieved_student.phone == '1112233'

    # Тест на випадок, коли студент не існує
    non_existent_student = student_list.get_student('NonExistent')
    assert non_existent_student is None

def test_list_students(test_list, capsys):
    student_list = StudentList()

    # Додаємо студентів до списку
    for data in test_list:
        student_list.add_student(Student(**data))

    # Тест на вивід списку студентів
    student_list.list_students()
    captured = capsys.readouterr()
    assert 'Bob' in captured.out
    assert 'Dilan' in captured.out
    assert 'Zak' in captured.out
    assert 'Mike' not in captured.out  # Новий студент не виводиться

def test_invalid_phone_input(test_list):
    with patch('builtins.input', side_effect=["John", "invalid_phone"]):
        student_list = StudentList()

        # Додаємо студента до списку через некоректний номер телефону
        student_list.add_student(Student(**Utils.get_new_params(('name', 'phone'))))

    # Студент не додався через некоректний номер телефону
    assert len(student_list.students_list) == 0
