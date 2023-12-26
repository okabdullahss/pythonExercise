stock_prices = [("APPL", 200), ("GOOG", 300), ("MCRSFT", 400)]

for x, y in stock_prices:
    print(x)

# create a function that returns employee of the month & his work hours

work_hours = [("Adam", 100), ("Stella", 500), ("Greg", 2020), ("Dawid", 300)]


def bestEmployee(list):
    current_work=0
    employee=None
    for name,hours in list:
        if hours>current_work:
            current_work=hours
            employee=name
        else:
            pass

    return employee,current_work

x,y = bestEmployee(work_hours)
print(f'name of the employee of the month is : {x}')
print(f'work hours of the employee of the month is : {y}')