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


class WSApplication(object):
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
        'uuid': 'str',
        'html_renderings': 'list[WSHtmlRendering]',
        'titles': 'list[WSLocalizedString]',
        'types': 'list[WSClassification]',
        'nature_types': 'list[WSClassification]',
        'statuses': 'list[WSApplicationStatus]',
        'short_titles': 'list[WSLocalizedString]',
        'acronym': 'str',
        'descriptions': 'list[WSClassifiedLocalizedValue]',
        'classified_sources': 'list[WSClassifiedValue]',
        'funding_opportunity': 'WSFundingOpportunityRef',
        'applicants': 'list[WSClassifiedApplicantAssociation]',
        'documents': 'list[WSApplicationDocument]',
        'budget_difference': 'float',
        'organisations': 'list[WSOrganisationRef]',
        'external_organisations': 'list[WSExternalOrganisationRef]',
        'managing_organisational_unit': 'WSOrganisationRef',
        'collaborative': 'bool',
        'collaborators': 'list[WSCollaboratorAssociation]',
        'total_academic_ownership_percentage': 'float',
        'fundings': 'list[WSApplicationFundingAssociation]',
        'total_applied_amount': 'float',
        'expected_period': 'WSDateRange',
        'related_project': 'WSUPMProjectRef',
        'related_applications': 'list[WSApplicationRef]',
        'related_awards': 'list[WSAwardRef]',
        'related_ethical_reviews': 'list[WSEthicalReviewRef]',
        'field_of_research_associations': 'list[WSERA2015FieldOfResearchAssociation]',
        'keyword_groups': 'list[WSKeywordGroup]',
        'visibilities': 'list[WSVisibility]',
        'confidential': 'bool',
        'workflows': 'list[WSWorkflow]',
        'externalable_info': 'WSExternalableInformation',
        'info': 'WSContentInformation'
    }

    attribute_map = {
        'uuid': 'uuid',
        'html_renderings': 'htmlRenderings',
        'titles': 'titles',
        'types': 'types',
        'nature_types': 'natureTypes',
        'statuses': 'statuses',
        'short_titles': 'shortTitles',
        'acronym': 'acronym',
        'descriptions': 'descriptions',
        'classified_sources': 'classifiedSources',
        'funding_opportunity': 'fundingOpportunity',
        'applicants': 'applicants',
        'documents': 'documents',
        'budget_difference': 'budgetDifference',
        'organisations': 'organisations',
        'external_organisations': 'externalOrganisations',
        'managing_organisational_unit': 'managingOrganisationalUnit',
        'collaborative': 'collaborative',
        'collaborators': 'collaborators',
        'total_academic_ownership_percentage': 'totalAcademicOwnershipPercentage',
        'fundings': 'fundings',
        'total_applied_amount': 'totalAppliedAmount',
        'expected_period': 'expectedPeriod',
        'related_project': 'relatedProject',
        'related_applications': 'relatedApplications',
        'related_awards': 'relatedAwards',
        'related_ethical_reviews': 'relatedEthicalReviews',
        'field_of_research_associations': 'fieldOfResearchAssociations',
        'keyword_groups': 'keywordGroups',
        'visibilities': 'visibilities',
        'confidential': 'confidential',
        'workflows': 'workflows',
        'externalable_info': 'externalableInfo',
        'info': 'info'
    }

    def __init__(self, uuid=None, html_renderings=None, titles=None, types=None, nature_types=None, statuses=None, short_titles=None, acronym=None, descriptions=None, classified_sources=None, funding_opportunity=None, applicants=None, documents=None, budget_difference=None, organisations=None, external_organisations=None, managing_organisational_unit=None, collaborative=False, collaborators=None, total_academic_ownership_percentage=None, fundings=None, total_applied_amount=None, expected_period=None, related_project=None, related_applications=None, related_awards=None, related_ethical_reviews=None, field_of_research_associations=None, keyword_groups=None, visibilities=None, confidential=False, workflows=None, externalable_info=None, info=None):
        """
        WSApplication - a model defined in Swagger
        """

        self._uuid = None
        self._html_renderings = None
        self._titles = None
        self._types = None
        self._nature_types = None
        self._statuses = None
        self._short_titles = None
        self._acronym = None
        self._descriptions = None
        self._classified_sources = None
        self._funding_opportunity = None
        self._applicants = None
        self._documents = None
        self._budget_difference = None
        self._organisations = None
        self._external_organisations = None
        self._managing_organisational_unit = None
        self._collaborative = None
        self._collaborators = None
        self._total_academic_ownership_percentage = None
        self._fundings = None
        self._total_applied_amount = None
        self._expected_period = None
        self._related_project = None
        self._related_applications = None
        self._related_awards = None
        self._related_ethical_reviews = None
        self._field_of_research_associations = None
        self._keyword_groups = None
        self._visibilities = None
        self._confidential = None
        self._workflows = None
        self._externalable_info = None
        self._info = None

        if uuid is not None:
          self.uuid = uuid
        if html_renderings is not None:
          self.html_renderings = html_renderings
        if titles is not None:
          self.titles = titles
        if types is not None:
          self.types = types
        if nature_types is not None:
          self.nature_types = nature_types
        if statuses is not None:
          self.statuses = statuses
        if short_titles is not None:
          self.short_titles = short_titles
        if acronym is not None:
          self.acronym = acronym
        if descriptions is not None:
          self.descriptions = descriptions
        if classified_sources is not None:
          self.classified_sources = classified_sources
        if funding_opportunity is not None:
          self.funding_opportunity = funding_opportunity
        if applicants is not None:
          self.applicants = applicants
        if documents is not None:
          self.documents = documents
        if budget_difference is not None:
          self.budget_difference = budget_difference
        if organisations is not None:
          self.organisations = organisations
        if external_organisations is not None:
          self.external_organisations = external_organisations
        if managing_organisational_unit is not None:
          self.managing_organisational_unit = managing_organisational_unit
        if collaborative is not None:
          self.collaborative = collaborative
        if collaborators is not None:
          self.collaborators = collaborators
        if total_academic_ownership_percentage is not None:
          self.total_academic_ownership_percentage = total_academic_ownership_percentage
        if fundings is not None:
          self.fundings = fundings
        if total_applied_amount is not None:
          self.total_applied_amount = total_applied_amount
        if expected_period is not None:
          self.expected_period = expected_period
        if related_project is not None:
          self.related_project = related_project
        if related_applications is not None:
          self.related_applications = related_applications
        if related_awards is not None:
          self.related_awards = related_awards
        if related_ethical_reviews is not None:
          self.related_ethical_reviews = related_ethical_reviews
        if field_of_research_associations is not None:
          self.field_of_research_associations = field_of_research_associations
        if keyword_groups is not None:
          self.keyword_groups = keyword_groups
        if visibilities is not None:
          self.visibilities = visibilities
        if confidential is not None:
          self.confidential = confidential
        if workflows is not None:
          self.workflows = workflows
        if externalable_info is not None:
          self.externalable_info = externalable_info
        if info is not None:
          self.info = info

    @property
    def uuid(self):
        """
        Gets the uuid of this WSApplication.

        :return: The uuid of this WSApplication.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this WSApplication.

        :param uuid: The uuid of this WSApplication.
        :type: str
        """

        self._uuid = uuid

    @property
    def html_renderings(self):
        """
        Gets the html_renderings of this WSApplication.

        :return: The html_renderings of this WSApplication.
        :rtype: list[WSHtmlRendering]
        """
        return self._html_renderings

    @html_renderings.setter
    def html_renderings(self, html_renderings):
        """
        Sets the html_renderings of this WSApplication.

        :param html_renderings: The html_renderings of this WSApplication.
        :type: list[WSHtmlRendering]
        """

        self._html_renderings = html_renderings

    @property
    def titles(self):
        """
        Gets the titles of this WSApplication.

        :return: The titles of this WSApplication.
        :rtype: list[WSLocalizedString]
        """
        return self._titles

    @titles.setter
    def titles(self, titles):
        """
        Sets the titles of this WSApplication.

        :param titles: The titles of this WSApplication.
        :type: list[WSLocalizedString]
        """

        self._titles = titles

    @property
    def types(self):
        """
        Gets the types of this WSApplication.

        :return: The types of this WSApplication.
        :rtype: list[WSClassification]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this WSApplication.

        :param types: The types of this WSApplication.
        :type: list[WSClassification]
        """

        self._types = types

    @property
    def nature_types(self):
        """
        Gets the nature_types of this WSApplication.

        :return: The nature_types of this WSApplication.
        :rtype: list[WSClassification]
        """
        return self._nature_types

    @nature_types.setter
    def nature_types(self, nature_types):
        """
        Sets the nature_types of this WSApplication.

        :param nature_types: The nature_types of this WSApplication.
        :type: list[WSClassification]
        """

        self._nature_types = nature_types

    @property
    def statuses(self):
        """
        Gets the statuses of this WSApplication.
        Not available when the Award Management module is enabled

        :return: The statuses of this WSApplication.
        :rtype: list[WSApplicationStatus]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """
        Sets the statuses of this WSApplication.
        Not available when the Award Management module is enabled

        :param statuses: The statuses of this WSApplication.
        :type: list[WSApplicationStatus]
        """

        self._statuses = statuses

    @property
    def short_titles(self):
        """
        Gets the short_titles of this WSApplication.

        :return: The short_titles of this WSApplication.
        :rtype: list[WSLocalizedString]
        """
        return self._short_titles

    @short_titles.setter
    def short_titles(self, short_titles):
        """
        Sets the short_titles of this WSApplication.

        :param short_titles: The short_titles of this WSApplication.
        :type: list[WSLocalizedString]
        """

        self._short_titles = short_titles

    @property
    def acronym(self):
        """
        Gets the acronym of this WSApplication.

        :return: The acronym of this WSApplication.
        :rtype: str
        """
        return self._acronym

    @acronym.setter
    def acronym(self, acronym):
        """
        Sets the acronym of this WSApplication.

        :param acronym: The acronym of this WSApplication.
        :type: str
        """

        self._acronym = acronym

    @property
    def descriptions(self):
        """
        Gets the descriptions of this WSApplication.

        :return: The descriptions of this WSApplication.
        :rtype: list[WSClassifiedLocalizedValue]
        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions):
        """
        Sets the descriptions of this WSApplication.

        :param descriptions: The descriptions of this WSApplication.
        :type: list[WSClassifiedLocalizedValue]
        """

        self._descriptions = descriptions

    @property
    def classified_sources(self):
        """
        Gets the classified_sources of this WSApplication.

        :return: The classified_sources of this WSApplication.
        :rtype: list[WSClassifiedValue]
        """
        return self._classified_sources

    @classified_sources.setter
    def classified_sources(self, classified_sources):
        """
        Sets the classified_sources of this WSApplication.

        :param classified_sources: The classified_sources of this WSApplication.
        :type: list[WSClassifiedValue]
        """

        self._classified_sources = classified_sources

    @property
    def funding_opportunity(self):
        """
        Gets the funding_opportunity of this WSApplication.
        Not available when the Award Management module is disabled

        :return: The funding_opportunity of this WSApplication.
        :rtype: WSFundingOpportunityRef
        """
        return self._funding_opportunity

    @funding_opportunity.setter
    def funding_opportunity(self, funding_opportunity):
        """
        Sets the funding_opportunity of this WSApplication.
        Not available when the Award Management module is disabled

        :param funding_opportunity: The funding_opportunity of this WSApplication.
        :type: WSFundingOpportunityRef
        """

        self._funding_opportunity = funding_opportunity

    @property
    def applicants(self):
        """
        Gets the applicants of this WSApplication.

        :return: The applicants of this WSApplication.
        :rtype: list[WSClassifiedApplicantAssociation]
        """
        return self._applicants

    @applicants.setter
    def applicants(self, applicants):
        """
        Sets the applicants of this WSApplication.

        :param applicants: The applicants of this WSApplication.
        :type: list[WSClassifiedApplicantAssociation]
        """

        self._applicants = applicants

    @property
    def documents(self):
        """
        Gets the documents of this WSApplication.

        :return: The documents of this WSApplication.
        :rtype: list[WSApplicationDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this WSApplication.

        :param documents: The documents of this WSApplication.
        :type: list[WSApplicationDocument]
        """

        self._documents = documents

    @property
    def budget_difference(self):
        """
        Gets the budget_difference of this WSApplication.

        :return: The budget_difference of this WSApplication.
        :rtype: float
        """
        return self._budget_difference

    @budget_difference.setter
    def budget_difference(self, budget_difference):
        """
        Sets the budget_difference of this WSApplication.

        :param budget_difference: The budget_difference of this WSApplication.
        :type: float
        """

        self._budget_difference = budget_difference

    @property
    def organisations(self):
        """
        Gets the organisations of this WSApplication.

        :return: The organisations of this WSApplication.
        :rtype: list[WSOrganisationRef]
        """
        return self._organisations

    @organisations.setter
    def organisations(self, organisations):
        """
        Sets the organisations of this WSApplication.

        :param organisations: The organisations of this WSApplication.
        :type: list[WSOrganisationRef]
        """

        self._organisations = organisations

    @property
    def external_organisations(self):
        """
        Gets the external_organisations of this WSApplication.

        :return: The external_organisations of this WSApplication.
        :rtype: list[WSExternalOrganisationRef]
        """
        return self._external_organisations

    @external_organisations.setter
    def external_organisations(self, external_organisations):
        """
        Sets the external_organisations of this WSApplication.

        :param external_organisations: The external_organisations of this WSApplication.
        :type: list[WSExternalOrganisationRef]
        """

        self._external_organisations = external_organisations

    @property
    def managing_organisational_unit(self):
        """
        Gets the managing_organisational_unit of this WSApplication.

        :return: The managing_organisational_unit of this WSApplication.
        :rtype: WSOrganisationRef
        """
        return self._managing_organisational_unit

    @managing_organisational_unit.setter
    def managing_organisational_unit(self, managing_organisational_unit):
        """
        Sets the managing_organisational_unit of this WSApplication.

        :param managing_organisational_unit: The managing_organisational_unit of this WSApplication.
        :type: WSOrganisationRef
        """

        self._managing_organisational_unit = managing_organisational_unit

    @property
    def collaborative(self):
        """
        Gets the collaborative of this WSApplication.

        :return: The collaborative of this WSApplication.
        :rtype: bool
        """
        return self._collaborative

    @collaborative.setter
    def collaborative(self, collaborative):
        """
        Sets the collaborative of this WSApplication.

        :param collaborative: The collaborative of this WSApplication.
        :type: bool
        """

        self._collaborative = collaborative

    @property
    def collaborators(self):
        """
        Gets the collaborators of this WSApplication.

        :return: The collaborators of this WSApplication.
        :rtype: list[WSCollaboratorAssociation]
        """
        return self._collaborators

    @collaborators.setter
    def collaborators(self, collaborators):
        """
        Sets the collaborators of this WSApplication.

        :param collaborators: The collaborators of this WSApplication.
        :type: list[WSCollaboratorAssociation]
        """

        self._collaborators = collaborators

    @property
    def total_academic_ownership_percentage(self):
        """
        Gets the total_academic_ownership_percentage of this WSApplication.

        :return: The total_academic_ownership_percentage of this WSApplication.
        :rtype: float
        """
        return self._total_academic_ownership_percentage

    @total_academic_ownership_percentage.setter
    def total_academic_ownership_percentage(self, total_academic_ownership_percentage):
        """
        Sets the total_academic_ownership_percentage of this WSApplication.

        :param total_academic_ownership_percentage: The total_academic_ownership_percentage of this WSApplication.
        :type: float
        """

        self._total_academic_ownership_percentage = total_academic_ownership_percentage

    @property
    def fundings(self):
        """
        Gets the fundings of this WSApplication.

        :return: The fundings of this WSApplication.
        :rtype: list[WSApplicationFundingAssociation]
        """
        return self._fundings

    @fundings.setter
    def fundings(self, fundings):
        """
        Sets the fundings of this WSApplication.

        :param fundings: The fundings of this WSApplication.
        :type: list[WSApplicationFundingAssociation]
        """

        self._fundings = fundings

    @property
    def total_applied_amount(self):
        """
        Gets the total_applied_amount of this WSApplication.

        :return: The total_applied_amount of this WSApplication.
        :rtype: float
        """
        return self._total_applied_amount

    @total_applied_amount.setter
    def total_applied_amount(self, total_applied_amount):
        """
        Sets the total_applied_amount of this WSApplication.

        :param total_applied_amount: The total_applied_amount of this WSApplication.
        :type: float
        """

        self._total_applied_amount = total_applied_amount

    @property
    def expected_period(self):
        """
        Gets the expected_period of this WSApplication.

        :return: The expected_period of this WSApplication.
        :rtype: WSDateRange
        """
        return self._expected_period

    @expected_period.setter
    def expected_period(self, expected_period):
        """
        Sets the expected_period of this WSApplication.

        :param expected_period: The expected_period of this WSApplication.
        :type: WSDateRange
        """

        self._expected_period = expected_period

    @property
    def related_project(self):
        """
        Gets the related_project of this WSApplication.

        :return: The related_project of this WSApplication.
        :rtype: WSUPMProjectRef
        """
        return self._related_project

    @related_project.setter
    def related_project(self, related_project):
        """
        Sets the related_project of this WSApplication.

        :param related_project: The related_project of this WSApplication.
        :type: WSUPMProjectRef
        """

        self._related_project = related_project

    @property
    def related_applications(self):
        """
        Gets the related_applications of this WSApplication.

        :return: The related_applications of this WSApplication.
        :rtype: list[WSApplicationRef]
        """
        return self._related_applications

    @related_applications.setter
    def related_applications(self, related_applications):
        """
        Sets the related_applications of this WSApplication.

        :param related_applications: The related_applications of this WSApplication.
        :type: list[WSApplicationRef]
        """

        self._related_applications = related_applications

    @property
    def related_awards(self):
        """
        Gets the related_awards of this WSApplication.

        :return: The related_awards of this WSApplication.
        :rtype: list[WSAwardRef]
        """
        return self._related_awards

    @related_awards.setter
    def related_awards(self, related_awards):
        """
        Sets the related_awards of this WSApplication.

        :param related_awards: The related_awards of this WSApplication.
        :type: list[WSAwardRef]
        """

        self._related_awards = related_awards

    @property
    def related_ethical_reviews(self):
        """
        Gets the related_ethical_reviews of this WSApplication.
        Only available when the Award Management module is enabled

        :return: The related_ethical_reviews of this WSApplication.
        :rtype: list[WSEthicalReviewRef]
        """
        return self._related_ethical_reviews

    @related_ethical_reviews.setter
    def related_ethical_reviews(self, related_ethical_reviews):
        """
        Sets the related_ethical_reviews of this WSApplication.
        Only available when the Award Management module is enabled

        :param related_ethical_reviews: The related_ethical_reviews of this WSApplication.
        :type: list[WSEthicalReviewRef]
        """

        self._related_ethical_reviews = related_ethical_reviews

    @property
    def field_of_research_associations(self):
        """
        Gets the field_of_research_associations of this WSApplication.
        Only available when the ERA module is enabled

        :return: The field_of_research_associations of this WSApplication.
        :rtype: list[WSERA2015FieldOfResearchAssociation]
        """
        return self._field_of_research_associations

    @field_of_research_associations.setter
    def field_of_research_associations(self, field_of_research_associations):
        """
        Sets the field_of_research_associations of this WSApplication.
        Only available when the ERA module is enabled

        :param field_of_research_associations: The field_of_research_associations of this WSApplication.
        :type: list[WSERA2015FieldOfResearchAssociation]
        """

        self._field_of_research_associations = field_of_research_associations

    @property
    def keyword_groups(self):
        """
        Gets the keyword_groups of this WSApplication.

        :return: The keyword_groups of this WSApplication.
        :rtype: list[WSKeywordGroup]
        """
        return self._keyword_groups

    @keyword_groups.setter
    def keyword_groups(self, keyword_groups):
        """
        Sets the keyword_groups of this WSApplication.

        :param keyword_groups: The keyword_groups of this WSApplication.
        :type: list[WSKeywordGroup]
        """

        self._keyword_groups = keyword_groups

    @property
    def visibilities(self):
        """
        Gets the visibilities of this WSApplication.

        :return: The visibilities of this WSApplication.
        :rtype: list[WSVisibility]
        """
        return self._visibilities

    @visibilities.setter
    def visibilities(self, visibilities):
        """
        Sets the visibilities of this WSApplication.

        :param visibilities: The visibilities of this WSApplication.
        :type: list[WSVisibility]
        """

        self._visibilities = visibilities

    @property
    def confidential(self):
        """
        Gets the confidential of this WSApplication.

        :return: The confidential of this WSApplication.
        :rtype: bool
        """
        return self._confidential

    @confidential.setter
    def confidential(self, confidential):
        """
        Sets the confidential of this WSApplication.

        :param confidential: The confidential of this WSApplication.
        :type: bool
        """

        self._confidential = confidential

    @property
    def workflows(self):
        """
        Gets the workflows of this WSApplication.

        :return: The workflows of this WSApplication.
        :rtype: list[WSWorkflow]
        """
        return self._workflows

    @workflows.setter
    def workflows(self, workflows):
        """
        Sets the workflows of this WSApplication.

        :param workflows: The workflows of this WSApplication.
        :type: list[WSWorkflow]
        """

        self._workflows = workflows

    @property
    def externalable_info(self):
        """
        Gets the externalable_info of this WSApplication.

        :return: The externalable_info of this WSApplication.
        :rtype: WSExternalableInformation
        """
        return self._externalable_info

    @externalable_info.setter
    def externalable_info(self, externalable_info):
        """
        Sets the externalable_info of this WSApplication.

        :param externalable_info: The externalable_info of this WSApplication.
        :type: WSExternalableInformation
        """

        self._externalable_info = externalable_info

    @property
    def info(self):
        """
        Gets the info of this WSApplication.

        :return: The info of this WSApplication.
        :rtype: WSContentInformation
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this WSApplication.

        :param info: The info of this WSApplication.
        :type: WSContentInformation
        """

        self._info = info

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
        if not isinstance(other, WSApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
