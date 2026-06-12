# Telegram API - GET Method /posts

Allows retrieving processed results from each configured Telegram Worker.
Time-range delimiters can be used to scope the returned content, and additional boolean queries can be applied via `q=`.

# GET Parameters

Let's examine the structure of the example query:

```
https://telegram.trawlingweb.com/posts/{WORKERID}?token={APIKEY}&ts=1518472804000&tsi=1524818189854
```

## PATH Parameters

| Element  | Description                                  |
| :------- | :------------------------------------------- |
| protocol | Can be either **http** or **https**          |
| domain   | API address telegram.trawlingweb.com         |
| method   | posts                                        |
| workerid | WORKERID for TrawlingWeb system access.      |

## QUERY Parameters

| Parameter | Description                                                                  | Default                                                 | Example            |
| :-------- | :--------------------------------------------------------------------------- | :------------------------------------------------------ | :----------------- |
| token     | Client's APIKEY access to TrawlingWeb system.                                | Required value                                          | ?token={APIKEY}    |
| q         | Additional boolean / Lucene query to refine results                          | Empty                                                   | &q=crisis          |
| ts        | Initial time delimiter. Unix time format in milliseconds                     | Delimits to 1 month back from the request               | &ts=1518472804000  |
| tsi       | Final time delimiter. Unix time format in milliseconds                       | Delimits with the request date                          | &tsi=1524818189854 |
| size      | Maximum number of results per response                                       | Plan's `default_maxsize` (typically 100)                | &size=50           |

> Note: `ts`/`tsi` ranges are validated with a maximum of 1 month back relative to the current date. If `ts > tsi`, the API returns an error.

# Output Response - RESPONSE

Upon making a request to the Telegram API, it will return a structured response as follows:

## Message Data

| Field            | Description                                                                       | Searchable | Sortable |  Type  |              Format               |
| ---------------- | --------------------------------------------------------------------------------- | :--------: | :------: | :----: | :-------------------------------: |
| id               | Identification code assigned by Trawlingweb to each tracked message               |     No     |    No    | String |                                   |
| post_id          | Telegram message ID                                                                |     No     |    No    | String |                                   |
| url              | Public URL of the message (when channel/group is public)                          |     No     |    No    | String |                                   |
| text             | Message text                                                                       |    Yes     |    No    | String |                                   |
| published        | Message publication date                                                          |     No     |   Yes    | Date   |           ISO 8601-UTC            |
| crawled          | Date and time when the message was captured                                       |     No     |   Yes    | Integer| UNIX Timestamp in milliseconds     |

## Author / channel data

| Field             | Description                                              | Searchable | Sortable |  Type  | Format |
| ----------------- | -------------------------------------------------------- | :--------: | :------: | :----: | :----: |
| user_name         | Channel / author display name                            |    Yes     |    No    | String |        |
| user_screen_name  | Technical name (@username) of the channel / author       |    Yes     |    No    | String |        |

## Request data

| Field        | Description                                                             |   Type   |
| :----------- | :---------------------------------------------------------------------- | :------: |
| totalResults | Total number of results found by the query                              | Integer  |
| restResults  | Remaining results after this page                                       | Integer  |
| next         | URL to continue pagination and retrieve all results                     | String   |

## Example response in JSON format:

```json
{
  "response": {
    "data": [
      {
        "id": "...",
        "post_id": "...",
        "url": "https://t.me/publicchannel/12345",
        "text": "...",
        "user_name": "Channel name",
        "user_screen_name": "publicchannel",
        "published": "2024-08-03T11:00:04.000Z",
        "crawled": 1722682829465
      }
    ],
    "totalResults": 12345,
    "restResults": 12245,
    "next": "https://telegram.trawlingweb.com/posts/{WORKERID}?token={APIKEY}&ts=...&tsi=..."
  }
}
```

# Telegram API - Best practices

To use the API, you must call an endpoint URL with your private access token and your Worker ID.
You can generate your call URL in our API Visual Tester (accessible at https://dashboard.trawlingweb.com/workers).

## Data integrity

Each API request can return a maximum number of results equal to the configured `size` (subject to the plan's limit). However, there may be many more matching results. To consume all data, you must keep calling the URL indicated in the **next** parameter of each request's output.

## Output example

```
totalResults  295404987
restResults   295404887
next          "https://telegram.trawlingweb.com/posts/1234567891234567891234567891234567.12345678?token=1234567891234567891234567891234567891234&ts=1555327617000&tsi=1554076800000"
```

## Pagination

Requests to `/posts/:worker_id` return at most the plan-defined limit (typically 100). A `next` URL is provided to continue retrieving results if the total exceeds that limit.

# Contact
If you have any questions, need assistance, or want to contract or expand your services, please contact us.

**SAT (Technical Support):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20Telegram)

**SAC (Administrative Support):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales (Sales Support):**
* [Sales Email](mailto:sales@trawlingweb.com)
