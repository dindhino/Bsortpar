from mpi4py import MPI
import time

def mergeSort(tubes):
    if len(tubes)>1:
        mid = len(tubes)//2
        left = tubes[:mid]
        right = tubes[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                tubes[k]=left[i]
                i=i+1
            else:
                tubes[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            tubes[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            tubes[k]=right[j]
            j=j+1
            k=k+1

def bubblesort(rk):
    for length in range(len(rk)-1,0,-1):
        for i in range(length):
            if rk[i]>rk[i+1]:
               temp = rk[i]
               rk[i] = rk[i+1]
               rk[i+1] = temp

#tools untuk mpi
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#menghitung waktu
start = time.time()

#memasukan dataset

if rank==0:
    hasil = []
    #memasukan semua rk dari rank 1-4 ke dalam satu array
    for i in range (1,size):
	rk = comm.recv(source=i)
	for j in range(0,len(rk)):
	    hasil.append(rk[j])

    #merge sort si hasil
    mergeSort(hasil)
    print "array hasil dibawah ini: "
    print (hasil)

    print ("===================================================================")
    end = time.time()
    print "start time: {}".format(start)
    print "end time: {}".format(end)
    print "waktu running: {} ".format(end-start)
    
else:
#rk = array tiap baris
	if rank == 1:
		rk = []
		rk.append(6695)
		rk.append(6624)
		rk.append(6615)
		rk.append(6694)
		rk.append(6531)
	elif rank == 2:
		rk = []
		rk.append(6654)
		rk.append(6614)
		rk.append(6646)
		rk.append(6672)
		rk.append(6639)
	elif rank == 3:
		rk = []
		rk.append(6602)
		rk.append(6607)
		rk.append(6609)
		rk.append(6621)
		rk.append(6629)
	elif rank == 4:
		rk = []
		rk.append(6139)
		rk.append(6089)
		rk.append(6524)
		rk.append(6000)
		rk.append(6001)
	bubblesort(rk)
	print(rk)
	print "Rank %d" %(rank)
	comm.send(rk, dest=0)
