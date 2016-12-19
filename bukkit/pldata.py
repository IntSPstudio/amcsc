#|==============================================================|#
# Made by IntSPstudio
# AMCsc
# Thank you for using this software!
#
# ID: 980005025
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import it8c
#EVENTS
eventID =4

#GLOBAL PLAYER LIST
def getGlobalPlayerList(rawArrayContent,fileName):
	#LIMITS
	array1Height = len(rawArrayContent)
	array1Width =  len(rawArrayContent[0])
	array2Width = array1Height
	array2Content = it8c.dataCreateList(array2Width,"")
	#CONTENT
	for yp in range(0, array1Height):
		for xp in range(0, array1Width):
			if (xp == eventID):
				array2Content[yp] = str.lower(rawArrayContent[yp][xp])
	#LIMITS
	array3Content = sorted(array2Content)
	array3Width = len(array3Content)
	pointa =""
	#CONTENT
	for i in range(0,2):
		if (i == 1):
			array4Height = ypb
			array4Width = 2
			array4Content = it8c.dataCreateArray(array4Height,array4Width,"")
		ypb =0
		for ypa in range(0, array3Width):
			pointb = array3Content[ypa]
			if (pointb != pointa):
				if (i == 1):
					array4Content[ypb][0] = str(ypb +1)
					array4Content[ypb][1] = pointb
				ypb +=1
			pointa = pointb
	#SAVE LIST
	it8c.csvWriteFile(array4Content,fileName,";")
	return array4Content
def getGlobalPlayerLog(rawArrayContent,fileStartName,fileEndName,playerCounterContent):
	#RAW
	rawArrayHeight = len(rawArrayContent)
	rawArrayWidth =  len(rawArrayContent[0])
	#PLAYER COUNTER (1D!)
	playerCounter = len(playerCounterContent)
	
	for i in range(0,playerCounter):
		pointCurrentPlayer = playerCounterContent[i][1]
		ypb =0
		for ypa in range(0,rawArrayHeight):
			checkEventAb = str.lower(rawArrayContent[ypa][eventID])
			if (checkEventAb == pointCurrentPlayer):
				ypb +=1
		#MAIN EVENT LIST
		array1Height = ypb
		array1Width = rawArrayWidth
		array1Content = it8c.dataCreateArray(array1Height,array1Width,"")
		#PICK FROM RAW ARRAY
		ypb =0
		for ypa in range(0,rawArrayHeight):
			checkEventAb = str.lower(rawArrayContent[ypa][eventID])
			if (checkEventAb == pointCurrentPlayer):
				for xpa in range(0,rawArrayWidth):
					array1Content[ypb][xpa] = str(rawArrayContent[ypa][xpa])
				ypb +=1
		#SAVE LIST
		fileName = fileStartName + pointCurrentPlayer + fileEndName
		it8c.csvWriteFile(array1Content,fileName,";")