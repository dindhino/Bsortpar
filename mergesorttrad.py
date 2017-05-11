import time
def mergeSort(data):
    print("Splitting ",data)
    if len(data)>1:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k]=left[i]
                i=i+1
            else:
                data[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            data[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            data[k]=right[j]
            j=j+1
            k=k+1
    print("Merging ",data)

data = [6000, 6001, 6089, 6139, 6524, 6531, 6602, 6607, 6609, 6614, 6615, 6621, 6624, 6629, 6639, 6646, 6654, 6672, 6694, 6695]
print"Sebelum: {}".format(data)
start = time.time()
mergeSort(data)
end = time.time()
print"Sesudah: {}".format(data)
print"Waktu Eksekusi: {} detik".format(end-start)
