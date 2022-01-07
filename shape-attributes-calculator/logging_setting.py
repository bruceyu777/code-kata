import logging
import logging.config
import yaml

# logging.config.fileConfig('logging.conf')
with open("logconf.yml", 'r') as f:
    log_config = yaml.safe_load(f)
    logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)
logger.info("loggind started...")