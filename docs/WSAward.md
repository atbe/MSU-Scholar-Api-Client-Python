# WSAward

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**html_renderings** | [**list[WSHtmlRendering]**](WSHtmlRendering.md) |  | [optional] 
**titles** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**nature_types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**statuses** | [**list[WSAwardStatus]**](WSAwardStatus.md) |  | [optional] 
**status_details** | [**WSAwardStatusDetails**](WSAwardStatusDetails.md) | Only available when the Award Management module is enabled | [optional] 
**short_titles** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**acronym** | **str** |  | [optional] 
**descriptions** | [**list[WSClassifiedLocalizedValue]**](WSClassifiedLocalizedValue.md) |  | [optional] 
**classified_sources** | [**list[WSClassifiedValue]**](WSClassifiedValue.md) |  | [optional] 
**awardholders** | [**list[WSClassifiedAwardholderAssociation]**](WSClassifiedAwardholderAssociation.md) |  | [optional] 
**organisations** | [**list[WSOrganisationRef]**](WSOrganisationRef.md) |  | [optional] 
**external_organisations** | [**list[WSExternalOrganisationRef]**](WSExternalOrganisationRef.md) |  | [optional] 
**managing_organisational_unit** | [**WSOrganisationRef**](WSOrganisationRef.md) |  | [optional] 
**collaborative** | **bool** |  | [optional] [default to False]
**collaborators** | [**list[WSCollaboratorAssociation]**](WSCollaboratorAssociation.md) |  | [optional] 
**total_academic_ownership_percentage** | **float** |  | [optional] 
**fundings** | [**list[WSAwardFundingAssociation]**](WSAwardFundingAssociation.md) |  | [optional] 
**total_awarded_amount** | **float** |  | [optional] 
**total_spend_amount** | **float** |  | [optional] 
**actual_period** | [**WSDateRange**](WSDateRange.md) |  | [optional] 
**expected_period** | [**WSDateRange**](WSDateRange.md) |  | [optional] 
**award_date** | **datetime** |  | [optional] 
**curtailed** | **bool** |  | [optional] [default to False]
**curtail_date** | **datetime** |  | [optional] 
**curtail_reason** | **str** |  | [optional] 
**documents** | [**list[WSDocument]**](WSDocument.md) |  | [optional] 
**links** | [**list[WSLink]**](WSLink.md) |  | [optional] 
**related_project** | [**WSUPMProjectRef**](WSUPMProjectRef.md) |  | [optional] 
**related_applications** | [**list[WSApplicationRef]**](WSApplicationRef.md) |  | [optional] 
**related_awards** | [**list[WSAwardRef]**](WSAwardRef.md) |  | [optional] 
**field_of_research_associations** | [**list[WSERA2015FieldOfResearchAssociation]**](WSERA2015FieldOfResearchAssociation.md) | Only available when the ERA module is enabled | [optional] 
**keyword_groups** | [**list[WSKeywordGroup]**](WSKeywordGroup.md) |  | [optional] 
**visibilities** | [**list[WSVisibility]**](WSVisibility.md) |  | [optional] 
**confidential** | **bool** |  | [optional] [default to False]
**workflows** | [**list[WSWorkflow]**](WSWorkflow.md) |  | [optional] 
**externalable_info** | [**WSExternalableInformation**](WSExternalableInformation.md) |  | [optional] 
**info** | [**WSContentInformation**](WSContentInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


