#|==============================================================|#
# Made by IntSPstudio
# AMCsc
# Thank you for using this software!
# Version: 0.0.1.20161219
# ID: 980005025
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import it8c
import arsep
import pldata
#SETTINGS
fileNameI ="trade.log"
fileSep =","
#START
if __name__ == "__main__":
	if it8c.fileTextExists(fileNameI) == 1:
		#RAW CONTENT
		logArrayContent = it8c.csvReadFile(fileNameI,fileSep)
		logArrayHeight = len(logArrayContent)
		logArrayWidth = len(logArrayContent[0])
		#LOG PLAYER LIST
		logArrayPlayersFileName = "glog-users.csv"
		logArrayPlayersContent = pldata.getGlobalPlayerList(logArrayContent,logArrayPlayersFileName)
		logArrayPlayersCounter = len(logArrayPlayersContent)
		logArrayPlayersPvFileNameA = "user-glog-"
		logArrayPlayersPvFileNameB = ".csv"
		pldata.getGlobalPlayerLog(logArrayContent,logArrayPlayersPvFileNameA,logArrayPlayersPvFileNameB,logArrayPlayersContent)
		#GLOBAL EKONEV
		ekonevArrayFileName = "ekonev.csv"
		ekonevArrayContent = arsep.getEkonevArray(logArrayContent,ekonevArrayFileName)
		#WARP
		warpArrayFileName =  "warp.csv"
		warpArrayContent = arsep.getWarpArray(logArrayContent,warpArrayFileName)