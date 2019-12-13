import msvcrt
while True:
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()
        if str(key_stroke[0]) == "48":
            print("key_stroke is a")
        print(str(key_stroke[0]))   # will print which key is pressed