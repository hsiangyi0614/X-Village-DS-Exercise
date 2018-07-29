import sys
sys.path.append(r'C:\Users\HSIANG-YI HUNG\Desktop\data-structure-course')


from lib.queue import Queue

q = Queue()
def hot_potato(name_list, num):
    # Finish the function
    for name in name_list:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    print(q.dequeue()) 


hot_potato(["Susan", "Brad", "Kent", "David"], 6)               # 回傳 "Brad"
print('-'*20)
hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)  # 回傳 "Susan"
