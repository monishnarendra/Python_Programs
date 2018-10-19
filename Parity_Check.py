class Sender:

    def Get_Bits():
        n = int(input("Enter the number of bits u are going to send"))
        print("Enter the bits in binary")
        for i in range(n):
            a = int(input())
            print(a)
            if a == 1 or a == 0:
                list1.append(a)
            else:
                print("please Enter again 0 ot 1 ")
                i = i - 1
        print(list1)

    def Generator(A):
        count_ones = 0
        for i in range(n):
            if A[i] == 1:
                count_ones = count_ones + 1
        if count_ones % 2 == 0:
            return 0
        else:
            return 1

class Reciver:

    def Recive_Data():
        print("Data has been recived")

    def Checker(A):
        count_ones = 0
        for i in range(n):
            if A[i] == 1:
                count_ones = count_ones + 1
        if count_ones % 2 == 0:
            return 0
        else:
            return 1

def Currupt_data():
    x1 = int(input("Enter the number of bits to be currupted"))
    for i in range(x1):
        x = int(input("Enter the Data position to be Currupted"))
        if list2[x] == 1:
            list2[x] = 0
        else:
            list2[x] = 1

list1 = []
list2 = []

n = 0
M = Sender

M.Get_Bits()
Parity_Bit = M.Generator(list1)
list1.append(Parity_Bit)
list2 = list1.copy()

if input("Do u wish to currupt the Data??") == 'y':
    Currupt_data()

if input("Do u wish to send the bit to the Reciver??") == 'y':
    N = Reciver
    N.Recive_Data()
    Syndrome = N.Checker(list2)
    if Syndrome != Parity_Bit:
        print("Data has been Discarded")
    else:
        print("Bit has no error")

print("Sender Bits")
print(list1)
print("Party_bit = ",Parity_Bit)

print("Reciver Bits")
print(list2)
print("Syndrome_bit = ",Syndrome)
