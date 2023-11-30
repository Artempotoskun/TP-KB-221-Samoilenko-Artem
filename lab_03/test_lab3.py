import pytest
from lab3 import Student, StudentList, FileHandler, get_new_params, main
from io import StringIO
import os
from unittest.mock import patch

@pytest.fixture
def test_list():
    return [
        {'name': 'Bob', 'phone': '1112233'},
        {'name': 'Dilan', 'phone': '2223344'},
        {'name': 'Zak', 'phone': '3334455'}
    ]

@pytest.fixture
def param_tuple():
    return ('name', 'phone')


def test_load(test_list):
    file_path = 'lab3.csv'
    test_data, params= FileHandler.load_back_file(file_path)
    assert test_list == test_data
    assert params == ('name', 'phone')


def test_save(test_list):
    params = tuple(test_list[0].keys())

    file_path = 'lab3_out.csv'
    FileHandler.save_all_data(test_list, params, file_path)
    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) > 0


def test_add_new_element(test_list, param_tuple):
    with patch('builtins.input', side_effect=["Mike", "1234567890"]):
        student_list = StudentList()
        student_list.add_student(Student(**get_new_params(param_tuple)))

    added_item = {'name': "Mike", 'phone': "1234567890"}
    assert any(item.__dict__ == added_item for item in student_list.students_list)


def test_delete(test_list):
    deleted_name = 'Bob'
    with patch('builtins.input', side_effect=[deleted_name]):
        student_list = StudentList()
        for data in test_list:
            student_list.add_student(Student(**data))
        student_list.delete_student(deleted_name)

    assert not any(student.name == deleted_name for student in student_list.students_list)


def test_update(test_list, param_tuple):
    updated_name = 'Bob'
    with patch('builtins.input', side_effect=[updated_name, "Mike", "1234567890"]):
        student_list = StudentList()
        for data in test_list:
            student_list.add_student(Student(**data))
        student_list.update_student(Student(**get_new_params(param_tuple)))

    updated_item = {'name': 'Mike', 'phone': '1234567890'}
    assert any(student.__dict__ == updated_item for student in student_list.students_list)
