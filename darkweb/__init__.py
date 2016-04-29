from flask import Flask 

def createApp():
	app = Flask(__name__)
	with app.app_context():
		from darkweb.views import views
		app.register_blueprint(views)

	return app 

if __name__ == "__main__":
	app = createApp()
	app.run(host="0.0.0.0", port=8080)
