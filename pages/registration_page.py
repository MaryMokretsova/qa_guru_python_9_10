from selene import browser, have, be


class RegistrationPage:
    def open_registration_page(self):
        browser.open('automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def gender_selection(self):
        browser.element('#gender-radio-2').double_click()

    def fill_user_mobile_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value)

    def fill_current_adreess(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def fill_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def click_submit(self):
        browser.element('#submit').press_enter()
