
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from openapi_client.api.group_controller_api import GroupControllerApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openapi_client.api.group_controller_api import GroupControllerApi
from openapi_client.api.instance_controller_api import InstanceControllerApi
from openapi_client.api.send_message_controller_api import SendMessageControllerApi
from openapi_client.api.webhook_controller_api import WebhookControllerApi
