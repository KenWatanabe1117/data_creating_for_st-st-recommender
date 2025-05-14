import pandas as pd

from google import genai

import argparse
import time
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('source_data_file')
args = parser.parse_args()

df = pd.read_csv(args.source_data_file)

song_list = df['SongName'].unique()[:-1]
prompt_list, response_list = [], []

client = genai.Client()

start_time = datetime.datetime.now()
for i, song in enumerate(song_list):
    print(f"Epoch {i}: {song}")

    prompt = f"SixTONESの楽曲「{song}」について、以下のような説明があります。"
    prompt += "\n" + "-"*20 + "\n"
    prompt += ("\n" + "-"*20 + "\n").join(df[df["SongName"]==song]["Text"].to_list())
    prompt += "\n" + "-"*20 + "\n"
    prompt += f"これらの説明から「{song}」がどのような楽曲であるかを解釈して、最後に重要度の高いキーワードをカンマ区切りで可能な限り書き出してください。"

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-04-17",
        contents=prompt
    )
    prompt_list.append(prompt)
    response_list.append(response.text)

    if (i+1) % 10 == 0:
        elapsed_time = datetime.datetime.now() - start_time
        if elapsed_time.seconds / 60 < 1:
            time.sleep(60 - elapsed_time.seconds)
        start_time = datetime.datetime.now()

result_df = pd.DataFrame({
    'SongName': song_list,
    'Prompt': prompt_list,
    'Response': response_list
})

result_df.to_csv('results/promt_and_response.csv')