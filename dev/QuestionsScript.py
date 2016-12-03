import sys

def xyz():
	f=open('attributes_model.txt','r')
	x=eval(f.read())
	f.close()
	#print(x.keys())
	#print(x['price']['expensive'])
	#print(x['price']['midlevel'])
	#print(x['price']['cheap'])
	l1=['cheap','moderate', 'expensive']
	l2=list()
	#print(x['location'])
	#print(l1)
	#['expensive', 'midlevel', 'cheap']
	#return
	l=list()
	for y in x['cuisine']:
		l.append("<s> I am interested in "+y+" food. </s>")
		l.append("<s> I am interested in "+y+" restaurant near me. </s>")
		l.append("<s> Looking for "+y+" food.</s>")
		l.append("<s> Looking for "+y+" restaurant near me. </s>")
		l.append("<s> "+y+" food. </s>")
		l.append("<s> "+y+" restaurant. </s>")
		l.append("<s> Restaurants near me with "+y+" cuisine. </s>")
	print(len(l))

	f=open('Cusines.txt','w')
	for i in l:
		f.write(i+'\n')
	f.close()
xyz()
'''
f=open('Cusines.txt','w')
l=x.split()
for i in l:
	f.write("<s> I’m interested in "++"</s>")
f.close()
'''