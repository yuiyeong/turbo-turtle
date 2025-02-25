import dataclasses


@dataclasses.dataclass(frozen=True)
class Postgres:
    host: str
    port: int
    user: str
    password: str
    db: str

    @property
    def django_db_settings(self) -> dict:
        return {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": self.db,
            "USER": self.user,
            "PASSWORD": self.password,
            "HOST": self.host,
            "PORT": self.port,
        }


@dataclasses.dataclass(frozen=True)
class Redis:
    host: str
    port: int
    user: str
    password: str
    db: str

    @property
    def django_cache_settings(self) -> dict:
        location = "redis://"
        if self.user and self.password:
            location += f"{self.user}:{self.password}@"
        location += f"{self.host}:{self.port}/{self.db}"
        return {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": location,
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            },
        }
