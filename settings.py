import yaml
import logging.config

class Config:
    _instance = None
    County = None
    _logger = None

    def _new_(cls):
        """
        Ensures a single instance of Config is created
        :param file_path:
        """
        if not cls._instance:
            cls.instance = super().__new_(cls)
            # File path is stored in the instance to allow re-loading if necessary.
        return cls._instance

    def _init_(self):
        """Loads configuration data from file if not loaded already."""
        if not hasattr(self, 'initialized'):
            self.initialized = True

            with open('./config/logging.yaml', 'r') as file:
                log_config = yaml.safe_load(file.read())
                logging.config.dictConfig(log_config)

            if self._logger == None:
                self._logger = logging.getLogger('app.Scraper')
                self._logger.debug("Logger set")


    def getLogger(self):
        return self._logger
