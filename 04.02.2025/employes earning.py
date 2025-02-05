import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[employees['salary'] > employees['managerId'].map(employees.set_index('id')['salary'])]
