"""
    Api documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.webhook_controller_enable_message_webhook_request import WebhookControllerEnableMessageWebhookRequest
from openapi_client.model.webhook_controller_update_webhook_url_request import WebhookControllerUpdateWebhookUrlRequest


class WebhookControllerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.webhook_controller_enable_message_webhook_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/rest/webhook/{instance_key}/enableMessage',
                'operation_id': 'webhook_controller_enable_message_webhook',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'instance_key',
                    'webhook_controller_enable_message_webhook_request',
                ],
                'required': [
                    'instance_key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'instance_key':
                        (str,),
                    'webhook_controller_enable_message_webhook_request':
                        (WebhookControllerEnableMessageWebhookRequest,),
                },
                'attribute_map': {
                    'instance_key': 'instance_key',
                },
                'location_map': {
                    'instance_key': 'path',
                    'webhook_controller_enable_message_webhook_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.webhook_controller_get_webhook_stauts_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/rest/webhook/{instance_key}',
                'operation_id': 'webhook_controller_get_webhook_stauts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'instance_key',
                ],
                'required': [
                    'instance_key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'instance_key':
                        (str,),
                },
                'attribute_map': {
                    'instance_key': 'instance_key',
                },
                'location_map': {
                    'instance_key': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.webhook_controller_update_webhook_url_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/rest/webhook/{instance_key}/updateUrl',
                'operation_id': 'webhook_controller_update_webhook_url',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'instance_key',
                    'webhook_controller_update_webhook_url_request',
                ],
                'required': [
                    'instance_key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'instance_key':
                        (str,),
                    'webhook_controller_update_webhook_url_request':
                        (WebhookControllerUpdateWebhookUrlRequest,),
                },
                'attribute_map': {
                    'instance_key': 'instance_key',
                },
                'location_map': {
                    'instance_key': 'path',
                    'webhook_controller_update_webhook_url_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def webhook_controller_enable_message_webhook(
        self,
        instance_key,
        **kwargs
    ):
        """webhook_controller_enable_message_webhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.webhook_controller_enable_message_webhook(instance_key, async_req=True)
        >>> result = thread.get()

        Args:
            instance_key (str):

        Keyword Args:
            webhook_controller_enable_message_webhook_request (WebhookControllerEnableMessageWebhookRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['instance_key'] = \
            instance_key
        return self.webhook_controller_enable_message_webhook_endpoint.call_with_http_info(**kwargs)

    def webhook_controller_get_webhook_stauts(
        self,
        instance_key,
        **kwargs
    ):
        """Get an instance webhook data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.webhook_controller_get_webhook_stauts(instance_key, async_req=True)
        >>> result = thread.get()

        Args:
            instance_key (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['instance_key'] = \
            instance_key
        return self.webhook_controller_get_webhook_stauts_endpoint.call_with_http_info(**kwargs)

    def webhook_controller_update_webhook_url(
        self,
        instance_key,
        **kwargs
    ):
        """webhook_controller_update_webhook_url  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.webhook_controller_update_webhook_url(instance_key, async_req=True)
        >>> result = thread.get()

        Args:
            instance_key (str):

        Keyword Args:
            webhook_controller_update_webhook_url_request (WebhookControllerUpdateWebhookUrlRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['instance_key'] = \
            instance_key
        return self.webhook_controller_update_webhook_url_endpoint.call_with_http_info(**kwargs)
