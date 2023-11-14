import random

def randomnumber():
    targetNumber = random.randint(1, 100)
    
    while True:
        try:
            userInput = int(input("ทายตัวเลขที่มีค่าอยู่ที่ 1-100: "))
            if userInput == targetNumber:
                print("ยินดีด้วยคุณทายถูก!")
                break
            elif userInput < targetNumber:
                print("คุณทายผิดตัวเลขที่ป้อนน้อยไป")
            else:
                print("คุณทายผิดตัวเลขที่ป้อนมากไป")
        except ValueError:
            print("กรุณาป้อนตัวเลขเท่านั้น")

randomnumber()