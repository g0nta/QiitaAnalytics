import sys
import MeCab
import pandas as pd

if __name__ == "__main__":
	m = MeCab.Tagger("-d /usr/lib/mecab/dic/mecab-ipadic-neologd")
	df = pd.read_csv('./data/qiita/2018-04-01.csv')
	line = df.head(1)
	text = line['body']
