from environs import Env
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

env = Env()
env.read_env()

class Config:
    """
    """
    SECRET_KEY = env.str("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # BOOTSTRAP_SERVE_LOCAL = True
    # BOOTSTRAP_USE_MINIFIED = True
    SEND_FILE_MAX_AGE_DEFAULT = env.int("SEND_FILE_MAX_AGE_DEFAULT")
    BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS")
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = "simple" 
    ADMIN_TEL = '0799582648'


class DevConfig(Config):
    """
    """
    DEBUG = True
    DEBUG_TB_ENABLED = DEBUG
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://timoh:bigboy999@localhost/glam_spa"


class ProdConfig(Config):
    """
    """
    DEBUG = False
    DEBUG_TB_ENABLED = DEBUG
    SQLALCHEMY_DATABASE_URI = env.str('SQLALCHEMY_DATABASE_URI')


config_options = {
    'development': DevConfig(),
    'production': ProdConfig()
}
