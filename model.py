from inference import fed_aggregate
import json

def predict_global(inp):
	oldinp=inp[:]
	for i in range(len(oldinp)):
		try:
			inp[i]=float(oldinp[i])
		except:
			return "Some inputs are missing"
	inter=inp[0]
	inp=inp[1:]
	fed=fed_aggregate()
	if len(fed)==0:
		return "Global model is not trained"
	res=0
	print(fed)
	print(inp)
	for i in range(len(inp)):
		res+=float(inp[i])*float(fed[i])
	res+=float(inter)
	try:
		val=1/(1+exp(-res))
	except:
		val=0
	if(val>0.5):
		return "Benign"
	else:
		return "Malignant"

def predict_local(inp,user):
	oldinp=inp[:]
	for i in range(len(oldinp)):
		try:
			inp[i]=float(oldinp[i])
		except:
			return "Some inputs are missing"
	inp=[float(x) for x in inp]
	inter=inp[0]
	inp=inp[1:]
	res=0
	fed=[]
	with open("all_data.txt","r",encoding="utf-8") as f:
		x=f.read()
		x=x.strip()
		if x=='':
			x="{}"
		x=json.loads(x)
		try:
			fed=x[user]
		except:
			return "Local model is not trained"

	for i in range(len(inp)):
		res+=inp[i]*fed[i]
	res+=inter
	try:
		val=1/(1+exp(-res))
	except:
		val=0
	if(val>0.5):
		return "Benign"
	else:
		return "Malignant"
