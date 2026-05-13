# Twitter API - Method GET /posts

This method allows obtaining results processed from each Worker configured in Twitter. Temporal delimiters can be used to narrow down the returned content.

This is an advanced method that returns complete results about a tweet's publication, expanding the information compared to the basic method. In addition to basic data about the user who posted it, this method includes more detailed information about the user. It is ideal for statistical analysis that requires detailed information about the user and their posts.

Additionally, compared to other methods, this one allows the use of temporal delimiters to narrow down the returned content, along with boolean search expressions to further refine the results.

# GET Parameters

Let's examine the structure of the example query:

```
https://twitter.trawlingweb.com/posts_full/?token={APIKEY}&q={Boollean_Expression}
```

## PATH Parameters

| Element  | Description                                |
| :------- | :----------------------------------------- |
| protocol | It can be **http** as **https**            |
| domain   | Address of the API twitter.trawlingweb.com |
| method   | posts                                      |

## QUERY Parameters

| Parameter | Description                                                                                                                                                                          | Default                                          | Example                       |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------- | :---------------------------- |
| token     | APIKEY of access of the client to the system of TrawlingWeb.                                                                                                                         | Required value                                   | ?token={APIKEY}               |
| ts        | It is the initial temporal delimiter. Unix Time format in milliseconds                                                                                                               | Delimit to 1 months in the past from the request | &ts=1518472804000             |
| tsi       | It is the final temporal delimiter. Unix Time format is milliseconds                                                                                                                 | Delimit with the date of petition                | &tsi=1524818189854            |
| q         | Expression built with keywords or phrases that configure the search filters. Allows combinations with different types of available filters using boolean operators and, or, and not. |                                                  | &q=("barcelona" AND "Madrid") |

# Output Response - RESPONSE

This method aims to retrieve all results related to a worker's keywords. Additionally, using this method, some of the elements listed below will be considered searchable and sortable by date-related attributes.

Once a request is made to the Twitter API, a response will be received structured as follows:

## Data of publication

| Field                  | Description                                                                                                                                                | Findable | Sortable |  Type   | Format                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | :------: | :------: | :-----: | ----------------------------- |
| id                     | Identification code assigned by Trawlingweb to each crawled post                                                                                           |    No    |    No    | String  |                               |
| hash                   | Identification code based on the text                                                                                                                      |    No    |    No    | String  |                               |
| published              | Date the post was published                                                                                                                                |    No    |    No    |  Date   | ISO 8601-UTC                  |
| crawled                | Date of capture                                                                                                                                            |    No    |   Yes    | Integer | UNIX Timestamp (milliseconds) |
| updated                | Date of update                                                                                                                                             |    No    |   Yes    | Integer | UNIX Timestamp (milliseconds) |
| post_id                | Post ID                                                                                                                                                    |    No    |    No    | String  |                               |
| url                    | Publication URL                                                                                                                                            |    No    |    No    | String  |                               |
| text                   | Descriptive text of the publication                                                                                                                        |    No    |    No    | String  |                               |
| lang                   | When present, indicates a BCP 47 language identifier corresponding to the language detected by the text machine, or "und" if no language could be detected |    No    |    No    | String  |                               |
| retweet_count          | Number of times this Tweet has been retweeted                                                                                                              |    No    |    No    | Integer |                               |
| reply_count            | Number of times this Tweet has been replied                                                                                                                |    No    |    No    | Integer |                               |
| favorite_count         | Indicates approximately how many times users on Twitter have liked this Tweet                                                                              |    No    |    No    | Integer |                               |
| reproductions_count    | Number of times this Tweet has been reproduced                                                                                                             |    No    |    No    | Integer |                               |
| user_name              | User name                                                                                                                                                  |    No    |    No    | String  |                               |
| user_screen_name       | Displayed user name                                                                                                                                        |    No    |    No    | String  |                               |
| user_url               | User URL                                                                                                                                                   |    No    |    No    | String  |                               |
| user_profile_image_url | An HTTP-based URL pointing to the user's profile image                                                                                                     |    No    |    No    | String  |                               |
| entities_url           | Mentioned links                                                                                                                                            |    no    |    no    | String  |                               |
| hashtags               | Hashtags referenced in the text                                                                                                                            |    No    |    No    | String  |                               |
| user_mentions          | Users referenced in the text                                                                                                                               |    No    |    No    | String  |                               |
| time_distance          | Hours elapsed between the publication date and the capture date                                                                                            |    No    |    No    |  Fload  |                               |
| reply                  | Indicates if it is a retweet                                                                                                                      |    No    |    No    | Boolean |                               |

