company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}

print(company_employees)

company_employees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}
print(company_employees)

company_employees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}
print("\nUpdated company_employees dictionary with new employee:")
print(company_employees)

def count_total_employees(company_dict):
    total_count = 0
    for department, employees in company_dict.items():
        total_count += len(employees)
    return total_count

total_employees = count_total_employees(company_employees)
print("\nTotal number of employees in the company:", total_employees)