import pandas as pd
import json

df = pd.read_csv('results/merged_keywords_adjusted.csv', index_col=0)

df.to_json('results/keywords.json', orient='split', indent=4)

urls = pd.read_csv('source_data/urls.csv')

# index = [
#     'Imitation Rain',
#     'Telephone',
#     'NEW WORLD',
#     'NAVIGATOR',
#     'JAPONICA STYLE',
#     'NEW ERA',
#     'NAVIGATOR（H ZETTRIO Crossover Rearrange）',
#     'ST',
#     'Special Order',
#     'S.I.X',
#     'Life Time',
#     '"Laugh" in the LIFE',
#     'RAM-PAM-PAM',
#     'うやむや',
#     '僕が僕じゃないみたいだ',
#     'Strawberry Breakfast',
#     'Call me',
#     'マスカラ',
#     'フィギュア',
#     '僕が僕じゃないみたいだ (Dramatic Rearrange)',
#     'Rosy',
#     'Everlasting',
#     'WHIP THAT',
#     '共鳴',
#     'FASHION',
#     'Gum Tape',
#     'マスカラ -Emotional Afrobeats Remix-',
#     'Wave Crash',
#     'わたし',
#     'シアター',
#     'オンガク',
#     'セピア',
#     '共鳴 -Brave Marching Band Remix-',
#     'Good Luck!',
#     'ふたり',
#     'Boom-Pow-Wow!',
#     'PARTY PEOPLE',
#     'Outrageous',
#     '人人人',
#     "Chillin' with you",
#     'STAMP IT',
#     'ABARERO',
#     'Drive',
#     'こっから',
#     'FIREWORKS',
#     'Tu-tu-lu',
#     'CREAK',
#     'ガラス花',
#     'MUSIC IN ME',
#     'Never Ending Love',
#     "We can't go back",
#     'Love is…',
#     'Sorry',
#     "こっから -Old School Breakin' Remix-",
#     'アンセム',
#     'Something from Nothing',
#     'Only Holy',
#     "Bang Bang Bangin'",
#     'DRAMA',
#     '君がいない',
#     '音色',
#     'GONG',
#     'ここに帰ってきて',
#     'THE BALLERS',
#     'バリア',
#     'Strawberry Breakfast -Live on MTV Unplugged-'
# ]

# urls.sort_values('SongName', key=lambda s: [index.index(n) for n in s], inplace=True)

# urls.to_csv('source_data/urls.csv', index=False)

urls_dict = {k: urls[k].to_list() for k in urls.columns.to_list()}

with open('results/urls.json','w') as f:
    json.dump(urls_dict, f, indent=4)