employees = [
    {'ID': 1, 'Name': 'Ashik', 'Age': 12, 'Salary': 50000},
    {'ID': 2, 'Name': 'Nafee', 'Age': 10, 'Salary': 60000},
    {'ID': 3, 'Name': 'Tahrin', 'Age': 13, 'Salary': 70000},
]

print('%-5s %-30s %-10s %-10s' %
      ('ID', 'Name', 'Age', 'Salary'))
print('='*80)
for emp in employees:
    print('%-5s %-30s %-10s %-10s' %
          (emp['ID'], emp['Name'], emp['Age'], emp['Salary']))
