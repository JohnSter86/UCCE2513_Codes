import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) #use GP17 as output

while True:
    try:
        print("Menu:")
        print("1. Turn on LED")
        print("2. Turn off LED")
        print("3. Quit program")
        choice = int(input("Please enter your choice: "))

        if choice == 1:
            GPIO.output(17, 1)       #turn on LED
        elif choice == 2:
            GPIO.output(17, 0)       #turn on LED
        elif choice == 3:
            print("Bye")
            GPIO.cleanup()
            exit()
        else:
            print("Invalid selection")
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
