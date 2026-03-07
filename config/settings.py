from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_name: str = "frame² – red sox intelligence"

SETTINGS = Settings()
