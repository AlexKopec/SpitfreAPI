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

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.marketplaceserviceresource_api import MarketplaceserviceresourceApi


class TestMarketplaceserviceresourceApi(unittest.TestCase):
    """ MarketplaceserviceresourceApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.marketplaceserviceresource_api.MarketplaceserviceresourceApi()

    def tearDown(self):
        pass

    def test_create_marketplace_service_using_post(self):
        """
        Test case for create_marketplace_service_using_post

        createMarketplaceService
        """
        pass

    def test_delete_marketplace_service_using_delete(self):
        """
        Test case for delete_marketplace_service_using_delete

        deleteMarketplaceService
        """
        pass

    def test_get_all_marketplace_services_using_get(self):
        """
        Test case for get_all_marketplace_services_using_get

        getAllMarketplaceServices
        """
        pass

    def test_get_marketplace_service_using_get(self):
        """
        Test case for get_marketplace_service_using_get

        getMarketplaceService
        """
        pass

    def test_update_marketplace_service_using_put(self):
        """
        Test case for update_marketplace_service_using_put

        updateMarketplaceService
        """
        pass


if __name__ == '__main__':
    unittest.main()
