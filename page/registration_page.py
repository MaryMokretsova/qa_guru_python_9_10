import os

from selene import browser, have, be, command


class RegistrationPage:
    def open_registration_page(self):
        browser.open('automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    def registration(self, user):
        browser.element('#firstName').should(be.blank).type(user.first_name)
        browser.element('#lastName').should(be.blank).type(user.last_name)
#         browser.element('#userEmail').should(be.blank).type(value)
#         browser.element('#gender-radio-2').double_click()
#         browser.element('#userNumber').should(be.blank).type(value)
#         browser.element('#dateOfBirthInput').click()
#         browser.element('.react-datepicker__month-select').click().type(month)
#         browser.element('.react-datepicker__year-select').type(year)
#         browser.element(f'.react-datepicker__day--0{day}').click()
#         browser.element('#subjectsInput').should(be.blank).type(value).press_enter()
#         browser.element('[for=hobbies-checkbox-3]').perform(command.js.scroll_into_view).click()
#         browser.element('#uploadPicture').send_keys(os.path.abspath(
#             'qa_guru_python_9_10/pictures/run_girl.png'))
#         browser.element('#currentAddress').should(be.blank).type(value)
#         browser.element('#react-select-3-input').type(value).press_enter()
#         browser.element('#react-select-4-input').type(value).press_enter()
#         browser.element('#submit').press_enter()
#
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

#     def should_registered_user_with(
#         self,
#         text,
#         full_name,
#         email,
#         gender,
#         user_mobile_number,
#         date_of_birth,
#         subject,
#         hobby,
#         picture,
#         current_address,
#         state_and_city,
#     ):
#         browser.element('.modal-header').should(have.text(text))
#         browser.all('.table').all('td')[1].should(have.exact_text(full_name))
#         browser.all('.table').all('td')[3].should(have.exact_text(email))
#         browser.all('.table').all('td')[5].should(have.exact_text(gender))
#         browser.all('.table').all('td')[7].should(have.exact_text(user_mobile_number))
#         browser.all('.table').all('td')[9].should(have.exact_text(date_of_birth))
#         browser.all('.table').all('td')[11].should(have.exact_text(subject))
#         browser.all('.table').all('td')[13].should(have.exact_text(hobby))
#         browser.all('.table').all('td')[15].should(have.exact_text(picture))
#         browser.all('.table').all('td')[17].should(have.exact_text(current_address))
#         browser.all('.table').all('td')[19].should(have.exact_text(state_and_city))
#
#     def press_close(self):
#         browser.element('#closeLargeModal').press_enter()

