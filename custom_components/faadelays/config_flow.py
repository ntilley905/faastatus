"""Config flow for FAA Delays integration."""
import logging

from aiohttp import ClientConnectionError
import faadelays
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_ID
from homeassistant.helpers import aiohttp_client

from .const import DOMAIN  # pylint:disable=unused-import

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema({vol.Required(CONF_ID): str})


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for FAA Delays."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if not user_input:
            return self.async_show_form(
                step_id="user", data_schema=DATA_SCHEMA, errors=errors
            )

        await self.async_set_unique_id(user_input[CONF_ID])
        self._abort_if_unique_id_configured()

        websession = aiohttp_client.async_get_clientsession(self.hass)

        try:
            data = faadelays.Airport(user_input[CONF_ID], websession)
            await data.update()
            _LOGGER.debug(
                "Creating entry with id: %s, name: %s", user_input[CONF_ID], data.name
            )
        except faadelays.InvalidAirport:
            _LOGGER.error("Airport code %s is invalid", user_input[CONF_ID])
            errors[CONF_ID] = "invalid_airport"
            return self.async_show_form(
                step_id="user", data_schema=DATA_SCHEMA, errors=errors
            )
        except ClientConnectionError:
            _LOGGER.error("Error connecting to FAA API")
            errors["base"] = "cannot_connect"
            return self.async_show_form(
                step_id="user", data_schema=DATA_SCHEMA, errors=errors
            )
        except Exception as error:  # pylint: disable=broad-except
            _LOGGER.exception("Unexpected exception: %s", error)
            errors["base"] = "unknown"
            return self.async_show_form(
                step_id="user", data_schema=DATA_SCHEMA, errors=errors
            )

        return self.async_create_entry(title=data.name, data=user_input)
