# API NEWS & BLOGS * Best Practices and Tips

To use the API, you need to call an endpoint URL with your private access token. You can generate the URL for your call in our API Visual Tester (which you can access at [https://dashboard.trawlingweb.com/playground](https://dashboard.trawlingweb.com/playground)).


## Example Call

The API call is constructed from the basic structure:
```
http://api.trawlingweb.com/?token=0000000000000000000000000000&q=casa
```

This structure includes:
* **News & Blogs API Subdomain**: `http://api.trawlingweb.com/`
* **Access Token (API key)**: `token=0000000000000000000000000000` to validate usage.
* **Query (Q)**: `q=house` to execute the query (which in this case searches for results containing the word "casa").

This is the minimum structure to access the News & Blogs API, but from here you can use the parameters available in this documentation to refine and optimize queries according to user needs.


## Example Output
Below is an example output of an API call. This output includes information about the remaining results, the total number of results, and the URL to obtain the next results.

```
requestLeft	9999999
totalResults	295404987
restResults	295404887
next	"http://api.trawlingweb.com/?token=0000000000000000000000000000&q=house&ts=1517443760316&tsi=1524818189854"

```

## Use of `published` and `crawled` Dates

Trawlingweb provides two dates for each news item: `published` (publication date) and `crawled` (indexing date). This distinction is crucial because when incorporating new sections, the system may detect as new news items that were published days or even months ago.

It is also possible for media outlets to modify their publication systems, leading to the appearance of old news due to errors or SEO strategies. To prevent or control these occurrences, we advise clients to implement security rules in their systems.

### Tips for Rules to Ensure Proper Use of Dates:

* **Date Filters**: Set filters to ignore news items with very old publication dates.
* **Relevance Rules**: Create criteria to determine the relevance of news items based on their publication date and indexing date.
* **Monitoring Changes**: Monitor changes in media publication systems to adjust indexing and processing rules accordingly.
* **Alerts and Notifications**: Configure alerts to detect and notify the appearance of old news items, allowing for manual review if necessary.

Implementing these measures helps our clients maintain the integrity and relevance of the data indexed by TrawlingWeb.

## Pagination
Each API request can return a maximum of 100 messages that match your query. However, there may be many more results that match your filter parameters. To consume all the data, you must continue making calls to the URL indicated in the **next** parameter of the output of each request.

Depending on the sorting criteria and desired order for results, the "next" URL includes the values &ts and &tsi, which adjust according to how the results are sorted. Both &ts and &tsi are timestamps (UnixMicrotime).

By default, the news and blogs API returns 100 results per request, even though the total number of matching news items may be higher (e.g., 300 results). The JSON response will include the next parameter, which allows for making an additional API call to fetch the next page of results. This process repeats until all available results are consumed.

Additionally, it is possible to modify the number of results desired per API call. If you need to receive fewer than 100 results per API call, you can adjust this number using the size=n parameter.

## Pagination Modes

Cases and examples of pagination operational modes.

#### Case 1:
&sort=**crawled** &order=**asc** _(Default mode that can deliver up to a maximum of 100 results)_

example: 
```
https://api.trawlingweb.com/?token=0000000000000000000&q=obama&sort=crawled&order=desc&ts=1719784800000&tsi=1720130400000
```

Explanation:
* **Search**: Searches for news containing the word "obama" in the text ***(q=obama)***
* **Grouping*: News items are organized by indexing date ***(sort=crawled)***
* **Sorting**: News items are sorted from oldest to newest ***(order=asc)***
* **Results**: If size=n is not defined, the maximum is always 100.
* **Next**: The "next" parameter in the JSON allows jumping to the next set of results, with a maximum of 100.

#### Case 2:
&sort=**published** &order=**desc** _(Default mode that can deliver up to a maximum of 100 results)_

example: 
```
https://api.trawlingweb.com/?token=0000000000000000000&q=obama&sort=published&order=desc&ts=1719784800000&tsi=1720130400000
```

Explanation:
* **Search**: Searches for news containing the word "obama" in the text ***(q=obama)***
* **Grouping*: News items are organized by publication date ***(sort=published)***
* **Sorting**: News items are sorted from newest to oldest ***(order=desc)***
* **Results**: If size=n is not defined, the maximum is always 100.
* **Next**: The "next" parameter in the JSON allows jumping to the next set of results, with a maximum of 100.

#### Case 3:
&sort=**published** &order=**desc** &size=**4** _(Default mode that can deliver up to a maximum of 100 results)_

example: 
```
https://api.trawlingweb.com/?token=0000000000000000000&q=obama&sort=published&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explanation:
* **Search**: Searches for news containing the word "obama" in the text ***(q=obama)***
* **Grouping*: News items are organized by publication date ***(sort=published)***
* **Sorting**: News items are sorted from newest to oldest ***(order=desc)***
* **Results**: With size=4 defined, the maximum will always be 4 per pagination.
* **Next**: The "next" parameter in the JSON allows jumping to the next set of results, which will be the number defined by size=n; in this case, size=4 means 4 results.

## Search (`q=`)
Review sections 04_Filtering_Parameter and 05_Syntax_for_Queries to properly handle `q=`.

## Grouping (`sort=`)

The grouping parameter is used with the following syntax: `sort=`. This allows grouping news items by two types of temporal criteria:

* **Crawled**: Groups by indexing date. The date used in the API call is the date the news article or post was indexed. `sort=crawled`
* **Published**: Groups by publication date. The date used in the API call is the date the news article or post was originally published by its creator. `sort=published`

### Example 1: Grouping by indexing date

example: 
```
https://api.trawlingweb.com/?token=0000000000000000000&q=obama&sort=crawled&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explanation:
* **Search**: Searches for news containing the word "obama" in the text ***(q=obama)***
* **Grouping*: News items are organized by indexing date ***(sort=crawled)***
* **Sorting**: News items are sorted from newest to oldest ***(order=desc)***
* **Results**: With size=4 defined, the maximum will always be 4 per pagination.
* **Next**: The "next" parameter in the JSON allows jumping to the next set of results, which will be the number defined by size=n; in this case, size=4 means 4 results.

### Example 2: Grouping by publication date

example: 
```
https://api.trawlingweb.com/?token=0000000000000000000&q=obama&sort=published&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explanation:
* **Search**: Searches for news containing the word "obama" in the text ***(q=obama)***
* **Grouping*: News items are organized by publication date ***(sort=published)***
* **Sorting**: News items are sorted from newest to oldest ***(order=desc)***
* **Results**: With size=4 defined, the maximum will always be 4 per pagination.
* **Next**: The "next" parameter in the JSON allows jumping to the next set of results, which will be the number defined by size=n; in this case, size=4 means 4 results.

#### Tips:
* If we want to get results grouped by indexing date, we use `sort=crawled`, and if we want to get results grouped by publication date, we use `sort=published`.
* If we do not use the `sort=` parameter, the default grouping will be by `crawled`.

## Ordering (`order=`)

The sorting parameter is used with the following syntax: `order=`. This allows ordering the grouping criterion in ascending or descending order:

* **order=asc**: Sorts the `sort` grouping criterion in ascending order.
* **order=desc**: Sorts the `sort` grouping criterion in descending order.

### Examples:

* To get results grouped by indexing date in ***ascending*** order, use `sort=crawled&order=asc`.
* To get results grouped by publication date in ***descending*** order, use `sort=published&order=desc`.

## Number of Results (`size=`)
As mentioned in the previous section "Pagination," each call to this API returns a maximum of 100 results by default. However, as demonstrated in the pagination examples, this maximum number of returned results can be adjusted according to usage needs for the calls.

To modify the maximum number of results returned by the API call, use the `size=` parameter.

## Examples:
* No use of `size=`: It will return up to 100 results if available.
* `size=1`: It will return only one result per pagination, regardless of whether more results are available.
* `size=20`: It will return a maximum of 20 results per pagination, regardless of whether more results are available.


## Periodic Maintenance of Media Sources

Periodic maintenance of media sources is continuous and core to TrawlingWeb, involving a comprehensive reevaluation of each source, often including adding new sections to index previously unprocessed content. Having both indexing (`crawled`) and publication (`published`) dates allows for efficient management of these updates.

When adding new media sources to our coverage, we often include their history by conducting an initial deep indexing of all their sections. Again, indexing (`crawled`) and publication (`published`) dates facilitate this process.

Certain sections of media outlets, in addition to chronological content, display non-chronological content (such as rankings or related news) that we also index.

### Considerations

* **Indexing Frequency**: The indexing frequency of a media source is determined by client needs, functional requirements, the volume of news, and the frequency of publication by the media outlet.
* **Differentiating Dates**: Clearly differentiating indexing (`crawled`) and publication (`published`) dates allows clients to decide which news to incorporate.
* **Information Delivery Philosophy**: Our philosophy is to deliver all indexed news, leaving the decision on how to use this information to the clients.

### Delivered and Discarded News

* **Delivered News**: All indexed news is delivered to the client.
* **Discarded News**: Clients have the option to discard news based on their specific criteria and needs.

## Lucene Query Syntax

TrawlingWeb APIs allow for queries that can contain boolean operators based on Lucene syntax, providing a powerful tool for conducting complex and precise searches. The Lucene query syntax is designed to be intuitive and expressive.

For details on how to properly use boolean expressions and Lucene syntax, refer to section 03_consultas.

---
**Contact Us:**
If you have any questions, need assistance, want to hire or expand your services, please contact us.
**Technical Support (SAT):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://docs.trawlingweb.com)

**Administrative Support (SAC):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales Support (Sales):**
* [Sales Email](mailto:sales@trawlingweb.com)

