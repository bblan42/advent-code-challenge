
depthMeasurementsFile = open("input.txt")
depthMeasurementsFileRead = depthMeasurementsFile.read()
depthMeasurementsFile.close()
measurements = depthMeasurementsFileRead.split("\n")
measurements = list(measurements)
print(measurements)
index = 0
count = 0
for measurement in measurements:
    currentIndex = measurements.index
    nextValue = measurements[index + 1]
    intMeas = int(measurement)
    intNextMeas = int(nextValue)
    if intNextMeas > intMeas:
        count +=1
    print(count)
    index += 1
print(count)
