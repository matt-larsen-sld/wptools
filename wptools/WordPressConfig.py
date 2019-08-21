""" Class to define the database config properties in a wp-config.php file """


class WpDbConfig:
    def __init__(self):
        self.db_name = None
        self.db_host = None
        self.db_user = None
        self.db_password = None
