import sys
import MeCab
import pandas as pd
import neologd_normalizer as norm

if __name__ == "__main__":
	m = MeCab.Tagger("-d /usr/lib/mecab/dic/mecab-ipadic-neologd")
	df = pd.read_csv('./data/qiita/2018-04-02.csv')
	body = df.iat[0,2]
	print(df.iat[0,0])
	normalized_body = norm.normalize_neologd(body)
	nodes = m.parseToNode(normalized_body)
	target_parts = ('名詞','動詞','形容詞',)
	
	words = []
	while nodes:
		if nodes.feature.split(',')[0] in target_parts:
			words.append(nodes.surface0
		nodes = nodes.next

