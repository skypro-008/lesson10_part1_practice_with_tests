from flask import Flask

app = Flask(__name__)


def load_users():
    from .users import users
    return users


if __name__ == '__main__':
    app.run()
