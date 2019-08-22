import os

from wptools.PhpVariableExtractor import Extractor

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
WP_CONFIG_FILE = "wp-config.php"

wp_config_file = os.path.join(BASE_PATH, WP_CONFIG_FILE)
with open(wp_config_file, "r") as handle:
    variables = Extractor.extract(handle)
db_config_values = {
    "DB_NAME": dict.get(variables, "DB_NAME"),
    "DB_HOST": dict.get(variables, "DB_HOST"),
    "DB_USER": dict.get(variables, "DB_USER"),
    "DB_PASSWORD": dict.get(variables, "DB_PASSWORD"),
}
print(db_config_values)
