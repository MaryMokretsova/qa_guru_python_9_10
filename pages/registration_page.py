from selene import browser, have, be, command
from pictures import resource


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
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()

    def fill_hobby_checkbox(self):
        browser.element('[for=hobbies-checkbox-3]').perform(command.js.scroll_into_view).click()

    def fill_picture(self, value):
        browser.element('#uploadPicture').send_keys(resource.path(value))

    def fill_current_adress(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def fill_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def press_submit(self):
        browser.element('#submit').press_enter()

    def should_have_registration_table(
        self,
        text,
        full_name,
        email,
        gender,
        user_mobile_number,
        date_of_birth,
        subject,
        hobby,
        picture,
        current_address,
        state_and_city,
    ):
        browser.element('.modal-header').should(have.text(text))
        browser.all('.table').all('td')[1].should(have.exact_text(full_name))
        browser.all('.table').all('td')[3].should(have.exact_text(email))
        browser.all('.table').all('td')[5].should(have.exact_text(gender))
        browser.all('.table').all('td')[7].should(have.exact_text(user_mobile_number))
        browser.all('.table').all('td')[9].should(have.exact_text(date_of_birth))
        browser.all('.table').all('td')[11].should(have.exact_text(subject))
        browser.all('.table').all('td')[13].should(have.exact_text(hobby))
        browser.all('.table').all('td')[15].should(have.exact_text(picture))
        browser.all('.table').all('td')[17].should(have.exact_text(current_address))
        browser.all('.table').all('td')[19].should(have.exact_text(state_and_city))

    def press_close(self):
        browser.element('#closeLargeModal').press_enter()
