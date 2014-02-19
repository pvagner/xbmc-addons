import xbmc
import json
import urlparse
import time
import sys
if sys.platform.find('linux') >=0:
	from speechdispatcher import SPEECHDISPATCHER as TTS
else:
	from nvda import NVDA as TTS

args = urlparse.parse_qs(sys.argv[2][1:])

oldID =json.loads(xbmc.executeJSONRPC(r'{"jsonrpc":"2.0","id":0,"method":"Gui.GetProperties","params":{"properties":["currentwindow"]}}'))['result']['currentwindow']['id']
action = args.get('action', None)

if action:
	action = action[0]
	xbmc.executebuiltin("Action(%s)"%action)
	time.sleep(0.2)

resp =json.loads(xbmc.executeJSONRPC(r'{"jsonrpc":"2.0","id":0,"method":"Gui.GetProperties","params":{"properties":["currentwindow","currentcontrol"]}}'))
s = TTS()
if s.canSpeak():
	text=""
	if action==None or resp['result']['currentwindow']['id'] !=oldID:
		text="%s: "%resp['result']['currentwindow']['label']
	text="%s%s"%(text,resp['result']['currentcontrol']['label'])
	s.speak(text)
s.terminate()
sys.exit(0)

