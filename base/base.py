class ModelToolBase(object):
    def __init__(self, model):
        self.model = model

    def insert_pdb_layer(self, layer_index, debugger='pdb', where='forward_in'):
        """Insert (i)pdb into some layer (in/out)
        :param layer_index:
        :param debugger: ['pdb', 'ipdb']
        :param where: ['forward_in', 'forward_out']
        :return:
        """
        # Now don't support forward_out

        layer = self.get_layer(layer_index)
        try:
            self.regis_hook[where](layer, hook_pdb)
        except ValueError:
            raise ValueError("where arg in pdb_layer method should be pre or after.")

    def get_layer(self, layer_index):
        #Caution: Depends on pytorch
        layers_index = layer_index.split('.')
        model = self.model
        ind_path = ''
        for ind in layers_index:
            # if ind.isdigit():
            #     ind = int(ind)
            try:
                model = model._modules[ind]
            except KeyError as e:
                print('\n', repr(e), 'Current model is {},index should be in :'.format(ind_path))
                print('\t\n'.join(model.state_dict().keys()))
                import pdb
                pdb.set_trace()
            finally:
                ind_path = ind_path + '.' + ind
        layer = model
        return layer

    def get_para(self, layer_index, para_name):
        # Caution: Depends on pytorch

        layer = self.get_layer(layer_index)
        try:
            para = layer._parameters[para_name]

        except KeyError as e:
            print(repr(e))
            print('Hint:')
            print("\t layer: ")
            print("\t\tClass Info: ", layer.__class__)
            print("\t\tLayer Index: ", layer_index)
            print("\t para: ", list(layer._parameters.keys()))
            import pdb;
            pdb.set_trace()

        return para

    def register_para_gradient_hook(self, layer_index, para_name):
        para = self.get_layer(layer_index, para_name)
        para.register_hook(lambda grad: grad)

    @staticmethod
    def register_var_gradient_hook(var):
        pass