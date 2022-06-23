# openapi_client.GroupControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_controller_add_to_group**](GroupControllerApi.md#group_controller_add_to_group) | **POST** /rest/group/{instance_key}/addParticipants | Add participants to a group
[**group_controller_create_group**](GroupControllerApi.md#group_controller_create_group) | **POST** /rest/group/{instance_key}/create | Create a group
[**group_controller_demote_participants**](GroupControllerApi.md#group_controller_demote_participants) | **DELETE** /rest/group/{instance_key}/demoteParticipants | Demote certain participants in group
[**group_controller_get_admin_groups**](GroupControllerApi.md#group_controller_get_admin_groups) | **GET** /rest/group/{instance_key}/adminGroups | List all groups in which you are and admin
[**group_controller_get_admin_groups_with_participants**](GroupControllerApi.md#group_controller_get_admin_groups_with_participants) | **GET** /rest/group/{instance_key}/adminGroupsWithParticipants | List all groups in which you are and admin along with the participants array
[**group_controller_get_group**](GroupControllerApi.md#group_controller_get_group) | **GET** /rest/group/{instance_key}/group/{group_id} | Get a group
[**group_controller_get_group_invite_code**](GroupControllerApi.md#group_controller_get_group_invite_code) | **GET** /rest/group/{instance_key}/groupInviteCode | Get group invite code
[**group_controller_leave_group**](GroupControllerApi.md#group_controller_leave_group) | **DELETE** /rest/group/{instance_key}/leaveGroup | Leave group
[**group_controller_list_groups**](GroupControllerApi.md#group_controller_list_groups) | **GET** /rest/group/list/{instance_key} | List all groups
[**group_controller_promote_participants**](GroupControllerApi.md#group_controller_promote_participants) | **POST** /rest/group/{instance_key}/promoteParticipants | Promote certain participants in group
[**group_controller_remove_from_group**](GroupControllerApi.md#group_controller_remove_from_group) | **DELETE** /rest/group/{instance_key}/removeParticipants | Remove participants from group
[**group_controller_set_who_can_change_settings**](GroupControllerApi.md#group_controller_set_who_can_change_settings) | **PUT** /rest/group/{instance_key}/setWhoCanChangeSettings | Set who can change settings of group
[**group_controller_set_who_can_send_message**](GroupControllerApi.md#group_controller_set_who_can_send_message) | **PUT** /rest/group/{instance_key}/setWhoCanSendMessage | Set who can send message in group


# **group_controller_add_to_group**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} group_controller_add_to_group(instance_key)

Add participants to a group

Please note that the participants should not contain @s.whatsapp.net <br>

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from openapi_client.model.group_controller_add_to_group_request import GroupControllerAddToGroupRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
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

    # example passing only required values which don't have defaults set
    try:
        # Add participants to a group
        api_response = api_instance.group_controller_add_to_group(instance_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_add_to_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add participants to a group
        api_response = api_instance.group_controller_add_to_group(instance_key, group_controller_add_to_group_request=group_controller_add_to_group_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_add_to_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **group_controller_add_to_group_request** | [**GroupControllerAddToGroupRequest**](GroupControllerAddToGroupRequest.md)|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_create_group**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} group_controller_create_group(instance_key)

Create a group

Please note that the participants should not contain @s.whatsapp.net

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from openapi_client.model.group_controller_create_group_request import GroupControllerCreateGroupRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_controller_api.GroupControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    group_controller_create_group_request = GroupControllerCreateGroupRequest(
        group_data=CreateGroupData(
            group_name="group_name_example",
            participants=[
                "participants_example",
            ],
        ),
    ) # GroupControllerCreateGroupRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a group
        api_response = api_instance.group_controller_create_group(instance_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_create_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a group
        api_response = api_instance.group_controller_create_group(instance_key, group_controller_create_group_request=group_controller_create_group_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_create_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **group_controller_create_group_request** | [**GroupControllerCreateGroupRequest**](GroupControllerCreateGroupRequest.md)|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_demote_participants**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} group_controller_demote_participants(instance_key)

Demote certain participants in group

Please note that the participants should not contain @s.whatsapp.net <br>

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from openapi_client.model.group_controller_add_to_group_request import GroupControllerAddToGroupRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
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

    # example passing only required values which don't have defaults set
    try:
        # Demote certain participants in group
        api_response = api_instance.group_controller_demote_participants(instance_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_demote_participants: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Demote certain participants in group
        api_response = api_instance.group_controller_demote_participants(instance_key, group_controller_add_to_group_request=group_controller_add_to_group_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_demote_participants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **group_controller_add_to_group_request** | [**GroupControllerAddToGroupRequest**](GroupControllerAddToGroupRequest.md)|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_get_admin_groups**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} group_controller_get_admin_groups(instance_key)

List all groups in which you are and admin

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_controller_api.GroupControllerApi(api_client)
    instance_key = "instance_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List all groups in which you are and admin
        api_response = api_instance.group_controller_get_admin_groups(instance_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_get_admin_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_get_admin_groups_with_participants**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} group_controller_get_admin_groups_with_participants(instance_key)

List all groups in which you are and admin along with the participants array

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_controller_api.GroupControllerApi(api_client)
    instance_key = "instance_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List all groups in which you are and admin along with the participants array
        api_response = api_instance.group_controller_get_admin_groups_with_participants(instance_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_get_admin_groups_with_participants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_get_group**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} group_controller_get_group(instance_key, group_id)

Get a group

Please note that the group_id should contain @g.us in the end for example: 123456789@g.us

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_controller_api.GroupControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    group_id = "group_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a group
        api_response = api_instance.group_controller_get_group(instance_key, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_get_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **group_id** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_get_group_invite_code**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} group_controller_get_group_invite_code(instance_key)

Get group invite code

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_controller_api.GroupControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    group_id = "group_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get group invite code
        api_response = api_instance.group_controller_get_group_invite_code(instance_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_get_group_invite_code: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get group invite code
        api_response = api_instance.group_controller_get_group_invite_code(instance_key, group_id=group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_get_group_invite_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **group_id** | **str**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_leave_group**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} group_controller_leave_group(instance_key)

Leave group

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_controller_api.GroupControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    group_id = "group_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Leave group
        api_response = api_instance.group_controller_leave_group(instance_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_leave_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Leave group
        api_response = api_instance.group_controller_leave_group(instance_key, group_id=group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_leave_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **group_id** | **str**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_list_groups**
> str group_controller_list_groups(instance_key)

List all groups

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from openapi_client.model.unauthorized import Unauthorized
from openapi_client.model.not_found import NotFound
from openapi_client.model.forbidden import Forbidden
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_controller_api.GroupControllerApi(api_client)
    instance_key = "instance_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List all groups
        api_response = api_instance.group_controller_list_groups(instance_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_list_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Action completed successfully |  -  |
**401** | Phone not connected |  -  |
**403** | Invalid Instance Key |  -  |
**404** | Instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_promote_participants**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} group_controller_promote_participants(instance_key)

Promote certain participants in group

Please note that the participants should not contain @s.whatsapp.net <br>

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from openapi_client.model.group_controller_add_to_group_request import GroupControllerAddToGroupRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
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

    # example passing only required values which don't have defaults set
    try:
        # Promote certain participants in group
        api_response = api_instance.group_controller_promote_participants(instance_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_promote_participants: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Promote certain participants in group
        api_response = api_instance.group_controller_promote_participants(instance_key, group_controller_add_to_group_request=group_controller_add_to_group_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_promote_participants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **group_controller_add_to_group_request** | [**GroupControllerAddToGroupRequest**](GroupControllerAddToGroupRequest.md)|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_remove_from_group**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} group_controller_remove_from_group(instance_key)

Remove participants from group

Please note that the participants should not contain @s.whatsapp.net <br>

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from openapi_client.model.group_controller_add_to_group_request import GroupControllerAddToGroupRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
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

    # example passing only required values which don't have defaults set
    try:
        # Remove participants from group
        api_response = api_instance.group_controller_remove_from_group(instance_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_remove_from_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove participants from group
        api_response = api_instance.group_controller_remove_from_group(instance_key, group_controller_add_to_group_request=group_controller_add_to_group_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_remove_from_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **group_controller_add_to_group_request** | [**GroupControllerAddToGroupRequest**](GroupControllerAddToGroupRequest.md)|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_set_who_can_change_settings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} group_controller_set_who_can_change_settings(instance_key)

Set who can change settings of group

Please note that the participants should not contain @s.whatsapp.net <br>

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_controller_api.GroupControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    group_id = "group_id_example" # str |  (optional)
    allow_only_admins = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set who can change settings of group
        api_response = api_instance.group_controller_set_who_can_change_settings(instance_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_set_who_can_change_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set who can change settings of group
        api_response = api_instance.group_controller_set_who_can_change_settings(instance_key, group_id=group_id, allow_only_admins=allow_only_admins)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_set_who_can_change_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **group_id** | **str**|  | [optional]
 **allow_only_admins** | **bool**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_set_who_can_send_message**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} group_controller_set_who_can_send_message(instance_key)

Set who can send message in group

Please note that the participants should not contain @s.whatsapp.net <br>

### Example


```python
import time
import openapi_client
from openapi_client.api import group_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_controller_api.GroupControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    group_id = "group_id_example" # str |  (optional)
    allow_only_admins = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set who can send message in group
        api_response = api_instance.group_controller_set_who_can_send_message(instance_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_set_who_can_send_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set who can send message in group
        api_response = api_instance.group_controller_set_who_can_send_message(instance_key, group_id=group_id, allow_only_admins=allow_only_admins)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupControllerApi->group_controller_set_who_can_send_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **group_id** | **str**|  | [optional]
 **allow_only_admins** | **bool**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

