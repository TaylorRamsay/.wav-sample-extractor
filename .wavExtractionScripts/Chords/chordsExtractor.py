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
chiraAubio = aubio.source("C:\\Users\FSK8475\Documents\GitHub\.wav-sample-extractor\\ChiraStems\\Chords.wav")
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
file = open(".wavExtractionScripts\\Chords\\rawOutput.txt", "w")
for x in numsFloats:
    file.write(str(x) + "\n\n")
print("Done.......\n")

temp = []
segToSort = []
range_to_normalize = (0,15)

csvOutput = open(".wavExtractionScripts\\Chords\\chordsOutput.csv", "w")
writer = csv.writer(csvOutput)

print("Sorting and normalizing data........")
for i in range(len(numsFloats) - 1):
    if numsFloats[i] < 1 and numsFloats[i + 1] > 30:
        segToSort = sorted(temp, key = float)
        temp.clear()
        normalizedSeg = normalize(segToSort, range_to_normalize[0], range_to_normalize[1])
        normalizedSeg.reverse()

        for x in normalizedSeg:
            writer.writerow([str(x)])
    else:
        temp.append(numsFloats[i])

print("Processed output written to chordsOutput.csv")
print("Done.......\n")
print("Extraction complete........")