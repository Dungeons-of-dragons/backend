from api import create_app, sql
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
