import json

def validate(user,pswd):

	with open("login.txt","r",encoding="utf-8") as f:
		x=f.read()
		x=x.strip()
		if x=='':
			x="{}"
		d=json.loads(x)
		try:
			if d[user]==pswd:
				return True
			else:
				return False
		except:
			return False

def add_user(user,pswd):
	newx=""
	with open("login.txt","r",encoding="utf-8") as f:
		x=f.read()
		x.strip()
		if x=='':
			x="{}"
		d=json.loads(x)
		try:
			d[user]=pswd
			newx=json.dumps(d)
		except:
			return False
	with open("login.txt","w",encoding="utf-8") as f:
		f.write(newx)
	return True

print(validate("shiv","Sivanshu"))