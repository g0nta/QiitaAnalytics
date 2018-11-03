import sys
import MeCab
import pandas as pd
import neologd_normalizer as norm
import os
import csv
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

if __name__ == "__main__":
	csv.field_size_limit(5000000)
	m = MeCab.Tagger(r"-Ochasen -d /usr/lib/mecab/dic/mecab-ipadic-neologd")
	data_path = './data/qiita'
	file_list = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path,f))]
	trainings = []
	for file_path in file_list:
		file_path = os.path.join(data_path, file_path)
		with open(file_path) as f:
			reader = csv.reader((line.replace('\0','') for line in f), delimiter=",")
			next(reader)
			for article in reader:
				body = article[2]
				normalized_body = norm.normalize_neologd(body)
				try:
					lines = m.parse(normalized_body).splitlines()
				except AttributeError as ae:
					print('args:{0}'.format(ae.args))
					print('article id:{0}'.format(article[0]))
					continue
				words = []
				for line in lines:
					chunks = line.split('\t')
					if len(chunks)>3 and (chunks[3].startswith('名詞') or chunks[3].startswith('形容詞') or (chunks[3].startswith('名詞') and not chunks[3].startswith('名詞-数'))):
						words.append(chunks[0])

				trainings.append(TaggedDocument(words = words, tags=[article[0]]))
				print(file_path)
				print(len(words))
	model = Doc2Vec(documents=trainings, vector_size=150, alpha=0.0015, sample=1e-4, min_count=10, workers=4, epochs=30)
	model.save('Doc2VecModel_150dim.model')

