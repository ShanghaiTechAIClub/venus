import importlib
import configparser

_CFG_SUFFIX = ['.cfg']

class Config(object):

    def __init__(self, cfg_file):
        if cfg_file.endswith('.py'):
            module_path = 'config.settings.' + cfg_file[:-3]  #delete suffix .py, imitate import path
            module_obj = importlib.import_module(module_path)
            self._config = module_obj.config

        elif cfg_file.endswith(_CFG_SUFFIX):
            self._config = configparser.ConfigParser('.settings'+cfg_file)

            #TODO CHECK the content in _config

        # else:
            #raise ValueError("The file suffix should be ")

    def __getattr__(self, attr):
        return self._config[attr]

    def __setattr__(self, key, value):
        if '_config' not in self.__dict__:
            # _config initialization
            assert key is '_config'
            super(Config, self).__setattr__(key,value)
        else:
            self._config[key] = value
    def __getitem__(self, key):
        return self._config[key]

    def __setitem__(self, key, value):
        self._config[key] = value

    def get_config(self):
        return self._config


class EDictConfig(Config):
    """
    Input:
        cfg_file： also called module_file. Should be placed in subfolders of config folder
    """
    def __init__(self, cfg_file):
        super(EDictConfig, self).__init__(cfg_file)


    def getdict(self):
        """
        If you want to use edict special methods, you can call this method
        :return:
        """
        return self.config


class TxtConfig(Config):

    def __init__(self):
        super(TxtConfig, self).__init__()


class ClassConfig(Config):

    def __init__(self):
        super(ClassConfig, self).__init__()

    def __getitem__(self, key):
        return getattr(self._config,key)

    def __setitem__(self, key, value):
        setattr(self._config, key, value)
