"""Project configuration loaded from environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - dependency may not be installed yet.
    load_dotenv = None

if load_dotenv:
    load_dotenv()


def _env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def _env_int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer, got {value!r}") from exc


@dataclass(frozen=True)
class Settings:
    base_url: str
    email: str | None
    password: str | None
    headless: bool
    slow_mo: int
    default_timeout: int

    def require_credentials(self) -> tuple[str, str]:
        if not self.email or not self.password:
            raise RuntimeError(
                "Missing credentials. Set QA_EMAIL and QA_PASSWORD "
                "in your environment or in a local .env file."
            )
        return self.email, self.password


def get_settings() -> Settings:
    return Settings(
        base_url=os.getenv(
            "APP_BASE_URL",
            os.getenv("SWAPJOYS_BASE_URL", "https://swapjoys.com/"),
        ),
        email=os.getenv("QA_EMAIL", os.getenv("SWAPJOYS_EMAIL")),
        password=os.getenv("QA_PASSWORD", os.getenv("SWAPJOYS_PASSWORD")),
        headless=_env_bool("HEADLESS", True),
        slow_mo=_env_int("SLOW_MO", 0),
        default_timeout=_env_int("DEFAULT_TIMEOUT", 15_000),
    )
