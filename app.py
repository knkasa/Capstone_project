from flask import Flask, render_template

# specify image folder if loading image
app = Flask(__name__, static_url_path="/image", static_folder="image")
#app = Flask(__name__, static_url_path="/static", static_folder="static")

@app.route("/home")
def home():
	return  render_template('home.html')
	
#@app.route("/visual")
#def visual():
#    return  render_template('visual.html')

#@app.route("/regress")
#def regress():
#    return  render_template('regress.html')
	
#@app.route("/neural")
#def neural():
#    return  render_template('neural.html')
	
#@app.route("/tree")
#def tree():
#    return  render_template('tree.html')
	
# this allows you to run with python command 
# type " python file_name.py  
#if  __name__ == '__main__':  
	#app.run(debug=True)
	
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
	#app.run(port=5432)
	
	
	