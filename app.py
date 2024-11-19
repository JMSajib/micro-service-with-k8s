from flask import Flask
from auth.routes import auth_blueprint

app = Flask(__name__)

app.register_blueprint(auth_blueprint, url_prefix='/api/v1/auth')

if __name__ == '__main__':
    app.run(debug=True)
