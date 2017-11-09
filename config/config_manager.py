from . import config

class ConfigManager(object):
    """

    """
    def __init__(self, config_file, mode):
        config_cls_name = mode + 'Config'
        self.cfg = config.read_cfg_file(config_file, mode)

    def get_train_para(self):
        pass

    def get_optim_para(self):
        pass



