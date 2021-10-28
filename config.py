import os

basepath = os.path.abspath(os.path.dirname(__file__))
default_dbpath = os.path.join(basepath, 'app.db')


def set_config(env_var: str, default: str) -> str:
    env = os.environ.get(env_var)
    if not env:
        return default
    return env


class Cfg:
    SECRET_KEY = set_config('SECRET_KEY', 'secret')
    SQLALCHEMY_DATABASE_URI = set_config(
        'SQLALCHEMY_DATABASE_URI', f'sqlite:///{default_dbpath}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
