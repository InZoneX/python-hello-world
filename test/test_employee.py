from employee import Employee

def test_give_default_raise():
    """测试默认涨薪被正确的添加"""
    example_employee = Employee("小黑","刘",200000)
    example_employee.give_raise()
    assert example_employee.salary == 205000

def test_give_custom_raise():
    """测试自定义涨薪被正确的添加"""
    example_employee = Employee("小黑","刘",200000)
    example_employee.give_raise(60000)
    assert example_employee.salary == 260000
