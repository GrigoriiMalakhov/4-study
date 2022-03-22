import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

for k in 0, 1, 2, 3, 4, 5, 6, 7:
    GPIO.setup(dac[k], GPIO.OUT)

try:
    per = input("Let's try to shine, give me the number from 0 to 255: ")

    if (per.lower() == 'q'):
        raise Exception
    else:
        per = int(per)
        if 0 <= per <= 255:
            print("Good choyse")
        else:
            raise ValueError("Bad choyse, incorrect number")
        print("Estiamted voltage", (per/2550)*(33))
        for j in range(8) :
            GPIO.output(dac[7 - j], per % 2)
            per //= 2
        
        time.sleep(5)  

         
     
except KeyboardInterrupt:
    print("Problem with interrupt")
except ValueError:
    print("Value incorrct")
except Exception:
    print("Something wrong")
finally:
    print("Time to go home")
    for j in 0, 1, 2, 3, 4, 5, 6, 7 :
        GPIO.output(dac[7 - j], 0)