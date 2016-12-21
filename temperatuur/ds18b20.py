#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
import glob


class DS18B20:
	def meet(self):
		try:
			f = open ('%s/w1_slave' % glob.glob('/sys/bus/w1/devices/28*')[0],'rt')
			t = '%0.2f' % float(int(f.readlines()[1].split('=')[1]) /1000)			
			f.close()
			return t
		except:
			return False	
		
if __name__ == '__main__':
	import time
	s = DS18B20()
	while True:
		print(s.meet())
		time.sleep(5)
				
		
