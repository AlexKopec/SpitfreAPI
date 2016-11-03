# coding: utf-8

"""
    spitfire API

    spitfire API documentation

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class MaterialattachmentresourceApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_material_attachment_using_post(self, material_attachment_dto, **kwargs):
        """
        createMaterialAttachment
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_material_attachment_using_post(material_attachment_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MaterialAttachmentDTO material_attachment_dto: materialAttachmentDTO (required)
        :return: MaterialAttachmentDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_material_attachment_using_post_with_http_info(material_attachment_dto, **kwargs)
        else:
            (data) = self.create_material_attachment_using_post_with_http_info(material_attachment_dto, **kwargs)
            return data

    def create_material_attachment_using_post_with_http_info(self, material_attachment_dto, **kwargs):
        """
        createMaterialAttachment
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_material_attachment_using_post_with_http_info(material_attachment_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MaterialAttachmentDTO material_attachment_dto: materialAttachmentDTO (required)
        :return: MaterialAttachmentDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['material_attachment_dto']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_material_attachment_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'material_attachment_dto' is set
        if ('material_attachment_dto' not in params) or (params['material_attachment_dto'] is None):
            raise ValueError("Missing the required parameter `material_attachment_dto` when calling `create_material_attachment_using_post`")


        collection_formats = {}

        resource_path = '/api/material-attachments'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'material_attachment_dto' in params:
            body_params = params['material_attachment_dto']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MaterialAttachmentDTO',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def delete_material_attachment_using_delete(self, id, **kwargs):
        """
        deleteMaterialAttachment
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_material_attachment_using_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_material_attachment_using_delete_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_material_attachment_using_delete_with_http_info(id, **kwargs)
            return data

    def delete_material_attachment_using_delete_with_http_info(self, id, **kwargs):
        """
        deleteMaterialAttachment
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_material_attachment_using_delete_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_material_attachment_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_material_attachment_using_delete`")


        collection_formats = {}

        resource_path = '/api/material-attachments/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def get_all_material_attachments_using_get(self, **kwargs):
        """
        getAllMaterialAttachments
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_material_attachments_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[MaterialAttachmentDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_material_attachments_using_get_with_http_info(**kwargs)
        else:
            (data) = self.get_all_material_attachments_using_get_with_http_info(**kwargs)
            return data

    def get_all_material_attachments_using_get_with_http_info(self, **kwargs):
        """
        getAllMaterialAttachments
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_material_attachments_using_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[MaterialAttachmentDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_material_attachments_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/api/material-attachments'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[MaterialAttachmentDTO]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def get_material_attachment_using_get(self, id, **kwargs):
        """
        getMaterialAttachment
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_material_attachment_using_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id (required)
        :return: MaterialAttachmentDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_material_attachment_using_get_with_http_info(id, **kwargs)
        else:
            (data) = self.get_material_attachment_using_get_with_http_info(id, **kwargs)
            return data

    def get_material_attachment_using_get_with_http_info(self, id, **kwargs):
        """
        getMaterialAttachment
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_material_attachment_using_get_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id (required)
        :return: MaterialAttachmentDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_material_attachment_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_material_attachment_using_get`")


        collection_formats = {}

        resource_path = '/api/material-attachments/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MaterialAttachmentDTO',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def search_material_attachments_using_get(self, query, **kwargs):
        """
        searchMaterialAttachments
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_material_attachments_using_get(query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query: query (required)
        :return: list[MaterialAttachmentDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.search_material_attachments_using_get_with_http_info(query, **kwargs)
        else:
            (data) = self.search_material_attachments_using_get_with_http_info(query, **kwargs)
            return data

    def search_material_attachments_using_get_with_http_info(self, query, **kwargs):
        """
        searchMaterialAttachments
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_material_attachments_using_get_with_http_info(query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str query: query (required)
        :return: list[MaterialAttachmentDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_material_attachments_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search_material_attachments_using_get`")


        collection_formats = {}

        resource_path = '/api/_search/material-attachments'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'query' in params:
            query_params['query'] = params['query']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[MaterialAttachmentDTO]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def update_material_attachment_using_put(self, material_attachment_dto, **kwargs):
        """
        updateMaterialAttachment
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_material_attachment_using_put(material_attachment_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MaterialAttachmentDTO material_attachment_dto: materialAttachmentDTO (required)
        :return: MaterialAttachmentDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_material_attachment_using_put_with_http_info(material_attachment_dto, **kwargs)
        else:
            (data) = self.update_material_attachment_using_put_with_http_info(material_attachment_dto, **kwargs)
            return data

    def update_material_attachment_using_put_with_http_info(self, material_attachment_dto, **kwargs):
        """
        updateMaterialAttachment
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_material_attachment_using_put_with_http_info(material_attachment_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MaterialAttachmentDTO material_attachment_dto: materialAttachmentDTO (required)
        :return: MaterialAttachmentDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['material_attachment_dto']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_material_attachment_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'material_attachment_dto' is set
        if ('material_attachment_dto' not in params) or (params['material_attachment_dto'] is None):
            raise ValueError("Missing the required parameter `material_attachment_dto` when calling `update_material_attachment_using_put`")


        collection_formats = {}

        resource_path = '/api/material-attachments'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'material_attachment_dto' in params:
            body_params = params['material_attachment_dto']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MaterialAttachmentDTO',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)
