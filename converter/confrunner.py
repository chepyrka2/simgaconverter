import configparser
config = configparser.ConfigParser()
config['LANG'] = {'lang': 'eng'}
with open('lang.ini', 'w') as cf:
    config.write(cf)