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
chiraAubio = aubio.source("C:\\Users\FSK8475\Documents\GitHub\.wav-sample-extractor\\ChiraStems\\Bass Drum.wav")
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
file = open(".wavExtractionScripts\\BassDrum\\rawOutput.txt", "w")
for x in numsFloats:
    file.write(str(x) + "\n" + "\n")
print("Done.......\n")

temp = []
final = []
range_to_normalize = (0,15)

print("Sorting and normalizing data........")
for i in range(len(numsFloats) - 1):
    if numsFloats[i] >= 50:
        temp.append(numsFloats[i])
        temp[i - 1] = numsFloats[i]
        temp[i - 2] = numsFloats[i]
        temp[i - 3] = numsFloats[i]
        temp[i - 4] = numsFloats[i]
        temp[i - 5] = numsFloats[i]

    else:
        if (numsFloats[i] < 100):
            numsFloats[i] = 0.1
        temp.append(numsFloats[i])

csvOutput = open(".wavExtractionScripts\\BassDrum\\BassDrum.csv", "w")
writer = csv.writer(csvOutput)

print("Writing output to BassDrum.csv")
for x in temp:
    writer.writerow([str(x)])
print("Done.......\n")

print("Extraction complete........")