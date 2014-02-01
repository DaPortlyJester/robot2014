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
        _file = None
        _config = None
        file_opened = False
        self._open(parameters_file, mode)

    def _open(self, path, mode):
        """ Open a file with the mode "r".

         Open a file for reading parameters

         Args:
            path: Path to the file
            mode: mode to open the file with
        """

        if path:
            _file = open(path, mode)
            file_opened = True
            return True
        else:
            file_opened = False
            return False

    def _close(self):
        """ Close the file

        Close the file and mark not opened
        """
        if _file:
            _file.close()
            file_opened = False


    def read_values(self):
        """ Reads all parameter/value pairs from the file.

        Reads the entire parameter file and for NAME = VALUE pairs.
        The pairs are stored as a dictionary. Python should automatically
        handle typing

        Returns:
            A dictionary of the parameters read from the file
        """

        # Instantiate ConfigParser and build dictionary of config options
        _config = configparser.SafeConfigParser()

        _config.read(_file)

        _config._sections

        return _config._sections

    def get_value(self, section, parameter):
        """ Search the configuration dictionary for the parameter

        Search the configuration dictionary for the specified parameter
        and return the associated value

        Args:
            section: The section of the config file to read the parameter from
            parameter

        """
        if _config:
            return _config.get(section, parameter)
        else:
            return None
