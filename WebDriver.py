from selenium import webdriver


class WebDriver():
    ''' Class for webdriver configuration.
        Method param means method of installing: 
        local = install webdriver on venv level, global = use pre-installed webdriver in your OS
    '''

    def __init__(self, method='local', path='/usr/bin/chromedriver'):
        self.method_ = method
        self.path_ = path
    
    def get_driver(self):
        if self.method_ == 'local':
            from webdriver_manager.chrome import ChromeDriverManager
            return webdriver.Chrome(ChromeDriverManager(log_level=0).install(), service_log_path=False)
        
        elif self.method_ == 'global':
            return webdriver.Chrome(self.path_)

        raise ValueError('Wrong setup method')
    