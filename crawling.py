from selenium.webdriver.common.by import By
from selenium import webdriver
import re

driver = webdriver.Chrome("/Users/jeongjun/Downloads/chromedriver") # 본인 것으로 설정해야 함.

#`처음 url로 이동
URL = 'https://playground.tensorflow.org/'
driver.get(URL)

# play_pause 버튼 생성
play_pause = driver.find_element(By.ID, 'play-pause-button')

# test_loss 값 가져오기
test_loss = driver.find_element(By.ID, 'loss-test')

# epoch 값 가져오기
epoch = driver.find_element(By.ID, 'iter-number')

url = str()
networkShape = str()

# play_pause 버튼 클릭
def play_pause_button():
    global play_pause
    play_pause = driver.find_element(By.ID, 'play-pause-button')
    play_pause.click()

# networkShape 값 갱신하기
def updateNetworkShape():
    global networkShape
    url = getCurrentUrl() # 현재 url 가져오기
    exp = re.compile('\w+=\w?[,\w]+')
    exp_list = exp.findall(url)

    for i in exp_list:
        if i.startswith('networkShape'):
            networkShape = i.split('=')[1] #4,2와 같이 값이 저장

# test_loss 값 가져오기
def getTestLoss():
    global test_loss
    test_loss = driver.find_element(By.ID, 'loss-test')
    return test_loss.text

# epoch 값 가져오기
def getEpoch():
    global epoch
    epoch = driver.find_element(By.ID, 'iter-number')
    return epoch.text

# 현재 url 가져오기
def getCurrentUrl():
    global driver
    return driver.current_url

def setUrl(url):
    global driver
    driver.get(url=url)

# 새로운 NetworkShape 값 반영해서 url 변경해서 이동
def setNetworkShape(newNetworkShape):
    global networkShape
    global driver
    updateNetworkShape()
    temp = getCurrentUrl().split('networkShape={0}'.format(networkShape))
    next_url = str(temp[0]) + 'networkShape=' + newNetworkShape + str(temp[1])
    return next_url

# 웹 리로딩 (setUrl을 쓴 이후 리로딩하기 위함)
def refesh():
    global driver
    driver.refresh()
    updateNetworkShape()