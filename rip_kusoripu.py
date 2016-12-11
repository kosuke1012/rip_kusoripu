#-*-coding:utf-8-*-

import twkey
import datetime
import locale
import os
import time
import sys

if __name__ == '__main__':
	hashTag = u'#クソリプ3D供養'
	preKuso = 0
	nowKuso = 0
	wait = int(sys.argv[1]) #周期、秒で指定
	rmKuso = int(sys.argv[2]) #クソリプ摘出時間
	kusoNum = 0
	while True:
		api = twkey.get_accesstoken()
		#前回クソリプ供養をしていた場合
		if kusoNum >= 1:
			os.system('imagesnap -w 1.0')			
			d = datetime.datetime.today()
			time.sleep(1.0)
			api.update_with_media(filename=u'snapshot.jpg', status = u'クソリプ3D供養が完了しました。ホカホカの塊をご覧下さい。 ' + hashTag + u' ' + str(d.hour) + u'時' + str(d.minute) + u'分' + str(d.second) + u'秒')
			print u'クソリプ摘出開始'
			time.sleep(rmKuso)
		#クソリプ数検索
		nowKuso = len(api.search(hashTag))
		kusoNum = nowKuso - preKuso
		print u'現在のクソリプ数:' + str(nowKuso)
		print u'前回からのクソリプ差異:' + str(kusoNum)
		
		if kusoNum == 0:
			#クソリプ不足			
			print u'tweet クソリプ不足'
			d = datetime.datetime.today()
			api.update_status(status=u'前回より新たに投稿されたクソリプはありません。Twitter上の平和は保たれています。 '+ hashTag + u' ' + str(d.hour) + u'時' + str(d.minute) + u'分' + str(d.second) + u'秒')
			preKuso = nowKuso
	
		elif kusoNum >= 1:
			print u'クソリプ供養開始 '
			os.system('imagesnap -w 1.0')			
			d = datetime.datetime.today()
			time.sleep(1.0)
			api.update_with_media(filename=u'snapshot.jpg', status = u'現在クソリプの数は' + str(nowKuso) + u'個です。前回より' + str(kusoNum) + u'個増えました。規定水準を超えたため、これよりクソリプ3D供養を開始します。 ' + str(d.hour) + u'時' + str(d.minute) + u'分' + str(d.second) + u'秒')
			preKuso = nowKuso

			#systemコール
			os.system('osascript poogo1.scpt')
		print u'クソリプ供養完了'			
		time.sleep(wait)



