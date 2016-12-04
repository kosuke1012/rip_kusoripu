#-*-coding:utf-8-*-

import twkey
import datetime
import locale
import os
import time

if __name__ == '__main__':
	hashTag = u'#クソリプ3D供養'
	kusoPara = 100
	preKuso = 0
	nowKuso = 0
	wait = 10 #周期、秒で指定
	kusoNum = 0
	print nowKuso - preKuso
	while True:
		api = twkey.get_accesstoken()
		if kusoNum >= 1:
			os.system('imagesnap -w 1.0')			
			d = datetime.datetime.today()
			time.sleep(1.0)
			api.update_with_media(filename=u'snapshot.jpg', status = str(kusoNum) + u'個のクソリプを供養しました ' + str(d.hour) + u'時' + str(d.minute) + u'分' + str(d.second) + u'秒')
		nowKuso = len(api.search(hashTag, count=10))
		kusoNum = (nowKuso - preKuso) % kusoPara

		if kusoNum >= 1:
			os.system('imagesnap -w 1.0')			
			d = datetime.datetime.today()
			time.sleep(1.0)
			print os.system('ls ~/rip_kusoripu/')
			api.update_with_media(filename=u'snapshot.jpg', status = str(kusoNum) + u'個のクソリプを供養します ' + str(d.hour) + u'時' + str(d.minute) + u'分' + str(d.second) + u'秒')
			preKuso = nowKuso

			#systemコール
			

		time.sleep(wait)



	#print str(len(api.search(q=u'#クソリプ3D供養', count=10)))
