import pyautogui as auto
from time import sleep
width,height = auto.size()
# auto.moveTo(10,20, duration=1)
# auto.moveRel(200,100,duration=2)
auto.position()
sleep(2)
# for i in range(1,200):
#     auto.moveTo(i,i*2)
auto.moveTo(1230,30,duration=0.5)
auto.scroll(-200)
auto.click()
# auto.dragRel(20,30)
# auto.dragRel(20,-30)
a = 300
# auto.KEYBOARD_KEYS
# auto.typewrite() me shkru
# auto.hotkey() mi prek disa tastet per menjehere
auto.moveTo(20,360)
auto.click()
# auto.locateOnScreen() e merr ni foto si argument e tkallxon ku osht ne screen
auto.moveTo(323,306,duration=0.5)
auto.dragTo(655,610,duration=0.5)
auto.doubleClick()
auto.moveTo(20,215,duration=0.5)
auto.moveTo(30,475)
auto.click()
auto.moveTo(200,510)
auto.click()
auto.moveTo(350,320,duration=0.5)
while a>0:
    auto.dragRel(a,0)
    a-=20
    auto.dragRel(0 , a)
    a -= 20
    auto.dragRel(-a , 0)
    a -= 20
    auto.dragRel(0 , -a)
    a -= 20
