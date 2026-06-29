nilai = int(input("nilai kamu: "))

if nilai >=100 or nilai <=0:
    print("nilai tidak valid")
else:
    if nilai >= 75:
        print("lulus")
    else:
        print("tidak lulus")