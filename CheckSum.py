def Get_Text(text_original):
    text_copy = text_original
    list1 = ':'.join(hex(ord(x))[0:] for x in text_copy)  # text to hexa
    print("Given input in Hexadecimal format, with :", list1)
    list2 = list1.split(':')
    print("Given input in Hexadecimal format, split ",list2)
    list3 = ' '.join(list2).replace('0x', '').split()
    print("Given input in Hexadecimal format, without 0x = ",list3)
    list4 = [''.join(list3) for list3 in zip(list3[0::2], list3[1::2])]
    print("Given Text in Hexadecimal format ,",list4)
    return list4

def dec_to_hex(number):
    rValue = ""
    hex_bits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    while(number):
        rValue = hex_bits[int(number%16)] + rValue
        number = number/16
    return rValue

def hex_to_dec(hex_string):
    hex_dict = {"0" : 0,
                "1" : 1,
                "2" : 2,
                "3" : 3,
                "4" : 4,
                "5" : 5,
                "6" : 6,
                "7" : 7,
                "8" : 8,
                "9" : 9,
                "A" : 10,
                "B" : 11,
                "C" : 12,
                "D" : 13,
                "E" : 14,
                "F" : 15}
    rValue = 0
    multiplier = 1
    str_hex_string = str(hex_string)
    for i in range(len(str_hex_string)):
        rValue = hex_dict[str_hex_string[len(str_hex_string)-1-i]] * multiplier + rValue
        multiplier = multiplier * 16
    return rValue

def Remove_Leading_zero(A):
    A = A.lstrip('0')  # removing leading 0000000
    A = list(A)        # put in list
    return A


list1 = [] #contains original text to hexa
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
i,result = 0,0

text_original = input("Enter the text message to be sent")  # contains original values

list4 = Get_Text(text_original)

list4 = [element.upper() for element in list4] #capitalization

while i != len(list4):
    result = dec_to_hex(hex_to_dec(result) + hex_to_dec(list4[i]))
    i = i + 1

print("Result sum with zero = ",result)

result = Remove_Leading_zero(result)

print("Result sum without zero = ",result)

list5 = list(result)

print("Result sum without zero in list = ",list5)

if len(list5) > 4:
    a = list5.pop(0)
    print(list5)
    str1 = ''.join(list5) #convert a list to string
    result_new = dec_to_hex(hex_to_dec(str1) + hex_to_dec(a))

print("Result(2) new with zero = ",result_new)

result_new = Remove_Leading_zero(result_new)

print("Result(2) new sum without zero = ",result_new)

list6 = list(result_new)

print("Result(2) new sum without zero in list = ",list6)

complement = hex(int(result_new, 16) ^ 0xFFFF)
print("complement =",complement)

for i in range(len(list4)):
    list7.append(list4[i])

list7.append(complement)
i = 0

list7 = ' '.join(list7).replace('0x', '').split()

print(list7)

while i != len(list7):
    result_reciver = dec_to_hex(hex_to_dec(result) + hex_to_dec(list7[i]))
    i = i + 1

print("result Reciver add with zero = ",result_reciver)

result_reciver = Remove_Leading_zero(result_reciver)

print("result Reciver add without zero = ",result_reciver)

list8 = list(result_reciver)

if len(list8) > 4:
    a = list8.pop(0)
    print(list8)
    str1 = ''.join(list8) #convert a list to string
    final_result = dec_to_hex(hex_to_dec(str1) + hex_to_dec(a))

print("final result with zero = ",final_result)

final_result = Remove_Leading_zero(final_result)

print("final result without zero = ",final_result)

complement = hex(int(final_result, 16) ^ 0xFFFF)

print("compliment",complement)