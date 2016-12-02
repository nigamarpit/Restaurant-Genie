import sys

def xyz():
	f=open('attributes_model.txt','r')
	x=eval(f.read())
	f.close()
	#print(x.keys())
	#print(x['price']['expensive'])
	#print(x['price']['midlevel'])
	#print(x['price']['cheap'])
	l1=list()
	l1.extend(x['price']['expensive'])
	l1.extend(x['price']['midlevel'])
	l1.extend(x['price']['cheap'])
	l2=list()
	#print(x['location'])
	#print(l1)
	#['expensive', 'midlevel', 'cheap']
	#return
	l=list()
	for y in x['cuisine']:
		l.append("<s> I am interested in "+y+" food. </s>")
		l.append("<s> I would like "+y+" food. </s>")
		for z in l1:
			l.append("<s> I am interested in "+z+" "+y+" food. </s>")
			l.append("<s> I would like "+z+" "+y+" food. </s>")
			l.append("<s> I am interested in "+z+" "+y+" food near me. </s>")
			l.append("<s> I would like "+z+" "+y+" food near me. </s>")

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