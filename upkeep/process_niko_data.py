

import json

def split(num_lines, fname):
    data = []
    with open(fname) as f:
        for i, line in enumerate(f):
            data.append(json.loads(line))
            if i >= num_lines:
                return data

def read_json(fname):
    data = []
    with open(fname) as f:
        for i, line in enumerate(f):
            data.append(json.loads(line))
    return data

def split_dict(data):
    new_data = []
    for i in data:
        temp = i['_source']
        del i['_source']
        del i['_score']
        ind = {"index" : i}
        new_data.append(ind)
        new_data.append(temp)
    return new_data

def write_json(data, out_name):
    with open(out_name, 'w') as fp:

        fp.write('\n'.join(json.dumps(i) for i in data) + '\n')

if __name__ == '__main__':
    f_dev = 'devpost-2020-04-28.json'
    fname = 'devpost_es.json'
    num_lines = 2
    data = read_json(fname)
    # data = read_json(f_dev)
    # data = split_dict(data)
    # write_json(data, fname)
    for i in data:
        print(i)
