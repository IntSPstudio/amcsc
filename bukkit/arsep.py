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
#SETTINGS
fileNameI ="sample.csv"
#EVENTS
eventID =1
eventBuyName ="buy"
eventSellName ="sell"
eventPayName ="pay"
eventWarpName ="warp"
#EKONEV ARRAY
def getEkonevArray(rawArrayContent,fileName):
	#INPUT
	rawArrayHeight = len(rawArrayContent)
	rawArrayWidth = len(rawArrayContent[0])
	#CHECK EVENT
	ypb =0
	for ypa in range(0,rawArrayHeight):
		checkEventAb = str.lower(rawArrayContent[ypa][eventID])
		if (checkEventAb == eventBuyName or checkEventAb == eventSellName or checkEventAb == eventPayName):
			ypb +=1
	#MAIN EVENT LIST
	ekonEventArrayHeight = ypb
	ekonEventArrayWidth = rawArrayWidth
	ekonEventArrayContent = it8c.dataCreateArray(ekonEventArrayHeight,ekonEventArrayWidth,"")
	#PICK FROM RAW ARRAY
	ypb =0
	for ypa in range(0,rawArrayHeight):
		checkEventAb = str.lower(rawArrayContent[ypa][eventID])
		if (checkEventAb == eventBuyName or checkEventAb == eventSellName or checkEventAb == eventPayName):
			for xpa in range(0,rawArrayWidth):
				ekonEventArrayContent[ypb][xpa] = str(rawArrayContent[ypa][xpa])
			ypb +=1
	#SAVE EKONEV
	it8c.csvWriteFile(ekonEventArrayContent,fileName,";")
	return ekonEventArrayContent
#WARP ARRAY
def getWarpArray(rawArrayContent,fileName):
	#INPUT
	rawArrayHeight = len(rawArrayContent)
	rawArrayWidth = len(rawArrayContent[0])
	#CHECK EVENT
	ypb =0
	xpb =0
	for ypa in range(0,rawArrayHeight):
		xpc =0
		checkEventAb = str.lower(rawArrayContent[ypa][eventID])
		if (checkEventAb == eventWarpName):
			ypb +=1
			for xpa in range(0,rawArrayWidth):
				xpd = rawArrayContent[ypa][xpa]
				if xpd !="":
					xpc +=1
			if xpc > xpb:
				xpb = xpc
	#MAIN EVENT LIST
	warpEventArrayHeight = ypb
	warpEventArrayWidth = xpb
	warpEventArrayContent = it8c.dataCreateArray(warpEventArrayHeight,warpEventArrayWidth,"")
	#PICK FROM RAW ARRAY
	ypb =0
	for ypa in range(0,rawArrayHeight):
		checkEventAb = str.lower(rawArrayContent[ypa][eventID])
		if (checkEventAb == eventWarpName):
			xpc =0
			for xpa in range(0,rawArrayWidth):
				xpb = rawArrayContent[ypa][xpa]
				if xpb !="":
					warpEventArrayContent[ypb][xpc] = str(rawArrayContent[ypa][xpa])
					xpc +=1
			ypb +=1
	#SAVE EKONEV
	it8c.csvWriteFile(warpEventArrayContent,fileName,";")
	return warpEventArrayContent
