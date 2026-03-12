# API API TikTok - Best Practices and Tips

To use the API TikTok API, you need to call an endpoint URL with your private access token. You can generate the URL for your call using our API Visual Tester, accessible at [https://dashboard.trawlingweb.com/playground](https://dashboard.trawlingweb.com/playground).

## Example Call

The API call is constructed from the basic structure:
```
http://tiktok.trawlingweb.com/010101010101010101?token=0000000000000000000000000000&q=casa
```
# API API TikTok - Best Practices and Tips

To use the API TikTok API, you need to call an endpoint URL with your private access token. You can generate the URL for your call using our API Visual Tester, accessible at [https://dashboard.trawlingweb.com/playground](https://dashboard.trawlingweb.com/playground).

## Example Call

The API call is constructed from the basic structure:
- **API Subdomain**: `http://tiktok.trawlingweb.com/`
- **Worker ID**: `010101010101010101` (example numeric ID of a worker necessary for using stored recovery keywords within a worker)
- **Access Token (API Key)**: `token=0000000000000000000000000000` to authenticate the usage.
- **Query (Q)**: `q=casa` to execute the query (in this case, searching for results containing the word "casa").

This is the minimal structure to access the API TikTok API, but from here you can use the parameters available in this documentation to refine and optimize queries as per user needs.

## Example Output

Below is an example output of an API call. This output includes information about remaining results, total number of results, and the URL to fetch the next results.

```
requestLeft 9999999
totalResults 295404987
restResults 295404887
next "http://tiktok.trawlingweb.com/010101010101010101?token=0000000000000000000000000000
```


## Using Dates `created_at` and `crawled`

TrawlingWeb provides two dates for each tweet: `created_at` (creation date) and `crawled` (capture date). This is crucial as when incorporating new sections, the system may detect posts as new that were actually published days or even months ago.

It can also happen that API TikTok modifies its system, causing old posts to appear due to errors or SEO strategies. To prevent or control these occurrences, we advise clients to implement security rules in their systems.

### Tips for Rules to Ensure Proper Use of Dates:

- **Date Filters**: Set filters to ignore posts with very old creation dates.
- **Relevance Rules**: Create criteria to determine tweet relevance based on creation and processing dates.
- **Monitoring Changes**: Monitor changes in the API TikTok system to adjust indexing and processing rules accordingly.
- **Alerts and Notifications**: Configure alerts to detect and notify the appearance of old posts, allowing manual review if necessary.

Implementing these measures helps our clients maintain the integrity and relevance of the data processed by TrawlingWeb.

## Pagination

Each request to the API TikTok API can return a maximum of 500 posts matching your query. However, there may be many more results matching your filter parameters. To consume all data, you need to continue making calls to the URL indicated in the **next** parameter of each request output.

Depending on the sorting criterion and desired order for results, the "next" URL includes the `&ts` and `&tsi` values, which adjust according to how results are sorted. Both `&ts` and `&tsi` are UnixMicrotime timestamps.

By default, the API TikTok API returns 500 results per request, though the total matching posts can be greater. The JSON response will contain the `next` parameter, which allows you to make an additional API call to fetch the next page of results. This process repeats until all available results are consumed.

Additionally, it's possible to modify the number of results desired per request. If you need to receive fewer than 500 results per API call, you can adjust this number using the `size=n` parameter.

## Pagination Modes

Cases and examples of pagination operation modes.

#### Case 1:
`&sort=created_at&order=asc` _(Default mode that can deliver up to a maximum of 500 results)_

`example: https://API TikTok.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=created_at&order=asc&ts=1719784800000&tsi=1720130400000`

Explanation:
* **Organization**: posts are organized by creation date ***(sort=created_at)***
* **Sorting**: posts are sorted from oldest to newest ***(order=asc)***.
* **Results**: Without defining `size=n`, the maximum will always be 500.
* **Next**: The "next" within the JSON allows jumping to the next results, which can be up to 500 at most.

#### Case 2:
`&sort=created_at&order=desc` _(Default mode that can deliver up to a maximum of 500 results)_

example: 
```
https://API TikTok.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=created_at&order=desc&ts=1719784800000&tsi=1720130400000
```

Explanation:
* **Organization**: posts are organized by creation date ***(sort=created_at)***
* **Sorting**: posts are sorted from newest to oldest ***(order=desc)***.
* **Results**: Without defining `size=n`, the maximum will always be 500.
* **Next**: The "next" within the JSON allows jumping to the next results, which can be up to 500 at most.

#### Case 3:
`&sort=created_at&order=desc&size=4` _(Default mode that can deliver up to a maximum of 500 results)_

example:
```
https://API TikTok.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=created_at&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explanation:
* **Organization**: posts are organized by creation date ***(sort=created_at)***
* **Sorting**: posts are sorted from newest to oldest ***(order=desc)***.
* **Results**: By defining `size=4`, the maximum will be 4 per pagination.
* **Next**: The "next" within the JSON allows jumping to the next results, which will be up to the number defined in `size=n`, in this case `4` results.

## Grouping

The grouping parameter is used with the following syntax: `sort=`. This allows grouping posts by two types of time criteria:

* **Created_at**: Groups by creation date. The date used in the API call is the date the tweet was created. `sort=created_at`
* **Crawled**: Groups by capture date. The date used in the API call is the date the tweet was captured. `sort=crawled`

### Example 1: Grouping by Creation Date

example:
```
https://API TikTok.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=created_at&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explanation:
* **Organization**: posts are organized by creation date ***(sort=created_at)***
* **Sorting**: posts are sorted from newest to oldest ***(order=desc)***.
* **Results**: By defining `size=4`, the maximum will be 4 per pagination.
* **Next**: The "next" within the JSON allows jumping to the next results, which will be up to the number defined in `size=n`, in this case `4` results.

### Example 2: Grouping by Processing Date

example:
```
https://API TikTok.trawlingweb.com/01010101010101010?token=0000000000000000000&q=obama&sort=crawled&order=desc&ts=1719784800000&tsi=1720130400000&size=4
```

Explanation:
* **Organization**: posts are organized by capture date ***(sort=crawled)***
* **Sorting**: posts are sorted from newest to oldest ***(order=desc)***.
* **Results**: By defining `size=4`, the maximum will be 4 per pagination.
* **Next**: The "next" within the JSON allows jumping to the next results, which will be up to the number defined in `size=n`, in this case `4` results.

#### Tips:
- Use `sort=created_at` to get results grouped by creation date and `sort=crawled` to get results grouped by capture date.
- If `sort=` parameter is not used, default grouping will be `created_at`.

## Sorting

The sorting parameter is used with the following syntax: `order=`. This allows sorting the grouping criterion in ascending or descending order:

* **order=asc**: Sorts the `sort` grouping criterion in ascending order.
* **order=desc**: Sorts the `sort` grouping criterion in descending order.

### Examples:

* To get results grouped by creation date in ascending order, use `sort=created_at&order=asc`.
* To get results grouped by creation date in descending order, use `sort=created_at&order=desc`.

## Number of Results

As mentioned in the "Pagination" section earlier, each call to this API returns a maximum of 500 results by default. However, as demonstrated in the pagination examples, this maximum number of returned results can be adjusted according to usage needs for calls.

To modify the maximum number of results returned by the API call, use the `size=` parameter.

## Examples:
* No use of `size=`: Returns a maximum of 500 results if available.
* `size=1`: Returns only one result in each pagination, regardless of whether more results are available.
* `size=20`: Returns a maximum of 20 results in each pagination, regardless of whether more results are available.

## Regular Maintenance of Data Sources

Regular maintenance of data sources is constant and essential at TrawlingWeb. It involves a comprehensive reassessment of each source, often involving the addition of new sections to index previously uncollected content. Having creation dates (`created_at`) and capture dates (`crawled`) allows efficient management of these updates.

When adding new data sources to our coverage, we often include their history by performing an initial deep indexing of all their sections. Again, creation dates (`created_at`) and capture dates (`crawled`) facilitate this process.

Certain sections of API TikTok, in addition to chronological content, may display non-chronological content (such as highlighted or related posts) that we also index.

### Considerations

* **Indexing Frequency**: The indexing frequency of a data source is determined by client needs, functional requirements, tweet volume, and source publishing frequency.
* **Differentiation of Dates**: Clearly differentiating capture date (`crawled`) from creation date (`created_at`) allows clients to decide which posts to incorporate.
* **Content Delivery Philosophy**: Our philosophy is to deliver all processed posts, leaving the decision on how to use this content to clients.

### Delivered and Discarded posts

* **Delivered posts**: All processed posts are delivered to the client.
* **Discarded posts**: Clients have the option to discard posts according to their specific criteria and needs.

## Lucene Query Syntax

TrawlingWeb APIs allow queries that may contain Boolean operators based on Lucene syntax, offering a powerful tool for performing complex and precise searches. Lucene query syntax is designed to be intuitive and expressive.

In section 03_queries you will find how to use Boolean expressions and Lucene syntax properly.

---

# Contact
If you have any questions, need assistance, want to hire or extend your services, please contact us.

**Technical Support (SAT):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20TikTok)

**Administrative Support (SAC):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales Support (Sales):**
* [Sales Email](mailto:sales@trawlingweb.com)
