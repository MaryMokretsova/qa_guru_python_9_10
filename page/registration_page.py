from selene import browser, have, be, command
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

    def should_registered_user_with(self, user):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.phone_number,
                f'{user.day} {user.month},{user.year}',
                user.subject,
                user.hobby,
                user.picture,
                user.current_address,
                f'{user.state} {user.city}',
            )
        )

    def close_the_form(self):
        browser.element('#closeLargeModal').press_enter()
