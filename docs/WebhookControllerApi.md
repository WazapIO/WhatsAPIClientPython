# openapi_client.WebhookControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_controller_enable_message_webhook**](WebhookControllerApi.md#webhook_controller_enable_message_webhook) | **POST** /rest/webhook/{instance_key}/enableMessage | 
[**webhook_controller_get_webhook_stauts**](WebhookControllerApi.md#webhook_controller_get_webhook_stauts) | **GET** /rest/webhook/{instance_key} | Get an instance webhook data
[**webhook_controller_update_webhook_url**](WebhookControllerApi.md#webhook_controller_update_webhook_url) | **POST** /rest/webhook/{instance_key}/updateUrl | 


# **webhook_controller_enable_message_webhook**
> webhook_controller_enable_message_webhook(instance_key)



### Example


```python
import time
import openapi_client
from openapi_client.api import webhook_controller_api
from openapi_client.model.webhook_controller_enable_message_webhook_request import WebhookControllerEnableMessageWebhookRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = webhook_controller_api.WebhookControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    webhook_controller_enable_message_webhook_request = WebhookControllerEnableMessageWebhookRequest(
        data=UpdateWebhookStatusSchema(
            send_webhook=True,
        ),
    ) # WebhookControllerEnableMessageWebhookRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.webhook_controller_enable_message_webhook(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling WebhookControllerApi->webhook_controller_enable_message_webhook: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.webhook_controller_enable_message_webhook(instance_key, webhook_controller_enable_message_webhook_request=webhook_controller_enable_message_webhook_request)
    except openapi_client.ApiException as e:
        print("Exception when calling WebhookControllerApi->webhook_controller_enable_message_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **webhook_controller_enable_message_webhook_request** | [**WebhookControllerEnableMessageWebhookRequest**](WebhookControllerEnableMessageWebhookRequest.md)|  | [optional]

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

# **webhook_controller_get_webhook_stauts**
> webhook_controller_get_webhook_stauts(instance_key)

Get an instance webhook data

### Example


```python
import time
import openapi_client
from openapi_client.api import webhook_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = webhook_controller_api.WebhookControllerApi(api_client)
    instance_key = "instance_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get an instance webhook data
        api_instance.webhook_controller_get_webhook_stauts(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling WebhookControllerApi->webhook_controller_get_webhook_stauts: %s\n" % e)
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

# **webhook_controller_update_webhook_url**
> webhook_controller_update_webhook_url(instance_key)



### Example


```python
import time
import openapi_client
from openapi_client.api import webhook_controller_api
from openapi_client.model.webhook_controller_update_webhook_url_request import WebhookControllerUpdateWebhookUrlRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = webhook_controller_api.WebhookControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    webhook_controller_update_webhook_url_request = WebhookControllerUpdateWebhookUrlRequest(
        data=UpdateWebhookUrlSchema(
            url="url_example",
        ),
    ) # WebhookControllerUpdateWebhookUrlRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.webhook_controller_update_webhook_url(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling WebhookControllerApi->webhook_controller_update_webhook_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.webhook_controller_update_webhook_url(instance_key, webhook_controller_update_webhook_url_request=webhook_controller_update_webhook_url_request)
    except openapi_client.ApiException as e:
        print("Exception when calling WebhookControllerApi->webhook_controller_update_webhook_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **webhook_controller_update_webhook_url_request** | [**WebhookControllerUpdateWebhookUrlRequest**](WebhookControllerUpdateWebhookUrlRequest.md)|  | [optional]

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

