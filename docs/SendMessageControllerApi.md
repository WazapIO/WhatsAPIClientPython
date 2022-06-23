# openapi_client.SendMessageControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_message_controller_send_audio_message**](SendMessageControllerApi.md#send_message_controller_send_audio_message) | **POST** /rest/sendMessage/{instance_key}/audio | Send an audio to an WhatsApp User
[**send_message_controller_send_buttons_message**](SendMessageControllerApi.md#send_message_controller_send_buttons_message) | **POST** /rest/sendMessage/{instance_key}/templateMessage | Send an interactive template message to an WhatsApp User
[**send_message_controller_send_buttons_message_with_media**](SendMessageControllerApi.md#send_message_controller_send_buttons_message_with_media) | **POST** /rest/sendMessage/{instance_key}/templateMessageWithMedia | Send an interactive template message with mediaHeader to an WhatsApp User
[**send_message_controller_send_document_message**](SendMessageControllerApi.md#send_message_controller_send_document_message) | **POST** /rest/sendMessage/{instance_key}/document | Send an document to an WhatsApp User
[**send_message_controller_send_image_message**](SendMessageControllerApi.md#send_message_controller_send_image_message) | **POST** /rest/sendMessage/{instance_key}/image | Send an image message to an WhatsApp User
[**send_message_controller_send_list_message**](SendMessageControllerApi.md#send_message_controller_send_list_message) | **POST** /rest/sendMessage/{instance_key}/listMessage | Send an vacard message to an WhatsApp User
[**send_message_controller_send_location_message**](SendMessageControllerApi.md#send_message_controller_send_location_message) | **POST** /rest/sendMessage/{instance_key}/location | Send an location to an WhatsApp User
[**send_message_controller_send_media_url**](SendMessageControllerApi.md#send_message_controller_send_media_url) | **POST** /rest/sendMessage/{instance_key}/mediaUrl | Send a media message via a URL
[**send_message_controller_send_template_messsage**](SendMessageControllerApi.md#send_message_controller_send_template_messsage) | **POST** /rest/sendMessage/{instance_key}/contactMessage | Send an vacard message to an WhatsApp User
[**send_message_controller_send_text_message**](SendMessageControllerApi.md#send_message_controller_send_text_message) | **POST** /rest/sendMessage/{instance_key}/textToMany | Send a text message to multiple WhatsApp users
[**send_message_controller_send_text_message_to_single_user**](SendMessageControllerApi.md#send_message_controller_send_text_message_to_single_user) | **POST** /rest/sendMessage/{instance_key}/text | Send a text message to an WhatsApp User
[**send_message_controller_send_video_message**](SendMessageControllerApi.md#send_message_controller_send_video_message) | **POST** /rest/sendMessage/{instance_key}/video | Send an video to an WhatsApp User


# **send_message_controller_send_audio_message**
> send_message_controller_send_audio_message(instance_key)

Send an audio to an WhatsApp User

### Example


```python
import time
import openapi_client
from openapi_client.api import send_message_controller_api
from openapi_client.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = send_message_controller_api.SendMessageControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    id = "id_example" # str |  (optional)
    caption = "caption_example" # str |  (optional)
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an audio to an WhatsApp User
        api_instance.send_message_controller_send_audio_message(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_audio_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an audio to an WhatsApp User
        api_instance.send_message_controller_send_audio_message(instance_key, id=id, caption=caption, file=file)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_audio_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **id** | **str**|  | [optional]
 **caption** | **str**|  | [optional]
 **file** | **file_type**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | &lt;File too long | Too many parts | Too many files | Field name too long | Field value too long | Too many fields | Unexpected field&gt;  [fieldName] Example: File too long file1 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message_controller_send_buttons_message**
> send_message_controller_send_buttons_message(instance_key)

Send an interactive template message to an WhatsApp User

The templateMessage is a special type of message that allows <br />     you to send a message with a special buttons like quickReply, <br />     urlButton, callButton, etc. <br />     <br>     <strong>How to send templateMessage?</strong> <br />     <br>     The messageData object requires you to specify the type of button you <br />     want to send to the user. <br />     The type of button you can send are: <br />     <br>     <code>replyButton</code><br><br>     <code>urlButton</code><br><br>     <code>callButton</code><br><br>     <br>     In the <i>payload</i> field, you have to enter the payload <br>     i.e. url in case of the urlButton or phone number in case of callButton <br>     <br>     <strong>Example of templateMessage? </strong> <br />     <br>     <code><br> {<br>    \"messageData\":{<br>       \"to\":\"918788889688\",<br>       \"text\":\"string\",<br>       \"buttons\":[<br>          {<br>             \"type\":\"replyButton\",<br>             \"title\":\"This is a replyButton\"<br>          },<br>          {<br>             \"type\":\"urlButton\",<br>             \"title\":\"This is a urlButton\",<br>             \"payload\":\"https://google.com\"<br>          },<br>          {<br>             \"type\":\"callButton\",<br>             \"title\":\"This is a callButton\",<br>             \"payload\":\"918788889688\"<br>          }<br>       ],<br>       \"footerText\":\"Hello World\"<br>    }<br> }<br>     </code>     <br>     <strong>NOTE: </strong>     <i>Due to certain limitations from WhatsApp, when you send templateMessage to someone, <br>     the message won't be visible in you phone. Also you will also see that the message has been sent <br>     too your own phone number.<br>     </i> 

### Example


```python
import time
import openapi_client
from openapi_client.api import send_message_controller_api
from openapi_client.model.send_message_controller_send_buttons_message_request import SendMessageControllerSendButtonsMessageRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = send_message_controller_api.SendMessageControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    send_message_controller_send_buttons_message_request = SendMessageControllerSendButtonsMessageRequest(
        message_data=ButtonMessage(
            to="to_example",
            text="text_example",
            buttons=[
                Button(
                    type="type_example",
                    title="title_example",
                    payload="payload_example",
                ),
            ],
            footer_text="footer_text_example",
        ),
    ) # SendMessageControllerSendButtonsMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an interactive template message to an WhatsApp User
        api_instance.send_message_controller_send_buttons_message(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_buttons_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an interactive template message to an WhatsApp User
        api_instance.send_message_controller_send_buttons_message(instance_key, send_message_controller_send_buttons_message_request=send_message_controller_send_buttons_message_request)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_buttons_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **send_message_controller_send_buttons_message_request** | [**SendMessageControllerSendButtonsMessageRequest**](SendMessageControllerSendButtonsMessageRequest.md)|  | [optional]

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

# **send_message_controller_send_buttons_message_with_media**
> send_message_controller_send_buttons_message_with_media(instance_key)

Send an interactive template message with mediaHeader to an WhatsApp User

The templateMessage is a special type of message that allows <br />     you to send a message with a special buttons like quickReply, <br />     urlButton, callButton, etc. <br />     <br>     <strong>How to send templateMessage?</strong> <br />     <br>     The messageData object requires you to specify the type of button you <br />     want to send to the user. <br />     The type of button you can send are: <br />     <br>     <code>replyButton</code><br><br>     <code>urlButton</code><br><br>     <code>callButton</code><br><br>     <br>     In the <i>payload</i> field, you have to enter the payload <br>     i.e. url in case of the urlButton or phone number in case of callButton <br>     <br>     <strong>Example of templateMessage? </strong> <br />     <br>     <code><br> {<br>    \"messageData\":{<br>       \"to\":\"918788889688\",<br>       \"text\":\"string\",<br>       \"buttons\":[<br>          {<br>             \"type\":\"replyButton\",<br>             \"title\":\"This is a replyButton\"<br>          },<br>          {<br>             \"type\":\"urlButton\",<br>             \"title\":\"This is a urlButton\",<br>             \"payload\":\"https://google.com\"<br>          },<br>          {<br>             \"type\":\"callButton\",<br>             \"title\":\"This is a callButton\",<br>             \"payload\":\"918788889688\"<br>          }<br>       ],<br>       \"footerText\":\"Hello World\"<br>    }<br> }<br>     </code>     <br>     <strong>NOTE: </strong>     <i>Due to certain limitations from WhatsApp, when you send templateMessage to someone, <br>     the message won't be visible in you phone. Also you will also see that the message has been sent <br>     too your own phone number.<br>     </i> 

### Example


```python
import time
import openapi_client
from openapi_client.api import send_message_controller_api
from openapi_client.model.send_message_controller_send_buttons_message_with_media_request import SendMessageControllerSendButtonsMessageWithMediaRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = send_message_controller_api.SendMessageControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    send_message_controller_send_buttons_message_with_media_request = SendMessageControllerSendButtonsMessageWithMediaRequest(
        message_data=ButtonMessageWithImage(
            to="to_example",
            text="text_example",
            buttons=[
                Button(
                    type="type_example",
                    title="title_example",
                    payload="payload_example",
                ),
            ],
            footer_text="footer_text_example",
            image_url="image_url_example",
            media_type="media_type_example",
            mime_type="mime_type_example",
        ),
    ) # SendMessageControllerSendButtonsMessageWithMediaRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an interactive template message with mediaHeader to an WhatsApp User
        api_instance.send_message_controller_send_buttons_message_with_media(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_buttons_message_with_media: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an interactive template message with mediaHeader to an WhatsApp User
        api_instance.send_message_controller_send_buttons_message_with_media(instance_key, send_message_controller_send_buttons_message_with_media_request=send_message_controller_send_buttons_message_with_media_request)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_buttons_message_with_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **send_message_controller_send_buttons_message_with_media_request** | [**SendMessageControllerSendButtonsMessageWithMediaRequest**](SendMessageControllerSendButtonsMessageWithMediaRequest.md)|  | [optional]

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

# **send_message_controller_send_document_message**
> send_message_controller_send_document_message(instance_key)

Send an document to an WhatsApp User

### Example


```python
import time
import openapi_client
from openapi_client.api import send_message_controller_api
from openapi_client.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = send_message_controller_api.SendMessageControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    id = "id_example" # str |  (optional)
    caption = "caption_example" # str |  (optional)
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an document to an WhatsApp User
        api_instance.send_message_controller_send_document_message(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_document_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an document to an WhatsApp User
        api_instance.send_message_controller_send_document_message(instance_key, id=id, caption=caption, file=file)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_document_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **id** | **str**|  | [optional]
 **caption** | **str**|  | [optional]
 **file** | **file_type**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | &lt;File too long | Too many parts | Too many files | Field name too long | Field value too long | Too many fields | Unexpected field&gt;  [fieldName] Example: File too long file1 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message_controller_send_image_message**
> send_message_controller_send_image_message(instance_key)

Send an image message to an WhatsApp User

### Example


```python
import time
import openapi_client
from openapi_client.api import send_message_controller_api
from openapi_client.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = send_message_controller_api.SendMessageControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    id = "id_example" # str |  (optional)
    caption = "caption_example" # str |  (optional)
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an image message to an WhatsApp User
        api_instance.send_message_controller_send_image_message(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_image_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an image message to an WhatsApp User
        api_instance.send_message_controller_send_image_message(instance_key, id=id, caption=caption, file=file)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_image_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **id** | **str**|  | [optional]
 **caption** | **str**|  | [optional]
 **file** | **file_type**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | &lt;File too long | Too many parts | Too many files | Field name too long | Field value too long | Too many fields | Unexpected field&gt;  [fieldName] Example: File too long file1 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message_controller_send_list_message**
> send_message_controller_send_list_message(instance_key)

Send an vacard message to an WhatsApp User

### Example


```python
import time
import openapi_client
from openapi_client.api import send_message_controller_api
from openapi_client.model.send_message_controller_send_list_message_request import SendMessageControllerSendListMessageRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = send_message_controller_api.SendMessageControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    send_message_controller_send_list_message_request = SendMessageControllerSendListMessageRequest(
        message_data=SendListMessageData(
            to="to_example",
            button_text="button_text_example",
            text="text_example",
            title="title_example",
            description="description_example",
            sections=[
                ListSection(
                    title="title_example",
                    rows=[
                        ListRow(
                            title="title_example",
                            description="description_example",
                            row_id="row_id_example",
                        ),
                    ],
                ),
            ],
            list_type=3.14,
        ),
    ) # SendMessageControllerSendListMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an vacard message to an WhatsApp User
        api_instance.send_message_controller_send_list_message(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_list_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an vacard message to an WhatsApp User
        api_instance.send_message_controller_send_list_message(instance_key, send_message_controller_send_list_message_request=send_message_controller_send_list_message_request)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_list_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **send_message_controller_send_list_message_request** | [**SendMessageControllerSendListMessageRequest**](SendMessageControllerSendListMessageRequest.md)|  | [optional]

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

# **send_message_controller_send_location_message**
> send_message_controller_send_location_message(instance_key)

Send an location to an WhatsApp User

### Example


```python
import time
import openapi_client
from openapi_client.api import send_message_controller_api
from openapi_client.model.send_message_controller_send_location_message_request import SendMessageControllerSendLocationMessageRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = send_message_controller_api.SendMessageControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    send_message_controller_send_location_message_request = SendMessageControllerSendLocationMessageRequest(
        message_data=LocationMessage(
            to="to_example",
            caption="caption_example",
            coordinates=LocationCordinates(
                lat=3.14,
                long=3.14,
            ),
        ),
    ) # SendMessageControllerSendLocationMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an location to an WhatsApp User
        api_instance.send_message_controller_send_location_message(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_location_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an location to an WhatsApp User
        api_instance.send_message_controller_send_location_message(instance_key, send_message_controller_send_location_message_request=send_message_controller_send_location_message_request)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_location_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **send_message_controller_send_location_message_request** | [**SendMessageControllerSendLocationMessageRequest**](SendMessageControllerSendLocationMessageRequest.md)|  | [optional]

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

# **send_message_controller_send_media_url**
> send_message_controller_send_media_url(instance_key)

Send a media message via a URL

The this endpoint allows you to send a media URL to a user. <br>  The <strong>url</strong> parameter is the URL of the media to be sent. <br> The <strong>to</strong> parameter is the phone number of the user to send the media to. <br> The <strong>type</strong> parameter is the type of media to be sent. <br> The type of media can be one of the following: <ul> <li><strong>image</strong> - an image</li> <li><strong>video</strong> - a video</li> <li><strong>audio</strong> - an audio file</li> <li><strong>document</strong> - a document</li> </ul> <br> The <strong>caption</strong> parameter is the caption of the media to be sent. <br> The <strong>mimeType</strong> parameter is the mimeType of the media. 

### Example


```python
import time
import openapi_client
from openapi_client.api import send_message_controller_api
from openapi_client.model.send_message_controller_send_media_url_request import SendMessageControllerSendMediaUrlRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = send_message_controller_api.SendMessageControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    send_message_controller_send_media_url_request = SendMessageControllerSendMediaUrlRequest(
        message_data=MediaUrlMessage(
            to="to_example",
            url="url_example",
            type="type_example",
            caption="caption_example",
            mime_type="mime_type_example",
        ),
    ) # SendMessageControllerSendMediaUrlRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a media message via a URL
        api_instance.send_message_controller_send_media_url(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_media_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a media message via a URL
        api_instance.send_message_controller_send_media_url(instance_key, send_message_controller_send_media_url_request=send_message_controller_send_media_url_request)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_media_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **send_message_controller_send_media_url_request** | [**SendMessageControllerSendMediaUrlRequest**](SendMessageControllerSendMediaUrlRequest.md)|  | [optional]

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

# **send_message_controller_send_template_messsage**
> send_message_controller_send_template_messsage(instance_key)

Send an vacard message to an WhatsApp User

### Example


```python
import time
import openapi_client
from openapi_client.api import send_message_controller_api
from openapi_client.model.send_message_controller_send_template_messsage_request import SendMessageControllerSendTemplateMesssageRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = send_message_controller_api.SendMessageControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    send_message_controller_send_template_messsage_request = SendMessageControllerSendTemplateMesssageRequest(
        message_data=SendVCardData(
            to="to_example",
            vcard=ContactData(
                full_name="full_name_example",
                display_name="display_name_example",
                organization="organization_example",
                phone_number="phone_number_example",
            ),
        ),
    ) # SendMessageControllerSendTemplateMesssageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an vacard message to an WhatsApp User
        api_instance.send_message_controller_send_template_messsage(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_template_messsage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an vacard message to an WhatsApp User
        api_instance.send_message_controller_send_template_messsage(instance_key, send_message_controller_send_template_messsage_request=send_message_controller_send_template_messsage_request)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_template_messsage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **send_message_controller_send_template_messsage_request** | [**SendMessageControllerSendTemplateMesssageRequest**](SendMessageControllerSendTemplateMesssageRequest.md)|  | [optional]

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

# **send_message_controller_send_text_message**
> send_message_controller_send_text_message(instance_key)

Send a text message to multiple WhatsApp users

Note that while sending to single chat, the id should not contain @s.whatsapp.net. <br>     However, while sending to groups, the id should end with @g.us <br>     

### Example


```python
import time
import openapi_client
from openapi_client.api import send_message_controller_api
from openapi_client.model.send_message_controller_send_text_message_request import SendMessageControllerSendTextMessageRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = send_message_controller_api.SendMessageControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    send_message_controller_send_text_message_request = SendMessageControllerSendTextMessageRequest(
        message_data=TextMessge(
            to=[
                "to_example",
            ],
            text="text_example",
        ),
    ) # SendMessageControllerSendTextMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a text message to multiple WhatsApp users
        api_instance.send_message_controller_send_text_message(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_text_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a text message to multiple WhatsApp users
        api_instance.send_message_controller_send_text_message(instance_key, send_message_controller_send_text_message_request=send_message_controller_send_text_message_request)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_text_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **send_message_controller_send_text_message_request** | [**SendMessageControllerSendTextMessageRequest**](SendMessageControllerSendTextMessageRequest.md)|  | [optional]

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

# **send_message_controller_send_text_message_to_single_user**
> send_message_controller_send_text_message_to_single_user(instance_key)

Send a text message to an WhatsApp User

Note that while sending to single chat, the id should not contain @s.whatsapp.net. <br>     However, while sending to groups, the id should end with @g.us <br>     

### Example


```python
import time
import openapi_client
from openapi_client.api import send_message_controller_api
from openapi_client.model.send_message_controller_send_text_message_to_single_user_request import SendMessageControllerSendTextMessageToSingleUserRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = send_message_controller_api.SendMessageControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    send_message_controller_send_text_message_to_single_user_request = SendMessageControllerSendTextMessageToSingleUserRequest(
        message_data=TextMessgeSingle(
            to="to_example",
            text="text_example",
        ),
    ) # SendMessageControllerSendTextMessageToSingleUserRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a text message to an WhatsApp User
        api_instance.send_message_controller_send_text_message_to_single_user(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_text_message_to_single_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a text message to an WhatsApp User
        api_instance.send_message_controller_send_text_message_to_single_user(instance_key, send_message_controller_send_text_message_to_single_user_request=send_message_controller_send_text_message_to_single_user_request)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_text_message_to_single_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **send_message_controller_send_text_message_to_single_user_request** | [**SendMessageControllerSendTextMessageToSingleUserRequest**](SendMessageControllerSendTextMessageToSingleUserRequest.md)|  | [optional]

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

# **send_message_controller_send_video_message**
> send_message_controller_send_video_message(instance_key)

Send an video to an WhatsApp User

### Example


```python
import time
import openapi_client
from openapi_client.api import send_message_controller_api
from openapi_client.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = send_message_controller_api.SendMessageControllerApi(api_client)
    instance_key = "instance_key_example" # str | 
    id = "id_example" # str |  (optional)
    caption = "caption_example" # str |  (optional)
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an video to an WhatsApp User
        api_instance.send_message_controller_send_video_message(instance_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_video_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an video to an WhatsApp User
        api_instance.send_message_controller_send_video_message(instance_key, id=id, caption=caption, file=file)
    except openapi_client.ApiException as e:
        print("Exception when calling SendMessageControllerApi->send_message_controller_send_video_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_key** | **str**|  |
 **id** | **str**|  | [optional]
 **caption** | **str**|  | [optional]
 **file** | **file_type**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | &lt;File too long | Too many parts | Too many files | Field name too long | Field value too long | Too many fields | Unexpected field&gt;  [fieldName] Example: File too long file1 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

