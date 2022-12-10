from crawling import *
import time


# "8,3,4,4,7"로 퍼셉트론 변경 후 10초 동안 학습시킨 후 test_loss 값 출력, 이후 다시 "4,2"로 변경

#초기 퍼셉트론을 설정해서 테스트

테스트할_페셉트론 = '8,3,4,4,7'
setUrl(setNetworkShape(테스트할_페셉트론))
refesh()

play_pause_button()
time.sleep(4)
play_pause_button()
print("epoch :", getEpoch())
print("test-loss :",getTestLoss())

# 다른 퍼셉트론으로 변경
변경할_퍼셉트론 = '4,2' #반영될 값이 '4,2'
url = setNetworkShape(변경할_퍼셉트론)

# url을 설정해주고 새로고침
setUrl(url)
refesh()