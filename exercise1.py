import sys
sys.path.append(r'C:\Users\HSIANG-YI HUNG\Desktop\data-structure-course')

from lib.stack import Stack

s = Stack()
def dec_to_bin(dec):
    # Finish the function
    while dec != 0:
        n = dec//2
        l = dec%2
        dec = n
        s.push(l)
        print(l)
    for i in range(s.size()):
        print(s.pop(),end='')
    print('')

dec_to_bin(37)   # 回傳 101010
dec_to_bin(100)  # 回傳 1100100
