from website import create_app

app = create_app()

if __name__ == '__main__': #Only if you run this file dirrectly
    app.run(debug=True) #Debug - Rerun the server everytime we make a change. Product - Fals



