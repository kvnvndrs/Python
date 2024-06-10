from datetime import datetime
import time as tm
import os

def reloj():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

while(True): 
    print("La hora es: ",reloj())
    tm.sleep(1)
    os.system('cls')