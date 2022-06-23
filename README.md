# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/WazapIO/WhatsAPIClientPython.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/WazapIO/WhatsAPIClientPython.git`)

Then import the package:
```python
import wazap_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wazap_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import wazap_client
from pprint import pprint
from wazap_client.api import group_controller_api
from wazap_client.model.forbidden import Forbidden
from wazap_client.model.group_controller_add_to_group_request import GroupControllerAddToGroupRequest
from wazap_client.model.group_controller_create_group_request import GroupControllerCreateGroupRequest
from wazap_client.model.not_found import NotFound
from wazap_client.model.unauthorized import Unauthorized
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wazap_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with wazap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = group_controller_api.GroupControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    group_controller_add_to_group_request = GroupControllerAddToGroupRequest(
        group_data=GroupData(
            group_id="group_id_example",
            participants=[
                "participants_example",
            ],
        ),
    ) # GroupControllerAddToGroupRequest |  (optional)

    try:
        # Add participants to a group
        api_response = api_instance.group_controller_add_to_group(instance_key, group_controller_add_to_group_request=group_controller_add_to_group_request)
        pprint(api_response)
    except wazap_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_add_to_group: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GroupControllerApi* | [**group_controller_add_to_group**](docs/GroupControllerApi.md#group_controller_add_to_group) | **POST** /rest/group/{instance_key}/addParticipants | Add participants to a group
*GroupControllerApi* | [**group_controller_create_group**](docs/GroupControllerApi.md#group_controller_create_group) | **POST** /rest/group/{instance_key}/create | Create a group
*GroupControllerApi* | [**group_controller_demote_participants**](docs/GroupControllerApi.md#group_controller_demote_participants) | **DELETE** /rest/group/{instance_key}/demoteParticipants | Demote certain participants in group
*GroupControllerApi* | [**group_controller_get_admin_groups**](docs/GroupControllerApi.md#group_controller_get_admin_groups) | **GET** /rest/group/{instance_key}/adminGroups | List all groups in which you are and admin
*GroupControllerApi* | [**group_controller_get_admin_groups_with_participants**](docs/GroupControllerApi.md#group_controller_get_admin_groups_with_participants) | **GET** /rest/group/{instance_key}/adminGroupsWithParticipants | List all groups in which you are and admin along with the participants array
*GroupControllerApi* | [**group_controller_get_group**](docs/GroupControllerApi.md#group_controller_get_group) | **GET** /rest/group/{instance_key}/group/{group_id} | Get a group
*GroupControllerApi* | [**group_controller_get_group_invite_code**](docs/GroupControllerApi.md#group_controller_get_group_invite_code) | **GET** /rest/group/{instance_key}/groupInviteCode | Get group invite code
*GroupControllerApi* | [**group_controller_leave_group**](docs/GroupControllerApi.md#group_controller_leave_group) | **DELETE** /rest/group/{instance_key}/leaveGroup | Leave group
*GroupControllerApi* | [**group_controller_list_groups**](docs/GroupControllerApi.md#group_controller_list_groups) | **GET** /rest/group/list/{instance_key} | List all groups
*GroupControllerApi* | [**group_controller_promote_participants**](docs/GroupControllerApi.md#group_controller_promote_participants) | **POST** /rest/group/{instance_key}/promoteParticipants | Promote certain participants in group
*GroupControllerApi* | [**group_controller_remove_from_group**](docs/GroupControllerApi.md#group_controller_remove_from_group) | **DELETE** /rest/group/{instance_key}/removeParticipants | Remove participants from group
*GroupControllerApi* | [**group_controller_set_who_can_change_settings**](docs/GroupControllerApi.md#group_controller_set_who_can_change_settings) | **PUT** /rest/group/{instance_key}/setWhoCanChangeSettings | Set who can change settings of group
*GroupControllerApi* | [**group_controller_set_who_can_send_message**](docs/GroupControllerApi.md#group_controller_set_who_can_send_message) | **PUT** /rest/group/{instance_key}/setWhoCanSendMessage | Set who can send message in group
*InstanceControllerApi* | [**instance_controller_create_new_whats_app_instance**](docs/InstanceControllerApi.md#instance_controller_create_new_whats_app_instance) | **POST** /rest/instance/init | Initialize a new WhatsApp instance
*InstanceControllerApi* | [**instance_controller_delete_instance**](docs/InstanceControllerApi.md#instance_controller_delete_instance) | **DELETE** /rest/instance/{instance_key}/delete | Delete an instance
*InstanceControllerApi* | [**instance_controller_download_media_message**](docs/InstanceControllerApi.md#instance_controller_download_media_message) | **POST** /rest/instance/downloadMediaMessage/{instance_key} | 
*InstanceControllerApi* | [**instance_controller_get_all_chats**](docs/InstanceControllerApi.md#instance_controller_get_all_chats) | **GET** /rest/instance/chats/{instance_key} | Get all your chats
*InstanceControllerApi* | [**instance_controller_get_all_contacts**](docs/InstanceControllerApi.md#instance_controller_get_all_contacts) | **GET** /rest/instance/contacts/{instance_key} | Get all your contacts
*InstanceControllerApi* | [**instance_controller_get_instance_data**](docs/InstanceControllerApi.md#instance_controller_get_instance_data) | **GET** /rest/instance/{instance_key} | Get an instance
*InstanceControllerApi* | [**instance_controller_get_messages_from_chat**](docs/InstanceControllerApi.md#instance_controller_get_messages_from_chat) | **GET** /rest/instance/messages/{instance_key} | Get messages from a specific chat
*InstanceControllerApi* | [**instance_controller_get_qrcode**](docs/InstanceControllerApi.md#instance_controller_get_qrcode) | **GET** /rest/instance/qrcode/{instance_key} | Get an instance
*InstanceControllerApi* | [**instance_controller_get_qrcode_base64**](docs/InstanceControllerApi.md#instance_controller_get_qrcode_base64) | **GET** /rest/instance/qrcode_base64/{instance_key} | Get the qrcode in base64 format
*InstanceControllerApi* | [**instance_controller_is_on_whats_app**](docs/InstanceControllerApi.md#instance_controller_is_on_whats_app) | **GET** /rest/instance/isOnWhatsApp/{instance_key} | Check if number is registerd on WhatsApp
*InstanceControllerApi* | [**instance_controller_list_instances**](docs/InstanceControllerApi.md#instance_controller_list_instances) | **GET** /rest/instance/list | List all instances
*InstanceControllerApi* | [**instance_controller_logout_instance**](docs/InstanceControllerApi.md#instance_controller_logout_instance) | **DELETE** /rest/instance/{instance_key}/logout | Logout from an instance
*SendMessageControllerApi* | [**send_message_controller_send_audio_message**](docs/SendMessageControllerApi.md#send_message_controller_send_audio_message) | **POST** /rest/sendMessage/{instance_key}/audio | Send an audio to an WhatsApp User
*SendMessageControllerApi* | [**send_message_controller_send_buttons_message**](docs/SendMessageControllerApi.md#send_message_controller_send_buttons_message) | **POST** /rest/sendMessage/{instance_key}/templateMessage | Send an interactive template message to an WhatsApp User
*SendMessageControllerApi* | [**send_message_controller_send_buttons_message_with_media**](docs/SendMessageControllerApi.md#send_message_controller_send_buttons_message_with_media) | **POST** /rest/sendMessage/{instance_key}/templateMessageWithMedia | Send an interactive template message with mediaHeader to an WhatsApp User
*SendMessageControllerApi* | [**send_message_controller_send_document_message**](docs/SendMessageControllerApi.md#send_message_controller_send_document_message) | **POST** /rest/sendMessage/{instance_key}/document | Send an document to an WhatsApp User
*SendMessageControllerApi* | [**send_message_controller_send_image_message**](docs/SendMessageControllerApi.md#send_message_controller_send_image_message) | **POST** /rest/sendMessage/{instance_key}/image | Send an image message to an WhatsApp User
*SendMessageControllerApi* | [**send_message_controller_send_list_message**](docs/SendMessageControllerApi.md#send_message_controller_send_list_message) | **POST** /rest/sendMessage/{instance_key}/listMessage | Send an vacard message to an WhatsApp User
*SendMessageControllerApi* | [**send_message_controller_send_location_message**](docs/SendMessageControllerApi.md#send_message_controller_send_location_message) | **POST** /rest/sendMessage/{instance_key}/location | Send an location to an WhatsApp User
*SendMessageControllerApi* | [**send_message_controller_send_media_url**](docs/SendMessageControllerApi.md#send_message_controller_send_media_url) | **POST** /rest/sendMessage/{instance_key}/mediaUrl | Send a media message via a URL
*SendMessageControllerApi* | [**send_message_controller_send_template_messsage**](docs/SendMessageControllerApi.md#send_message_controller_send_template_messsage) | **POST** /rest/sendMessage/{instance_key}/contactMessage | Send an vacard message to an WhatsApp User
*SendMessageControllerApi* | [**send_message_controller_send_text_message**](docs/SendMessageControllerApi.md#send_message_controller_send_text_message) | **POST** /rest/sendMessage/{instance_key}/textToMany | Send a text message to multiple WhatsApp users
*SendMessageControllerApi* | [**send_message_controller_send_text_message_to_single_user**](docs/SendMessageControllerApi.md#send_message_controller_send_text_message_to_single_user) | **POST** /rest/sendMessage/{instance_key}/text | Send a text message to an WhatsApp User
*SendMessageControllerApi* | [**send_message_controller_send_video_message**](docs/SendMessageControllerApi.md#send_message_controller_send_video_message) | **POST** /rest/sendMessage/{instance_key}/video | Send an video to an WhatsApp User
*WebhookControllerApi* | [**webhook_controller_enable_message_webhook**](docs/WebhookControllerApi.md#webhook_controller_enable_message_webhook) | **POST** /rest/webhook/{instance_key}/enableMessage | 
*WebhookControllerApi* | [**webhook_controller_get_webhook_stauts**](docs/WebhookControllerApi.md#webhook_controller_get_webhook_stauts) | **GET** /rest/webhook/{instance_key} | Get an instance webhook data
*WebhookControllerApi* | [**webhook_controller_update_webhook_url**](docs/WebhookControllerApi.md#webhook_controller_update_webhook_url) | **POST** /rest/webhook/{instance_key}/updateUrl | 


## Documentation For Models

 - [BadRequest](docs/BadRequest.md)
 - [Button](docs/Button.md)
 - [ButtonMessage](docs/ButtonMessage.md)
 - [ButtonMessageWithImage](docs/ButtonMessageWithImage.md)
 - [ContactData](docs/ContactData.md)
 - [CreateGroupData](docs/CreateGroupData.md)
 - [Forbidden](docs/Forbidden.md)
 - [GenericError](docs/GenericError.md)
 - [GroupControllerAddToGroupRequest](docs/GroupControllerAddToGroupRequest.md)
 - [GroupControllerCreateGroupRequest](docs/GroupControllerCreateGroupRequest.md)
 - [GroupData](docs/GroupData.md)
 - [InstanceControllerDownloadMediaMessageRequest](docs/InstanceControllerDownloadMediaMessageRequest.md)
 - [ListRow](docs/ListRow.md)
 - [ListSection](docs/ListSection.md)
 - [LocationCordinates](docs/LocationCordinates.md)
 - [LocationMessage](docs/LocationMessage.md)
 - [MediaMessageKeys](docs/MediaMessageKeys.md)
 - [MediaUrlMessage](docs/MediaUrlMessage.md)
 - [NotFound](docs/NotFound.md)
 - [SendListMessageData](docs/SendListMessageData.md)
 - [SendMessageControllerSendButtonsMessageRequest](docs/SendMessageControllerSendButtonsMessageRequest.md)
 - [SendMessageControllerSendButtonsMessageWithMediaRequest](docs/SendMessageControllerSendButtonsMessageWithMediaRequest.md)
 - [SendMessageControllerSendListMessageRequest](docs/SendMessageControllerSendListMessageRequest.md)
 - [SendMessageControllerSendLocationMessageRequest](docs/SendMessageControllerSendLocationMessageRequest.md)
 - [SendMessageControllerSendMediaUrlRequest](docs/SendMessageControllerSendMediaUrlRequest.md)
 - [SendMessageControllerSendTemplateMesssageRequest](docs/SendMessageControllerSendTemplateMesssageRequest.md)
 - [SendMessageControllerSendTextMessageRequest](docs/SendMessageControllerSendTextMessageRequest.md)
 - [SendMessageControllerSendTextMessageToSingleUserRequest](docs/SendMessageControllerSendTextMessageToSingleUserRequest.md)
 - [SendVCardData](docs/SendVCardData.md)
 - [TextMessge](docs/TextMessge.md)
 - [TextMessgeSingle](docs/TextMessgeSingle.md)
 - [Unauthorized](docs/Unauthorized.md)
 - [UpdateWebhookStatusSchema](docs/UpdateWebhookStatusSchema.md)
 - [UpdateWebhookUrlSchema](docs/UpdateWebhookUrlSchema.md)
 - [WebhookControllerEnableMessageWebhookRequest](docs/WebhookControllerEnableMessageWebhookRequest.md)
 - [WebhookControllerUpdateWebhookUrlRequest](docs/WebhookControllerUpdateWebhookUrlRequest.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in wazap_client.apis and wazap_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from wazap_client.api.default_api import DefaultApi`
- `from wazap_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import wazap_client
from wazap_client.apis import *
from wazap_client.models import *
```
