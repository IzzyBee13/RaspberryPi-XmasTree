
from gpiozero import LEDBoard
from gpiozero import PWMLED
from time import sleep


tree = LEDBoard(6,7,8)
tree1 = LEDBoard(13,16,20)
tree2 = LEDBoard(19,21,26)
tree3 = LEDBoard(9,10,22)
tree4 = LEDBoard(23,24,25)
tree5 = LEDBoard(15,18,27)
tree6 = LEDBoard(4,17,14)
tree7 = LEDBoard(5,11,12)
tree8 = PWMLED(2)#This is the star

while True:
    tree8.pulse() #Put this first so it starts immediately
    tree.on()
    sleep(0.5)
    tree.off()
    tree1.on()
    sleep(0.5)
    tree1.off()
    tree2.on()
    sleep(0.5)
    tree2.off()
    tree3.on()
    sleep(1)
    tree3.off()
    tree4.on()
    sleep(0.5)
    tree4.off()
    tree5.on()
    sleep(1)
    tree5.off()
    tree6.on()
    sleep(0.5)
    tree6.off()
    tree7.on()
    sleep(0.5)
    tree7.off()
    
   


