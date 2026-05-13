# API Instagram - GET Method /comments

Allows you to retrieve **comments** captured by each Instagram Worker configured with `subtype=comments`. The endpoint is parallel to `GET /posts` but serves the comments TrawlingWeb has indexed for the Worker's posts. Time delimiters can narrow down the returned content.

# GET Parameters

Sample query structure:

```
https://instagram.trawlingweb.com/comments/{WORKERID}?token={APIKEY}
```

## PATH Parameters

| Element  | Description                                                              |
| :------- | :----------------------------------------------------------------------- |
| protocol | Either **http** or **https**                                             |
| domain   | Address of the API instagram.trawlingweb.com                             |
| method   | comments                                                                 |
| workerid | WORKERID of a Worker configured with `subtype=comments` in TrawlingWeb.  |

## Query Parameters

| Parameter | Description                                                            | Default                                          | Example            |
| :-------- | :--------------------------------------------------------------------- | :----------------------------------------------- | :----------------- |
| token     | APIKEY of the client to access the TrawlingWeb system.                 | Required value                                   | ?token={APIKEY}    |
| country_pref | Client country preference (ISO 3166-1 alpha-2, e.g. `es`). **Required for FeedScale Pay-per-Use contracts**. Omitting it penalises the request cost by x2.5 and risks access blocking. | Required (Pay-per-Use) | &country_pref=es |
| ts        | Initial temporal delimiter. Unix Time format in milliseconds.          | Delimits **30 days** in the past from the request | &ts=1518472804000  |
| tsi       | Final temporal delimiter. Unix Time format in milliseconds.            | Delimits with the request date                   | &tsi=1524818189854 |
| q         | (Optional) Lucene query string applied to the comment `text` field.    | No filter                                        | &q=manifestation   |
| size      | (Optional) Results per page. Maximum 100 (standard) or 500 (admin).    | 100                                              | &size=50           |

> **Note — time window**: the `/comments` endpoint uses a **30-day** default window (vs 1 month for `/posts`), as comments are typically queried over shorter horizons.

# Output Response - RESPONSE

Upon making a request, the endpoint returns a structured response. The **wrapper** (`data`, `totalResults`, `restResults`, `next`) is **identical** to `/posts`, but the inner shape of each element is different: each `data[i]` is a comment, not a post.

## Comment Data

| Field           | Description                                                                                | Searchable | Orderable |  Type   |          Format            |
| --------------- | ------------------------------------------------------------------------------------------ | :--------: | :-------: | :-----: | :------------------------: |
| id              | Internal document identifier. Deterministic: `<parent_post_id>_<comment_id>`.              |     No     |    No     | String  |                            |
| comment_id      | Comment ID on Instagram                                                                    |     No     |    No     | String  |                            |
| parent_post_id  | ID of the parent post                                                                      |     No     |    No     | String  |                            |
| parent_post_url | URL of the parent post                                                                     |     No     |    No     | String  |                            |
| worker_id       | WORKERID of the Worker that captured the comment                                           |     No     |    No     | String  |                            |
| client_id       | Internal client ID owning the Worker                                                       |     No     |    No     | Integer |                            |
| type            | Document type — always `"comment"`                                                         |     No     |    No     | String  |                            |
| platform        | Platform — always `"instagram_comments"`                                                   |     No     |    No     | String  |                            |
| text            | **Text of the comment** (not the post)                                                     |     No     |    No     | String  |                            |
| likes           | **Likes on the comment** (not the post)                                                    |     No     |    No     | Integer |                            |
| ad_value        | Estimated ad value (hybrid model: audience potential × CPM adjusted by likes)              |     No     |    No     | Decimal |                            |
| captured_at     | Date and time when the comment was scraped                                                 |     No     |    Yes    |  Date   |       ISO 8601-UTC         |
| raw             | Raw scrape object. **Not searchable** (`enabled: false` in the index mapping).             |     No     |    No     | Object  |                            |

## Comment Author Data

| Field            | Description                                                            | Searchable | Orderable |  Type    | Format |
| ---------------- | ---------------------------------------------------------------------- | :--------: | :-------: | :------: | :----: |
| user_name        | **Username of the comment author** (not the post author)               |     No     |    No     | String   |        |
| user_screen_name | Displayed name of the comment author. Equals `user_name` when Instagram does not expose a "full name". | No | No | String |  |
| user_profile     | Author profile picture URL (may be empty)                              |     No     |    No     | String   |        |
| is_verified      | The comment author has a verified account                              |     No     |    No     | Boolean  |        |

