# Python WordPress Tool
    A collection of tools for managing WordPress installations

## PhpVariableExtractor

### Extractor
    Class to extract variables from a PHP file as key value pairs in a Python dict.
  
#### Install
    $ pip install wordpresstools

#### Usage
    (example-env) utegrad@COMPUTER:/mnt/d/sources/wpcreds$ ipython
    Python 3.6.8 (default, Jan 14 2019, 11:02:34)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.7.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]: from wptools.PhpVariableExtractor import Extractor
    
    In [2]: php_vars = Extractor.extract('wp-config.php')
    
    In [3]: print(php_vars['DB_HOST'])
    10.10.0.44

