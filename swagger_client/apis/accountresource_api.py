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


class AccountresourceApi(object):
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

    def activate_account_using_get(self, key, **kwargs):
        """
        activateAccount
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.activate_account_using_get(key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key: key (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.activate_account_using_get_with_http_info(key, **kwargs)
        else:
            (data) = self.activate_account_using_get_with_http_info(key, **kwargs)
            return data

    def activate_account_using_get_with_http_info(self, key, **kwargs):
        """
        activateAccount
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.activate_account_using_get_with_http_info(key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key: key (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method activate_account_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if ('key' not in params) or (params['key'] is None):
            raise ValueError("Missing the required parameter `key` when calling `activate_account_using_get`")


        collection_formats = {}

        resource_path = '/api/activate'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'key' in params:
            query_params['key'] = params['key']

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
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def change_password_using_post(self, password, **kwargs):
        """
        changePassword
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.change_password_using_post(password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str password: password (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.change_password_using_post_with_http_info(password, **kwargs)
        else:
            (data) = self.change_password_using_post_with_http_info(password, **kwargs)
            return data

    def change_password_using_post_with_http_info(self, password, **kwargs):
        """
        changePassword
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.change_password_using_post_with_http_info(password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str password: password (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['password']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_password_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'password' is set
        if ('password' not in params) or (params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `change_password_using_post`")


        collection_formats = {}

        resource_path = '/api/account/change_password'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'password' in params:
            body_params = params['password']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain'])
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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def finish_password_reset_using_post(self, key_and_password, **kwargs):
        """
        finishPasswordReset
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.finish_password_reset_using_post(key_and_password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param KeyAndPasswordDTO key_and_password: keyAndPassword (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.finish_password_reset_using_post_with_http_info(key_and_password, **kwargs)
        else:
            (data) = self.finish_password_reset_using_post_with_http_info(key_and_password, **kwargs)
            return data

    def finish_password_reset_using_post_with_http_info(self, key_and_password, **kwargs):
        """
        finishPasswordReset
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.finish_password_reset_using_post_with_http_info(key_and_password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param KeyAndPasswordDTO key_and_password: keyAndPassword (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_and_password']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method finish_password_reset_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_and_password' is set
        if ('key_and_password' not in params) or (params['key_and_password'] is None):
            raise ValueError("Missing the required parameter `key_and_password` when calling `finish_password_reset_using_post`")


        collection_formats = {}

        resource_path = '/api/account/reset_password/finish'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'key_and_password' in params:
            body_params = params['key_and_password']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain'])
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
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def get_account_using_get(self, **kwargs):
        """
        getAccount
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: UserDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_account_using_get_with_http_info(**kwargs)
        else:
            (data) = self.get_account_using_get_with_http_info(**kwargs)
            return data

    def get_account_using_get_with_http_info(self, **kwargs):
        """
        getAccount
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_using_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: UserDTO
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
                    " to method get_account_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/api/account'.replace('{format}', 'json')
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
                                            response_type='UserDTO',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def is_authenticated_using_get(self, **kwargs):
        """
        isAuthenticated
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.is_authenticated_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.is_authenticated_using_get_with_http_info(**kwargs)
        else:
            (data) = self.is_authenticated_using_get_with_http_info(**kwargs)
            return data

    def is_authenticated_using_get_with_http_info(self, **kwargs):
        """
        isAuthenticated
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.is_authenticated_using_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: str
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
                    " to method is_authenticated_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/api/authenticate'.replace('{format}', 'json')
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
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def register_account_using_post(self, managed_user_dto, **kwargs):
        """
        registerAccount
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.register_account_using_post(managed_user_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ManagedUserDTO managed_user_dto: managedUserDTO (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.register_account_using_post_with_http_info(managed_user_dto, **kwargs)
        else:
            (data) = self.register_account_using_post_with_http_info(managed_user_dto, **kwargs)
            return data

    def register_account_using_post_with_http_info(self, managed_user_dto, **kwargs):
        """
        registerAccount
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.register_account_using_post_with_http_info(managed_user_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ManagedUserDTO managed_user_dto: managedUserDTO (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['managed_user_dto']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register_account_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'managed_user_dto' is set
        if ('managed_user_dto' not in params) or (params['managed_user_dto'] is None):
            raise ValueError("Missing the required parameter `managed_user_dto` when calling `register_account_using_post`")


        collection_formats = {}

        resource_path = '/api/register'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'managed_user_dto' in params:
            body_params = params['managed_user_dto']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/plain'])
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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def request_password_reset_using_post(self, mail, **kwargs):
        """
        requestPasswordReset
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.request_password_reset_using_post(mail, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str mail: mail (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.request_password_reset_using_post_with_http_info(mail, **kwargs)
        else:
            (data) = self.request_password_reset_using_post_with_http_info(mail, **kwargs)
            return data

    def request_password_reset_using_post_with_http_info(self, mail, **kwargs):
        """
        requestPasswordReset
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.request_password_reset_using_post_with_http_info(mail, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str mail: mail (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mail']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_password_reset_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mail' is set
        if ('mail' not in params) or (params['mail'] is None):
            raise ValueError("Missing the required parameter `mail` when calling `request_password_reset_using_post`")


        collection_formats = {}

        resource_path = '/api/account/reset_password/init'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'mail' in params:
            body_params = params['mail']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain'])
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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)

    def save_account_using_post(self, user_dto, **kwargs):
        """
        saveAccount
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.save_account_using_post(user_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserDTO user_dto: userDTO (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.save_account_using_post_with_http_info(user_dto, **kwargs)
        else:
            (data) = self.save_account_using_post_with_http_info(user_dto, **kwargs)
            return data

    def save_account_using_post_with_http_info(self, user_dto, **kwargs):
        """
        saveAccount
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.save_account_using_post_with_http_info(user_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserDTO user_dto: userDTO (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_dto']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_account_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_dto' is set
        if ('user_dto' not in params) or (params['user_dto'] is None):
            raise ValueError("Missing the required parameter `user_dto` when calling `save_account_using_post`")


        collection_formats = {}

        resource_path = '/api/account'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_dto' in params:
            body_params = params['user_dto']

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
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            collection_formats=collection_formats)
