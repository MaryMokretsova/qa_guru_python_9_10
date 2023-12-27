from selene import browser, have, be, command
from data.users import User
from pictures import resource


class RegistrationPage:
    def open_registration_page(self):
        browser.open('automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    def registration(self, user):
        browser.element('#firstName').should(be.blank).type(user.first_name)
        browser.element('#lastName').should(be.blank).type(user.last_name)
        browser.element('#userEmail').should(be.blank).type(user.email)
        browser.element('#gender-radio-2').double_click()
        browser.element('#userNumber').should(be.blank).type(user.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().type(user.month)
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element(f'.react-datepicker__day--0{user.day}').click()
        browser.element('#subjectsInput').should(be.blank).type(user.subject).press_enter()
        browser.element('[for=hobbies-checkbox-3]').perform(command.js.scroll_into_view).click()
        browser.element('#uploadPicture').send_keys(resource.path(user.picture))
        browser.element('#currentAddress').should(be.blank).type(user.current_address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').press_enter()


    def should_registered_user_with(self, test_user: User):
        browser.element('.modal-header').should(have.text(test_user.text))
        browser.all('.table').all('td')[1].should(have.exact_text(f'{test_user.first_name} {test_user.last_name}'))
        browser.all('.table').all('td')[3].should(have.exact_text(test_user.email))
        browser.all('.table').all('td')[5].should(have.exact_text(test_user.gender))
        browser.all('.table').all('td')[7].should(have.exact_text(test_user.phone_number))
        browser.all('.table').all('td')[9].should(have.exact_text(f'{test_user.day} {test_user.month},{test_user.year}'))
        browser.all('.table').all('td')[11].should(have.exact_text(test_user.subject))
        browser.all('.table').all('td')[13].should(have.exact_text(test_user.hobby))
        browser.all('.table').all('td')[15].should(have.exact_text(test_user.picture))
        browser.all('.table').all('td')[17].should(have.exact_text(test_user.current_address))
        browser.all('.table').all('td')[19].should(have.exact_text(f'{test_user.user_state} {test_user.user_city}'))

