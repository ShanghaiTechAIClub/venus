import sys
sys.path.append('../')

from config import ConfigFactory


class TestConfig(object):

    def test_edict_config(self):

        #test if configFactory work correctly
        #test edict
        #Caution: Don't ignore the file suffix such as .py .cfg



        config = ConfigFactory.create_config('edict_example.py', mode='EDict')

        #test write and read
        config['name'] = 'Hello'
        _name1 = config['name']
        assert _name1 is 'Hello'

        config.name = 'VeNus'
        _name2 = config.name
        assert _name2 is 'VeNus'



if __name__ == '__main__':
    TestConfig().test_edict_config()