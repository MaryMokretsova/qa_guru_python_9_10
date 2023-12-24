import os

from selene import browser, have, be, by, command


def test_complete_todo():

    browser.element('#uploadPicture').send_keys(os.path.abspath(
        'pictures/run_girl.png'))
