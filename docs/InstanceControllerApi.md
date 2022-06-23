# openapi_client.InstanceControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_controller_create_new_whats_app_instance**](InstanceControllerApi.md#instance_controller_create_new_whats_app_instance) | **POST** /rest/instance/init | Initialize a new WhatsApp instance
[**instance_controller_delete_instance**](InstanceControllerApi.md#instance_controller_delete_instance) | **DELETE** /rest/instance/{instance_key}/delete | Delete an instance
[**instance_controller_download_media_message**](InstanceControllerApi.md#instance_controller_download_media_message) | **POST** /rest/instance/downloadMediaMessage/{instance_key} | 
[**instance_controller_get_all_chats**](InstanceControllerApi.md#instance_controller_get_all_chats) | **GET** /rest/instance/chats/{instance_key} | Get all your chats
[**instance_controller_get_all_contacts**](InstanceControllerApi.md#instance_controller_get_all_contacts) | **GET** /rest/instance/contacts/{instance_key} | Get all your contacts
[**instance_controller_get_instance_data**](InstanceControllerApi.md#instance_controller_get_instance_data) | **GET** /rest/instance/{instance_key} | Get an instance
[**instance_controller_get_messages_from_chat**](InstanceControllerApi.md#instance_controller_get_messages_from_chat) | **GET** /rest/instance/messages/{instance_key} | Get messages from a specific chat
[**instance_controller_get_qrcode**](InstanceControllerApi.md#instance_controller_get_qrcode) | **GET** /rest/instance/qrcode/{instance_key} | Get an instance
[**instance_controller_get_qrcode_base64**](InstanceControllerApi.md#instance_controller_get_qrcode_base64) | **GET** /rest/instance/qrcode_base64/{instance_key} | Get the qrcode in base64 format
[**instance_controller_is_on_whats_app**](InstanceControllerApi.md#instance_controller_is_on_whats_app) | **GET** /rest/instance/isOnWhatsApp/{instance_key} | Check if number is registerd on WhatsApp
[**instance_controller_list_instances**](InstanceControllerApi.md#instance_controller_list_instances) | **GET** /rest/instance/list | List all instances
[**instance_controller_logout_instance**](InstanceControllerApi.md#instance_controller_logout_instance) | **DELETE** /rest/instance/{instance_key}/logout | Logout from an instance


# **instance_controller_create_new_whats_app_instance**
> instance_controller_create_new_whats_app_instance()

Initialize a new WhatsApp instance

### Example


```python
import time
import openapi_client
from openapi_client.api import instance_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instance_controller_api.InstanceControllerApi(api_client)
    instance_key = "instance_key_example" # str |  (optional)
    disable_webhook = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initialize a new WhatsApp instance
        api_instance.instance_controller_create_new_whats_app_instance(instance_key=instance_key, disable_webhook=disable_webhook)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_create_new_whats_app_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  | [optional]
 **disable_webhook** | **bool**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_delete_instance**
> instance_controller_delete_instance(instance_key)

Delete an instance

### Example


```python
import time
import openapi_client
from openapi_client.api import instance_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instance_controller_api.InstanceControllerApi(api_client)
    instance_key = "instance_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an instance
        api_instance.instance_controller_delete_instance(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_delete_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_download_media_message**
> instance_controller_download_media_message(instance_key)



### Example


```python
import time
import openapi_client
from openapi_client.api import instance_controller_api
from openapi_client.model.instance_controller_download_media_message_request import InstanceControllerDownloadMediaMessageRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instance_controller_api.InstanceControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    instance_controller_download_media_message_request = InstanceControllerDownloadMediaMessageRequest(
        message_keys=MediaMessageKeys(
            media_key="media_key_example",
            direct_path="direct_path_example",
            url="url_example",
            message_type="message_type_example",
        ),
    ) # InstanceControllerDownloadMediaMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.instance_controller_download_media_message(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_download_media_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.instance_controller_download_media_message(instance_key, instance_controller_download_media_message_request=instance_controller_download_media_message_request)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_download_media_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **instance_controller_download_media_message_request** | [**InstanceControllerDownloadMediaMessageRequest**](InstanceControllerDownloadMediaMessageRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_get_all_chats**
> instance_controller_get_all_chats(instance_key)

Get all your chats

### Example


```python
import time
import openapi_client
from openapi_client.api import instance_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instance_controller_api.InstanceControllerApi(api_client)
    instance_key = "instance_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get all your chats
        api_instance.instance_controller_get_all_chats(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_get_all_chats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_get_all_contacts**
> instance_controller_get_all_contacts(instance_key)

Get all your contacts

### Example


```python
import time
import openapi_client
from openapi_client.api import instance_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instance_controller_api.InstanceControllerApi(api_client)
    instance_key = "instance_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get all your contacts
        api_instance.instance_controller_get_all_contacts(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_get_all_contacts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_get_instance_data**
> instance_controller_get_instance_data(instance_key)

Get an instance

### Example


```python
import time
import openapi_client
from openapi_client.api import instance_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instance_controller_api.InstanceControllerApi(api_client)
    instance_key = "instance_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get an instance
        api_instance.instance_controller_get_instance_data(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_get_instance_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_get_messages_from_chat**
> instance_controller_get_messages_from_chat(instance_key)

Get messages from a specific chat

### Example


```python
import time
import openapi_client
from openapi_client.api import instance_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instance_controller_api.InstanceControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    chat_id = "chat_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get messages from a specific chat
        api_instance.instance_controller_get_messages_from_chat(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_get_messages_from_chat: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get messages from a specific chat
        api_instance.instance_controller_get_messages_from_chat(instance_key, chat_id=chat_id)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_get_messages_from_chat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **chat_id** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_get_qrcode**
> instance_controller_get_qrcode(instance_key)

Get an instance

### Example


```python
import time
import openapi_client
from openapi_client.api import instance_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instance_controller_api.InstanceControllerApi(api_client)
    instance_key = "instance_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get an instance
        api_instance.instance_controller_get_qrcode(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_get_qrcode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_get_qrcode_base64**
> instance_controller_get_qrcode_base64(instance_key)

Get the qrcode in base64 format

### Example


```python
import time
import openapi_client
from openapi_client.api import instance_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instance_controller_api.InstanceControllerApi(api_client)
    instance_key = "instance_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the qrcode in base64 format
        api_instance.instance_controller_get_qrcode_base64(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_get_qrcode_base64: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_is_on_whats_app**
> instance_controller_is_on_whats_app(instance_key)

Check if number is registerd on WhatsApp

### Example


```python
import time
import openapi_client
from openapi_client.api import instance_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instance_controller_api.InstanceControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    jid = "jid_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Check if number is registerd on WhatsApp
        api_instance.instance_controller_is_on_whats_app(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_is_on_whats_app: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Check if number is registerd on WhatsApp
        api_instance.instance_controller_is_on_whats_app(instance_key, jid=jid)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_is_on_whats_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **jid** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_list_instances**
> instance_controller_list_instances()

List all instances

### Example


```python
import time
import openapi_client
from openapi_client.api import instance_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instance_controller_api.InstanceControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all instances
        api_instance.instance_controller_list_instances()
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_list_instances: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_logout_instance**
> instance_controller_logout_instance(instance_key)

Logout from an instance

### Example


```python
import time
import openapi_client
from openapi_client.api import instance_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instance_controller_api.InstanceControllerApi(api_client)
    instance_key = "instance_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Logout from an instance
        api_instance.instance_controller_logout_instance(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling InstanceControllerApi->instance_controller_logout_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

