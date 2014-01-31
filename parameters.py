import common
import time
import configparser

class Parameters(object):
	""" Reads in a parameters file.
	
	Initializes parameters for robot functionality based on values provided
	in parameters file.
	
	Attributes:
		file_opened:	True if the parameters file is open

	"""
	
	# Public member variables
	file_opened = False
	
	# Private member objects
	#_string_parameters = {}
	# TODO: May not need to separate
	#_number_parameters = {}
	
	# Private member variables
	_file = None
	_config = None
	
	def __init__(self):
		""" Open the default file "parameters.par" to read program parameters
		
		Instantiate the parameters reader with default values
		
		"""
		_file = None
		_config = None
		file_opened = False
		self._open("parameters.par","r")
	
	
	def __init__(self, parameters_file, mode="r"):
		""" Open a file to read program parameters

		Instantiate the parameters reader with the passed file
		
		"""
		_file = None
		_config = None
		file_opened = False
		self._open(parameters_file,mode)
	
	def _open(path, mode):
		""" Open a file with the mode "r".
		 
		 Open a file for reading parameters
		 
		 Args:
			path: Path to the file
		"""
	
		if path:
			_file = open(path, mode)
			file_opened = true
			return true
		else:
			file_opened = false
			return false
			
	def _close():
		""" Close the file
		
		Close the file and mark not opened
		"""
		if _file:
			_file.close
			file_opened = false
	
	
	def read_values():
		""" Reads all parameter/value pairs from the file.
		
		Reads the entire parameter file and for NAME = VALUE pairs.
		The pairs are stored as a dictionary. Python should automatically
		handle typing
		
		Returns:
			A dictionary of the parameters read from the file
		"""
	
		# Instantiate ConfigParser and build dictionary of config options
		_config = ConfigParser.SafeConfigParser()
		
		_config.read(_file)

		_config._sections
		
		return _config._sections
	
	def get_value(section, parameter):
		""" Search the configuration dictionary for the parameter 
		
		Search the configuration dictionary for the specified parameter 
		and return the associated value
		
		"""
		return config.get(section, parameter)