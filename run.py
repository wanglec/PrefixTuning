#!/usr/bin/env python

import sys
import os
import json

sys.path.insert(0, 'src')

def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''

    if 'model' in targets:
        with open('gpt2/webnlg_models/webnlgprefixtune_y_5_act_cat_b=5-e=5_d=0.0_u=no_lr=5e-05_w=0.0_s=10_r=n_m=512_o=1_o=1/config.json') as fh:
            model_cfg = json.load(fh)

    if 'test' in targets:
        os.chdir("gpt2/webnlg_models/webnlgprefixtune_y_5_act_cat_b=5-e=5_d=0.0_u=no_lr=5e-05_w=0.0_s=10_r=n_m=512_o=1_o=1")
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        if 'pytorch_model.bin' not in files:
            print('Since the model parameters have large size (>100 Mb), it could not be uploaded to github. We are figuring out a way to share the model with you.')
        else:
            COMMANDLINE = "python gen.py webnlg yes test webnlg_models/webnlgprefixtune_y_5_act_cat_b=5-e=5_d=0.0_u=no_lr=5e-05_w=0.0_s=10_r=n_m=512_o=1_o=1 no"
            os.chdir("../../../gpt2/")
            os.system(COMMANDLINE)


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)
