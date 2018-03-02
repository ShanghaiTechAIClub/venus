def visdom_init(model, vis_specs):
    viz = visual.create_viz(name='root', model=model, env=str(paracfg_mgr))
    for vis_spec in vis_specs:
        print("Visualization List:", vis_spec)
        getattr(viz, vis_spec[0])(*vis_spec[1:])
    return viz
    
    
    
# TODO:
* tnt: visdom
    * change visdom so that it allows the modification of port
* test
    - test visdom
        + plot MeanStd
        + plot WeightRatio
        + plot Norm
    - test tensorboard
        + plot MeanStd
        + plot WeightRatio
        + plot Norm
Q: test tool
        travis
        