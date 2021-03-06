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
from swagger_client.apis.materialattachmentresource_api import MaterialattachmentresourceApi


class TestMaterialattachmentresourceApi(unittest.TestCase):
    """ MaterialattachmentresourceApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.materialattachmentresource_api.MaterialattachmentresourceApi()

    def tearDown(self):
        pass

    def test_create_material_attachment_using_post(self):
        """
        Test case for create_material_attachment_using_post

        createMaterialAttachment
        """
        pass

    def test_delete_material_attachment_using_delete(self):
        """
        Test case for delete_material_attachment_using_delete

        deleteMaterialAttachment
        """
        pass

    def test_get_all_material_attachments_using_get(self):
        """
        Test case for get_all_material_attachments_using_get

        getAllMaterialAttachments
        """
        pass

    def test_get_material_attachment_using_get(self):
        """
        Test case for get_material_attachment_using_get

        getMaterialAttachment
        """
        pass

    def test_search_material_attachments_using_get(self):
        """
        Test case for search_material_attachments_using_get

        searchMaterialAttachments
        """
        pass

    def test_update_material_attachment_using_put(self):
        """
        Test case for update_material_attachment_using_put

        updateMaterialAttachment
        """
        pass


if __name__ == '__main__':
    unittest.main()
