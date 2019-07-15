from hde_api_client import HelpDeskEddyClient

from dj_hde.models import Config
from .exceptions import NoActiveCredentials, MultipleActiveCredentials


class DjHelpDeskEddyClient(HelpDeskEddyClient):
    def __init__(self):
        try:
            self.config = Config.objects.get(is_active=True)
        except Config.DoesNotExist:
            raise NoActiveCredentials
        except Config.MultipleObjectsReturned:
            raise MultipleActiveCredentials

        super(DjHelpDeskEddyClient, self).__init__(
            domain=self.config.domain,
            email=self.config.email,
            api_key=self.config.api_key,
        )
