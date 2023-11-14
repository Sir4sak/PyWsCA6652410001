import math

def rectanglearea(width, length):
    return width * length

def circlearea(radius):
    return math.pi * radius**2

def rectangularvolume(width, length, height):
    return width * length * height

def spherevolume(radius):
    return (4/3) * math.pi * radius**3

def areaandcube():
    while True:
        print("AREA & CUBE")
        print("1. พื้นที่สี่เหลี่ยม")
        print("2. พื้นที่วงกลม")
        print("3. ปริมาตรทรงสี่เหลี่ยม")
        print("4. ปริมาตรทรงกลม")
        print("0. ออกจากการทำงาน")
        try:
            choice = input("เลือกเมนู: ")

            if choice == '1':
                width = float(input("ป้อนความกว้าง: "))
                length = float(input("ป้อนความยาว: "))
                area = rectanglearea(width, length)
                print(f"พื้นที่สี่เหลี่ยม: {area:.2f}")
            elif choice == '2':
                radius = float(input("ป้อนรัศมี: "))
                area = circlearea(radius)
                print(f"พื้นที่วงกลม: {area:.2f}")
            elif choice == '3':
                width = float(input("ป้อนความกว้าง: "))
                length = float(input("ป้อนความยาว: "))
                height = float(input("ป้อนความสูง: "))
                volume = rectangularvolume(width, length, height)
                print(f"ปริมาตรทรงสี่เหลี่ยม: {volume:.2f}")
            elif choice == '4':
                radius = float(input("ป้อนรัศมี: "))
                volume = spherevolume(radius)
                print(f"ปริมาตรทรงกลม: {volume:.2f}")
            elif choice == '0':
                print("ออกจากการทำงาน")
                break
            else:
                print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")
        except ValueError:
            print("กรุณาป้อนตัวเลข")
areaandcube()