from app.app import create_app

app = create_app()


@app.route('/v1/user/get')
def get_user():
    return 'i am qiyue'


if __name__ == "__main__":
    app.run(debug=True)
