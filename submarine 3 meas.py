
depthMeasurementsFile = open("input.txt")
depthMeasurementsFileRead = depthMeasurementsFile.read()
depthMeasurementsFile.close()
measurements = depthMeasurementsFileRead.split("\n")
measurements = list(measurements)
print(measurements)
index = 0
count = 0
for measurement in measurements:
    triple = [int(measurements[index]), int(measurements[index+1]),int(measurements[index+2])]
    nextTriple = [int(measurements[index+1]), int(measurements[index+2]),int(measurements[index+3])]
    tripleSum = sum(triple)
    nextTripleSum = sum(nextTriple)
    if nextTripleSum > tripleSum:
        count +=1
    print(count)
    index += 1
print(count)

