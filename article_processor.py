import sys
import MeCab
import pandas as pd
import neologd_normalizer as norm

if __name__ == "__main__":
	m = MeCab.Tagger("-d /usr/lib/mecab/dic/mecab-ipadic-neologd")
	df = pd.read_csv('./data/qiita/2018-04-01.csv')
	body = df.iat[0,2]
	normalized_body = norm.normalize_neologd(body)
	lines = m.parse(normalized_body).splitlines()
	words = []
	
	for line in lines:
		chunks = line.split('\t')
		print(line)
		break
		#if len(chunks) > 3: #and (chunks[3].startswith('動詞') or chunks[3].startswith('形容詞') or (chunks[3].startswith('名詞') and not chunks[3].startswith('名詞-数'))):
		#	words.append(chunks[0])
		#	print(chunks[0])

