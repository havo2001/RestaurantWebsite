from flask_website import flask_website, db
from flask_website.models import User, Order

@flask_website.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Order': Order}

if __name__ == '__main__':
    flask_website.run(host='localhost', port=5000, debug=True)