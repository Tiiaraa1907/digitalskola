a=int(input("Input angka positif: "))

if a>0:
    if a%2==0 or a%3==0 or a%5==0:
        if a%2==0:
            if a%2==0 and a%3==0 and a%5==0:
                print("kelipatan 2 , kelipatan 3, dan kelipatan 5")
                if a<100:
                    print("angka ini dibawah 100")
                elif a>100:
                    print("angka ini diatas 100")
                else:
                    print("angka ini adalah 100")
            elif a%2==0 and a%3==0:
                print("kelipatan 2 dan kelipatan 3")
                if a<100:
                    print("angka ini dibawah 100")
                elif a>100:
                    print("angka ini diatas 100")
                else:
                    print("angka ini adalah 100")
            elif a%2==0 and a%5==0:
                print("kelipatan 2 dan kelipatan 5")
                if a<100:
                    print("angka ini dibawah 100")
                elif a>100:
                    print("angka ini diatas 100")
                else:
                    print("angka ini adalah 100")
            elif a%2==0:
                print("kelipatan 2")
                if a<100:
                    print("angka ini dibawah 100")
                elif a>100:
                    print("angka ini diatas 100")
                else:
                    print("angka ini adalah 100")
            else:
                print()
        elif a%3==0:
            if a%3==0 and a%5==0:
                print("kelipatan 3 dan kelipatan 5")
                if a<100:
                    print("angka ini dibawah 100")
                if a>100:
                    print("angka ini diatas 100")
                else:
                    print("angka ini adalah 100")
            elif a%3==0:
                print("kelipatan 3")
                if a<100:
                    print("angka ini dibawah 100")
                elif a>100:
                    print("angka ini diatas 100")
                else:
                    print("angka ini adalah 100")
        elif a%5==0:
            print("kelipatan 5")
            if a<100:
                print("angka ini dibawah 100")
            elif a>100:
                print("angka ini diatas 100")
            else:
                print("angka ini adalah 100")
        else:
            print()
    else:
        print("bukan kelipatan 2, kelipatan 3, ataupun kelipatan 5")   
else:
    print("silahkan masukkan angka positif")