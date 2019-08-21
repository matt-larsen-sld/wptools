""" Given a file handle find the PHP variable assignments  """
import re


class Extractor:
    # Breaks a PHP 'define("KEY", "VALUE");' statement into 4 match groups where group 2 is KEY and group 4 is VALUE
    define_pattern = re.compile(r"""\bdefine\(\s*('|")(.*)\1\s*,\s*('|")(.*)\3\)\s*;""")
    # Breaks a PHP '$KEY = "VALUE";' statement into 4 match groups where group 2 is KEY and group 4 is VALUE
    assign_pattern = re.compile(
        r"""(^|;)\s*\$([a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)\s*=\s*('|")(.*)\3\s*;"""
    )

    @classmethod
    def php_variable_assignments(cls, line) -> tuple:
        """ Reads line and return PHP variable assignments and a tuple (key, value)
        :param line: string, intended to be a line from a php file
        :return: tuple with key value pairs from variable assignments in line
        """
        define_match = cls.define_pattern.match(line)
        assign_match = cls.assign_pattern.match(line)
        if define_match:
            return define_match.group(2), define_match.group(4)
        if assign_match:
            return assign_match.group(2), assign_match.group(4)

    @classmethod
    def extract(cls, open_file) -> dict:
        """ Extract a dictionary of PHP variable assignments from a given file handle
        :param open_file: File handle to read from
        :return: dict with the variable assignments from the given open_file
        """
        result = {}
        for line in open_file:
            try:
                k, v = cls.php_variable_assignments(line)
                result[k] = v
            except TypeError:
                # Get a TypeError when trying to unpack cls.php_variable_assignments to a tuple when no match was found.
                pass
        return result
