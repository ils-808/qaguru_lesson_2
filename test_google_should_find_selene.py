from selene.support.shared import browser
from selene import be, have
import time


def test_google_contains_text():
    browser.open('https://google.com')
    time.sleep(1)
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    time.sleep(1)
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_google_not_contains_text():
    browser.open('https://google.com')

    browser.element('[name="q"]').should(be.blank).type('qwert3445sdfoiuytrew xcv2332bnm,kjhgfdcvb qwd234as').press_enter()

    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
