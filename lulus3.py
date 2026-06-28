nilai = int(input("nilai kamu: "))

if nilai >= 0:
    if nilai <= 100:
        if nilai >= 75:
            print("lulus")
        else:
            print("tidak lulus")
    else:
        print("nilai tidak valid")
else:
    print("nilai tidak valid")