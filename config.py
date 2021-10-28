import os


def set_config(env_var: str, default: str) -> str:
    env = os.environ.get(env_var)
    if env == '':
        return ''
    return env


class Cfg:
    SECRET_KEY = set_config('SECRET_KEY', 'secret')
