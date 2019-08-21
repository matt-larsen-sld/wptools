import io
import pytest

from wptools.WordPressConfigExtractor import Extractor

php_define_strings = [
    ("define('DB_NAME', 'wordpress_db');", ("DB_NAME", "wordpress_db")),
    ("define('DB_USER', 'wpdata_user');", ("DB_USER", "wpdata_user")),
    ("define('DB_HOST', '127.0.0.1');", ("DB_HOST", "127.0.0.1")),
    ("define('DB_HOST', 'localhost');", ("DB_HOST", "localhost")),
    ("define('DB_PASSWORD', 'blahblahblah');", ("DB_PASSWORD", "blahblahblah")),
    ("/** Some comment */", None),
    (" * Some other comment.", None),
    ("<$php", None),
]

php_assign_strings = [
    ("$DB_NAME = 'wordpress_db';", ("DB_NAME", "wordpress_db")),
    ("$DB_NAME='wordpress_db';", ("DB_NAME", "wordpress_db")),
    ("$DB_USER = 'wpdata_user';", ("DB_USER", "wpdata_user")),
    ("$DB_HOST = 'localhost';", ("DB_HOST", "localhost")),
    ("$DB_HOST = '127.0.0.1';", ("DB_HOST", "127.0.0.1")),
    ("$DB_PASSOWRD  = 'passowrd';", ("DB_PASSOWRD", "passowrd")),
    ("$DB_PASSWORD = 'password';", ("DB_PASSWORD", "password")),
    ("/** Some comment */", None),
    (" * Some other comment.", None),
    ("<$php", None),
]


def test_db_config_dict_from_content():
    content = """
/** Blah blah blah
 * blah blah blah
 */
define('DB_NAME', 'wordpress_db');

/** MySQL database username */
define('DB_USER', 'wpdata_user');

/** MySQL database password */
define('DB_PASSWORD', 'password');

/** MySQL hostname */
define('DB_HOST', '127.0.0.1');

$something = "something";

define('FORCE_SSL_ADMIN', true);
define('FORCE_SSL_LOGIN', true);
if ($_SERVER['HTTP_X_FORWARDED_PROTO'] == 'https')
       $_SERVER['HTTPS']='on';


"""
    result_dict = {
        "DB_NAME": "wordpress_db",
        "DB_USER": "wpdata_user",
        "DB_PASSWORD": "password",
        "DB_HOST": "127.0.0.1",
        "something": "something",
    }
    try:
        f = io.StringIO(initial_value=content)
        result = Extractor.extract(f)
    finally:
        f.close()
    assert result == result_dict


@pytest.mark.parametrize("line, expected_result", php_define_strings)
def test_db_config_parse_php_key_value_pairs(line, expected_result):
    result = Extractor.php_variable_assignments(line)
    if result:
        key, value = expected_result
        assert key == result[0]
        assert value == result[1]
    else:
        assert result is expected_result
