from hde_api_client import HelpDeskEddyClient

from dj_hde.models import Config
from .exceptions import NoActiveCredentials, MultipleActiveCredentials


class DjHelpDeskEddyClient(HelpDeskEddyClient):
    def __init__(self):
        try:
            api_credentials = Config.objects.get(is_active=True)
        except Config.DoesNotExist:
            raise NoActiveCredentials
        except Config.MultipleObjectsReturned:
            raise MultipleActiveCredentials

        super(DjHelpDeskEddyClient, self).__init__(
            domain=api_credentials.domain,
            email=api_credentials.email,
            api_key=api_credentials.api_key,
        )
