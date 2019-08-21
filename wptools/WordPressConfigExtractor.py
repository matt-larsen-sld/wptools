""" Given a file find the database values """
import re

from .WordPressConfig import WpDbConfig


class Extractor:
    # Breaks a PHP 'define("KEY", "VALUE");' statement into 4 match groups where group 2 is KEY and group 4 is VALUE
    define_pattern = re.compile(r"""\bdefine\(\s*('|")(.*)\1\s*,\s*('|")(.*)\3\)\s*;""")
    # Breaks a PHP '$KEY = "VALUE";' statement into 4 match groups where group 2 is KEY and group 4 is VALUE
    assign_pattern = re.compile(
        r"""(^|;)\s*\$([a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)\s*=\s*('|")(.*)\3\s*;"""
    )

    @classmethod
    def php_variable_assignment(cls, line):
        define_match = cls.define_pattern.match(line)
        assign_match = cls.assign_pattern.match(line)
        if define_match:
            return define_match.group(2), define_match.group(4)
        if assign_match:
            return assign_match.group(2), assign_match.group(4)

    @classmethod
    def extract(cls, open_file):
        result = {}
        for line in open_file:
            try:
                k, v = cls.php_variable_assignment(line)
                result[k] = v
            except TypeError:
                # Get a TypeError when trying to unpack cls.php_variable_assignment to a tuple when no match was found.
                pass
        return result


def db_config(config_file) -> WpDbConfig:
    """Read a wp-config.php file and return an object with the WordPress database config values

    :param config_file: wp-config.php file with WordPress configuration values
    :return: WbDbConfig object with properties for WordPress database configuration
    """

    # Breaks a PHP 'define("KEY", "VALUE");' statement into 4 match groups where group 2 is KEY and group 4 is VALUE
    define_pattern = re.compile(r"""\bdefine\(\s*('|")(.*)\1\s*,\s*('|")(.*)\3\)\s*;""")
    # Breaks a PHP '$KEY = "VALUE";' statement into 4 match groups where group 2 is KEY and group 4 is VALUE
    assign_pattern = re.compile(
        r"""(^|;)\s*\$([a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)\s*=\s*('|")(.*)\3\s*;"""
    )

    php_vars = {}
    with open(config_file, "r") as f:
        for line in f:
            define_match = define_pattern.match(line)
            assign_match = assign_pattern.match(line)
            if define_match:
                php_vars[define_match.group(2)] = define_match.group(4)
            if assign_match:
                php_vars[assign_match.group(2)] = assign_match.group(4)
    db_values = WpDbConfig()
    db_values.db_host = php_vars["DB_HOST"]
    db_values.db_name = php_vars["DB_NAME"]
    db_values.db_user = php_vars["DB_USER"]
    db_values.db_password = php_vars["DB_PASSWORD"]
    return db_values
