# msu_scholars_api.OrganisationalunitsApi

All URIs are relative to *https://localhosthttps://scholars.opb.msu.edu/ws/api/510/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_orderings**](OrganisationalunitsApi.md#get_available_orderings) | **GET** /organisational-units-meta/orderings | Lists available orderings
[**get_available_renderings**](OrganisationalunitsApi.md#get_available_renderings) | **GET** /organisational-units-meta/renderings | Lists available renderings
[**get_organisational_unit**](OrganisationalunitsApi.md#get_organisational_unit) | **GET** /organisational-units/{id} | Get organisational unit
[**list_active_organisational_units**](OrganisationalunitsApi.md#list_active_organisational_units) | **GET** /organisational-units/active | Lists all active organisational units
[**list_former_organisational_units**](OrganisationalunitsApi.md#list_former_organisational_units) | **GET** /organisational-units/former | Lists all former organisational units
[**list_organisational_unit_activities**](OrganisationalunitsApi.md#list_organisational_unit_activities) | **GET** /organisational-units/{id}/activities | Lists activities on an organisational unit
[**list_organisational_unit_applications**](OrganisationalunitsApi.md#list_organisational_unit_applications) | **GET** /organisational-units/{id}/applications | Lists applications on an organisational unit
[**list_organisational_unit_awards**](OrganisationalunitsApi.md#list_organisational_unit_awards) | **GET** /organisational-units/{id}/awards | Lists awards on an organisational unit
[**list_organisational_unit_fingerprints**](OrganisationalunitsApi.md#list_organisational_unit_fingerprints) | **GET** /organisational-units/{id}/fingerprints | Lists fingerprints on an organisational unit
[**list_organisational_unit_persons**](OrganisationalunitsApi.md#list_organisational_unit_persons) | **GET** /organisational-units/{id}/persons | Lists persons on an organisational unit
[**list_organisational_unit_press_media**](OrganisationalunitsApi.md#list_organisational_unit_press_media) | **GET** /organisational-units/{id}/press-media | Lists press / media on an organisational unit
[**list_organisational_unit_prizes**](OrganisationalunitsApi.md#list_organisational_unit_prizes) | **GET** /organisational-units/{id}/prizes | Lists prizes on an organisational unit
[**list_organisational_unit_projects**](OrganisationalunitsApi.md#list_organisational_unit_projects) | **GET** /organisational-units/{id}/projects | Lists projects on an organisational unit
[**list_organisational_unit_research_outputs**](OrganisationalunitsApi.md#list_organisational_unit_research_outputs) | **GET** /organisational-units/{id}/research-outputs | Lists research outputs on an organisational unit
[**list_organisational_unit_student_theses**](OrganisationalunitsApi.md#list_organisational_unit_student_theses) | **GET** /organisational-units/{id}/student-theses | Lists student-theses on an organisational unit
[**list_organisational_units**](OrganisationalunitsApi.md#list_organisational_units) | **GET** /organisational-units | Lists all organisational units
[**list_organisational_units_0**](OrganisationalunitsApi.md#list_organisational_units_0) | **POST** /organisational-units | Complex operation for organisational units


# **get_available_orderings**
> WSOrderingsList get_available_orderings()

Lists available orderings

Lists all orderings available to the organisational unit endpoint. These values can be used by the order parameter

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()

try: 
    # Lists available orderings
    api_response = api_instance.get_available_orderings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->get_available_orderings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WSOrderingsList**](WSOrderingsList.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_renderings**
> WSRenderingsList get_available_renderings()

Lists available renderings

Lists all renderings available to the organisational unit endpoint. These values can be used by the rendering parameter

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()

try: 
    # Lists available renderings
    api_response = api_instance.get_available_renderings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->get_available_renderings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WSRenderingsList**](WSRenderingsList.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organisational_unit**
> WSOrganisation get_organisational_unit(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Get organisational unit

Get organisational unit with specific ID (path parameter).

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
id = 'id_example' # str | Id of the desired organisational unit
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Get organisational unit
    api_response = api_instance.get_organisational_unit(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->get_organisational_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the desired organisational unit | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSOrganisation**](WSOrganisation.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_active_organisational_units**
> WSOrganisationListResult list_active_organisational_units(q=q, order=order, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, linking_strategy=linking_strategy, return_used_content=return_used_content, navigation_link=navigation_link, size=size, offset=offset, page=page, page_size=page_size)

Lists all active organisational units

Lists all active organisational units in the PURE installation

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
q = 'q_example' # str | Free text search string using Lucene query syntax. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#q_param\">Read more</a> (optional)
order = ['order_example'] # list[str] | Specify the ordering of content in the result. Default: ID ascending. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#order_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
linking_strategy = 'linking_strategy_example' # str | Specifies the linking strategy to use used when creating HTML renderings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#linkingStrategy_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)
size = 56 # int | Enter the number of results per window. Default: 10. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\">Read more</a> (optional)
offset = 56 # int | Enter the offset into the total result set where items should be returned from. Default: 0. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\">Read more</a> (optional)
page = 56 # int | Enter the desired page number. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\">Read more</a> (optional)
page_size = 56 # int | Enter the desired number of results per page. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\">Read more</a> (optional)

try: 
    # Lists all active organisational units
    api_response = api_instance.list_active_organisational_units(q=q, order=order, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, linking_strategy=linking_strategy, return_used_content=return_used_content, navigation_link=navigation_link, size=size, offset=offset, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_active_organisational_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Free text search string using Lucene query syntax. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#q_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **order** | [**list[str]**](str.md)| Specify the ordering of content in the result. Default: ID ascending. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#order_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **linking_strategy** | **str**| Specifies the linking strategy to use used when creating HTML renderings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#linkingStrategy_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **size** | **int**| Enter the number of results per window. Default: 10. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **offset** | **int**| Enter the offset into the total result set where items should be returned from. Default: 0. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **page** | **int**| Enter the desired page number. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **page_size** | **int**| Enter the desired number of results per page. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSOrganisationListResult**](WSOrganisationListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_former_organisational_units**
> WSOrganisationListResult list_former_organisational_units(q=q, order=order, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, linking_strategy=linking_strategy, return_used_content=return_used_content, navigation_link=navigation_link, size=size, offset=offset, page=page, page_size=page_size)

Lists all former organisational units

Lists all former organisational units in the PURE installation

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
q = 'q_example' # str | Free text search string using Lucene query syntax. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#q_param\">Read more</a> (optional)
order = ['order_example'] # list[str] | Specify the ordering of content in the result. Default: ID ascending. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#order_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
linking_strategy = 'linking_strategy_example' # str | Specifies the linking strategy to use used when creating HTML renderings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#linkingStrategy_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)
size = 56 # int | Enter the number of results per window. Default: 10. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\">Read more</a> (optional)
offset = 56 # int | Enter the offset into the total result set where items should be returned from. Default: 0. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\">Read more</a> (optional)
page = 56 # int | Enter the desired page number. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\">Read more</a> (optional)
page_size = 56 # int | Enter the desired number of results per page. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\">Read more</a> (optional)

try: 
    # Lists all former organisational units
    api_response = api_instance.list_former_organisational_units(q=q, order=order, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, linking_strategy=linking_strategy, return_used_content=return_used_content, navigation_link=navigation_link, size=size, offset=offset, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_former_organisational_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Free text search string using Lucene query syntax. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#q_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **order** | [**list[str]**](str.md)| Specify the ordering of content in the result. Default: ID ascending. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#order_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **linking_strategy** | **str**| Specifies the linking strategy to use used when creating HTML renderings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#linkingStrategy_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **size** | **int**| Enter the number of results per window. Default: 10. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **offset** | **int**| Enter the offset into the total result set where items should be returned from. Default: 0. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **page** | **int**| Enter the desired page number. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **page_size** | **int**| Enter the desired number of results per page. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSOrganisationListResult**](WSOrganisationListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organisational_unit_activities**
> WSActivityListResult list_organisational_unit_activities(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Lists activities on an organisational unit

Lists all activities associated to the organisational unit specified by an ID (supplied as path parameter)

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
id = 'id_example' # str | id
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Lists activities on an organisational unit
    api_response = api_instance.list_organisational_unit_activities(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_organisational_unit_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSActivityListResult**](WSActivityListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organisational_unit_applications**
> WSApplicationListResult list_organisational_unit_applications(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Lists applications on an organisational unit

Lists all applications associated to the organisational unit specified by an ID (supplied as path parameter)

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
id = 'id_example' # str | id
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Lists applications on an organisational unit
    api_response = api_instance.list_organisational_unit_applications(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_organisational_unit_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSApplicationListResult**](WSApplicationListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organisational_unit_awards**
> WSAwardListResult list_organisational_unit_awards(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Lists awards on an organisational unit

Lists all awards associated to the organisational unit specified by an ID (supplied as path parameter)

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
id = 'id_example' # str | id
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Lists awards on an organisational unit
    api_response = api_instance.list_organisational_unit_awards(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_organisational_unit_awards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSAwardListResult**](WSAwardListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organisational_unit_fingerprints**
> WSFingerprintListResult list_organisational_unit_fingerprints(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Lists fingerprints on an organisational unit

Lists all fingerprints associated to the organisational unit specified by an ID (supplied as path parameter)

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
id = 'id_example' # str | id
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Lists fingerprints on an organisational unit
    api_response = api_instance.list_organisational_unit_fingerprints(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_organisational_unit_fingerprints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSFingerprintListResult**](WSFingerprintListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organisational_unit_persons**
> WSPersonListResult list_organisational_unit_persons(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Lists persons on an organisational unit

Lists all persons associated to the organisational unit specified by an ID (supplied as path parameter)

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
id = 'id_example' # str | id
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Lists persons on an organisational unit
    api_response = api_instance.list_organisational_unit_persons(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_organisational_unit_persons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSPersonListResult**](WSPersonListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organisational_unit_press_media**
> WSPressMediaListResult list_organisational_unit_press_media(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Lists press / media on an organisational unit

Lists all press / media associated to the organisational unit specified by an ID (supplied as path parameter)

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
id = 'id_example' # str | id
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Lists press / media on an organisational unit
    api_response = api_instance.list_organisational_unit_press_media(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_organisational_unit_press_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSPressMediaListResult**](WSPressMediaListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organisational_unit_prizes**
> WSPrizeListResult list_organisational_unit_prizes(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Lists prizes on an organisational unit

Lists all prizes associated to the organisational unit specified by an ID (supplied as path parameter)

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
id = 'id_example' # str | id
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Lists prizes on an organisational unit
    api_response = api_instance.list_organisational_unit_prizes(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_organisational_unit_prizes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSPrizeListResult**](WSPrizeListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organisational_unit_projects**
> WSUPMProjectListResult list_organisational_unit_projects(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Lists projects on an organisational unit

Lists all projects associated to the organisational unit specified by an ID (supplied as path parameter)

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
id = 'id_example' # str | id
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Lists projects on an organisational unit
    api_response = api_instance.list_organisational_unit_projects(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_organisational_unit_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSUPMProjectListResult**](WSUPMProjectListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organisational_unit_research_outputs**
> WSResearchOutputListResult list_organisational_unit_research_outputs(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Lists research outputs on an organisational unit

Lists all research outputs associated to the organisational unit specified by an ID (supplied as path parameter)

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
id = 'id_example' # str | id
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Lists research outputs on an organisational unit
    api_response = api_instance.list_organisational_unit_research_outputs(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_organisational_unit_research_outputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSResearchOutputListResult**](WSResearchOutputListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organisational_unit_student_theses**
> WSStudentThesisListResult list_organisational_unit_student_theses(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Lists student-theses on an organisational unit

Lists all student-theses associated to the organisational unit specified by an ID (supplied as path parameter)

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
id = 'id_example' # str | id
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Lists student-theses on an organisational unit
    api_response = api_instance.list_organisational_unit_student_theses(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_organisational_unit_student_theses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSStudentThesisListResult**](WSStudentThesisListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organisational_units**
> WSOrganisationListResult list_organisational_units(q=q, order=order, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, linking_strategy=linking_strategy, return_used_content=return_used_content, navigation_link=navigation_link, size=size, offset=offset, page=page, page_size=page_size)

Lists all organisational units

Lists all organisational units in the PURE installation. If filtering of the returned organisational units is required, see the POST version which supports additional filtering.

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
q = 'q_example' # str | Free text search string using Lucene query syntax. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#q_param\">Read more</a> (optional)
order = ['order_example'] # list[str] | Specify the ordering of content in the result. Default: ID ascending. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#order_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
linking_strategy = 'linking_strategy_example' # str | Specifies the linking strategy to use used when creating HTML renderings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#linkingStrategy_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)
size = 56 # int | Enter the number of results per window. Default: 10. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\">Read more</a> (optional)
offset = 56 # int | Enter the offset into the total result set where items should be returned from. Default: 0. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\">Read more</a> (optional)
page = 56 # int | Enter the desired page number. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\">Read more</a> (optional)
page_size = 56 # int | Enter the desired number of results per page. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\">Read more</a> (optional)

try: 
    # Lists all organisational units
    api_response = api_instance.list_organisational_units(q=q, order=order, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, linking_strategy=linking_strategy, return_used_content=return_used_content, navigation_link=navigation_link, size=size, offset=offset, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_organisational_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Free text search string using Lucene query syntax. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#q_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **order** | [**list[str]**](str.md)| Specify the ordering of content in the result. Default: ID ascending. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#order_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **linking_strategy** | **str**| Specifies the linking strategy to use used when creating HTML renderings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#linkingStrategy_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **size** | **int**| Enter the number of results per window. Default: 10. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **offset** | **int**| Enter the offset into the total result set where items should be returned from. Default: 0. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **page** | **int**| Enter the desired page number. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **page_size** | **int**| Enter the desired number of results per page. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSOrganisationListResult**](WSOrganisationListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organisational_units_0**
> WSOrganisationListResult list_organisational_units_0(body=body)

Complex operation for organisational units

Lists organisational units in the PURE installation, similar to the GET version, instead of using parameters to alter the response, an XML document is posted with the request. The XML document contains fields for all the parameters available for the GET version, but also additional filtering options. For documentation of the XML format see <a href=\"documentation/Content/Topics/CT_OrganisationalUnit.htm#post_xml\">Organisational unit documentation</a>

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.OrganisationalunitsApi()
body = msu_scholars_api.WSOrganisationsQuery() # WSOrganisationsQuery |  (optional)

try: 
    # Complex operation for organisational units
    api_response = api_instance.list_organisational_units_0(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationalunitsApi->list_organisational_units_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WSOrganisationsQuery**](WSOrganisationsQuery.md)|  | [optional] 

### Return type

[**WSOrganisationListResult**](WSOrganisationListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

