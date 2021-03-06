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


class WSApplicationFundingAssociation(object):
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
        'funder': 'WSExternalOrganisationRef',
        'funding_classifications': 'list[WSClassification]',
        'funding_project_scheme': 'str',
        'financial': 'bool',
        'estimated_value': 'float',
        'non_financial_description': 'str',
        'applied_amount_in_applied_currency': 'float',
        'applied_currencies': 'list[WSClassification]',
        'applied_amount': 'float',
        'institutional_estimated_value': 'float',
        'institutional_part': 'float',
        'institutional_contribution': 'float',
        'institutional_fec': 'float',
        'funding_collaborators': 'list[WSFundingCollaboratorAssociation]',
        'budget_and_expenditures': 'list[WSFundingExpenditureAssociation]',
        'visibilities': 'list[WSVisibility]',
        'fecpercentage': 'float'
    }

    attribute_map = {
        'id': 'id',
        'funder': 'funder',
        'funding_classifications': 'fundingClassifications',
        'funding_project_scheme': 'fundingProjectScheme',
        'financial': 'financial',
        'estimated_value': 'estimatedValue',
        'non_financial_description': 'nonFinancialDescription',
        'applied_amount_in_applied_currency': 'appliedAmountInAppliedCurrency',
        'applied_currencies': 'appliedCurrencies',
        'applied_amount': 'appliedAmount',
        'institutional_estimated_value': 'institutionalEstimatedValue',
        'institutional_part': 'institutionalPart',
        'institutional_contribution': 'institutionalContribution',
        'institutional_fec': 'institutionalFEC',
        'funding_collaborators': 'fundingCollaborators',
        'budget_and_expenditures': 'budgetAndExpenditures',
        'visibilities': 'visibilities',
        'fecpercentage': 'fecpercentage'
    }

    def __init__(self, id=None, funder=None, funding_classifications=None, funding_project_scheme=None, financial=False, estimated_value=None, non_financial_description=None, applied_amount_in_applied_currency=None, applied_currencies=None, applied_amount=None, institutional_estimated_value=None, institutional_part=None, institutional_contribution=None, institutional_fec=None, funding_collaborators=None, budget_and_expenditures=None, visibilities=None, fecpercentage=None):
        """
        WSApplicationFundingAssociation - a model defined in Swagger
        """

        self._id = None
        self._funder = None
        self._funding_classifications = None
        self._funding_project_scheme = None
        self._financial = None
        self._estimated_value = None
        self._non_financial_description = None
        self._applied_amount_in_applied_currency = None
        self._applied_currencies = None
        self._applied_amount = None
        self._institutional_estimated_value = None
        self._institutional_part = None
        self._institutional_contribution = None
        self._institutional_fec = None
        self._funding_collaborators = None
        self._budget_and_expenditures = None
        self._visibilities = None
        self._fecpercentage = None

        if id is not None:
          self.id = id
        if funder is not None:
          self.funder = funder
        if funding_classifications is not None:
          self.funding_classifications = funding_classifications
        if funding_project_scheme is not None:
          self.funding_project_scheme = funding_project_scheme
        if financial is not None:
          self.financial = financial
        if estimated_value is not None:
          self.estimated_value = estimated_value
        if non_financial_description is not None:
          self.non_financial_description = non_financial_description
        if applied_amount_in_applied_currency is not None:
          self.applied_amount_in_applied_currency = applied_amount_in_applied_currency
        if applied_currencies is not None:
          self.applied_currencies = applied_currencies
        if applied_amount is not None:
          self.applied_amount = applied_amount
        if institutional_estimated_value is not None:
          self.institutional_estimated_value = institutional_estimated_value
        if institutional_part is not None:
          self.institutional_part = institutional_part
        if institutional_contribution is not None:
          self.institutional_contribution = institutional_contribution
        if institutional_fec is not None:
          self.institutional_fec = institutional_fec
        if funding_collaborators is not None:
          self.funding_collaborators = funding_collaborators
        if budget_and_expenditures is not None:
          self.budget_and_expenditures = budget_and_expenditures
        if visibilities is not None:
          self.visibilities = visibilities
        if fecpercentage is not None:
          self.fecpercentage = fecpercentage

    @property
    def id(self):
        """
        Gets the id of this WSApplicationFundingAssociation.

        :return: The id of this WSApplicationFundingAssociation.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WSApplicationFundingAssociation.

        :param id: The id of this WSApplicationFundingAssociation.
        :type: int
        """

        self._id = id

    @property
    def funder(self):
        """
        Gets the funder of this WSApplicationFundingAssociation.

        :return: The funder of this WSApplicationFundingAssociation.
        :rtype: WSExternalOrganisationRef
        """
        return self._funder

    @funder.setter
    def funder(self, funder):
        """
        Sets the funder of this WSApplicationFundingAssociation.

        :param funder: The funder of this WSApplicationFundingAssociation.
        :type: WSExternalOrganisationRef
        """

        self._funder = funder

    @property
    def funding_classifications(self):
        """
        Gets the funding_classifications of this WSApplicationFundingAssociation.

        :return: The funding_classifications of this WSApplicationFundingAssociation.
        :rtype: list[WSClassification]
        """
        return self._funding_classifications

    @funding_classifications.setter
    def funding_classifications(self, funding_classifications):
        """
        Sets the funding_classifications of this WSApplicationFundingAssociation.

        :param funding_classifications: The funding_classifications of this WSApplicationFundingAssociation.
        :type: list[WSClassification]
        """

        self._funding_classifications = funding_classifications

    @property
    def funding_project_scheme(self):
        """
        Gets the funding_project_scheme of this WSApplicationFundingAssociation.

        :return: The funding_project_scheme of this WSApplicationFundingAssociation.
        :rtype: str
        """
        return self._funding_project_scheme

    @funding_project_scheme.setter
    def funding_project_scheme(self, funding_project_scheme):
        """
        Sets the funding_project_scheme of this WSApplicationFundingAssociation.

        :param funding_project_scheme: The funding_project_scheme of this WSApplicationFundingAssociation.
        :type: str
        """

        self._funding_project_scheme = funding_project_scheme

    @property
    def financial(self):
        """
        Gets the financial of this WSApplicationFundingAssociation.

        :return: The financial of this WSApplicationFundingAssociation.
        :rtype: bool
        """
        return self._financial

    @financial.setter
    def financial(self, financial):
        """
        Sets the financial of this WSApplicationFundingAssociation.

        :param financial: The financial of this WSApplicationFundingAssociation.
        :type: bool
        """

        self._financial = financial

    @property
    def estimated_value(self):
        """
        Gets the estimated_value of this WSApplicationFundingAssociation.

        :return: The estimated_value of this WSApplicationFundingAssociation.
        :rtype: float
        """
        return self._estimated_value

    @estimated_value.setter
    def estimated_value(self, estimated_value):
        """
        Sets the estimated_value of this WSApplicationFundingAssociation.

        :param estimated_value: The estimated_value of this WSApplicationFundingAssociation.
        :type: float
        """

        self._estimated_value = estimated_value

    @property
    def non_financial_description(self):
        """
        Gets the non_financial_description of this WSApplicationFundingAssociation.

        :return: The non_financial_description of this WSApplicationFundingAssociation.
        :rtype: str
        """
        return self._non_financial_description

    @non_financial_description.setter
    def non_financial_description(self, non_financial_description):
        """
        Sets the non_financial_description of this WSApplicationFundingAssociation.

        :param non_financial_description: The non_financial_description of this WSApplicationFundingAssociation.
        :type: str
        """

        self._non_financial_description = non_financial_description

    @property
    def applied_amount_in_applied_currency(self):
        """
        Gets the applied_amount_in_applied_currency of this WSApplicationFundingAssociation.

        :return: The applied_amount_in_applied_currency of this WSApplicationFundingAssociation.
        :rtype: float
        """
        return self._applied_amount_in_applied_currency

    @applied_amount_in_applied_currency.setter
    def applied_amount_in_applied_currency(self, applied_amount_in_applied_currency):
        """
        Sets the applied_amount_in_applied_currency of this WSApplicationFundingAssociation.

        :param applied_amount_in_applied_currency: The applied_amount_in_applied_currency of this WSApplicationFundingAssociation.
        :type: float
        """

        self._applied_amount_in_applied_currency = applied_amount_in_applied_currency

    @property
    def applied_currencies(self):
        """
        Gets the applied_currencies of this WSApplicationFundingAssociation.

        :return: The applied_currencies of this WSApplicationFundingAssociation.
        :rtype: list[WSClassification]
        """
        return self._applied_currencies

    @applied_currencies.setter
    def applied_currencies(self, applied_currencies):
        """
        Sets the applied_currencies of this WSApplicationFundingAssociation.

        :param applied_currencies: The applied_currencies of this WSApplicationFundingAssociation.
        :type: list[WSClassification]
        """

        self._applied_currencies = applied_currencies

    @property
    def applied_amount(self):
        """
        Gets the applied_amount of this WSApplicationFundingAssociation.

        :return: The applied_amount of this WSApplicationFundingAssociation.
        :rtype: float
        """
        return self._applied_amount

    @applied_amount.setter
    def applied_amount(self, applied_amount):
        """
        Sets the applied_amount of this WSApplicationFundingAssociation.

        :param applied_amount: The applied_amount of this WSApplicationFundingAssociation.
        :type: float
        """

        self._applied_amount = applied_amount

    @property
    def institutional_estimated_value(self):
        """
        Gets the institutional_estimated_value of this WSApplicationFundingAssociation.

        :return: The institutional_estimated_value of this WSApplicationFundingAssociation.
        :rtype: float
        """
        return self._institutional_estimated_value

    @institutional_estimated_value.setter
    def institutional_estimated_value(self, institutional_estimated_value):
        """
        Sets the institutional_estimated_value of this WSApplicationFundingAssociation.

        :param institutional_estimated_value: The institutional_estimated_value of this WSApplicationFundingAssociation.
        :type: float
        """

        self._institutional_estimated_value = institutional_estimated_value

    @property
    def institutional_part(self):
        """
        Gets the institutional_part of this WSApplicationFundingAssociation.

        :return: The institutional_part of this WSApplicationFundingAssociation.
        :rtype: float
        """
        return self._institutional_part

    @institutional_part.setter
    def institutional_part(self, institutional_part):
        """
        Sets the institutional_part of this WSApplicationFundingAssociation.

        :param institutional_part: The institutional_part of this WSApplicationFundingAssociation.
        :type: float
        """

        self._institutional_part = institutional_part

    @property
    def institutional_contribution(self):
        """
        Gets the institutional_contribution of this WSApplicationFundingAssociation.

        :return: The institutional_contribution of this WSApplicationFundingAssociation.
        :rtype: float
        """
        return self._institutional_contribution

    @institutional_contribution.setter
    def institutional_contribution(self, institutional_contribution):
        """
        Sets the institutional_contribution of this WSApplicationFundingAssociation.

        :param institutional_contribution: The institutional_contribution of this WSApplicationFundingAssociation.
        :type: float
        """

        self._institutional_contribution = institutional_contribution

    @property
    def institutional_fec(self):
        """
        Gets the institutional_fec of this WSApplicationFundingAssociation.

        :return: The institutional_fec of this WSApplicationFundingAssociation.
        :rtype: float
        """
        return self._institutional_fec

    @institutional_fec.setter
    def institutional_fec(self, institutional_fec):
        """
        Sets the institutional_fec of this WSApplicationFundingAssociation.

        :param institutional_fec: The institutional_fec of this WSApplicationFundingAssociation.
        :type: float
        """

        self._institutional_fec = institutional_fec

    @property
    def funding_collaborators(self):
        """
        Gets the funding_collaborators of this WSApplicationFundingAssociation.

        :return: The funding_collaborators of this WSApplicationFundingAssociation.
        :rtype: list[WSFundingCollaboratorAssociation]
        """
        return self._funding_collaborators

    @funding_collaborators.setter
    def funding_collaborators(self, funding_collaborators):
        """
        Sets the funding_collaborators of this WSApplicationFundingAssociation.

        :param funding_collaborators: The funding_collaborators of this WSApplicationFundingAssociation.
        :type: list[WSFundingCollaboratorAssociation]
        """

        self._funding_collaborators = funding_collaborators

    @property
    def budget_and_expenditures(self):
        """
        Gets the budget_and_expenditures of this WSApplicationFundingAssociation.

        :return: The budget_and_expenditures of this WSApplicationFundingAssociation.
        :rtype: list[WSFundingExpenditureAssociation]
        """
        return self._budget_and_expenditures

    @budget_and_expenditures.setter
    def budget_and_expenditures(self, budget_and_expenditures):
        """
        Sets the budget_and_expenditures of this WSApplicationFundingAssociation.

        :param budget_and_expenditures: The budget_and_expenditures of this WSApplicationFundingAssociation.
        :type: list[WSFundingExpenditureAssociation]
        """

        self._budget_and_expenditures = budget_and_expenditures

    @property
    def visibilities(self):
        """
        Gets the visibilities of this WSApplicationFundingAssociation.

        :return: The visibilities of this WSApplicationFundingAssociation.
        :rtype: list[WSVisibility]
        """
        return self._visibilities

    @visibilities.setter
    def visibilities(self, visibilities):
        """
        Sets the visibilities of this WSApplicationFundingAssociation.

        :param visibilities: The visibilities of this WSApplicationFundingAssociation.
        :type: list[WSVisibility]
        """

        self._visibilities = visibilities

    @property
    def fecpercentage(self):
        """
        Gets the fecpercentage of this WSApplicationFundingAssociation.

        :return: The fecpercentage of this WSApplicationFundingAssociation.
        :rtype: float
        """
        return self._fecpercentage

    @fecpercentage.setter
    def fecpercentage(self, fecpercentage):
        """
        Sets the fecpercentage of this WSApplicationFundingAssociation.

        :param fecpercentage: The fecpercentage of this WSApplicationFundingAssociation.
        :type: float
        """

        self._fecpercentage = fecpercentage

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
        if not isinstance(other, WSApplicationFundingAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
