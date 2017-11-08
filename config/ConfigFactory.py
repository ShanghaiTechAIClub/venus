from . import Config

class ConfigFactory(object):
    """

    """
    @staticmethod
    def create_config(config_file, mode):
        """

        :param config_file:
        :param mode:
        :return:
        """
        config_cls_name = mode + 'Config'
        config = getattr(Config, config_cls_name)(config_file)
        return config
