import keyboard
import pyautogui as pyag
x=0
#In this project i Have Automated Your mouse now if ur computer is idle it wont make ur laptop sleep .
#If u run this program your mouse will be moving automatically AND if u are on a specific app u should be online.
#You just run this program you can go anywhere ur laptop wont be idle hence it will show that u are online as
#Your laptop is not idle.
pyag.moveTo(1300,100,duration=7)
while(x==0):
    if (pyag.position().x==1300):
        pyag.moveTo(100,150, duration = 7)
    elif (pyag.position().x==100):
        pyag.moveTo(1300,150,duration=7)

    print(pyag.position())
    if keyboard.is_pressed("p"):
        x=0
        break
        
       


      

