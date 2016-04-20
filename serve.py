from darkweb import createApp

if __name__ == "__main__":
	app = createApp()
	app.run(debug=True, host="0.0.0.0", port=8080)

