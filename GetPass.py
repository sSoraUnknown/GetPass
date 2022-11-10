from pynput.mouse import Button
import pynput
import time
mouses=pynput.mouse.Controller() 


def MouseClick():
    mouses.press(Button.left)
    mouses.release(Button.left)
    time.sleep(0.2)

def MoveTo(number):
    mouses.move(-1366,-768) #перевод мышки в 0,0
    match number:
        case 1:
            mouses.move(600,305) #1
        case 2:
            mouses.move(685,305) #2
        case 3:
            mouses.move(770,305) #3
        case 4:
            mouses.move(600,395) #4
        case 5:
            mouses.move(685,395) #5
        case 6:
            mouses.move(770,395) #6
        case 7:
            mouses.move(600,480) #7
        case 8:
            mouses.move(685,480) #8
        case 9:
            mouses.move(770,480) #9
        case 0:
            mouses.move(600,565) #0
    MouseClick()
        


def Destruct(num):
    num = int(num)
    global num4
    num4 = num%10
    global num3
    num3 = (num//10)%10
    global num2
    num2 = (num//100)%10
    global num1
    num1 = (num//1000)%10

def Start():
    for x in range(0,10001):
        if(len(str(x))<2):
            number = "000"+str(x)
        elif(len(str(x))<3):
            number = "00"+str(x)
        elif(len(str(x))<4):
            number = "0"+str(x)
        elif(len(str(x))<5):
            number = str(x)
        Destruct(number)
        MoveTo(num1)
        MoveTo(num2)
        MoveTo(num3)
        MoveTo(num4)
        time.sleep(2)


time.sleep(3)
Start()
