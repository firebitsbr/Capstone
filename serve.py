from darkweb import app
import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8080)

