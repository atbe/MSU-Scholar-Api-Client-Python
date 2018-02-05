# WSFundingOpportunity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**html_renderings** | [**list[WSHtmlRendering]**](WSHtmlRendering.md) |  | [optional] 
**types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**titles** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**descriptions** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**classified_sources** | [**list[WSClassifiedValue]**](WSClassifiedValue.md) |  | [optional] 
**announcement_url** | **str** |  | [optional] 
**funding_organisation** | [**WSExternalOrganisationRef**](WSExternalOrganisationRef.md) |  | [optional] 
**opening_date** | **datetime** |  | [optional] 
**letter_of_intent_date** | **datetime** |  | [optional] 
**deadline** | **datetime** |  | [optional] 
**active** | **bool** |  | [optional] [default to False]
**award_ceiling** | **float** |  | [optional] 
**award_ceiling_currencies** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**estimated_funding** | **float** |  | [optional] 
**estimated_funding_currencies** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**eligibilities** | [**list[WSFundingOpportunityEligibility]**](WSFundingOpportunityEligibility.md) |  | [optional] 
**academic_degree_eligibilities** | [**list[WSFundingOpportunityEligibility]**](WSFundingOpportunityEligibility.md) |  | [optional] 
**limited_submission** | **bool** |  | [optional] [default to False]
**number_of_annual_applications_per_hei** | **int** |  | [optional] 
**number_of_awards** | **int** |  | [optional] 
**open_access_requirements** | **bool** |  | [optional] [default to False]
**applications** | [**list[WSApplicationRef]**](WSApplicationRef.md) | Only available when the Unified Project Model module is enabled | [optional] 
**externalable_info** | [**WSExternalableInformation**](WSExternalableInformation.md) |  | [optional] 
**keyword_groups** | [**list[WSKeywordGroup]**](WSKeywordGroup.md) |  | [optional] 
**info** | [**WSContentInformation**](WSContentInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


