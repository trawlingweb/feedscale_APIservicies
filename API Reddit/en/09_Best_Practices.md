# Reddit API - Best Practices and Tips

To use the Reddit API, you must call an endpoint URL with your private access token. You can generate your call URL in our API Visual Tester, available at [https://dashboard.trawlingweb.com/playground](https://dashboard.trawlingweb.com/playground).

## Example Call

The API call is built from the basic structure:

```
https://reddit.trawlingweb.com/posts/010101010101010101?token=0000000000000000000000000000&q=subreddit:soccer
```

This structure includes:
* **Reddit API Subdomain**: `https://reddit.trawlingweb.com/`
* **Method**: `posts/`
* **IDworker**: `010101010101010101` (numeric example of a worker ID required to use retrieval keywords stored within a previously created worker).
* **Access Token (API key)**: `token=0000000000000000000000000000` to validate usage.
* **Query (q)**: `q=subreddit:soccer` to execute the additional boolean query (which in this case scopes results to the `soccer` subreddit).

This is the minimum structure to access the Reddit API. From here, you can use the parameters available in this documentation (`ts`, `tsi`, `size`) to refine and optimize queries according to user needs.

## Output Example

Below is an example of the output from an API call. This output includes information about total and remaining results and the URL to retrieve subsequent results.

```
totalResults 295404987
restResults  295404887
next "https://reddit.trawlingweb.com/posts/010101010101010101?token=0000000000000000000000000000&ts=...&tsi=..."
```


## Using the `published` and `crawled` Dates

TrawlingWeb provides two dates for each post/comment: `published` (creation/publication date on Reddit) and `crawled` (capture date). This is crucial because, when adding new subreddits or performing backfill, the system may detect as new content that was published days or even months earlier.

It can also happen that Reddit changes the visibility of a subreddit or re-edits trigger later captures. To avoid or control these situations, we advise clients to implement safety rules in their systems.

### Tips on rules to ensure proper use of dates:

* **Date Filters**: Set up filters to ignore content with very old publication dates if not relevant.
* **Relevance Rules**: Create criteria that determine the relevance of content based on its publication date and capture date.
* **Change Monitoring**: Monitor changes in the tracked subreddits to adjust processing rules.
* **Alerts and Notifications**: Configure alerts to detect and notify the appearance of old posts, allowing manual review if needed.

Implementing these measures helps our clients maintain the integrity and relevance of the data processed by TrawlingWeb.

## Pagination

Each request to the Reddit API can return at most a number of results equal to the plan's `size` (default 100, configurable up to the maximum allowed by the token). However, there may be many more results matching your filter parameters. To consume all data, you must keep calling the URL indicated in the **next** parameter of each request's output.

The `next` URL includes `&ts` and `&tsi` values, automatically adjusted based on the `crawled` value of the last returned result, allowing pagination to continue without losing items.

By default the API returns up to 100 results per request, although the total number of matching items may be larger. The JSON response includes the `next` parameter, which is used to make an additional call to retrieve the next page of results. This process is repeated until all available results are consumed.

If you need to receive fewer results per API call, you can adjust this number using the `size=n` parameter.

## Time ranges `ts` and `tsi`

* `ts` (initial timestamp) — date from which to search for captured content. By default, 1 month back from the time of the request.
* `tsi` (final timestamp) — date up to which to search. By default, the current date.
* Both in Unix milliseconds.
* If omitted or invalid, default values are applied.
* If `ts > tsi`, the API returns an error.

## Boolean search endpoint over the consumer's universe

In addition to `/posts/:worker_id` (filtering by a specific worker's keywords), the API exposes `/posts/?q=…`, which runs the boolean query over **the union of keywords from all the consumer's workers**. Useful for cross-cutting searches without having to choose a specific worker, and it can be combined with `subreddit:...` filters.

```
https://reddit.trawlingweb.com/posts/?token={APIKEY}&q=cocacola%20AND%20subreddit:business&ts=...&tsi=...
```

## Subreddit Filtering

Unlike other social APIs, Reddit indexes the `subreddit` field and includes it among the searchable fields. Take advantage of this in `q=` to:

* Limit results to specific communities: `subreddit:soccer`
* Combine several communities: `(subreddit:soccer OR subreddit:football)`
* Exclude irrelevant communities: `cocacola NOT subreddit:ads`

## Periodic Maintenance of Data Sources

Periodic maintenance of the tracked subreddits is constant and essential at TrawlingWeb. It involves a comprehensive reevaluation of each source, which often entails the incorporation of new relevant subreddits. Having the publication (`published`) and capture (`crawled`) dates allows managing these updates efficiently.

### Considerations

* **Indexing Frequency**: The indexing frequency of a source is determined by client needs, functional requirements, the volume of posts/comments, and the publication cadence of each subreddit.
* **Date Differentiation**: Clearly differentiating the capture date (`crawled`) from the publication date (`published`) allows clients to decide which content to incorporate.
* **Content Delivery Philosophy**: Our philosophy is to deliver all processed content, leaving the decision on how to use it to the clients.

### Delivered and Discarded Content

* **Delivered Content**: All processed posts/comments are delivered to the client.
* **Discarded Content**: Clients have the option to discard items according to their specific criteria and needs.

## Lucene Query Syntax

The TrawlingWeb APIs allow running queries that may contain boolean operators based on Lucene syntax, offering a powerful tool to perform complex and precise searches. Lucene's query syntax is designed to be intuitive and expressive.

In `06_Workers_Filtering_Syntax.md` you will find how to properly use boolean expressions and Lucene syntax, including filtering by `subreddit:`.

---

# Contact
If you have any questions, need assistance, or want to contract or expand your services, please contact us.

**SAT (Technical Support):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20Reddit)

**SAC (Administrative Support):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales (Sales Support):**
* [Sales Email](mailto:sales@trawlingweb.com)
