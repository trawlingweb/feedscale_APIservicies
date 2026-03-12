# TWITTER API - Best Practices and Tips

To use the Twitter API, you need to call an endpoint URL with your private access token. You can generate your call URL in our Visual API Tester, accessible at [https://dashboard.trawlingweb.com/playground](https://dashboard.trawlingweb.com/playground).

## Example Call

The API call is constructed from the basic structure:

```
http://twitter.trawlingweb.com/010101010101010101?token=0000000000000000000000000000&q=house
```


This structure includes:
- **Twitter API Subdomain**: `http://twitter.trawlingweb.com/`
* **IDworker**: `010101010101010101` example numeric ID of a worker necessary to use recovery keywords stored within a worker and created previously.
- **Access Token (API key)**: `token=0000000000000000000000000000` to validate usage.
- **Query (Q)**: `q=house` to execute the query (which in this case searches for results containing the word house).

This is the minimum structure to access the Twitter API, but from here you can use the parameters available in this documentation to refine and optimize the queries according to the user's needs.

## Example Output

Below is an example of output from an API call. This output includes information about the remaining results, the total number of results, and the URL to get the next results.

```
requestLeft 9999999
totalResults 295404987
restResults 295404887
next "http://twitter.trawlingweb.com/010101010101010101?token=0000000000000000000000000000
```


## Using `published` and `crawled` Dates

TrawlingWeb provides two dates for each tweet: `published` (creation date) and `crawled` (capture date). This is crucial as, when incorporating new sections, the system may detect as new tweets that were published days or even months ago.

It can also happen that Twitter modifies its system, which may cause the appearance of old tweets due to errors or SEO strategies. To avoid or control these occurrences, we advise clients to implement security rules in their systems.

### Tips for rules to ensure proper use of dates:

- **Date Filters**: Set filters to ignore tweets with very old creation dates.
- **Relevance Rules**: Create criteria that determine the relevance of tweets based on their creation and processing dates.
- **Change Monitoring**: Monitor changes in the Twitter system to adjust indexing and processing rules accordingly.
- **Alerts and Notifications**: Set up alerts to detect and notify the appearance of old tweets, allowing for manual review if necessary.

Implementing these measures helps our clients maintain the integrity and relevance of the data processed by TrawlingWeb.

## Pagination

Each request to the Twitter API can return a maximum of 500 tweets matching your query. However, there may be many more results that match your filter parameters. To consume all the data, you must continue making calls to the URL indicated in the **next** parameter of the output of each request.

Depending on the sorting criteria and the desired order for the results, the "next" URL includes the `&ts` and `&tsi` values, which adjust according to how the results are sorted. Both `&ts` and `&tsi` are UnixMicrotime timestamps.

By default, the Twitter API returns 500 results per request, although the total matching tweets may be greater. The JSON response will include the `next` parameter, which is used to make an additional API call to get the next page of results. This process is repeated until all available results are consumed.

Additionally, you can modify the number of results you want to get per request. If you need to receive fewer than 500 results per API call, you can adjust this number using the `size=n` parameter.

## Pagination Modes

Cases and examples of pagination modes.

#### Case 1:
`&sort=published&order=asc` _(Default mode that can return up to 500 results)_

example: 
```
https://twitter.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=published&order=asc&ts=1719784800000&tsi=1720130400000
```

Explanation:
* **Organization**: Tweets are organized by creation date ***(sort=published)***
* **Ordering**: Tweets are sorted from old to new ***(order=asc)***.
* **Results**: Without defining `size=n`, the maximum will always be 500.
* **Next**: The "next" in the JSON allows you to jump to the next results, which will be a maximum of 500.

#### Case 2:
`&sort=published&order=desc` _(Default mode that can return up to 500 results)_

example: 
```
https://twitter.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=published&order=desc&ts=1719784800000&tsi=1720130400000
```

Explanation:
* **Organization**: Tweets are organized by creation date ***(sort=published)***
* **Ordering**: Tweets are sorted from new to old ***(order=desc)***.
* **Results**: Without defining `size=n`, the maximum will always be 500.
* **Next**: The "next" in the JSON allows you to jump to the next results, which will be a maximum of 500.

#### Case 3:
`&sort=published&order=desc&size=4` _(Default mode that can return up to 500 results)_

example: 
```
https://twitter.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=published&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explanation:
* **Organization**: Tweets are organized by creation date ***(sort=published)***
* **Ordering**: Tweets are sorted from new to old ***(order=desc)***.
* **Results**: Defining `size=4`, the maximum will always be 4 in each pagination.
* **Next**: The "next" in the JSON allows you to jump to the next results, which will be a maximum of those defined in `size=n`, which in this case being `size=4` will be 4 results.

## Grouping

The grouping parameter is used with the following syntax: `sort=`. This allows tweets to be grouped by two types of temporal criteria:

* **published**: Groups by creation date. The date used in the API call is the date the tweet was created. `sort=published`
* **Crawled**: Groups by capture date. The date used in the API call is the date the tweet was captured. `sort=crawled`

### Example 1: Group by creation date

example: 
```
https://twitter.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=published&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explanation:
* **Organization**: Tweets are organized by creation date ***(sort=published)***
* **Ordering**: Tweets are sorted from new to old ***(order=desc)***.
* **Results**: Defining `size=4`, the maximum will always be 4 in each pagination.
* **Next**: The "next" in the JSON allows you to jump to the next results, which will be a maximum of those defined in `size=n`, which in this case being `size=4` will be 4 results.

### Example 2: Group by processing date

example: 
```
https://twitter.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=crawled&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explanation:
* **Organization**: Tweets are organized by capture date ***(sort=crawled)***
* **Ordering**: Tweets are sorted from new to old ***(order=desc)***.
* **Results**: Defining `size=4`, the maximum will always be 4 in each pagination.
* **Next**: The "next" in the JSON allows you to jump to the next results, which will be a maximum of those defined in `size=n`, which in this case being `size=4` will be 4 results.

#### Tips:
* If we want to get results grouped by creation date, we will use `sort=published`, and if we want to get results grouped by capture date, we will use `sort=crawled`.
* If we do not use the `sort=` parameter, the default grouping will be `published`.

## Sorting

The sorting parameter is used with the following syntax: `order=`. This allows the grouping criteria to be sorted in ascending or descending order:

* **order=asc**: Sorts the `sort` grouping in ascending order.
* **order=desc**: Sorts the `sort` grouping in descending order.

### Examples:

* If we want to get results grouped by creation date in ascending order, we will use `sort=published&order=asc`.
* If we want to get results grouped by creation date in descending order, we will use `sort=published&order=desc`.

## Number of Results

As mentioned in the previous section "Pagination," each call to this API returns by default a maximum of 500 results. However, as shown in the pagination examples, this maximum number of results returned can be adjusted according to usage needs.

To modify the maximum number of results returned by the API call, use the `size=` parameter.

## Examples:
* No use of `size=`: Will return a maximum of 500 results if available.
* `size=1`: Will return only one result in each pagination, regardless of whether more results are available.
* `size=20`: Will return a maximum of 20 results in each pagination, regardless of whether more results are available.

## Periodic Data Source Maintenance

Periodic maintenance of data sources is constant and essential at TrawlingWeb. It involves a comprehensive reevaluation of each source, often incorporating new sections to index content not previously collected. Having the creation (`published`) and capture (`crawled`) dates allows us to manage these updates efficiently.

When adding new data sources to our coverage, we frequently include their history by performing a deep initial indexing of all their sections. Again, the creation (`published`) and capture (`crawled`) dates facilitate this process.

Certain sections of Twitter, in addition to chronological content, may display non-chronological content (such as highlighted or related tweets) that we also index.

### Considerations

* **Indexing Frequency**: The indexing frequency of a data source is determined by client needs, functional requirements, the number of tweets, and the publication frequency of the source.
* **Date Differentiation**: Clearly differentiating the capture date (`crawled`) from the creation date (`published`) allows clients to decide which tweets to incorporate.
* **Content Delivery Philosophy**: Our philosophy is to deliver all processed tweets, leaving the decision on how to use this content to the clients.

### Delivered and Discarded Tweets

* **Delivered Tweets**: All processed tweets are delivered to the client.
* **Discarded Tweets**: Clients have the option to discard tweets according to their specific criteria and needs.

## Lucene Query Syntax

TrawlingWeb APIs allow queries that can contain boolean operators based on Lucene syntax, offering a powerful tool for performing complex and precise searches. The Lucene query syntax is designed to be intuitive and expressive.

In section 03_consultas you will find how to properly use boolean expressions and Lucene syntax.

---

# Contact

If you have any questions, need assistance, want to hire or expand your services, please contact us.

**Technical Support (SAT):**
* [Email SAT](mailto:support@trawlingweb.com)
* [Official Documentation](https://docs.trawlingweb.com)

**Administrative Support (SAC):**
* [Email SAC](mailto:gestion@trawlingweb.com)

**Sales Support:**
* [Email Sales](mailto:sales@trawlingweb.com)
