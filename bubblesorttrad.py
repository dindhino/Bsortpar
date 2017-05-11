import time

data = [6000, 6001, 6089, 6139, 6524, 6531, 6602, 6607, 6609, 6614, 6615, 6621, 6624, 6629, 6639, 6646, 6654, 6672, 6694, 6695]
print"Sebelum: {}".format(data)

mulai = time.time()
for isi in range(len(data)-1, 0, -1):
	for i in range(isi):
		if data[i] > data[i+1]:
			data[i], data[i+1] = data[i+1], data[i]
	print data
selesai = time.time()
print"Sesudah: {}".format(data)
print"Waktu Eksekusi: {} detik".format(selesai-mulai)
