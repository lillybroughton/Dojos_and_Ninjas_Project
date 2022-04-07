from flask_application import app
from flask_application.controllers import dojos, ninjas

if __name__=="__main__":
	app.run(debug=True)