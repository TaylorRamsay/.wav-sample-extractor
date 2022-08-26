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

chiraAubio = aubio.source("C:\\Users\FSK8475\Documents\GitHub\.wav-sample-extractor\\visualEdits\\SynthLead.wav")
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
file = open(".wavExtractionScripts\\SynthLead\\rawOutput.txt", "w")
for x in numsFloats:
    file.write(str(x) + "\n\n")
print("Done.......\n")

csvOutput = open(".wavExtractionScripts\\SynthLead\\synthLeadOutput.csv", "w")
writer = csv.writer(csvOutput)

print("Writing output to synthLeadOutput.csv")
for x in numsFloats:
    if x < 0.01:
        x = 0.0001
    writer.writerow([str(x)])
    #print(str(x))   
print("Done.......\n")
print("Extraction complete........")