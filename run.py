from blog import create_app, db


app = create_app()



if __name__ == '__main__':
    #create_user()
    with app.app_context():
        db.drop_all()
        db.create_all()
        app.run(debug=True)