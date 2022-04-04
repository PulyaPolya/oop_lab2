import configparser
from configparser import ConfigParser
parser = ConfigParser()
parser.read('example.ini')
print(parser.sections())
print(parser.get('files','ass'))