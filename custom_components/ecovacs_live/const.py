"""Constants for ECOVACS Live View."""
from __future__ import annotations

from homeassistant.const import Platform

DOMAIN = "ecovacs_live"
PLATFORMS: list[Platform] = [Platform.CAMERA, Platform.BUTTON, Platform.SENSOR]

CONF_ACCOUNT = "account"
CONF_PASSWORD = "password"
CONF_COUNTRY = "country"
CONF_LIVE_VIEW_PIN = "live_view_pin"
CONF_CLIENT_ID = "client_id"
CONF_AUTO_STOP_MINUTES = "auto_stop_minutes"
CONF_ACCOUNT_CREDENTIALS = "account_credentials"

DEFAULT_COUNTRY = "VN"
DEFAULT_AUTO_STOP_MINUTES = 5
