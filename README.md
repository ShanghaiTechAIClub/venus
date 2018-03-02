# torchnet_Venus
The base framework for deep learning based on pytorch, torchnet, etc.


## TODO
[TODO Issue](https://github.com/ShanghaiTechVENUS/torchnet_Venus/issues/1)
## Credits

Primarily referenced tnt of pytorch:  [Torchnet @pytorch](https://github.com/pytorch/tnt)

Many thanks to [@pytorch](https://github.com/pytorch).


# Code Structure: a lib that helps us to do some debugs, tune parameters, visualize, config
Wish the lib to be a wrapper, but users can also use the modules separately.

* debug utilities

## Recently
* base
* initializer    
* visual
* hyperopt: tune hyper parameters
* optimizer: multistep learner
* config
* autosave, autoload: If unexpected interruption or active keyboard interruption happens to the program, then will save the checkpoint and parameters automatically.
* utils
    - seed initialization
    - weight initialization
    

## Long-term goal
* profiler
* common dataloader
* search structure
* tnt such as engine, meter



# Class graph
config 

Engine: Tune network parameters
    - autosave
    - train
    - test
    - load_test
    - load_train
     
StructureSearcher     
Hyperopt            ->         Engine             -> config
                                        -> visual


DataLoader

Should be a template or a library?
Flexibility should be the first.
Utilities follows.
