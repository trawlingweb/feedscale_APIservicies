# API TikTok - GET Method /posts

It allows to obtain the processed result of each configured TikTok Worker.
You can use temporary delimiters to narrow the content returned.

# GET Parameters

Let's see the structure of the sample query:

```
https://tiktok.trawlingweb.com/posts/{WORKERID}?token={APIKEY}
```

## PATH Parameters

| Element  | Description                                         |
| :------- | :-------------------------------------------------- |
| protocol | It can be **http** as **https**                     |
| domain   | Address of the API tiktok.trawlingweb.com        |
| method   | Posts                                               |
| workerid | WORKERID of access to to the system of TrawlingWeb. |

## Query Parameters

| Parameter | Description                                                            | Default                                          | Example            |
| :-------- | :--------------------------------------------------------------------- | :----------------------------------------------- | :----------------- |
| token     | APIKEY of access of the client to the system of TrawlingWeb.           | Required value                                   | ?token={APIKEY}    |
| ts        | It is the initial temporal delimiter. Unix Time format in milliseconds | Delimit to 1 months in the past from the request | &ts=1518472804000  |
| tsi       | It is the final temporal delimiter. Unix Time format is milliseconds   | Delimit with the date of petition                | &tsi=1524818189854 |

# Output Response - RESPONSE

Upon making a request to the TikTok API, it will return a structured response as follows:

## Post Data

| Field     | Description                                                                 | Searchable | Orderable |  Type   |           Format           |
| --------- | --------------------------------------------------------------------------- | :--------: | :-------: | :-----: | :-------------------------: |
| id        | Identification code assigned by Trawlingweb to each tracked post            |     No     |     No    | String  |                             |
| post_id   | ID of the post                                                              |     No     |     No    | String  |                             |
| type      | Type of post (photo or video)                                               |     No     |     No    | String  |                             |
| url       | URL of the post                                                             |     No     |     No    | String  |                             |
| media_url | URL of the media content                                                    |     No     |     No    | String  |                             |
| likes     | Number of likes                                                             |     No     |     No    | Integer |                             |
| text      | Text description of the post                                                |     No     |     No    | String  |                             |
| published | Date the post was published                                                 |     No     |     No    |  Date   |        ISO 8601-UTC         |
| crawled   | Date and time when the post was captured                                    |     No     |    Yes    | Integer | UNIX Timestamp in milliseconds |

## User Data

| Field             | Description                | Searchable | Orderable |  Type   | Format  |
| ----------------- | -------------------------- | :--------: | :-------: | :-----: | :-----: |
| user_name         | Username                   |     No     |     No    | String  |         |
| user_screen_name  | Displayed username         |     No     |     No    | String  |         |
| user_publications | Number of posts            |     No     |     No    | Integer |         |
| user_followers    | Number of followers        |     No     |     No    | Integer |         |
| user_followed     | Number of followed users   |     No     |     No    | Integer |         |

## Comments Data

| Field    | Description | Searchable | Orderable |  Type   | Format  |
| -------- | ----------- | :--------: | :-------: | :-----: | :-----: |
| comments | Comments    |     No     |     No    | String  |         |

## Request Data

| Field        | Description                                                             |  Type   |
| ------------ | ----------------------------------------------------------------------- | :-----: |
| requestLeft  | Total remaining queries for the subscription                            | Integer |
| totalResults | Total results found for the query                                       | Integer |
| next         | URL to continue pagination and retrieve all results                     | String  |

## Example response in JSON format:

```json
{
  "data": [
    {
      "id": "...",
      "user_screen_name": "...",
      "user_publications": 239,
      "user_followers": 6762,
      "user_followed": 1792,
      "user_name": "...",
      "post_id": "...",
      "type": "...",
      "url": "...",
      "media_url": "...",
      "likes": 125,
      "text": "...",
      "comments": null,
      "published": "2024-08-03T11:00:04.000Z",
      "crawled": 1722682829465
    }
  ],
  "totalResults": "...",
  "restResults": "...",
  "next": "..."
}

```

# API TikTok - Best practices

In order to use the API it is necessary to call an endpoint URL with its private access token and its Worker id.
You can generate the URL of your call in our Visual API Tester (you must access https://dashboard.trawlingweb.com/workers).

## Data Integrity

Each API request can return a maximum of 100 messages matching your query. However, there may be many more results that match your filter parameters. To consume all the data, you must continue making calls to the URL indicated in the parameter **next** of the output of each request.

## Outcome example

```
requestLeft	9999999
totalResults	295404987
next	"http://tiktok.trawlingweb.com/posts/1234567891234567891234567891234567.123456789?token=1234567891234567891234567891234567891234&ts=1555327617000&tsi=1554076800000"
}
```

## Pagination

When making requests to the POST methods, they return a maximum of 100 results. A url of next is enabled to continue with the obtaining if they surpass this amount.

# Contact

If you have any questions, need assistance, or want to contract or expand your services, please contact us.

**SAT (Technical Support):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20TikTok)

**SAC (Administrative Support):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales (Sales Support):**
* [Sales Email](mailto:sales@trawlingweb.com)

