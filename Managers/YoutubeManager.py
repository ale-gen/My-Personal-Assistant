from selenium import webdriver
from selenium.webdriver.support import ui
import selenium.webdriver.common.keys as keys
import time
from random import randint


end_patterns = ["finish", "end", "close", "exit", "no", "thanks"]


def search(user_query, driver, wait):
    search_box = driver.find_element_by_xpath('//*[@id="search"]')
    search_box.send_keys(user_query)
    time.sleep(randint(2, 5))
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="search-icon-legacy"]'))
    search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    search_button.click()
    time.sleep(randint(2, 5))


def get_title_from_user():
    title = input("Write the title: ")
    return title


def choose_video(title, driver):
    driver.find_element_by_partial_link_text(title).click()
    time.sleep(randint(2, 4))


def accept_conditions(driver):
    accept_box = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button')
    accept_box.click()
    time.sleep(randint(2, 5))


def stop_video(driver):
    driver.find_element_by_class_name("ytp-play-button-container").click()


def resume_video(driver):
    driver.find_element_by_class_name("ytp-play-button-container").click()


def maximize_window(driver):
    driver.maximize_window()


def minimize_window(driver):
    driver.minimize_window()


def fullscreen(driver):
    driver.find_element_by_class_name('ytp-fullscreen-button-container').click()


def skip_ads(driver):
    button = driver.find_element_by_class_name('ytp-ad-skip-button-container').click()
    #button.click()


def subtitles(driver):
    driver.find_element_by_class_name('ytp-subtitiles-button-container').click()


def volume(driver):
    driver.find_element_by_xpath('//*[@id="movie_player"]/div[29]/div[2]/div[1]/span/div/div/div')


def scroll_down(driver):
    scroll_height = 2
    document_height_before = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script(f"window.scrollTo(0, {document_height_before + scroll_height});")
    time.sleep(2)
    document_height_after = driver.execute_script("return document.documentElement.scrollHeight")


def scroll_up(driver):
    scroll_height = 2
    document_height_before = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script(f"window.scrollTo(0, {document_height_before - scroll_height});")
    time.sleep(2)
    document_height_after = driver.execute_script("return document.documentElement.scrollHeight")


def trail(driver):
    driver.find_element_by_id("dismiss-button").click()


def login(assistant, driver, wait):
    assistant.respond("Do you want to log in?")
    answer = assistant.talk()
    if answer == "yes":
        driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[1]/div[1]/div/div/a').click()
        wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="identifierId"]'))
        username = driver.find_element_by_xpath('//*[@id="identifierId"]')
        username.send_keys("o.generowicz@gmail.com")
        driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
        wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input'))
        password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password.send_keys("alegen25")
        submit = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
        submit.click()


def options_during_watching(assistant, driver):
    answer = ""
    while answer == "":
        answer = assistant.talk()
        if answer != "":
            if 'screen' in answer:
                try:
                    fullscreen(driver)
                except:
                    assistant.respond("Sorry, there isn't fullscreen option")
            elif 'stop' in answer:
                try:
                    stop_video(driver)
                except:
                    assistant.respond("Sorry, I can't stop video")
            elif 'resume' in answer:
                try:
                    resume_video(driver)
                except:
                    assistant.respond("Sorry, I can't resume video")
            elif 'down' in answer:
                scroll_down(driver)
            elif 'higher' in answer:
                scroll_up(driver)
            elif 'subtitles' in answer:
                try:
                    subtitles(driver)
                except:
                    assistant.respond("Sorry, there isn't subtitles option")
            elif 'close' in answer:
                return
            elif 'Trail' in answer:
                try:
                    trail(driver)
                except:
                    assistant.respond("Sorry, I can't help you.")
            elif 'skip' in answer:
                try:
                    skip_ads(driver)
                except:
                    assistant.respond("Sorry, Skip ads is unavailable")
            answer = ""


def manage_youtube(assistant):
    answer = ""
    assistant.respond("Let me just start youtube session")
    driver = webdriver.Safari()
    wait = ui.WebDriverWait(driver, 100)
    driver.get("https://www.youtube.com")
    maximize_window(driver)
    login(assistant, driver, wait)
    assistant.respond("Do you want to accept condition?")
    while answer == "":
        answer = assistant.talk()

    if answer != "yes":
        return
    else:
        accept_conditions(driver)
        while not end_patterns.__contains__(answer):
            assistant.respond("What do you want to search?")
            done = False
            while not done:
                answer = ""
                while answer == "":
                    answer = assistant.talk()
                    if 'down' in answer:
                        scroll_down(driver)
                        answer = ""
                    elif 'higher' in answer:
                        scroll_up(driver)
                        answer = ""
                try:
                    search(answer, driver, wait)
                    done = True
                except:
                    done = False
            assistant.respond("What do you want to choose?")
            done = False
            while not done:
                answer = ""
                while answer == "":
                    answer = assistant.talk()
                    if 'down' in answer:
                        scroll_down(driver)
                        answer = ""
                    elif 'up' in answer:
                        scroll_up(driver)
                        answer = ""
                try:
                    choose_video(answer.capitalize(), driver)
                    done = True
                except:
                    done = False
            options_during_watching(assistant, driver)
            assistant.respond("Do you want to search something else?")
            answer = assistant.talk()
        driver.close()

