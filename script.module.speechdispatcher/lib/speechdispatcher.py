import locale
import speechd

class SPEECHDISPATCHER:
	"""Supports The speech-dispatcher on linux"""

	def __init__(self, *args, **kwargs):
		try:
			self.speechdObject = speechd.Speaker('XBMC', 'XBMC')
		except:
			self.speechdObject =None 
			return
		try:
			self.speechdObject.set_language(locale.getdefaultlocale()[0][:2])
		except (KeyError,IndexError):
			pass
		self.speechdObject.set_rate(50)

	def speak(self, text, interrupt=0):
		if not self.speechdObject:
			return
		if interrupt:
			self.silence()
		self.speechdObject.speak(text)

	def silence(self):
		if not self.speechdObject:
			return
		self.speechdObject.cancel()

	def canSpeak(self):
		return bool(self.speechdObject)

