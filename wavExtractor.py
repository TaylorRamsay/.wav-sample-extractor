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
print("\nAubio........")
chiraAubio = aubio.source("C:\\Users\\CDK345\Desktop\wavExtractor\\ChiraStems\\Chords.wav")
total_read = 0
nums = []

print("Extracting data.......")
while True:
    samples, read = chiraAubio()
    nums.append(np.format_float_positional(samples.sum()))
    total_read += read
    if read < chiraAubio.hop_size:
        break


# Convert string list nums to float list numsFloats
numsFloats = [float(ele) for ele in nums]

temp = []
segToSort = []
final = []
range_to_normalize = (0,50)

csvOutput = open("output.csv", "w")
writer = csv.writer(csvOutput)

print("Sorting and normalizing data........")
for i in range(len(numsFloats) - 1):
    if numsFloats[i] < 1 and numsFloats[i + 1] > 30:
        segToSort = sorted(temp, key = float)
        temp.clear()
        normalizedSeg = normalize(segToSort, range_to_normalize[0], range_to_normalize[1])
        normalizedSeg.reverse()
        final.append(normalizedSeg)

        for x in normalizedSeg:
            writer.writerow([str(x)])
    else:
        temp.append(numsFloats[i])



#file = open("sorted.txt", "w")
#for x in final:
 #   file.write(str(x) + "\n")

print("Done.......")
# Displays original array
#print("Original Array = ", sorted)

# Displays normalized array
#print("Normalized Array = ",normalized_array_1d)