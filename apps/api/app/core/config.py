import os

class Settings:
    PROJECT_NAME: str = "AI Recruitment & Talent Sourcing API"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://copilot_user:copilot_secure_password@localhost:5432/recruitment_sourcing_db")

settings = Settings()
