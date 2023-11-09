from api import create_app, sql
from api.models import User
import os

conf = os.getenv("FLASK_CONFIG") or "default"
app = create_app(conf)


@app.cli.command()
def test():
    """
    Running the unit test
    """
    import unittest

    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.shell_context_processor
def shell_context():
    return dict(sql=sql, User=User)
