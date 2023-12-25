from pages.registration_page import RegistrationPage


def test_registration():
    registration_page = RegistrationPage()
    registration_page.open_registration_page()

    # WHEN
    registration_page.fill_first_name('Mariya')
    registration_page.fill_last_name('Mokretsova')
    registration_page.fill_email('cameron105@mail.ru')
    registration_page.gender_selection()
    registration_page.fill_user_mobile_number('9066507373')
    registration_page.fill_date_of_birth('1989', 'June', '27')
    registration_page.fill_subject('English')
    registration_page.fill_hobby_checkbox()
    registration_page.fill_picture('run_girl.png')
    registration_page.fill_current_adress('Sant-Peterburg, Aleksandra Matrosova')
    registration_page.fill_state('Rajasthan')
    registration_page.fill_city('Jaiselmer')
    registration_page.press_submit()

    #THEN
    registration_page.should_have_registration_table(
        'Thanks for submitting the form',
        'Mariya Mokretsova',
        'cameron105@mail.ru',
        'Female',
        '9066507373',
        '27 June,1989',
        'English',
        'Music',
        'run_girl.png',
        'Sant-Peterburg, Aleksandra Matrosova',
        'Rajasthan Jaiselmer'
    )

    registration_page.press_close()

