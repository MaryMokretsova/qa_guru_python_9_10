



class RegistrationPage:

    def open(self):
        browser.open('automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))