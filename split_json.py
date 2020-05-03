

import json

def split(num_lines, fname):
    data = []
    with open(fname) as f:
        for i, line in enumerate(f):
            data.append(json.loads(line))
            if i >= num_lines:
                return data

if __name__ == '__main__':
    fname = 'devpost_es_formatted.json'
    num_lines = 50
    print(split(num_lines, fname)[0])
