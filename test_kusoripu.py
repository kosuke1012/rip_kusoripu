#-*-coding:utf-8-*-

import twkey
import datetime
import locale
import os
import time
import sys

if __name__ == '__main__':
	hashTag = u'#クソリプ3D供養'
	print u'twitter API テスト'
	try:
		api = twkey.get_accesstoken()
		nowKuso = len(api.search(hashTag))
		print u'OK'
	except:
		print u'NG'
		raise
	
	print u'カメラテスト'
	try:
		d = datetime.datetime.today()
		fileName = str(d.second) + u'.jpg'
		command = u'imagesnap '+ fileName + ' -w 1.0'
		os.system(command)			

		if(os.path.exists(fileName)):
			print u'OK'
			rmCommand = u'rm ' + fileName
			os.system(rmCommand)
		else:
			print u'NG'
	except:
		print u'NG'
		raise

