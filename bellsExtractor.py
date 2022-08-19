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
chiraAubio = aubio.source("C:\\Users\FSK8475\Documents\GitHub\.wav-sample-extractor\\ChiraStems\\Bells.wav")
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

file = open("rawOutput.txt", "w")
for x in numsFloats:
    file.write(str(x) + "\n\n")

temp = []
final = []
range_to_normalize = (0,10)

csvOutput = open("bellsOutput.csv", "w")
writer = csv.writer(csvOutput)

print("Normalizing data........")
'''for i in range(len(numsFloats) - 1):
    #temp.clear()
    normalizedSeg = normalize(numsFloats, range_to_normalize[0], range_to_normalize[1])
    print("working")
    #normalizedSeg.reverse()
    #final.append(normalizedSeg)
'''
normalizedNums = normalize(numsFloats, range_to_normalize[0], range_to_normalize[1])
for x in normalizedNums:
    writer.writerow([str(x)])
    print(str(x))
    


print("Done.......")
# Displays original array
#print("Original Array = ", sorted)

# Displays normalized array
#print("Normalized Array = ",normalized_array_1d)