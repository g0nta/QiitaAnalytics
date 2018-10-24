import sys
import MeCab
import pandas as pd

if __name__ == "__main__":
	m = MeCab.Tagger("-d /usr/lib/mecab/dic/mecab-ipadic-neologd")
	df = pd.read_csv('./data/qiita/2018-10-17.csv')
	line = df.head(1)
	for column_name, item in line.iteritems():
		print(column_name)
		print(item[0])

