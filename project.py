from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

# https://flask.palletsprojects.com/en/3.0.x/quickstart/#about-responses
with app.test_request_context():
    ...