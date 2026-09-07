from src.NLP_Text_Summary.logging import logger
import os
import sys
from src.NLP_Text_Summary.utils.common import sqare
from src.NLP_Text_Summary.config.configuration import ConfigurationManager
import ssl
import urllib.request

# Bypass SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context


logger.info("Welcome to my NLP project")



if __name__=="__main__":
    print("Welcome to text sumarization project")
    print(sqare(15))
    config_manager = ConfigurationManager()
    info = config_manager.get_info()
    print(info)
