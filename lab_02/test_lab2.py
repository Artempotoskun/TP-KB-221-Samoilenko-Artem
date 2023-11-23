import pytest
import lab2
import csv
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
    return ('name','phone')


def test_load(test_list):
    file_path = 'lab2.csv'
    test_data,params = lab2.LoadBackFile(file_path)
    assert test_list == test_data
    assert params == ('name','phone')

def test_save(test_list):
    params = tuple(test_list[0].keys())

    file_path = 'lab2_out.csv'
    lab2.SaveAllData(test_list,params,file_path)
    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) > 0

def test_add_new_elemet(test_list,param_tuple):
    with patch('builtins.input', side_effect=["Mike", "1234567890"]):
        lab2.addNewElement(test_list,param_tuple)

    added_item = {'name' : "Mike", 'phone' : "1234567890"}
    assert added_item in test_list

def test_delete(test_list):
    deleted_name = 'Bob'
    with patch('builtins.input', side_effect=[deleted_name]):
        lab2.deleteElement(test_list)

    assert not any(item['name'] == deleted_name for item in test_list)

def test_update(test_list,param_tuple):
    updated_name = 'Bob'
    with patch('builtins.input', side_effect=[updated_name,"Mike", "1234567890"]):
        lab2.updateElement(test_list,param_tuple)
        lab2.printAllList(param_tuple,test_list)

    updated_item = {'name': 'Mike', 'phone': '1234567890'}
    assert updated
