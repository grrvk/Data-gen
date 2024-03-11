"""
    Main
"""
from tqdm import tqdm
from generator import layout_functions as lf
from generator.settings import Settings


# -*- coding: utf-8 -*-

def generate(amount: int, samples_path: str, dataset_path: str = None, dataset_name: str = None, upload: bool = False):
    conf = Settings(dataset_path=dataset_path, samples_path=samples_path,
                    dataset_name=dataset_name, upload=upload)
    print(conf)

    for i in tqdm(range(amount), desc='images created', colour='green'):
        lf.generate_brochure(i + conf.NAMING_INDEX, conf)

    conf.clear_temp_samples()
    print('Finished generating')
