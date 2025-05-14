import pandas as pd

import argparse
import time
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('source_data_file')
args = parser.parse_args()

df = pd.read_csv(args.source_data_file)

keywords = {s:[k.strip() for k in r.split('\n')[-1].split(',')] for s,r in zip(df['SongName'],df['Response'])}

keyword_list = list(set(sum([v for v in keywords.values()],[])))

pd.DataFrame.from_dict(keywords, orient='index').to_csv('results/keywords_original.csv')
with open('results/keywords_original.txt','w') as f:
    f.write('\n'.join(keyword_list))
