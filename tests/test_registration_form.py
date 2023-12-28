from page.registration_page import RegistrationPage
from data.users import test_user

def test_complete_todo():
    registration_page = RegistrationPage()

    # WHEN
    registration_page.open_registration_page()
    registration_page.registration(test_user)

    # THEN
    registration_page.should_registered_user_with(test_user)
    registration_page.close_the_form()
