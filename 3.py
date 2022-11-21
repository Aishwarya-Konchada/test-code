def RotatedNumberExist(num):
    rotate_map = {"0":"0", "1":"1", "2":"2", "5":"5", "6":"9", "8":"8", "9":"6"}
    nums_list = list(str(num))
    new_num = ""
    for i in nums_list:
        if i in rotate_map.keys():
            new_num = new_num + rotate_map[i]
        else:
            return False
    return new_num

def FindNthRotatableNumber(number):
    count = 0
    number = 0
    while count < 8:
        number += 1
        if RotatedNumberExist(number):
            count += 1
    return number

print(FindNthRotatableNumber(8))