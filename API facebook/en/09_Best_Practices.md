# Facebook API - Best Practices and Tips

To use the Facebook API, you need to call an endpoint URL with your private access token. You can generate the URL for your call using our API Visual Tester, accessible at [https://dashboard.trawlingweb.com/playground](https://dashboard.trawlingweb.com/playground).

## Example Call

The API call is constructed from the basic structure:

```
http://facebook.trawlingweb.com/010101010101010101?token=0000000000000000000000000000&q=casa
```

This structure includes:
* **Facebook API Subdomain**: `http://facebook.trawlingweb.com/`
* **IDworker**: `010101010101010101` example numeric ID of a worker necessary for using stored recovery keywords within a worker and previously created
* **Access Token (API key)**: `token=0000000000000000000000000000` to validate usage.
* **Query (Q)**: `q=casa` to execute the query (which in this case searches for results containing the word casa).

This is the minimum structure to access the Facebook API, but from here, the parameters available in this documentation can be used to refine and optimize queries according to user needs.

## Example Output

Below is an example output from an API call. This output includes information about remaining results, the total number of results, and the URL to fetch the next results.

```
requestLeft 9999999
totalResults 295404987
restResults 295404887
next "http://facebook.trawlingweb.com/010101010101010101?token=0000000000000000000000000000
```

## Usage of Dates `created_at` and `crawled`

TrawlingWeb provides two dates for each tweet: `created_at` (creation date) and `crawled` (processing date). This is crucial as, when incorporating new sections, the system may detect as new posts that were actually published days or even months ago.

It can also happen that Facebook modifies its system, which may lead to old posts appearing due to errors or SEO strategies. To prevent or control these occurrences, we advise clients to implement security rules in their systems.

### Tips on rules to ensure proper use of dates:

* **Date Filters**: Set filters to ignore posts with very old creation dates.
* **Relevance Rules**: Create criteria to determine tweet relevance based on their creation date and processing date.
* **Monitoring Changes**: Monitor changes in the Facebook system to adjust processing rules accordingly.
* **Alerts and Notifications**: Configure alerts to detect and notify the appearance of old posts, allowing manual review if necessary.

Implementing these measures helps our clients maintain the integrity and relevance of data processed by TrawlingWeb.

## Pagination

Each request to the Facebook API can return a maximum of 500 posts matching your query. However, there may be many more results matching your filter parameters. To consume all data, you must continue making calls to the URL indicated in the **next** parameter of the output from each request.

Depending on the sorting criteria and desired order for results, the "next" URL includes the values `&ts` and `&tsi`, which adjust according to how results are sorted. Both `&ts` and `&tsi` are UnixMicrotime timestamps.

By default, the Facebook API returns 500 results per request, even though the total matching posts may be greater. The JSON response includes a `next` parameter for making an additional API call to fetch the next page of results. This process repeats until all available results are consumed.

It is also possible to adjust the number of results per request. If you need to receive fewer than 500 results per API call, you can adjust this number using the `size=n` parameter.

## Pagination Modes

Cases and examples of pagination operation modes.

#### Case 1:
`&sort=created_at&order=asc` _(Default mode that can deliver up to a maximum of 500 results)_

example: 
```
https://Facebook.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=created_at&order=asc&ts=1719784800000&tsi=1720130400000
```

Explanation:
* **Organization**: posts are organized by creation date ***(sort=created_at)***
* **Order**: posts are ordered from oldest to newest ***(order=asc)***
* **Results**: Without defining `size=n`, the maximum will always be 500.
* **Next**: The "next" within the JSON allows jumping to the following results, which will be up to a maximum of 500.

#### Case 2:
`&sort=created_at&order=desc` _(Default mode that can deliver up to a maximum of 500 results)_

example:
```
https://Facebook.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=created_at&order=desc&ts=1719784800000&tsi=1720130400000
```

Explanation:
* **Organization**: posts are organized by creation date ***(sort=created_at)***
* **Order**: posts are ordered from newest to oldest ***(order=desc)***
* **Results**: Without defining `size=n`, the maximum will always be 500.
* **Next**: The "next" within the JSON allows jumping to the following results, which will be up to a maximum of 500.

#### Case 3:
`&sort=created_at&order=desc&size=4` _(Default mode that can deliver up to a maximum of 500 results)_

example: 
```
https://Facebook.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=created_at&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explanation:
* **Organization**: posts are organized by creation date ***(sort=created_at)***
* **Order**: posts are ordered from newest to oldest ***(order=desc)***
* **Results**: By defining `size=4`, the maximum will always be 4 per pagination.
* **Next**: The "next" within the JSON allows jumping to the following results, which will be up to the number defined in `size=n`. In this case, with `size=4`, there will be 4 results.

## Grouping

The grouping parameter is used with the syntax: `sort=`. This allows grouping posts by two types of temporal criteria:

- **Created_at**: Groups by creation date. The date used in the API call is when the tweet was created. `sort=created_at`
- **Crawled**: Groups by processing date. The date used in the API call is when the tweet was processed. `sort=crawled`

### Example 1: Grouping by creation date

example:
```
https://Facebook.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=created_at&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explanation:
* **Organization**: posts are organized by creation date ***(sort=created_at)***
* **Order**: posts are ordered from newest to oldest ***(order=desc)***
* **Results**: By defining `size=4`, the maximum will always be 4 per pagination.
* **Next**: The "next" within the JSON allows jumping to the following results, which will be up to the number defined in `size=n`. In this case, with `size=4`, there will be 4 results.

### Example 2: Grouping by processing date

example: 
```
https://Facebook.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=crawled&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explanation:
* **Organization**: posts are organized by processing date ***(sort=crawled)***
* **Order**: posts are ordered from newest to oldest ***(order=desc)***
* **Results**: By defining `size=4`, the maximum will always be 4 per pagination.
* **Next**: The "next" within the JSON allows jumping to the following results, which will be up to the number defined in `size=n`. In this case, with `size=4`, there will be 4 results.

#### Tips:
* To obtain results grouped by creation date, use `sort=created_at`, and for grouping by processing date, use `sort=crawled`.
- If the `sort=` parameter is not used, the default grouping will be `created_at`.

## Sorting

The sorting parameter is used with the syntax: `order=`. This allows ordering the grouping criterion in ascending or descending order:

* **order=asc**: Sorts the `sort` grouping in ascending order.
* **order=desc**: Sorts the `sort` grouping in descending order.

### Examples:

* To obtain results grouped by creation date in ascending order, use `sort=created_at&order=asc`.
* To obtain results grouped by creation date in descending order, use `sort=created_at&order=desc`.

## Number of Results

As mentioned in the previous "Pagination" section, each API call by default returns a maximum of 500 results. However, as demonstrated in the pagination examples, this maximum number of returned results can be adjusted according to usage needs for the calls.

To modify the maximum number of results returned by the API call, use the `size=` parameter.

## Examples:
* No use of `size=`: Will return a maximum of 500 results if available.
* `size=1`: Will return only one result in each pagination, regardless of whether more results are available.
* `size=20`: Will return a maximum of 20 results in each pagination, regardless of whether more results are available.

## Periodic Maintenance of Data Sources

Periodic maintenance of data sources is constant and essential at TrawlingWeb. It involves a comprehensive reevaluation of each source, often incorporating new sections to process previously uncollected content. Having creation dates (`created_at`) and processing dates (`crawled`) allows managing these updates efficiently.

When adding new data sources to our coverage, we frequently include their history by performing an initial deep indexing of all their sections. Again, creation dates (`created_at`) and processing dates (`crawled`) facilitate this process.

Certain sections of Facebook, in addition to chronological content, may display non-chronological content (such as highlighted or related posts) that we also index.

### Considerations

* **Indexing Frequency**: The indexing frequency of a data source is determined by client needs, functional requirements, tweet volume, and source publication frequency.
* **Date Differentiation**: Clearly differentiating processing date (`crawled`) from creation date (`created_at`) allows clients to decide which posts to incorporate.
* **Content Delivery Philosophy**: Our philosophy is to deliver all processed posts, leaving the decision on how to use this content to the clients.

### Delivered and Discarded posts

* **Delivered posts**: All processed posts are delivered to the client.
* **Discarded posts**: Clients have the option to discard posts based on their specific criteria and needs.

## Lucene Query Syntax

TrawlingWeb's APIs allow for queries that can contain boolean operators based on Lucene syntax, providing a powerful tool for performing complex and precise searches. The Lucene query syntax is designed to be intuitive and expressive.

In section 03_consultas you will find how to properly use boolean expressions and the Lucene syntax.

---

# Contact
If you have any questions, need assistance, want to hire or expand your services, please contact us.

**Technical Support (SAT):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://docs.trawlingweb.com)

**Administrative Support (SAC):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales Support (Sales):**
* [Sales Email](mailto:sales@trawlingweb.com)
