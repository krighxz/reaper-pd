# PARSES ALL AUTOMATION DATA FROM .RPP PROJECT FILE AND CONVERTS
# INTO PD/MAX READABLE .COLL FORMAT AT 1ms INTERVALS:
#
# index, lane 1, lane 2, lane 3, lane 4, ..., lane n;

#import easygui as eg

trackID = -1
laneID = -1
# 3-D array vectorList[track][lane][ [time][value] ]
vectorList = [[[ ]]]

with open('project4.RPP', 'r') as f:
	# go through each line in .RPP file
	for line in f:
		# store selection markers
		if line.strip().startswith("SELECTION"):
			selection = [float(line.strip().split()[1]),float(line.strip().split()[2])]
		# iterate track
		if line.strip().startswith("<TRACK"):
			trackID += 1
			vectorList.append([[]])
		# iterate automation lane
		if line.strip().startswith("<PARMENV"):
			# return PARMENV ID for this track
			laneID = int(line.strip().split()[1])
			vectorList[trackID].append([])
		# iterate parameter timestamp/values
		if line.strip().startswith("PT") and laneID >= 0:
			vectorList[trackID][laneID].append([float(line.strip().split()[1]), float(line.strip().split()[2])])

# length of selected sequence in seconds
totalLength = selection[1] - selection[0]

currentData = [[]]
for t in range(len(vectorList)-1):
	for l in range(len(vectorList[t])-1):
		# don't append first (ie. empty) element of array
		if (len(currentData[0]) > 0):
			currentData.append([])
		# iterate through points in vector list
		for i in range(len(vectorList[t][l])):
			# retrieve current and next point and length in milliseconds between two points
			if i == 0:
				# creates data between 0 and first timestamp
				p1 = 0
				p2 = vectorList[t][l][i][0]
				v1 = vectorList[t][l][i][1]
				v2 = vectorList[t][l][i][1]
			else:
				p1 = vectorList[t][l][i-1][0]
				p2 = vectorList[t][l][i][0]
				v1 = vectorList[t][l][i-1][1]
				v2 = vectorList[t][l][i][1]
			pLength = int(round( (p2-p1) * 1000 ))
			# don't write data if length == 0 (eg. if there is a point at timestamp 0)
			if pLength == 0:
				pass
			# interpolate between two points and write into currentData
			else:
				for s in range(pLength):
					k = (v2-v1) / pLength
					currentData[len(currentData)-1].append(k*s+v1)
			# in last iteration check if timestamp is less than total duration
			if i == len(vectorList[t][l])-1:
				if p2 < selection[1]:
					# if true then append rest of array with last value (+1 sample in case of rounding error)
					for s in range(int(selection[1]*1000 - p2*1000 + 1)):
						currentData[len(currentData)-1].append(v2)

# write into textfile in max/pd readable coll format
with open('project4.coll','w') as f:
	for i in range(int(round(totalLength*1000)-1)):
		f.write(str(i) + ', ')
		for j in range(len(currentData)):
			f.write(str(currentData[j][i+ int(selection[0]*1000) ]))
			if j < len(currentData)-1:
				f.write(' ')
		f.write(';\n')

with open()

print totalLength

