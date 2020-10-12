import redis
from ..utils.format_conf import format_sec, format_address
from ..conf.config import DEFAULT_SECONDS, REDIS_TIMEOUT


class FlaskStateConf:
    def __init__(self):
        # Enter the database name, address and conf directory or superior directory, the default is 0
        # If the project has a console_host database, it is not created
        # The default value is('console_host', 0)
        self.ADDRESS = 'sqlite:///console_host'

        # Set the interval to record the local state, with a minimum interval of 10 seconds
        # The default value is 60
        self.SECS = DEFAULT_SECONDS

    def set_address(self, address):
        self.ADDRESS = format_address(address)

    def set_secs(self, secs):
        self.SECS = format_sec(secs)


flask_state_conf = FlaskStateConf()


# Create redis object
class RedisConn:
    def __init__(self):
        self.redis = None

    def set_redis(self, redis_conf):
        self.redis = redis.Redis(host=redis_conf.get('REDIS_HOST'), port=redis_conf.get('REDIS_PORT'),
                                 password=redis_conf.get('REDIS_PASSWORD'), socket_connect_timeout=REDIS_TIMEOUT)

    def get_redis(self) -> redis.Redis:
        return self.redis


redis_conn = RedisConn()