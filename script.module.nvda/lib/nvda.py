from ctypes import windll
import os

class NVDA (object):
	"""Supports The NVDA screen reader"""

	def __init__(self, *args, **kwargs):
		try:
			self.dll = windll.LoadLibrary(os.path.join(os.path.dirname(__file__), 'nvdaControllerClient32.dll'))
		except:
			self.dll =None

	def speak(self, text, interrupt=0):
		if not self.dll:
			return
		if interrupt:
			self.silence()
		self.dll.nvdaController_speakText(unicode(text))

	def silence(self):
		if not self.dll:
			return
		self.dll.nvdaController_cancelSpeech()

	def canSpeak(self):
		try:
			return self.dll.nvdaController_testIfRunning() == 0
		except:
			return False

	def terminate(self):
		pass

