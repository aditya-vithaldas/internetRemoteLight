from MotorClass import MotorClass
import requests

from time import sleep
Ena, In1, In2 = 2,3,4
Enb, In3, In4 = 14,15,18
m = MotorClass(Ena, In1, In2, In3, In4, Enb)

url = "http://internetRemoteRobotCar.adityavithaldas.repl.co/getcontrol"


prevcommand = ""

while 1:
    command = requests.get(url).text
    print (command)
    if command == "up":
        m.forward()
    elif command == "down":
        m.back()
    elif command == "left":
        m.left() 
    elif command == "right":
        m.right()
    elif command == "stop":
        m.stop()
