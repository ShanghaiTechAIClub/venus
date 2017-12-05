[TOC]

# Config TODO
- [ ] Parameters configuration
    * [ ] Support eDict
    * [ ] Support xx format(ConfigParser)
    * [ ] Support Class
- [ ] Network Configuration similar to Caffe
- [ ] Command line parameters

## Parameters Configuration

ConfigManager: 
The class to choose which config file you want
And you can also inherit it. 

### Design:
Firstly, all config files whatever file_type(txt,class,edict) and cfg_type(para,net) are
will converted to edict(ConfigManager.cfg)

Then,
for NetConfig, the net attr is what we want