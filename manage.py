import os
import unittest

from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import blueprint
from app.main import create_app, db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
migrate = Migrate(app, db)

app.app_context().push()

cli = FlaskGroup(app)


@cli.command('run')
def run():
    app.run(port=5002, host="0.0.0.0",debug=True)


@cli.command('test')
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    app.run(port=5002, host="0.0.0.0")