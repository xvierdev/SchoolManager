from flask import Flask
import routes

app = Flask(__name__)

app.register_blueprint(routes.main_routes)

if __name__ == '__main__':
    app.run(debug=True)