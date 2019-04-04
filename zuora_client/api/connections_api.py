# coding: utf-8




from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from zuora_client.api_client import ApiClient


class ConnectionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def p_ost_connections(self, api_access_key_id, api_secret_access_key, content_type, **kwargs):  # noqa: E501
        """Establish connection to Zuora REST API service  # noqa: E501

        Establishes a connection to the Zuora REST API service based on a valid user credentials.   **Note:**This is a legacy REST API. Zuora recommends you to use [OAuth](https://www.zuora.com/developer/api-reference/#section/Authentication/OAuth-v2.0) for authentication instead.   This call authenticates the user and returns an API session cookie that's used to authorize subsequent calls to the REST API. The credentials must belong to a user account that has permission to access the API service.  As noted elsewhere, it's strongly recommended that an account used for Zuora API activity is never used to log into the Zuora UI.  Once an account is used to log into the UI, it may be subject to periodic forced password changes, which may eventually lead to authentication failures when using the API.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_connections(api_access_key_id, api_secret_access_key, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_access_key_id: Account username  (required)
        :param str api_secret_access_key: Account password  (required)
        :param str content_type: Must be set to \"application/json\"  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ost_connections_with_http_info(api_access_key_id, api_secret_access_key, content_type, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ost_connections_with_http_info(api_access_key_id, api_secret_access_key, content_type, **kwargs)  # noqa: E501
            return data

    def p_ost_connections_with_http_info(self, api_access_key_id, api_secret_access_key, content_type, **kwargs):  # noqa: E501
        """Establish connection to Zuora REST API service  # noqa: E501

        Establishes a connection to the Zuora REST API service based on a valid user credentials.   **Note:**This is a legacy REST API. Zuora recommends you to use [OAuth](https://www.zuora.com/developer/api-reference/#section/Authentication/OAuth-v2.0) for authentication instead.   This call authenticates the user and returns an API session cookie that's used to authorize subsequent calls to the REST API. The credentials must belong to a user account that has permission to access the API service.  As noted elsewhere, it's strongly recommended that an account used for Zuora API activity is never used to log into the Zuora UI.  Once an account is used to log into the UI, it may be subject to periodic forced password changes, which may eventually lead to authentication failures when using the API.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_connections_with_http_info(api_access_key_id, api_secret_access_key, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_access_key_id: Account username  (required)
        :param str api_secret_access_key: Account password  (required)
        :param str content_type: Must be set to \"application/json\"  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_access_key_id', 'api_secret_access_key', 'content_type', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_connections" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_access_key_id' is set
        if ('api_access_key_id' not in params or
                params['api_access_key_id'] is None):
            raise ValueError("Missing the required parameter `api_access_key_id` when calling `p_ost_connections`")  # noqa: E501
        # verify the required parameter 'api_secret_access_key' is set
        if ('api_secret_access_key' not in params or
                params['api_secret_access_key'] is None):
            raise ValueError("Missing the required parameter `api_secret_access_key` when calling `p_ost_connections`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `p_ost_connections`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501
        if 'api_access_key_id' in params:
            header_params['apiAccessKeyId'] = params['api_access_key_id']  # noqa: E501
        if 'api_secret_access_key' in params:
            header_params['apiSecretAccessKey'] = params['api_secret_access_key']  # noqa: E501
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/connections', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
