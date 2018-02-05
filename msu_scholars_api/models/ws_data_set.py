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


class WSDataSet(object):
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
        'descriptions': 'list[WSClassifiedLocalizedValue]',
        'temporal_coverage_period': 'WSCompoundDateRange',
        'data_production_period': 'WSCompoundDateRange',
        'classified_sources': 'list[WSClassifiedValue]',
        'geographical_coverages': 'list[WSLocalizedString]',
        'geo_location': 'WSGeoLocation',
        'person_associations': 'list[WSClassifiedDataSetPersonAssociation]',
        'managing_organisational_unit': 'WSOrganisationRef',
        'publisher': 'WSPublisherRef',
        'doi': 'str',
        'documents': 'list[WSDocument]',
        'physical_datas': 'list[WSDataSetPhysicalData]',
        'contact_person': 'WSPersonRef',
        'legal_conditions': 'list[WSDataSetLegalCondition]',
        'organisations': 'list[WSOrganisationRef]',
        'external_organisations': 'list[WSExternalOrganisationRef]',
        'publication_date': 'WSCompoundDate',
        'open_access_permissions': 'list[WSClassification]',
        'related_data_sets': 'list[WSDataSetRef]',
        'related_projects': 'list[WSUPMProjectRef]',
        'related_research_outputs': 'list[WSResearchOutputRef]',
        'related_activities': 'list[WSActivityRef]',
        'related_press_media': 'list[WSPressMediaRef]',
        'related_student_thesis': 'list[WSStudentThesisRef]',
        'related_impacts': 'list[WSImpactRef]',
        'related_prizes': 'list[WSPrizeRef]',
        'nature_types': 'list[WSClassification]',
        'links': 'list[WSLink]',
        'workflows': 'list[WSWorkflow]',
        'keyword_groups': 'list[WSKeywordGroup]',
        'visibilities': 'list[WSVisibility]',
        'confidential': 'bool',
        'info': 'WSContentInformation',
        'externalable_info': 'WSExternalableInformation',
        'open_access_embargo_months': 'int',
        'open_access_embargo_date': 'datetime'
    }

    attribute_map = {
        'uuid': 'uuid',
        'html_renderings': 'htmlRenderings',
        'titles': 'titles',
        'types': 'types',
        'descriptions': 'descriptions',
        'temporal_coverage_period': 'temporalCoveragePeriod',
        'data_production_period': 'dataProductionPeriod',
        'classified_sources': 'classifiedSources',
        'geographical_coverages': 'geographicalCoverages',
        'geo_location': 'geoLocation',
        'person_associations': 'personAssociations',
        'managing_organisational_unit': 'managingOrganisationalUnit',
        'publisher': 'publisher',
        'doi': 'doi',
        'documents': 'documents',
        'physical_datas': 'physicalDatas',
        'contact_person': 'contactPerson',
        'legal_conditions': 'legalConditions',
        'organisations': 'organisations',
        'external_organisations': 'externalOrganisations',
        'publication_date': 'publicationDate',
        'open_access_permissions': 'openAccessPermissions',
        'related_data_sets': 'relatedDataSets',
        'related_projects': 'relatedProjects',
        'related_research_outputs': 'relatedResearchOutputs',
        'related_activities': 'relatedActivities',
        'related_press_media': 'relatedPressMedia',
        'related_student_thesis': 'relatedStudentThesis',
        'related_impacts': 'relatedImpacts',
        'related_prizes': 'relatedPrizes',
        'nature_types': 'natureTypes',
        'links': 'links',
        'workflows': 'workflows',
        'keyword_groups': 'keywordGroups',
        'visibilities': 'visibilities',
        'confidential': 'confidential',
        'info': 'info',
        'externalable_info': 'externalableInfo',
        'open_access_embargo_months': 'openAccessEmbargoMonths',
        'open_access_embargo_date': 'openAccessEmbargoDate'
    }

    def __init__(self, uuid=None, html_renderings=None, titles=None, types=None, descriptions=None, temporal_coverage_period=None, data_production_period=None, classified_sources=None, geographical_coverages=None, geo_location=None, person_associations=None, managing_organisational_unit=None, publisher=None, doi=None, documents=None, physical_datas=None, contact_person=None, legal_conditions=None, organisations=None, external_organisations=None, publication_date=None, open_access_permissions=None, related_data_sets=None, related_projects=None, related_research_outputs=None, related_activities=None, related_press_media=None, related_student_thesis=None, related_impacts=None, related_prizes=None, nature_types=None, links=None, workflows=None, keyword_groups=None, visibilities=None, confidential=False, info=None, externalable_info=None, open_access_embargo_months=None, open_access_embargo_date=None):
        """
        WSDataSet - a model defined in Swagger
        """

        self._uuid = None
        self._html_renderings = None
        self._titles = None
        self._types = None
        self._descriptions = None
        self._temporal_coverage_period = None
        self._data_production_period = None
        self._classified_sources = None
        self._geographical_coverages = None
        self._geo_location = None
        self._person_associations = None
        self._managing_organisational_unit = None
        self._publisher = None
        self._doi = None
        self._documents = None
        self._physical_datas = None
        self._contact_person = None
        self._legal_conditions = None
        self._organisations = None
        self._external_organisations = None
        self._publication_date = None
        self._open_access_permissions = None
        self._related_data_sets = None
        self._related_projects = None
        self._related_research_outputs = None
        self._related_activities = None
        self._related_press_media = None
        self._related_student_thesis = None
        self._related_impacts = None
        self._related_prizes = None
        self._nature_types = None
        self._links = None
        self._workflows = None
        self._keyword_groups = None
        self._visibilities = None
        self._confidential = None
        self._info = None
        self._externalable_info = None
        self._open_access_embargo_months = None
        self._open_access_embargo_date = None

        if uuid is not None:
          self.uuid = uuid
        if html_renderings is not None:
          self.html_renderings = html_renderings
        if titles is not None:
          self.titles = titles
        if types is not None:
          self.types = types
        if descriptions is not None:
          self.descriptions = descriptions
        if temporal_coverage_period is not None:
          self.temporal_coverage_period = temporal_coverage_period
        if data_production_period is not None:
          self.data_production_period = data_production_period
        if classified_sources is not None:
          self.classified_sources = classified_sources
        if geographical_coverages is not None:
          self.geographical_coverages = geographical_coverages
        if geo_location is not None:
          self.geo_location = geo_location
        if person_associations is not None:
          self.person_associations = person_associations
        if managing_organisational_unit is not None:
          self.managing_organisational_unit = managing_organisational_unit
        if publisher is not None:
          self.publisher = publisher
        if doi is not None:
          self.doi = doi
        if documents is not None:
          self.documents = documents
        if physical_datas is not None:
          self.physical_datas = physical_datas
        if contact_person is not None:
          self.contact_person = contact_person
        if legal_conditions is not None:
          self.legal_conditions = legal_conditions
        if organisations is not None:
          self.organisations = organisations
        if external_organisations is not None:
          self.external_organisations = external_organisations
        if publication_date is not None:
          self.publication_date = publication_date
        if open_access_permissions is not None:
          self.open_access_permissions = open_access_permissions
        if related_data_sets is not None:
          self.related_data_sets = related_data_sets
        if related_projects is not None:
          self.related_projects = related_projects
        if related_research_outputs is not None:
          self.related_research_outputs = related_research_outputs
        if related_activities is not None:
          self.related_activities = related_activities
        if related_press_media is not None:
          self.related_press_media = related_press_media
        if related_student_thesis is not None:
          self.related_student_thesis = related_student_thesis
        if related_impacts is not None:
          self.related_impacts = related_impacts
        if related_prizes is not None:
          self.related_prizes = related_prizes
        if nature_types is not None:
          self.nature_types = nature_types
        if links is not None:
          self.links = links
        if workflows is not None:
          self.workflows = workflows
        if keyword_groups is not None:
          self.keyword_groups = keyword_groups
        if visibilities is not None:
          self.visibilities = visibilities
        if confidential is not None:
          self.confidential = confidential
        if info is not None:
          self.info = info
        if externalable_info is not None:
          self.externalable_info = externalable_info
        if open_access_embargo_months is not None:
          self.open_access_embargo_months = open_access_embargo_months
        if open_access_embargo_date is not None:
          self.open_access_embargo_date = open_access_embargo_date

    @property
    def uuid(self):
        """
        Gets the uuid of this WSDataSet.

        :return: The uuid of this WSDataSet.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this WSDataSet.

        :param uuid: The uuid of this WSDataSet.
        :type: str
        """

        self._uuid = uuid

    @property
    def html_renderings(self):
        """
        Gets the html_renderings of this WSDataSet.

        :return: The html_renderings of this WSDataSet.
        :rtype: list[WSHtmlRendering]
        """
        return self._html_renderings

    @html_renderings.setter
    def html_renderings(self, html_renderings):
        """
        Sets the html_renderings of this WSDataSet.

        :param html_renderings: The html_renderings of this WSDataSet.
        :type: list[WSHtmlRendering]
        """

        self._html_renderings = html_renderings

    @property
    def titles(self):
        """
        Gets the titles of this WSDataSet.

        :return: The titles of this WSDataSet.
        :rtype: list[WSLocalizedString]
        """
        return self._titles

    @titles.setter
    def titles(self, titles):
        """
        Sets the titles of this WSDataSet.

        :param titles: The titles of this WSDataSet.
        :type: list[WSLocalizedString]
        """

        self._titles = titles

    @property
    def types(self):
        """
        Gets the types of this WSDataSet.

        :return: The types of this WSDataSet.
        :rtype: list[WSClassification]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this WSDataSet.

        :param types: The types of this WSDataSet.
        :type: list[WSClassification]
        """

        self._types = types

    @property
    def descriptions(self):
        """
        Gets the descriptions of this WSDataSet.

        :return: The descriptions of this WSDataSet.
        :rtype: list[WSClassifiedLocalizedValue]
        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions):
        """
        Sets the descriptions of this WSDataSet.

        :param descriptions: The descriptions of this WSDataSet.
        :type: list[WSClassifiedLocalizedValue]
        """

        self._descriptions = descriptions

    @property
    def temporal_coverage_period(self):
        """
        Gets the temporal_coverage_period of this WSDataSet.

        :return: The temporal_coverage_period of this WSDataSet.
        :rtype: WSCompoundDateRange
        """
        return self._temporal_coverage_period

    @temporal_coverage_period.setter
    def temporal_coverage_period(self, temporal_coverage_period):
        """
        Sets the temporal_coverage_period of this WSDataSet.

        :param temporal_coverage_period: The temporal_coverage_period of this WSDataSet.
        :type: WSCompoundDateRange
        """

        self._temporal_coverage_period = temporal_coverage_period

    @property
    def data_production_period(self):
        """
        Gets the data_production_period of this WSDataSet.

        :return: The data_production_period of this WSDataSet.
        :rtype: WSCompoundDateRange
        """
        return self._data_production_period

    @data_production_period.setter
    def data_production_period(self, data_production_period):
        """
        Sets the data_production_period of this WSDataSet.

        :param data_production_period: The data_production_period of this WSDataSet.
        :type: WSCompoundDateRange
        """

        self._data_production_period = data_production_period

    @property
    def classified_sources(self):
        """
        Gets the classified_sources of this WSDataSet.

        :return: The classified_sources of this WSDataSet.
        :rtype: list[WSClassifiedValue]
        """
        return self._classified_sources

    @classified_sources.setter
    def classified_sources(self, classified_sources):
        """
        Sets the classified_sources of this WSDataSet.

        :param classified_sources: The classified_sources of this WSDataSet.
        :type: list[WSClassifiedValue]
        """

        self._classified_sources = classified_sources

    @property
    def geographical_coverages(self):
        """
        Gets the geographical_coverages of this WSDataSet.

        :return: The geographical_coverages of this WSDataSet.
        :rtype: list[WSLocalizedString]
        """
        return self._geographical_coverages

    @geographical_coverages.setter
    def geographical_coverages(self, geographical_coverages):
        """
        Sets the geographical_coverages of this WSDataSet.

        :param geographical_coverages: The geographical_coverages of this WSDataSet.
        :type: list[WSLocalizedString]
        """

        self._geographical_coverages = geographical_coverages

    @property
    def geo_location(self):
        """
        Gets the geo_location of this WSDataSet.

        :return: The geo_location of this WSDataSet.
        :rtype: WSGeoLocation
        """
        return self._geo_location

    @geo_location.setter
    def geo_location(self, geo_location):
        """
        Sets the geo_location of this WSDataSet.

        :param geo_location: The geo_location of this WSDataSet.
        :type: WSGeoLocation
        """

        self._geo_location = geo_location

    @property
    def person_associations(self):
        """
        Gets the person_associations of this WSDataSet.

        :return: The person_associations of this WSDataSet.
        :rtype: list[WSClassifiedDataSetPersonAssociation]
        """
        return self._person_associations

    @person_associations.setter
    def person_associations(self, person_associations):
        """
        Sets the person_associations of this WSDataSet.

        :param person_associations: The person_associations of this WSDataSet.
        :type: list[WSClassifiedDataSetPersonAssociation]
        """

        self._person_associations = person_associations

    @property
    def managing_organisational_unit(self):
        """
        Gets the managing_organisational_unit of this WSDataSet.

        :return: The managing_organisational_unit of this WSDataSet.
        :rtype: WSOrganisationRef
        """
        return self._managing_organisational_unit

    @managing_organisational_unit.setter
    def managing_organisational_unit(self, managing_organisational_unit):
        """
        Sets the managing_organisational_unit of this WSDataSet.

        :param managing_organisational_unit: The managing_organisational_unit of this WSDataSet.
        :type: WSOrganisationRef
        """

        self._managing_organisational_unit = managing_organisational_unit

    @property
    def publisher(self):
        """
        Gets the publisher of this WSDataSet.

        :return: The publisher of this WSDataSet.
        :rtype: WSPublisherRef
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """
        Sets the publisher of this WSDataSet.

        :param publisher: The publisher of this WSDataSet.
        :type: WSPublisherRef
        """

        self._publisher = publisher

    @property
    def doi(self):
        """
        Gets the doi of this WSDataSet.

        :return: The doi of this WSDataSet.
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """
        Sets the doi of this WSDataSet.

        :param doi: The doi of this WSDataSet.
        :type: str
        """

        self._doi = doi

    @property
    def documents(self):
        """
        Gets the documents of this WSDataSet.

        :return: The documents of this WSDataSet.
        :rtype: list[WSDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this WSDataSet.

        :param documents: The documents of this WSDataSet.
        :type: list[WSDocument]
        """

        self._documents = documents

    @property
    def physical_datas(self):
        """
        Gets the physical_datas of this WSDataSet.

        :return: The physical_datas of this WSDataSet.
        :rtype: list[WSDataSetPhysicalData]
        """
        return self._physical_datas

    @physical_datas.setter
    def physical_datas(self, physical_datas):
        """
        Sets the physical_datas of this WSDataSet.

        :param physical_datas: The physical_datas of this WSDataSet.
        :type: list[WSDataSetPhysicalData]
        """

        self._physical_datas = physical_datas

    @property
    def contact_person(self):
        """
        Gets the contact_person of this WSDataSet.

        :return: The contact_person of this WSDataSet.
        :rtype: WSPersonRef
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """
        Sets the contact_person of this WSDataSet.

        :param contact_person: The contact_person of this WSDataSet.
        :type: WSPersonRef
        """

        self._contact_person = contact_person

    @property
    def legal_conditions(self):
        """
        Gets the legal_conditions of this WSDataSet.

        :return: The legal_conditions of this WSDataSet.
        :rtype: list[WSDataSetLegalCondition]
        """
        return self._legal_conditions

    @legal_conditions.setter
    def legal_conditions(self, legal_conditions):
        """
        Sets the legal_conditions of this WSDataSet.

        :param legal_conditions: The legal_conditions of this WSDataSet.
        :type: list[WSDataSetLegalCondition]
        """

        self._legal_conditions = legal_conditions

    @property
    def organisations(self):
        """
        Gets the organisations of this WSDataSet.

        :return: The organisations of this WSDataSet.
        :rtype: list[WSOrganisationRef]
        """
        return self._organisations

    @organisations.setter
    def organisations(self, organisations):
        """
        Sets the organisations of this WSDataSet.

        :param organisations: The organisations of this WSDataSet.
        :type: list[WSOrganisationRef]
        """

        self._organisations = organisations

    @property
    def external_organisations(self):
        """
        Gets the external_organisations of this WSDataSet.

        :return: The external_organisations of this WSDataSet.
        :rtype: list[WSExternalOrganisationRef]
        """
        return self._external_organisations

    @external_organisations.setter
    def external_organisations(self, external_organisations):
        """
        Sets the external_organisations of this WSDataSet.

        :param external_organisations: The external_organisations of this WSDataSet.
        :type: list[WSExternalOrganisationRef]
        """

        self._external_organisations = external_organisations

    @property
    def publication_date(self):
        """
        Gets the publication_date of this WSDataSet.

        :return: The publication_date of this WSDataSet.
        :rtype: WSCompoundDate
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """
        Sets the publication_date of this WSDataSet.

        :param publication_date: The publication_date of this WSDataSet.
        :type: WSCompoundDate
        """

        self._publication_date = publication_date

    @property
    def open_access_permissions(self):
        """
        Gets the open_access_permissions of this WSDataSet.

        :return: The open_access_permissions of this WSDataSet.
        :rtype: list[WSClassification]
        """
        return self._open_access_permissions

    @open_access_permissions.setter
    def open_access_permissions(self, open_access_permissions):
        """
        Sets the open_access_permissions of this WSDataSet.

        :param open_access_permissions: The open_access_permissions of this WSDataSet.
        :type: list[WSClassification]
        """

        self._open_access_permissions = open_access_permissions

    @property
    def related_data_sets(self):
        """
        Gets the related_data_sets of this WSDataSet.

        :return: The related_data_sets of this WSDataSet.
        :rtype: list[WSDataSetRef]
        """
        return self._related_data_sets

    @related_data_sets.setter
    def related_data_sets(self, related_data_sets):
        """
        Sets the related_data_sets of this WSDataSet.

        :param related_data_sets: The related_data_sets of this WSDataSet.
        :type: list[WSDataSetRef]
        """

        self._related_data_sets = related_data_sets

    @property
    def related_projects(self):
        """
        Gets the related_projects of this WSDataSet.
        Only available when the Unified Project Model module is enabled

        :return: The related_projects of this WSDataSet.
        :rtype: list[WSUPMProjectRef]
        """
        return self._related_projects

    @related_projects.setter
    def related_projects(self, related_projects):
        """
        Sets the related_projects of this WSDataSet.
        Only available when the Unified Project Model module is enabled

        :param related_projects: The related_projects of this WSDataSet.
        :type: list[WSUPMProjectRef]
        """

        self._related_projects = related_projects

    @property
    def related_research_outputs(self):
        """
        Gets the related_research_outputs of this WSDataSet.

        :return: The related_research_outputs of this WSDataSet.
        :rtype: list[WSResearchOutputRef]
        """
        return self._related_research_outputs

    @related_research_outputs.setter
    def related_research_outputs(self, related_research_outputs):
        """
        Sets the related_research_outputs of this WSDataSet.

        :param related_research_outputs: The related_research_outputs of this WSDataSet.
        :type: list[WSResearchOutputRef]
        """

        self._related_research_outputs = related_research_outputs

    @property
    def related_activities(self):
        """
        Gets the related_activities of this WSDataSet.
        Only available when the Activity module is enabled

        :return: The related_activities of this WSDataSet.
        :rtype: list[WSActivityRef]
        """
        return self._related_activities

    @related_activities.setter
    def related_activities(self, related_activities):
        """
        Sets the related_activities of this WSDataSet.
        Only available when the Activity module is enabled

        :param related_activities: The related_activities of this WSDataSet.
        :type: list[WSActivityRef]
        """

        self._related_activities = related_activities

    @property
    def related_press_media(self):
        """
        Gets the related_press_media of this WSDataSet.
        Only available when the Press / Media module is enabled

        :return: The related_press_media of this WSDataSet.
        :rtype: list[WSPressMediaRef]
        """
        return self._related_press_media

    @related_press_media.setter
    def related_press_media(self, related_press_media):
        """
        Sets the related_press_media of this WSDataSet.
        Only available when the Press / Media module is enabled

        :param related_press_media: The related_press_media of this WSDataSet.
        :type: list[WSPressMediaRef]
        """

        self._related_press_media = related_press_media

    @property
    def related_student_thesis(self):
        """
        Gets the related_student_thesis of this WSDataSet.
        Only available when the Student Thesis module is enabled

        :return: The related_student_thesis of this WSDataSet.
        :rtype: list[WSStudentThesisRef]
        """
        return self._related_student_thesis

    @related_student_thesis.setter
    def related_student_thesis(self, related_student_thesis):
        """
        Sets the related_student_thesis of this WSDataSet.
        Only available when the Student Thesis module is enabled

        :param related_student_thesis: The related_student_thesis of this WSDataSet.
        :type: list[WSStudentThesisRef]
        """

        self._related_student_thesis = related_student_thesis

    @property
    def related_impacts(self):
        """
        Gets the related_impacts of this WSDataSet.
        Only available when the Impact module is enabled

        :return: The related_impacts of this WSDataSet.
        :rtype: list[WSImpactRef]
        """
        return self._related_impacts

    @related_impacts.setter
    def related_impacts(self, related_impacts):
        """
        Sets the related_impacts of this WSDataSet.
        Only available when the Impact module is enabled

        :param related_impacts: The related_impacts of this WSDataSet.
        :type: list[WSImpactRef]
        """

        self._related_impacts = related_impacts

    @property
    def related_prizes(self):
        """
        Gets the related_prizes of this WSDataSet.
        Only available when the Prize module is enabled

        :return: The related_prizes of this WSDataSet.
        :rtype: list[WSPrizeRef]
        """
        return self._related_prizes

    @related_prizes.setter
    def related_prizes(self, related_prizes):
        """
        Sets the related_prizes of this WSDataSet.
        Only available when the Prize module is enabled

        :param related_prizes: The related_prizes of this WSDataSet.
        :type: list[WSPrizeRef]
        """

        self._related_prizes = related_prizes

    @property
    def nature_types(self):
        """
        Gets the nature_types of this WSDataSet.

        :return: The nature_types of this WSDataSet.
        :rtype: list[WSClassification]
        """
        return self._nature_types

    @nature_types.setter
    def nature_types(self, nature_types):
        """
        Sets the nature_types of this WSDataSet.

        :param nature_types: The nature_types of this WSDataSet.
        :type: list[WSClassification]
        """

        self._nature_types = nature_types

    @property
    def links(self):
        """
        Gets the links of this WSDataSet.

        :return: The links of this WSDataSet.
        :rtype: list[WSLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this WSDataSet.

        :param links: The links of this WSDataSet.
        :type: list[WSLink]
        """

        self._links = links

    @property
    def workflows(self):
        """
        Gets the workflows of this WSDataSet.

        :return: The workflows of this WSDataSet.
        :rtype: list[WSWorkflow]
        """
        return self._workflows

    @workflows.setter
    def workflows(self, workflows):
        """
        Sets the workflows of this WSDataSet.

        :param workflows: The workflows of this WSDataSet.
        :type: list[WSWorkflow]
        """

        self._workflows = workflows

    @property
    def keyword_groups(self):
        """
        Gets the keyword_groups of this WSDataSet.

        :return: The keyword_groups of this WSDataSet.
        :rtype: list[WSKeywordGroup]
        """
        return self._keyword_groups

    @keyword_groups.setter
    def keyword_groups(self, keyword_groups):
        """
        Sets the keyword_groups of this WSDataSet.

        :param keyword_groups: The keyword_groups of this WSDataSet.
        :type: list[WSKeywordGroup]
        """

        self._keyword_groups = keyword_groups

    @property
    def visibilities(self):
        """
        Gets the visibilities of this WSDataSet.

        :return: The visibilities of this WSDataSet.
        :rtype: list[WSVisibility]
        """
        return self._visibilities

    @visibilities.setter
    def visibilities(self, visibilities):
        """
        Sets the visibilities of this WSDataSet.

        :param visibilities: The visibilities of this WSDataSet.
        :type: list[WSVisibility]
        """

        self._visibilities = visibilities

    @property
    def confidential(self):
        """
        Gets the confidential of this WSDataSet.

        :return: The confidential of this WSDataSet.
        :rtype: bool
        """
        return self._confidential

    @confidential.setter
    def confidential(self, confidential):
        """
        Sets the confidential of this WSDataSet.

        :param confidential: The confidential of this WSDataSet.
        :type: bool
        """

        self._confidential = confidential

    @property
    def info(self):
        """
        Gets the info of this WSDataSet.

        :return: The info of this WSDataSet.
        :rtype: WSContentInformation
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this WSDataSet.

        :param info: The info of this WSDataSet.
        :type: WSContentInformation
        """

        self._info = info

    @property
    def externalable_info(self):
        """
        Gets the externalable_info of this WSDataSet.

        :return: The externalable_info of this WSDataSet.
        :rtype: WSExternalableInformation
        """
        return self._externalable_info

    @externalable_info.setter
    def externalable_info(self, externalable_info):
        """
        Sets the externalable_info of this WSDataSet.

        :param externalable_info: The externalable_info of this WSDataSet.
        :type: WSExternalableInformation
        """

        self._externalable_info = externalable_info

    @property
    def open_access_embargo_months(self):
        """
        Gets the open_access_embargo_months of this WSDataSet.

        :return: The open_access_embargo_months of this WSDataSet.
        :rtype: int
        """
        return self._open_access_embargo_months

    @open_access_embargo_months.setter
    def open_access_embargo_months(self, open_access_embargo_months):
        """
        Sets the open_access_embargo_months of this WSDataSet.

        :param open_access_embargo_months: The open_access_embargo_months of this WSDataSet.
        :type: int
        """

        self._open_access_embargo_months = open_access_embargo_months

    @property
    def open_access_embargo_date(self):
        """
        Gets the open_access_embargo_date of this WSDataSet.

        :return: The open_access_embargo_date of this WSDataSet.
        :rtype: datetime
        """
        return self._open_access_embargo_date

    @open_access_embargo_date.setter
    def open_access_embargo_date(self, open_access_embargo_date):
        """
        Sets the open_access_embargo_date of this WSDataSet.

        :param open_access_embargo_date: The open_access_embargo_date of this WSDataSet.
        :type: datetime
        """

        self._open_access_embargo_date = open_access_embargo_date

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
        if not isinstance(other, WSDataSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other