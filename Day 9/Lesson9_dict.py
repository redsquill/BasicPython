#employees = [1, 'Ashik', 12, 50000]
employee1 = {'ID': 1, 'Name': 'Ashik', 'Age': 12, 'Salary': 50000}
employee2 = {'ID': 2, 'Name': 'Nafee', 'Age': 10, 'Salary': 60000}
employee3 = {'ID': 3, 'Name': 'Tahrin', 'Age': 13, 'Salary': 70000}
print(employee1)
print(f"ID = {employee1['ID']}")
print(f"Name = {employee1['Name']}")
print(f"Age = {employee1['Age']}")
print(f"Salary = {employee1['Salary']}")

employee1.update({'Age': 18})
print(employee1)
del employee3['Salary']
print(employee3)
print('Display only keys: ')
for k in employee1.keys():
    print(k)

for v in employee1.values():
    print(v)

for k, v in employee1.items():
    # print(k, v)
    print(f"{k} = {v}")
