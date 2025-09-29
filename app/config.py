
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/fastapiml"
    SECRET_KEY: str = "CHANGE_THIS_TO_A_RANDOM_SECRET"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    ALGORITHM: str = "HS256"
    MODEL_PATH: str = "./model/model.pkl"
    class Config:
        env_file = ".env"
        
settings = Settings()