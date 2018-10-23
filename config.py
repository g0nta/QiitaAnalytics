import configparser

class Config():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self._apiKey = config['DEFAULT']['ApiKey']
    
    @property
    def ApiKey(self):
        return self._apiKey

if __name__=="__main__":
    conf = Config()
    print(conf.ApiKey)