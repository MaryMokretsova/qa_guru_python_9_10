import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    user_mobile_number: str
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
    user_email='cameron105@mail.ru',
    user_gender='Famele',
    user_phone_number='9066507373',
    month='June',
    year='1989',
    day='11',
    user_subject='English',
    user_hobby='Music',
    user_picture='run_girl.png',
    user_current_address='Sant-Peterburg, Aleksandra Matrosova',
    user_state='Rajasthan',
    user_city='Jaiselmer',
)