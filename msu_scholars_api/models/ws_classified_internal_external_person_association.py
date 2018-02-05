# coding: utf-8

"""
    PURE API 510

    This is the Pure Web Service. Listed below are all available endpoints, along with a short description.<br/>In order to use the Pure Web Service, you must enter an API key. These are generated in the Administrator tab of Pure, and issues with a given set of available endpoints.<br/>To enter your API key and begin your use, press the Authorize button to at the top of the page. You are then presented with two options for entering the API key: the first option is to use the API key in query format, and the second option is to use the API key in a header.<br/> For further documentation, see <a href=\"documentation/Default.htm\">API Documentation</a>.<br/>A new version of the API is released with each major version of Pure, and remains available for one year. This version is no longer available in Pure 5.14<br/>The old web service is deprecated, but still available <a href=\"../../../doc/\">here</a>, and it will no longer be available in Pure 5.13

    OpenAPI spec version: 510
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WSClassifiedInternalExternalPersonAssociation(object):
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
        'id': 'int',
        'person_roles': 'list[WSClassification]',
        'person': 'WSPersonRef',
        'external_person': 'WSExternalPersonRef'
    }

    attribute_map = {
        'id': 'id',
        'person_roles': 'personRoles',
        'person': 'person',
        'external_person': 'externalPerson'
    }

    def __init__(self, id=None, person_roles=None, person=None, external_person=None):
        """
        WSClassifiedInternalExternalPersonAssociation - a model defined in Swagger
        """

        self._id = None
        self._person_roles = None
        self._person = None
        self._external_person = None

        if id is not None:
          self.id = id
        if person_roles is not None:
          self.person_roles = person_roles
        if person is not None:
          self.person = person
        if external_person is not None:
          self.external_person = external_person

    @property
    def id(self):
        """
        Gets the id of this WSClassifiedInternalExternalPersonAssociation.

        :return: The id of this WSClassifiedInternalExternalPersonAssociation.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WSClassifiedInternalExternalPersonAssociation.

        :param id: The id of this WSClassifiedInternalExternalPersonAssociation.
        :type: int
        """

        self._id = id

    @property
    def person_roles(self):
        """
        Gets the person_roles of this WSClassifiedInternalExternalPersonAssociation.

        :return: The person_roles of this WSClassifiedInternalExternalPersonAssociation.
        :rtype: list[WSClassification]
        """
        return self._person_roles

    @person_roles.setter
    def person_roles(self, person_roles):
        """
        Sets the person_roles of this WSClassifiedInternalExternalPersonAssociation.

        :param person_roles: The person_roles of this WSClassifiedInternalExternalPersonAssociation.
        :type: list[WSClassification]
        """

        self._person_roles = person_roles

    @property
    def person(self):
        """
        Gets the person of this WSClassifiedInternalExternalPersonAssociation.

        :return: The person of this WSClassifiedInternalExternalPersonAssociation.
        :rtype: WSPersonRef
        """
        return self._person

    @person.setter
    def person(self, person):
        """
        Sets the person of this WSClassifiedInternalExternalPersonAssociation.

        :param person: The person of this WSClassifiedInternalExternalPersonAssociation.
        :type: WSPersonRef
        """

        self._person = person

    @property
    def external_person(self):
        """
        Gets the external_person of this WSClassifiedInternalExternalPersonAssociation.

        :return: The external_person of this WSClassifiedInternalExternalPersonAssociation.
        :rtype: WSExternalPersonRef
        """
        return self._external_person

    @external_person.setter
    def external_person(self, external_person):
        """
        Sets the external_person of this WSClassifiedInternalExternalPersonAssociation.

        :param external_person: The external_person of this WSClassifiedInternalExternalPersonAssociation.
        :type: WSExternalPersonRef
        """

        self._external_person = external_person

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
        if not isinstance(other, WSClassifiedInternalExternalPersonAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other