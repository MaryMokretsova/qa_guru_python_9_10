import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    month: str
    year: str
    day: str
    subject: str
    hobby: str
    picture: str
    current_address: str
    state: str
    city: str


test_user = User(
    first_name='Mariya',
    last_name='Mokretsova',
    email='cameron105@mail.ru',
    gender='Female',
    phone_number='9066507373',
    month='June',
    year='1989',
    day='11',
    subject='English',
    hobby='Music',
    picture='run_girl.png',
    current_address='Sant-Peterburg, Aleksandra Matrosova',
    state='Rajasthan',
    city='Jaiselmer',
)
