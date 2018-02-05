# WSDataSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**html_renderings** | [**list[WSHtmlRendering]**](WSHtmlRendering.md) |  | [optional] 
**titles** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**descriptions** | [**list[WSClassifiedLocalizedValue]**](WSClassifiedLocalizedValue.md) |  | [optional] 
**temporal_coverage_period** | [**WSCompoundDateRange**](WSCompoundDateRange.md) |  | [optional] 
**data_production_period** | [**WSCompoundDateRange**](WSCompoundDateRange.md) |  | [optional] 
**classified_sources** | [**list[WSClassifiedValue]**](WSClassifiedValue.md) |  | [optional] 
**geographical_coverages** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**geo_location** | [**WSGeoLocation**](WSGeoLocation.md) |  | [optional] 
**person_associations** | [**list[WSClassifiedDataSetPersonAssociation]**](WSClassifiedDataSetPersonAssociation.md) |  | [optional] 
**managing_organisational_unit** | [**WSOrganisationRef**](WSOrganisationRef.md) |  | [optional] 
**publisher** | [**WSPublisherRef**](WSPublisherRef.md) |  | [optional] 
**doi** | **str** |  | [optional] 
**documents** | [**list[WSDocument]**](WSDocument.md) |  | [optional] 
**physical_datas** | [**list[WSDataSetPhysicalData]**](WSDataSetPhysicalData.md) |  | [optional] 
**contact_person** | [**WSPersonRef**](WSPersonRef.md) |  | [optional] 
**legal_conditions** | [**list[WSDataSetLegalCondition]**](WSDataSetLegalCondition.md) |  | [optional] 
**organisations** | [**list[WSOrganisationRef]**](WSOrganisationRef.md) |  | [optional] 
**external_organisations** | [**list[WSExternalOrganisationRef]**](WSExternalOrganisationRef.md) |  | [optional] 
**publication_date** | [**WSCompoundDate**](WSCompoundDate.md) |  | [optional] 
**open_access_permissions** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**related_data_sets** | [**list[WSDataSetRef]**](WSDataSetRef.md) |  | [optional] 
**related_projects** | [**list[WSUPMProjectRef]**](WSUPMProjectRef.md) | Only available when the Unified Project Model module is enabled | [optional] 
**related_research_outputs** | [**list[WSResearchOutputRef]**](WSResearchOutputRef.md) |  | [optional] 
**related_activities** | [**list[WSActivityRef]**](WSActivityRef.md) | Only available when the Activity module is enabled | [optional] 
**related_press_media** | [**list[WSPressMediaRef]**](WSPressMediaRef.md) | Only available when the Press / Media module is enabled | [optional] 
**related_student_thesis** | [**list[WSStudentThesisRef]**](WSStudentThesisRef.md) | Only available when the Student Thesis module is enabled | [optional] 
**related_impacts** | [**list[WSImpactRef]**](WSImpactRef.md) | Only available when the Impact module is enabled | [optional] 
**related_prizes** | [**list[WSPrizeRef]**](WSPrizeRef.md) | Only available when the Prize module is enabled | [optional] 
**nature_types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**links** | [**list[WSLink]**](WSLink.md) |  | [optional] 
**workflows** | [**list[WSWorkflow]**](WSWorkflow.md) |  | [optional] 
**keyword_groups** | [**list[WSKeywordGroup]**](WSKeywordGroup.md) |  | [optional] 
**visibilities** | [**list[WSVisibility]**](WSVisibility.md) |  | [optional] 
**confidential** | **bool** |  | [optional] [default to False]
**info** | [**WSContentInformation**](WSContentInformation.md) |  | [optional] 
**externalable_info** | [**WSExternalableInformation**](WSExternalableInformation.md) |  | [optional] 
**open_access_embargo_months** | **int** |  | [optional] 
**open_access_embargo_date** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


