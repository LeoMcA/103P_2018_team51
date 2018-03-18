from autofixture import generators, AutoFixture
from datetime import datetime


class UserRegistration(AutoFixture):
    field_values = {
        'name': generators.StaticGenerator('user_registration'),
        'datetime': generators.DateTimeGenerator(min_date=datetime(2018, 1, 1), max_date=datetime(2018, 1, 30)),
        'increment': generators.ChoicesGenerator(values=(-1, 1, 1, 1, 1, 1, 1, 1, 1))
    }
