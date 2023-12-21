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


    registration_page.fill_current_address('Sant-Peterburg, Aleksandra Matrosova')
    registration_page.fill_state('Rajasthan')
    registration_page.fill_city('Jaiselmer')
    registration_page.click_submit()

def test_complete_todo():
    # browser.open('automation-practice-form')
    # browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    # browser.element('#firstName').should(be.blank).type('Mariya')
    # browser.element('#lastName').should(be.blank).type('Mokretsova')
    # browser.element('#userEmail').should(be.blank).type('cameron105@mail.ru')

    # browser.element('#gender-radio-2').double_click()
    #
    # browser.element('#userNumber').should(be.blank).type('9066507373')
    #
    # browser.element('#dateOfBirthInput').click()
    # browser.element('.react-datepicker__month-select').click().type('June').press_enter()
    # browser.element('.react-datepicker__year-select').click().type('1989').press_enter()
    # browser.element('.react-datepicker__day--027').click()
    # browser.element('#subjectsInput').should(be.blank).type('English').press_enter()
    browser.element('[for=hobbies-checkbox-3]').perform(command.js.scroll_into_view).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(
        'pictures/run_girl.png'))
    # browser.element('#currentAddress').should(be.blank).type('Sant-Peterburg, Aleksandra Matrosova')

    # browser.element('#react-select-3-input').type('Rajasthan').press_enter()
    # browser.element('#react-select-4-input').type('Jaiselmer').press_enter()
    # browser.element('#submit').press_enter()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.all('.table').all('td')[1].should(have.exact_text('Mariya Mokretsova'))
    browser.all('.table').all('td')[3].should(have.exact_text('cameron105@mail.ru'))
    browser.all('.table').all('td')[5].should(have.exact_text('Female'))
    browser.all('.table').all('td')[7].should(have.exact_text('9066507373'))
    browser.all('.table').all('td')[9].should(have.exact_text('27 June,1989'))
    browser.all('.table').all('td')[11].should(have.exact_text('English'))
    browser.all('.table').all('td')[13].should(have.exact_text('Music'))
    browser.all('.table').all('td')[15].should(have.exact_text('run_girl.png'))
    browser.all('.table').all('td')[17].should(have.exact_text('Sant-Peterburg, Aleksandra Matrosova'))
    browser.all('.table').all('td')[19].should(have.exact_text('Rajasthan Jaiselmer'))

    browser.element('#closeLargeModal').press_enter()
