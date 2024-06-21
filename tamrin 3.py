def heapify(arr, n, a) :
    largest = a
    left = 2 * a + 1
    right = 2 * a + 2 

    if left < n and arr [a] < arr [left]:
        largest = left

    if right < n and arr [largest] < arr [right]:
        largest = right

    if largest != a:
        arr [a], arr [largest] = arr[largest], arr[a]
        heapify (arr, n, largest)

        
def heap_sort (arr):
    n = len (arr)

    for a in range (n // 2 - 1, -1, -1):
        heapify (arr, n, a)
        
    for a in range(n-1, 0, -1):
        arr[a], arr[0] = arr[0], arr[a] 
        heapify (arr, a, 0)


def main():
    data = input("maghadir ra vared konid")
    
    arr = list(map(int, data.split()))
    
    heap_sort (arr)

    print("areye moratab shode:", arr)
               
