from hde_api_client import HelpDeskEddyClient

from dj_hde.models import APICredentials


class DjHelpDeskEddyClient(HelpDeskEddyClient):
    def __init__(self):
        api_credentials = APICredentials.objects.filter(is_active=True).last()

        assert api_credentials is not None, 'No active credentials'

        super(DjHelpDeskEddyClient, self).__init__(
            domain=api_credentials.domain,
            email=api_credentials.email,
            api_key=api_credentials.api_key,
        )
