from typing import Optional

from pygal.maps.world import COUNTRIES


def get_country_code(country_name: str) -> Optional[str]:
    """ Return the pygal 2-digit country code for the given country """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
