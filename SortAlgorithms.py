#bubblesort
def bubble_sort(a_list):
    sorta = False
    size = len(a_list)
    while not sorta:
        sorta = True
        for num in range(0,size - 1):
            if a_list[num + 1] < a_list[num]:
                temp = a_list[num + 1]
                a_list[num + 1] = a_list[num]
                a_list[num] = temp
                sorta = False
        size -= 1
#-------------------------------------------------------------------------------------
#Merge Sort
def merge(a_list, first, mid, last):
    tempList = []
    first1 = first
    last1 = mid
    first2= mid + 1
    last2 = last
    #print('Start' + ' ' + str(first) + ' ' + str(mid) + ' '+ str(last))
    #print(a_list)
    #print(tempList)
    index = first1
    try:
        while first1 <= last1 and first2 <= last2:
            if a_list[first1] <= a_list[first2]:
                tempList.append(a_list[first1])
                first1 += 1
            else:
                tempList.append(a_list[first2])
                first2 += 1
            #index += 1
    except IndexError:
        #print('Index is ' + str(first1))
        pass
    while first1 <= last1:
        tempList.append(a_list[first1])
        first1 += 1
    while first2 <= last2:
        tempList.append(a_list[first2])
        first2 += 1
    #print('Processing')
    #print(tempList)
    index = 0
    try:
        for num in range(first, last + 1):
            a_list[num]= tempList[index]
            index += 1
    except IndexError:
        print('For loop index: ' + str(num))
    #print('Finish')
    #print(a_list)
def mergeSort(a_list, first, last):
    if first < last:
        mid = int((first + last)/2)
        mergeSort(a_list, first, mid)
        mergeSort(a_list, mid + 1, last)
        #print(str(first) + ' ' + str(mid) + ' '+ str(last))
        merge(a_list, first, mid, last)
#-------------------------------------------------------------------------------------
c = []
d = []
import random
for num in range(1,16):
    c.append(random.randint(1,100))
d = list(c)
#for num in range(1,21):
    #d.append(random.randint(1,100))
print(c)
bubble_sort(c)
print(c)
print('Merge')
print(d)
mergeSort(d, 0,(len(d)-1))
print(d)