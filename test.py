import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#1 Проверка присутствия питомцев
def test_my_pets_stat(driver_pet_friends_chrome):
    driver_pet_friends_chrome.implicitly_wait(10)
    driver_pet_friends_chrome.find_element(By.XPATH, '//body/nav/div[1]/ul/li[1]/a').click()
    WebDriverWait(driver_pet_friends_chrome, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    pets = 'Питомцев: 3'
    pets_text = driver_pet_friends_chrome.find_element(By.XPATH, '//body/div[1]/div[1]/div[1]')
    assert pets in pets_text.text

#2 Проверка, что хотя бы у половины питомцев есть фото
def test_at_least_half_of_the_pets_have_photos(driver_pet_friends_chrome):
    driver_pet_friends_chrome.implicitly_wait(5)  # неявное ожидание до 5 сек
    # Поиск и подсчет карточек питомцев
    driver_pet_friends_chrome.find_element(By.XPATH, '//body/nav/div[1]/ul/li[1]/a').click()
    pets_cards = driver_pet_friends_chrome.find_elements(By.TAG_NAME, 'tr')
    driver_pet_friends_chrome.implicitly_wait(5)  # неявное ожидание до 5 сек
    pets_images = driver_pet_friends_chrome.find_elements(By.CSS_SELECTOR, '#all_my_pets img')
    # Счетчик картинок
    pets_images_counter = 0
    for i in pets_images:
        # Проверка аттрибута объекта: есть ли там картинка
        if i.get_attribute('src') != '':
            pets_images_counter += 1
    # Сравнение количество картинок с количеством питомцев
    assert (len(pets_cards)-1)/2 <= pets_images_counter


#3 Проверка наличия у всех питомцев имени, возраста и породы
def test_all_pets_have_a_name_age_breed(driver_pet_friends_chrome):
    driver_pet_friends_chrome.implicitly_wait(10)  # неявное ожидание до 10 сек
    driver_pet_friends_chrome.find_element(By.XPATH, '//body/nav/div[1]/ul/li[1]/a').click()
    # Проверка пустых полей в данных питомцев
    pet_data = driver_pet_friends_chrome.find_elements(By.TAG_NAME, 'td')
    for i in pet_data:
        assert i.text != ''

#4 Проверка того, что у всех питомцев разные имена
def test_all_pets_have_different_names(driver_pet_friends_chrome):
    driver_pet_friends_chrome.implicitly_wait(10)  # неявное ожидание до 10 сек
    driver_pet_friends_chrome.find_element(By.XPATH, '//body/nav/div[1]/ul/li[1]/a').click()
    pets_cards = driver_pet_friends_chrome.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    pets_name = []
    for i in range(len(pets_cards)):
        pets_data = pets_cards[i].text.replace('\n', '').replace('×', '')
        split_pets_data = pets_data.split(' ')
        pets_name.append(split_pets_data[0])
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
        assert r == 0

#5 Проверка того, что нет повторяющихся питомцев



