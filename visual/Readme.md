def visdom_init(model, vis_specs):
    viz = visual.create_viz(name='root', model=model, env=str(paracfg_mgr))
    for vis_spec in vis_specs:
        print("Visualization List:", vis_spec)
        getattr(viz, vis_spec[0])(*vis_spec[1:])
    return viz