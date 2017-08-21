import os
import sys
from emojilist import emojis
import pandas as pd
df = pd.DataFrame()
emoji_set = set(emojis)
data_folder = 'data/'

'''
    "line" is a string including emoji (from twitter)
'''


def clean():
    '''
        None -> line generator
    '''
    with open('old_outfile.txt') as infile:
        for line in infile:
            line = line.strip()
            if line and line[-1] in emoji_set:
                yield line


def seperate_emojis(line):
    '''
        line -> (text, emoji) pairs
    '''
    text_part = ''.join(filter(lambda x: x not in emoji_set, line))
    return text_part.strip(), list(set(filter(lambda x: x in emoji_set, line)))


def get_all(lines):
    '''
        list of lines -> iterator of (text, emoji) pairs
    '''
    got_all = (seperate_emojis(line) for line in lines)
    return filter(lambda x: len(x[0]) > 1 and len(x[1]) > 0, got_all)


def format_convert(data_folder='data/'):
    '''
        data_folder (optional) -> EFFECT: writes on disk magpie format.
    '''
    os.system('rm -rf {}; mkdir {}'.format(data_folder, data_folder))
    for i, (x, y) in enumerate(get_all(clean())):
        if not i % 100:
            print(i)
        with open('{}{}.lab'.format(data_folder, i), 'w') as outfile:
            outfile.write('\n'.join(y))
        with open("{}{}.txt".format(data_folder, i), 'w') as outfile:
            outfile.write(x)
    print('twitter convert to werid magpie format... done.')


def csv_format_convert(df=df, data_folder=data_folder):
    '''
        just in case of input being CSV
    '''
    os.system('rm -rf {}; mkdir {}'.format(data_folder, data_folder))
    for i,(_,x,y) in enumerate(df.values):
        with open('{}{}.lab'.format(data_folder, i), 'w') as outfile:
            outfile.write('\n'.join(y))
        with open("{}{}.txt".format(data_folder, i), 'w') as outfile:
            outfile.write(x)
    print('csv convert to werid magpie format... done.')  
    
    
def get_all_labels(df):
    '''
        get labels from robert's mock data.
    '''
    return list(set(each_y for _,x,y in df.values for each_y in y.strip().split('_')))
    
    
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        format_convert()
    else:
        format_convert(data_folder=sys.argv[1] + '/')
