import pytest
from employee import Employee

@pytest.fixture
def example_employee():
    """一个可供所有测试函数使用的Employee实例"""
    example_employee = Employee("小黑","刘",200000)
    return example_employee

def test_give_default_raise(example_employee):
    example_employee.give_raise()
    assert example_employee.salary == 205000

def test_give_custom_raise(example_employee):
    example_employee.give_raise(90000)
    assert example_employee.salary == 290000
