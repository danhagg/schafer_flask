from flaskblog import create_app

# Uses our Config class as default
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
