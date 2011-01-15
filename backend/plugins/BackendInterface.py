try:
	import plugins
except ImportError:
	import __init__ as plugins
	
class Backend(object):
	'''Implements a backend'''
	
	#at start, the backend has no plugins
	def __init__(self):
		self.plugins = []
	
	#Save the tuple of name, plugin and priority in the plugins list
	def registerPlugin(self, name, plugin, priority):
		self.plugins.append((name, plugin, priority))
		self.plugins.sort(key=lambda t: t[2])
	
	#has to be 
	def send(self, data):
		print("backend received: ", data)
	
	def loadPlugins(self):
		self.plugins = []
		PClasses=plugins.getPluginClasses()
		for pluginClass in PClasses:
			p=pluginClass(self)
			p.registerInBackend()


if __name__ == "__main__":
	backend=Backend()
	import TestPlugin
	plu=TestPlugin.TestPlugin(backend)
	print(backend.plugins)
	plu.registerInBackend()
	print(backend.plugins)
	backend.loadPlugins()
	print(backend.plugins)