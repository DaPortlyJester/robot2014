import configparser

class Parameters(object):
    """ Reads in a parameters file.

    Initializes parameters for robot functionality based on values provided
    in parameters file.

    Attributes:
        file_opened:    True if the parameters file is open

    """

    # Public member variables
    file_opened = False

    # Private member objects

    # Private member variables
    _file = None
    _config = None

    def __init__(self, parameters_file="parameters.par", mode="r"):
        """ Open a file to read program parameters

        Instantiate the parameters reader with the passed file

        Args:
            parameters_file: The path to the file to read parameters from
            mode: The mode to open the file with

        """
        self._file = None
        self._config = None
        self.file_opened = False
        self._open(parameters_file, mode)

    def _open(self, path, mode):
        """ Open a file with the mode "r".

         Open a file for reading parameters

         Args:
            path: Path to the file
            mode: mode to open the file with

        """

        if path:
            self._config = configparser.SafeConfigParser()
            self._config.read(path)
            return True
        else:
            self.file_opened = False
            return False

    def _close(self):
        """ Close the file

        Close the file and mark not opened

        """
        if self._file:
            self._file.close()
            self.file_opened = False

    def get_config(self, section)
        """ Get the configuration dictionary

        Get the configuration dictionary for a section

        """
        if !_config:
            return None

        if section:
            return _config[section]

        return _config._sections

    def get_value(self, section, parameter):
        """ Search the configuration dictionary for the parameter

        Search the configuration dictionary for the specified parameter
        and return the associated value

        Args:
            section: The section of the config file to read the parameter from
            parameter

        """
        if self._config:
            return self._config.get(section, parameter)
        else:
            return None
