import json

newx=""
def update_inference(user,params):
	params=[float(x) for  x in params]
	with open("all_data.txt","r",encoding="utf-8") as f:
		x=f.read()
		x=x.strip()
		if x=='':
			x="{}"
		d=json.loads(x)
		d[user]=params
		global newx
		newx=json.dumps(d)

	with open("all_data.txt","w",encoding="utf-8") as f:
		f.write(newx)



def fed_aggregate():
	final_agg=[]
	x={}
	with open("all_data.txt","r",encoding="utf-8") as f:
		x=f.read()
		x=x.strip()
		if x=='':     # if no model has been trained
			return []
		x=json.loads(x)
	for i in x.keys():
		if len(final_agg)==0:
			final_agg=[float(xx) for xx in x[i]]
		else:
			for j in range(len(x[i])):
				final_agg[j]+=float(x[i][j])
	tot_clients=len(x)
	final_agg=[float(i/tot_clients) for i  in final_agg]
	return final_agg

