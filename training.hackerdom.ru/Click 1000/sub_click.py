import sys
from subprocess import Popen, PIPE
from progressbar import ProgressBar, Bar, ETA, Percentage

def parse(hash):
	BASE_URL = "http://click1000.training.hackerdom.ru/"
	url = BASE_URL + hash
	p = Popen(["curl", url], stdout=PIPE) 
	output = p.communicate()[0]
	#print ("Output:\n{}".format(output))
	hash = output[8:41]	
	return hash
	


pbar_widgets = ['Progress: ', Percentage(), ' ', Bar(), ' ', ETA(), ' ']
pbar = ProgressBar(widgets=pbar_widgets)

limit = 1001
hash = 'start'
#for item in pbar(range(0, limit+1)):
for item in range(0,limit+1):
	print ("#{}".format(item))
	hash = parse(hash)
	outputFile = open ('tmp/item-{}.log'.format(item), 'w')
	outputFile.write(hash)
	outputFile.close()