# Reddit API - GET Method /posts

Allows retrieving processed results from each configured Reddit Worker.
Time-range delimiters can be used to scope the returned content, and additional boolean queries can be applied via `q=`.

# GET Parameters

Let's examine the structure of the example query:

```
https://reddit.trawlingweb.com/posts/{WORKERID}?token={APIKEY}&ts=1518472804000&tsi=1524818189854
```

## PATH Parameters

| Element  | Description                                  |
| :------- | :------------------------------------------- |
| protocol | Can be either **http** or **https**          |
| domain   | API address reddit.trawlingweb.com           |
| method   | posts                                        |
| workerid | WORKERID for TrawlingWeb system access.      |

## QUERY Parameters

| Parameter | Description                                                                  | Default                                                 | Example                  |
| :-------- | :--------------------------------------------------------------------------- | :------------------------------------------------------ | :----------------------- |
| token     | Client's APIKEY access to TrawlingWeb system.                                | Required value                                          | ?token={APIKEY}          |
| q         | Additional boolean / Lucene query (includes `subreddit:` filter)             | Empty                                                   | &q=subreddit:soccer      |
| ts        | Initial time delimiter. Unix time format in milliseconds                     | Delimits to 1 month back from the request               | &ts=1518472804000        |
| tsi       | Final time delimiter. Unix time format in milliseconds                       | Delimits with the request date                          | &tsi=1524818189854       |
| size      | Maximum number of results per response                                       | Plan's `default_maxsize` (typically 100)                | &size=50                 |

> Note: `ts`/`tsi` ranges are validated with a maximum of 1 month back relative to the current date. If `ts > tsi`, the API returns an error.

# Output Response - RESPONSE

Upon making a request to the Reddit API, it will return a structured response as follows:

## Post / comment data

| Field            | Description                                                                       | Searchable | Sortable |  Type  |              Format               |
| ---------------- | --------------------------------------------------------------------------------- | :--------: | :------: | :----: | :-------------------------------: |
| id               | Identification code assigned by Trawlingweb                                       |     No     |    No    | String |                                   |
| post_id          | Reddit post/comment ID                                                            |     No     |    No    | String |                                   |
| url              | Public URL of the post or comment on Reddit                                       |     No     |    No    | String |                                   |
| text             | Post or comment text                                                              |    Yes     |    No    | String |                                   |
| subreddit        | Subreddit where the content appears                                               |    Yes     |    No    | String |                                   |
| published        | Publication date                                                                  |     No     |   Yes    | Date   |           ISO 8601-UTC            |
| crawled          | Date and time the content was captured                                            |     No     |   Yes    | Integer| UNIX Timestamp in milliseconds     |

## Author data

| Field             | Description                                              | Searchable | Sortable |  Type  | Format |
| ----------------- | -------------------------------------------------------- | :--------: | :------: | :----: | :----: |
| user_name         | Author display name                                       |    Yes     |    No    | String |        |
| user_screen_name  | Technical name (u/username) of the author                 |    Yes     |    No    | String |        |

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
        "url": "https://www.reddit.com/r/soccer/comments/abc123/title/",
        "text": "...",
        "subreddit": "soccer",
        "user_name": "...",
        "user_screen_name": "username",
        "published": "2024-08-03T11:00:04.000Z",
        "crawled": 1722682829465
      }
    ],
    "totalResults": 12345,
    "restResults": 12245,
    "next": "https://reddit.trawlingweb.com/posts/{WORKERID}?token={APIKEY}&ts=...&tsi=..."
  }
}
```

# Reddit API - Best practices

To use the API, you must call an endpoint URL with your private access token and your Worker ID.
You can generate your call URL in our API Visual Tester (accessible at https://dashboard.trawlingweb.com/workers).

## Data integrity

Each API request can return a maximum number of results equal to the configured `size` (subject to the plan's limit). However, there may be many more matching results. To consume all data, you must keep calling the URL indicated in the **next** parameter of each request's output.

## Output example

```
totalResults  295404987
restResults   295404887
next          "https://reddit.trawlingweb.com/posts/1234567891234567891234567891234567.12345678?token=1234567891234567891234567891234567891234&ts=1555327617000&tsi=1554076800000"
```

## Pagination

Requests to `/posts/:worker_id` return at most the plan-defined limit (typically 100). A `next` URL is provided to continue retrieving results if the total exceeds that limit.

# Contact
If you have any questions, need assistance, or want to contract or expand your services, please contact us.

**SAT (Technical Support):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20Reddit)

**SAC (Administrative Support):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales (Sales Support):**
* [Sales Email](mailto:sales@trawlingweb.com)
