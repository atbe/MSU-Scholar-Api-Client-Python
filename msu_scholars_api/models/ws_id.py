# coding: utf-8

"""
    Pure API 511

    This is the Pure Web Service. Listed below are all available endpoints, along with a short description.<br/><br/>In order to use the Pure Web Service, you must enter an API key. These are generated in the Administrator tab of Pure, and issued with a given set of available endpoints.<br/>To enter your API key and begin your use, press the 'Authorize' button to at the top of this page. <br/>You are then presented with two options for entering the API key: <ol><li>Use the API key in query format.</li><li>Use the API key in a header.</li><br/> For further documentation, see <a href=\"documentation/Default.htm\">API Documentation</a>.<br/><br/>A new version of the API is released with each major version of Pure, and remains available for one year. This version is no longer available in Pure 5.15.<br/>The old web service is deprecated, but still available <a href=\"../../../doc/\">here</a>, and it will no longer be available in Pure 5.13.

    OpenAPI spec version: 511
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WSId(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'id_source': 'str'
    }

    attribute_map = {
        'id': 'id',
        'id_source': 'idSource'
    }

    def __init__(self, id=None, id_source=None):
        """
        WSId - a model defined in Swagger
        """

        self._id = None
        self._id_source = None

        if id is not None:
          self.id = id
        if id_source is not None:
          self.id_source = id_source

    @property
    def id(self):
        """
        Gets the id of this WSId.

        :return: The id of this WSId.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WSId.

        :param id: The id of this WSId.
        :type: str
        """

        self._id = id

    @property
    def id_source(self):
        """
        Gets the id_source of this WSId.

        :return: The id_source of this WSId.
        :rtype: str
        """
        return self._id_source

    @id_source.setter
    def id_source(self, id_source):
        """
        Sets the id_source of this WSId.

        :param id_source: The id_source of this WSId.
        :type: str
        """

        self._id_source = id_source

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, WSId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
