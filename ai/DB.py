example_data = {'example data'}

import pickle

def save(learnt_data):
    with open('./ai/data_set.pickle', 'wb') as fw:
        pickle.dump(learnt_data, fw)

def load():
    with open('./ai/data_set.pickle', 'rb') as fr:
        return pickle.load(fr)


save(example_data)
