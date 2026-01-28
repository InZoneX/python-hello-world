from employee import Employee

"""员工年薪示例，并显示涨薪后的年薪"""
employee_1 = Employee("小黑","刘",200000)

print(
    f"{employee_1.last_name}{employee_1.first_name}的年薪"
    f"是{employee_1.salary}元"
)

employee_1.give_raise(30000)

print(f"In 2026,{employee_1.last_name}{employee_1.first_name}'s salary \
is ¥{employee_1.salary}")
