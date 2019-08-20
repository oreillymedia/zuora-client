# coding: utf-8




from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from zuora_client.api_client import ApiClient


class BillingPreviewRunApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_billing_preview_run(self, billing_preview_run_id, **kwargs):  # noqa: E501
        """Get Billing Preview Run  # noqa: E501

        **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).    Retrieves a preview of future invoice items for multiple customer accounts through a billing preview run. If you have the Invoice Settlement feature enabled,  you can also retrieve a preview of future credit memo items. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   A billing preview run asynchronously generates a downloadable CSV file containing a preview of invoice item data and credit memo item data for a batch of customer accounts.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_billing_preview_run(billing_preview_run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str billing_preview_run_id: Id of the billing preview run.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :return: GetBillingPreviewRunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_billing_preview_run_with_http_info(billing_preview_run_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_billing_preview_run_with_http_info(billing_preview_run_id, **kwargs)  # noqa: E501
            return data

    def get_billing_preview_run_with_http_info(self, billing_preview_run_id, **kwargs):  # noqa: E501
        """Get Billing Preview Run  # noqa: E501

        **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).    Retrieves a preview of future invoice items for multiple customer accounts through a billing preview run. If you have the Invoice Settlement feature enabled,  you can also retrieve a preview of future credit memo items. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   A billing preview run asynchronously generates a downloadable CSV file containing a preview of invoice item data and credit memo item data for a batch of customer accounts.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_billing_preview_run_with_http_info(billing_preview_run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str billing_preview_run_id: Id of the billing preview run.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :return: GetBillingPreviewRunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_preview_run_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_billing_preview_run" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'billing_preview_run_id' is set
        if ('billing_preview_run_id' not in params or
                params['billing_preview_run_id'] is None):
            raise ValueError("Missing the required parameter `billing_preview_run_id` when calling `get_billing_preview_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'billing_preview_run_id' in params:
            path_params['billingPreviewRunId'] = params['billing_preview_run_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

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
            '/v1/billing-preview-runs/{billingPreviewRunId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetBillingPreviewRunResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_billing_preview_run(self, request, **kwargs):  # noqa: E501
        """Create Billing Preview Run  # noqa: E501

        **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates billing preview runs for multiple customer accounts.  You can run up to 10 billing previews in batches concurrently. A single batch of customer accounts can only have one billing preview run at a time. So you can have up to 10 batches running at the same time. If you create a billing preview run for all customer batches, you cannot create another billing preview run until this preview run is completed.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_billing_preview_run(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostBillingPreviewRunParam request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_billing_preview_run_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.post_billing_preview_run_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_billing_preview_run_with_http_info(self, request, **kwargs):  # noqa: E501
        """Create Billing Preview Run  # noqa: E501

        **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates billing preview runs for multiple customer accounts.  You can run up to 10 billing previews in batches concurrently. A single batch of customer accounts can only have one billing preview run at a time. So you can have up to 10 batches running at the same time. If you create a billing preview run for all customer batches, you cannot create another billing preview run until this preview run is completed.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_billing_preview_run_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostBillingPreviewRunParam request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_billing_preview_run" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `post_billing_preview_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/billing-preview-runs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
