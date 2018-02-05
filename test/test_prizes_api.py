# coding: utf-8

"""
    PURE API 510

    This is the Pure Web Service. Listed below are all available endpoints, along with a short description.<br/>In order to use the Pure Web Service, you must enter an API key. These are generated in the Administrator tab of Pure, and issues with a given set of available endpoints.<br/>To enter your API key and begin your use, press the Authorize button to at the top of the page. You are then presented with two options for entering the API key: the first option is to use the API key in query format, and the second option is to use the API key in a header.<br/> For further documentation, see <a href=\"documentation/Default.htm\">API Documentation</a>.<br/>A new version of the API is released with each major version of Pure, and remains available for one year. This version is no longer available in Pure 5.14<br/>The old web service is deprecated, but still available <a href=\"../../../doc/\">here</a>, and it will no longer be available in Pure 5.13

    OpenAPI spec version: 510
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import msu_scholars_api
from msu_scholars_api.rest import ApiException
from msu_scholars_api.apis.prizes_api import PrizesApi


class TestPrizesApi(unittest.TestCase):
    """ PrizesApi unit test stubs """

    def setUp(self):
        self.api = msu_scholars_api.apis.prizes_api.PrizesApi()

    def tearDown(self):
        pass

    def test_get_available_orderings(self):
        """
        Test case for get_available_orderings

        Lists available orderings
        """
        pass

    def test_get_available_renderings(self):
        """
        Test case for get_available_renderings

        Lists available renderings
        """
        pass

    def test_get_prize(self):
        """
        Test case for get_prize

        Get prize
        """
        pass

    def test_list_prizes(self):
        """
        Test case for list_prizes

        Lists all prizes
        """
        pass

    def test_list_prizes_0(self):
        """
        Test case for list_prizes_0

        Complex operation for prizes
        """
        pass


if __name__ == '__main__':
    unittest.main()
