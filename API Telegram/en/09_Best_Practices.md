# Telegram API - Best Practices and Tips

To use the Telegram API, you must call an endpoint URL with your private access token. You can generate your call URL in our API Visual Tester, available at [https://dashboard.trawlingweb.com/playground](https://dashboard.trawlingweb.com/playground).

## Example Call

The API call is built from the basic structure:

```
https://telegram.trawlingweb.com/posts/010101010101010101?token=0000000000000000000000000000&q=crisis
```

This structure includes:
* **Telegram API Subdomain**: `https://telegram.trawlingweb.com/`
* **Method**: `posts/`
* **IDworker**: `010101010101010101` (numeric example of a worker ID required to use retrieval keywords stored within a previously created worker).
* **Access Token (API key)**: `token=0000000000000000000000000000` to validate usage.
* **Query (q)**: `q=crisis` to execute the additional boolean query (which in this case searches, within the worker's universe, results containing the word crisis).

This is the minimum structure to access the Telegram API. From here, you can use the parameters available in this documentation (`ts`, `tsi`, `size`) to refine and optimize queries according to user needs.

## Output Example

Below is an example of the output from an API call. This output includes information about total and remaining results and the URL to retrieve subsequent results.

```
totalResults 295404987
restResults  295404887
next "https://telegram.trawlingweb.com/posts/010101010101010101?token=0000000000000000000000000000&ts=...&tsi=..."
```


## Using the `published` and `crawled` Dates

TrawlingWeb provides two dates for each message: `published` (creation/publication date in Telegram) and `crawled` (capture date). This is crucial because, when adding new channels or performing backfill, the system may detect as new messages that were published days or even months earlier.

It can also happen that Telegram changes the visibility of a channel or re-edits trigger later captures. To avoid or control these situations, we advise clients to implement safety rules in their systems.

### Tips on rules to ensure proper use of dates:

* **Date Filters**: Set up filters to ignore messages with very old publication dates if they are not relevant.
* **Relevance Rules**: Create criteria that determine the relevance of messages based on their publication date and capture date.
* **Change Monitoring**: Monitor changes in the tracked channels to adjust processing rules.
* **Alerts and Notifications**: Configure alerts to detect and notify the appearance of old messages, allowing manual review if needed.

Implementing these measures helps our clients maintain the integrity and relevance of the data processed by TrawlingWeb.

## Pagination

Each request to the Telegram API can return at most a number of results equal to the plan's `size` (default 100, configurable up to the maximum allowed by the token). However, there may be many more results matching your filter parameters. To consume all data, you must keep calling the URL indicated in the **next** parameter of each request's output.

The `next` URL includes `&ts` and `&tsi` values, automatically adjusted based on the `crawled` value of the last returned result, allowing pagination to continue without losing messages.

By default the API returns up to 100 results per request, although the total number of matching messages may be larger. The JSON response includes the `next` parameter, which is used to make an additional call to retrieve the next page of results. This process is repeated until all available results are consumed.

If you need to receive fewer results per API call, you can adjust this number using the `size=n` parameter.

## Time ranges `ts` and `tsi`

* `ts` (initial timestamp) — date from which to search for captured messages. By default, 1 month back from the time of the request.
* `tsi` (final timestamp) — date up to which to search. By default, the current date.
* Both in Unix milliseconds.
* If omitted or invalid, default values are applied.
* If `ts > tsi`, the API returns an error.

## Boolean search endpoint over the consumer's universe

In addition to `/posts/:worker_id` (filtering by a specific worker's keywords), the API exposes `/posts/?q=…`, which runs the boolean query over **the union of keywords from all the consumer's workers**. Useful for cross-cutting searches without having to choose a specific worker.

```
https://telegram.trawlingweb.com/posts/?token={APIKEY}&q=cocacola%20AND%20crisis&ts=...&tsi=...
```

## Periodic Maintenance of Data Sources

Periodic maintenance of the tracked public channels and groups is constant and essential at TrawlingWeb. It involves a comprehensive reevaluation of each source, which often entails the incorporation of new relevant channels. Having the publication (`published`) and capture (`crawled`) dates allows managing these updates efficiently.

### Considerations

* **Indexing Frequency**: The indexing frequency of a source is determined by client needs, functional requirements, the volume of messages, and the publication cadence of each channel.
* **Date Differentiation**: Clearly differentiating the capture date (`crawled`) from the publication date (`published`) allows clients to decide which messages to incorporate.
* **Content Delivery Philosophy**: Our philosophy is to deliver all processed messages, leaving the decision on how to use this content to the clients.

### Delivered and Discarded Messages

* **Delivered Messages**: All processed messages are delivered to the client.
* **Discarded Messages**: Clients have the option to discard messages according to their specific criteria and needs.

## Lucene Query Syntax

The TrawlingWeb APIs allow running queries that may contain boolean operators based on Lucene syntax, offering a powerful tool to perform complex and precise searches. Lucene's query syntax is designed to be intuitive and expressive.

In `06_Workers_Filtering_Syntax.md` you will find how to properly use boolean expressions and Lucene syntax.

---

# Contact
If you have any questions, need assistance, or want to contract or expand your services, please contact us.

**SAT (Technical Support):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20Telegram)

**SAC (Administrative Support):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales (Sales Support):**
* [Sales Email](mailto:sales@trawlingweb.com)
