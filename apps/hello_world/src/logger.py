import logging

class Logger():
    def __init__(self, logger_name):
        
        self.logger = logging.getLogger(logger_name)
        
        self.logger.setLevel(logging.DEBUG)
        
        c_handler = logging.StreamHandler()
        c_format = '%(levelname)s - %(name)s - %(asctime)s - %(message)s'
        c_handler.setFormatter(logging.Formatter(c_format))

        self.logger.addHandler(c_handler)
        
        self.logger.propagate = False
        
    def get_logger(self):
        return self.logger
