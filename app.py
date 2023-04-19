from flask import *
from login import validate,add_user
from inference import fed_aggregate,update_inference
from model import predict_local,predict_global

app = Flask(__name__,template_folder="template")


@app.route('/')
def home():
	return render_template('login.html',error="")

@app.route('/login',methods=["POST","GET"])
def login():
	if request.method=="POST":
		user=request.form['user']
		pswd=request.form['pswd']
		if validate(user,pswd):
			fed_avg_params=fed_aggregate()
			return render_template("welcome.html",user=user,updated_params=str(fed_avg_params), error='')
		else:
			error="Authentication failed"
	else:
		error="Something went wrong"
	return render_template("login.html",error=error)


@app.route('/signin',methods=["POST","GET"])
def signin():
	if request.method=="POST":
		user=request.form['user']
		pswd=request.form['pswd']
		add_user(user,pswd)
		return render_template("login.html",error="Signed in successfully, You can login now")
	else:
		return render_template("login.html",error="Could not sign in, please try again later")


@app.route("/welcome",methods=["POST","GET"])
def welcome():
	if request.method=="POST":
		user=request.form['user']
		i=request.form['intercept']
		rm=request.form['rad_mean']
		tm=request.form['texture_mean']
		sm=request.form['smooth_mean']
		sym=request.form['symmetry_mean']
		cm=request.form['compact_mean']
		fdm=request.form['fract_dim_mean']
		rdm=request.form['rad_se']
		ts=request.form['texture_se']
		ss=request.form['smooth_se']
		cs=request.form['compact_se']
		ss=request.form['symmetry_se']
		fds=request.form['fract_dim_se']
		inference=[i,rm,tm,sm,sym,cm,fdm,rdm,ts,ss,cs,ss,fds]
		update_inference(user,inference)
		fed_avg_params=fed_aggregate()
		return render_template("welcome.html",error="Aggregated model updated successfully",user=user,updated_params=str(fed_avg_params))

@app.route('/predict',methods=["POST","GET"])
def prediction():
	if request.method=="POST":
		user=request.form['user']
		rm=request.form['rad_mean']
		tm=request.form['texture_mean']
		sm=request.form['smooth_mean']
		sym=request.form['symmetry_mean']
		cm=request.form['compact_mean']
		fdm=request.form['fract_dim_mean']
		rdm=request.form['rad_se']
		ts=request.form['texture_se']
		ss=request.form['smooth_se']
		cs=request.form['compact_se']
		ss=request.form['symmetry_se']
		fds=request.form['fract_dim_se']
		inputs=[rm,tm,sm,sym,cm,fdm,rdm,ts,ss,cs,ss,fds]
		return render_template("predict.html",user=user,fed_predict=predict_global(inputs),loc_predict=predict_local(inputs,user))
	else:
		user=request.args.get('user')
		return render_template("predict.html",user=user,fed_predict="Please provide inputs",loc_predict="Please provide inputs")

if __name__ == '__main__':
	app.run(debug=True)
