import time
from xbmcjson import XBMC
import sys
if sys.platform.find('linux') >=0:
	from speechdispatcher import SPEECHDISPATCHER as TTS
else:
	from nvda import NVDA as TTS

s = TTS()
xbmc=XBMC("http://localhost:8080/jsonrpc")

controlLabel=""
windowLabel=""
windowID=0
while True:
	resp =xbmc.GUI.GetProperties({"properties":["currentcontrol","currentwindow"]})
	# print resp
	win=resp['result']['currentwindow']
	ctrl=resp['result']['currentcontrol']
	if controlLabel !=ctrl['label']:
		if windowID !=win['id']:
			windowID =win['id']
			windowLabel=win['label']
		controlLabel=ctrl['label']
		if s.canSpeak():
			print("%s\t%s"%(windowLabel,controlLabel))
			s.speak("%s\t%s"%(windowLabel,controlLabel))
		windowLabel=""
	time.sleep(1)
