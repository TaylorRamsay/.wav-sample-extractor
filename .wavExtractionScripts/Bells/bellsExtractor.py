import numpy as np
import aubio
import csv

# explicit function to normalize array
def normalize(arr, t_min, t_max):
    norm_arr = []
    diff = t_max - t_min
    diff_arr = max(arr) - min(arr)    
    for i in arr:
        temp = (((i - min(arr))*diff)/diff_arr) + t_min
        norm_arr.append(temp)
    return norm_arr

#Aubio
chiraAubio = aubio.source("C:\\Users\FSK8475\Documents\GitHub\.wav-sample-extractor\\visualEdits\\Bells.wav")
total_read = 0
nums = []

print("Extracting data using Aubio library.......")
while True:
    samples, read = chiraAubio()
    nums.append(np.format_float_positional(samples.sum()))
    total_read += read
    if read < chiraAubio.hop_size:
        break


# Convert string list nums to float list numsFloats
numsFloats = [float(ele) for ele in nums]

print("Writing raw output to rawOutput.txt")
file = open(".wavExtractionScripts\\Bells\\rawOutput.txt", "w")
for x in numsFloats:
    file.write(str(x) + "\n\n")
print("Done.......\n")

temp = []
final = []
range_to_normalize = (0,10)

maximaIndices = []
padWindow = 4

for i in range(len(numsFloats) - 1):
    if numsFloats[i] >= .1:
        temp.append(5)
        maximaIndices.append(i)

    else:
        if numsFloats[i] < 1:
            numsFloats[i] = 0.0001
        temp.append(numsFloats[i])

count = 0

for x in maximaIndices:
    while count < padWindow:
        temp[x + count] = temp[x]
        temp[x - count] = temp[x]
        count += 1
    count = 0

csvOutput = open(".wavExtractionScripts\\Bells\\bellsOutput.csv", "w")
writer = csv.writer(csvOutput)

print("Writing output to bellsOutput.csv")
for x in temp:
    writer.writerow([str(x)])
    #print(str(x)) 
print("Done.......\n")

print("Extraction complete........")