import yaml
import logging.config
import os

def load():
    path = os.getenv('LOG_CFG', None) or os.path.join('config', 'log.yaml')
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level='DEBUG')

