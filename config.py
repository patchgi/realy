#coding:utf-8
import os

# celery_broker_url = 'redis://localhost:6379'
# celery_result_url = 'redis://localhost:6379'
mecab_dic_dir = os.getenv('mecab', '/usr/local/lib/mecab/dic/mecab-ipadic-neologd')
dirs = dict(template = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
				        static = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
						)