## Inherited Data from Parent Post

> **Important**: these fields describe the **POST author** and the **post itself**, not the comment author or the comment. They come inherited from the parent post by project convention. If you need to analyse the comment author, **do not use `user_followers` or `user_followed`** — you'll always see those of the media outlet that owns the post.

| Field          | Description                                                | Searchable | Orderable |  Type   | Format        |
| -------------- | ---------------------------------------------------------- | :--------: | :-------: | :-----: | :-----------: |
| user_followers | Number of followers of the **parent POST author**          |     No     |    No     | Integer |               |
| user_followed  | Number of accounts followed by the **parent POST author**  |     No     |    No     | Integer |               |
| published      | Publication date of the **parent POST** (not the comment)  |     No     |    No     |  Date   | ISO 8601-UTC  |

## Worker Data (Geographic Classification)

| Field   | Description                                                          | Searchable | Orderable |  Type   | Format               |
| ------- | -------------------------------------------------------------------- | :--------: | :-------: | :-----: | :------------------: |
| country | Country associated with the Worker (inherited from `workers_conf.country`) | No | No | String  | ISO 3166-1 alpha-2   |
| lang    | Comment language. Automatically derived from the `country` field.    |     No     |    No     | String  | ISO 639-1            |

## Request Data

| Field        | Description                                                             |  Type   |
| :----------- | :---------------------------------------------------------------------- | :-----: |
| requestLeft  | Total remaining queries for the subscription                            | Integer |
| totalResults | Total results found for the query                                       | Integer |
| restResults  | Remaining results after the current `size`                              | Integer |
| next         | URL to continue pagination and retrieve all results                     | String  |

## Example response in JSON format:

```json
{
  "data": [
    {
      "id": "3893360753113419201_18022373657822184",
      "comment_id": "18022373657822184",
      "parent_post_id": "3893360753113419201",
      "parent_post_url": "https://www.instagram.com/p/DYH_vofxc3B/",
      "worker_id": "66d3ba29a337dc2ca3f7745be24f5b29.c23551e0",
      "client_id": 1751,
      "country": "BR",
      "lang": "pt",
      "type": "comment",
      "platform": "instagram_comments",
      "text": "😢😢😢😢 Justiça",
      "user_name": "eurosangela.assuncao",
      "user_screen_name": "eurosangela.assuncao",
      "user_profile": "",
      "is_verified": false,
      "user_followers": 218323,
      "user_followed": 235,
      "likes": 0,
      "ad_value": 327.48,
      "published": "2026-05-09T16:40:51.000Z",
      "captured_at": "2026-05-12T15:26:20.642Z",
      "raw": { "id": "18022373657822184", "...": "..." }
    }
  ],
  "totalResults": 91,
  "restResults": 90,
  "next": "https://instagram.trawlingweb.com/comments/66d3ba29a337dc2ca3f7745be24f5b29.c23551e0?token=...&ts=...&tsi=..."
}
```

# Key Differences vs `/posts`

Although both endpoints share authentication and wrapper, they serve different entities. These fields have **the same name with different meaning**:

| Field        | In `/posts`                          | In `/comments`                          |
| :----------- | :----------------------------------- | :-------------------------------------- |
| `user_name`  | Post author (media outlet account)   | **Comment** author (a different person) |
| `text`       | Post caption                         | **Comment** text                        |
| `likes`      | Post likes                           | **Comment** likes                       |
| `type`       | "photo" / "video" / "carousel"       | Always `"comment"`                      |

# Best Practices

## Data Integrity

Each API request can return a maximum of **100 items** (standard). If the total exceeds that cap, you must continue making calls to the URL indicated in the **next** parameter of each response.

## Pagination

When making requests to `/comments/{WORKERID}`, the API returns at most 100 results (or 500 for admin tokens). When more exist, a `next` URL is included to continue.

## Worker Must Be of Type Comments

The `WORKERID` in the path must belong to a Worker created with `subtype=comments`. Passing a `worker_id` from a regular Worker (different `subtype`) will return `{"error": "No comments worker with this ID"}`.

# Contact

If you have any questions, need assistance, or want to contract or expand your services, please contact us.

**SAT (Technical Support):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://docs.trawlingweb.com)

**SAC (Administrative Support):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales (Sales Support):**
* [Sales Email](mailto:sales@trawlingweb.com)
