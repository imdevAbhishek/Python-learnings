#  Instance attributes, take preference over class attributes during assignment & retrieval.


class Employee:
    language="Python"    # class attribute
    Salary=120000

Abhi = Employee()
Abhi.language="JavaScript"     # Object attribute or Instance attribute
print(Abhi.language, Abhi.Salary)