| Campo                   | Descripción                                                                                                                                                    | Buscable | Ordenable |  Tipo   |           Formato           |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------: | :-------: | :-----: | :-------------------------: |
| id                      | Identification code assigned by Trawlingweb to each tracked publication                                                                                        |    No    |    No     | String  |                             |
| hash                    | Identification code based on the text                                                                                                                          |    No    |    No     | String  |                             |
| published               | Date the post was published                                                                                                                                    |    No    |    No     |  Date   |        ISO 8601-UTC         |
| crawled                 | Capture date                                                                                                                                                   |    No    |    Si     | Integer | UNIX Timestamp milisegundos |
| updated                 | Update date                                                                                                                                                    |    No    |    Si     | Integer | UNIX Timestamp milisegundos |
| post_id                 | Post ID                                                                                                                                                        |    No    |    No     | String  |                             |
| url                     | Publication URL                                                                                                                                                |    No    |    No     | String  |                             |
| text                    | Descriptive text of the publication                                                                                                                            |    No    |    No     | String  |                             |
| lang                    | When present, indicates a BCP 47 language identifier corresponding to the language detected by the Tweet text machine, or und if no language could be detected |    No    |    No     | String  |                             |
| retweet_count           | Number of times this Tweet has been retweeted                                                                                                                  |    No    |    No     | Integer |                             |
| reply_count             | Number of times this Tweet has been replied to                                                                                                                 |    No    |    No     | Integer |                             |
| favorite_count          | Indicates approximately how many times this Tweet has been liked by Twitter users                                                                              |    No    |    No     | Integer |                             |
| reproductions_count     | Number of times this Tweet has been played                                                                                                                     |    No    |    No     | Integer |                             |
| entities_url            | Mentioned links                                                                                                                                                |    no    |    no     | String  |                             |
| url_image               | Image links                                                                                                                                                    |    no    |    no     | String  |                             |
| hashtags                | Hashtags referenced in the text                                                                                                                                |    No    |    No     | String  |                             |
| user_mentions           | Referenced usernames                                                                                                                                           |    No    |    No     | String  |                             |
| time_distance           | Hours elapsed between the publication date and the capture date                                                                                                |    No    |    No     |  Fload  |                             |
| reply                   | Indicates if it is a reply to a Tweet                                                                                                                          |    No    |    No     | Boolean |                             |
| user_id                 | User identification code                                                                                                                                       |    No    |    No     | Integer |                             |
| user_name               | User name                                                                                                                                                      |    No    |    No     | String  |                             |
| user_screen_name        | Displayed user name                                                                                                                                            |    No    |    No     | String  |                             |
| user_creation_date      | User creation date                                                                                                                                             |    No    |    No     |  Date   |        ISO 8601-UTC         |
| user_url                | User URL                                                                                                                                                       |    No    |    No     | String  |                             |
| user_profile_image_url  | HTTP-based URL pointing to the user's profile avatar                                                                                                           |    No    |    No     | String  |                             |
| user_profile_banner_url | HTTP-based URL pointing to the user's profile banner                                                                                                           |    No    |    No     | String  |                             |
| user_description        | User's descriptive text                                                                                                                                        |    No    |    No     | String  |                             |
| user_external_url       | User's description URL                                                                                                                                         |    No    |    No     | String  |                             |
| user_location           | Location specified by the user                                                                                                                                 |    No    |    No     | String  |                             |
| user_follower_count     | Number of user followers                                                                                                                                       |    No    |    No     | Integer |                             |
| user_following_count    | Number of users the user is following                                                                                                                          |    No    |    No     | Integer |                             |
| user_favourites_count   | Number of user favorites                                                                                                                                       |    No    |    No     | Integer |                             |
| user_is_private         | Private user                                                                                                                                                   |    No    |    No     | Boolean |                             |
| user_is_verified        | Verified user                                                                                                                                                  |    No    |    No     | Boolean |                             |
| user_is_blue_verified   | Verified user as Blue                                                                                                                                          |    No    |    No     | Boolean |                             |
| user_number_of_tweets   | Number of Tweets made by the user                                                                                                                              |    No    |    No     | Integer |                             |

## Request Data

| Field        | Description                                              |  Type   |
| :----------- | :------------------------------------------------------- | :-----: |
| requestLeft  | Total number of pending queries for the subscription     | Integer |
| totalResults | Approximate total number of found results for the query  | Integer |
| next         | URL to continue with pagination and retrieve all results | String  |

## Example of response in json format:

```
"json"
"response" : {
    "data" : [{
        "id": "...",
        "hash": "...",
        "published" : "...",
        "crawled" : "...",
        "updated" : "...",
        "post_id" : "...",
        "url" : "...",
        "text" : "...",
        "lang" : "...",
        "retweet_count" : "...",
        "reply_count" : "...",
        "favorite_count" : "...",
        "reproductions_count" : "...",
        "entities_url" : "...",
        "url_image" : "...",
        "hashtags" : "...",
        "user_mentions" : "...",
        "time_distance" : "...",
        "reply" : "...",
        "user_name" : "...",
        "user_screen_name" : "...",
        "user_creation_date" : "...",
        "user_url" : "...",
        "user_profile_image_url" : "...",
        "user_profile_banner_url" : "...",
        "user_description" : "...",
        "user_external_url" : "...",
        "user_location" : "...",
        "user_follower_count" : "...",
        "user_following_count" : "...",
        "user_favourites_count" : "...",
        "user_is_private" : "...",
        "user_is_verified" : "...",
        "user_is_blue_verified" : "...",
        "user_number_of_tweets" : "...",
    }],
    "totalResults" : "...",
    "restResults" : "...",
    "next" : "..."
}
```

# API Twitter - Best practices

## Data Integrity

Each API request can return a maximum of 500 messages matching your query. However, there may be many more results that match your filter parameters. To consume all the data, you must continue making calls to the URL indicated in the parameter **next** of the output of each request.

## Outcome example

```
requestLeft	9999999
totalResults	295404987
next	"http://twitter.trawlingweb.com/posts/1234567891234567891234567891234567.123456789?token=1234567891234567891234567891234567891234&ts=1555327617000&tsi=1554076800000"
}
```
