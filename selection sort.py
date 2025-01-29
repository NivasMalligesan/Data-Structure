import array as arr 

def selectionSort(array,n):
    for i in range(0,n):
        minind = i
        for j in range(i,n):
            if array[i] > array[j] :
                minind = j
        array[i],array[minind] = array[minind],array[i]
        
    print(array)

n = int(input("Enter the number of elements: "))

my_array = arr.array('i', [])  
for i in range(0, n):
    element = int(input(f"Enter element {i+1}: "))
    my_array.append(element) 
print("Array elements:", my_array)
selectionSort(my_array,n)
    

    

