# start = 10
# sum_number=0
# for number in range(start,20) :
#     c=int(input("masukkan angka : ")) **2
#     sum_number+=c 
# print("jmlh kuadrat: {}" .format(sum_number))


p=int(input("Masukkan jumlah baris : "))

for i in range(1,p+1):
    for j in range(1,p+1):
        if j>i:
            print()
            break
        else:
            print(j, end='')
            j+=1