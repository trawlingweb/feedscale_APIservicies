# TikTok API - POST Method /create

Allows creating new Workers with their keywords.

## What is a Worker?

A Worker in TrawlingWeb is a user-configured entity to perform specific searches on social networks using Keywords. These Keywords are search terms configured within the Worker and are based on the contracted credits (1 credit = 1 Keyword).

## Creation and Configuration of Workers

Users can create and define search terms for each Worker directly on the dashboard ([https://dashboard.trawlingweb.com/workers](https://dashboard.trawlingweb.com/workers)) or using the method provided by the API. Once a Worker is created, it begins deployment to initiate its configuration process, which may take up to an hour.

## Workers Functionality

* **Keywords**: Workers function as a list of keywords. They use the configured Keywords to perform searches on social networks.
- **Search Process**: Workers deliver the Keywords to TrawlingWeb's spiders to execute searches on the social network.
- **Delivery Process**: Each time the client calls the Worker, it uses the list of Keywords to launch the search against the database of results obtained by TrawlingWeb and retrieve only those results related to the list of Keywords.

Implementing and managing Workers efficiently allows users to maximize the relevance and accuracy of the processed data, tailored to the specific needs of their social media analysis and monitoring.

# POST Parameters

Let's examine the structure of the example query:

```
https://tiktok.trawlingweb.com/create/?token={APIKEY}
```

## PATH Parameters:

| Element  | Description                                 |
| :-------- | :------------------------------------------ |
| protocol | Can be either **http** or **https**         |
| domain   | API address TikTok.trawlingweb.com       |
| method   | create                                      |

## QUERY Parameters:

| Parameter | Description                                              | Default           | Example         |
| :-------- | :------------------------------------------------------- | :---------------- | :-------------- |
| token     | Client's APIKEY access to TrawlingWeb system.            | Required value    | ?token={APIKEY} |

## BODY Parameters:

| Parameter   | Description                            | Default           | Limits                                                    |
| :---------- | :------------------------------------- | :---------------- | :-------------------------------------------------------- |
| description | Description of the Worker.              | Required value    | String up to 200 characters                                |
| words       | Search keywords.                       | Required value    | Number of words not exceeding agreed limit                  |

### Structure of the words parameter

The `words` parameter must be sent as a **JSON array** of text strings, where each array element represents a Keyword. Each Keyword can contain advanced TikTok syntax (hashtags, mentions, etc.).

### Example body in JSON format:

```json
{
    "description": "Example Worker for brand monitoring",
    "words": [
        "#pepsi",
        "@cocacola",
        "#openai"
    ]
}
```

In this example, the Worker is created with 3 Keywords:
1. A hashtag: "#pepsi"
2. A mention: "@cocacola"
3. A specific hashtag: "#openai"

Each element in the `words` array consumes 1 credit (1 credit = 1 Keyword).

# Output Response - RESPONSE

Upon making a request to the TikTok API, it will return a structured response as follows:

## Status 200 - Return Data

| Field  | Description                          |  Type  |
| ------ | ------------------------------------ | :----: |
| worker | Identifier of the created Worker.     | String |
| msg    | Description indicating successful action | String |

## Example response in JSON format:

```json
"response" : {
    "worker" : "...",
    "msg" : "..."
}
```
## Status 400 - Return Data

| Field | Description           |  Type  |
| ----- | --------------------- | :----: |
| error | Description of the error | String |

## Example response in JSON format:
```
json
"response" : {
    "error" : "..."
}
```

# Enhanced Searches with TikTok Syntax

TikTok utilizes its own advanced syntax to execute specific and detailed searches within its platform. This syntax allows filtering results by keywords, hashtags, mentions, locations, dates, and other parameters. When defining keywords for a Worker, you can use this syntax to launch precise queries against TikTok's search engine. This maximizes the efficiency and relevance of the data processed by each Worker, facilitating more effective monitoring and analysis of conversations on TikTok.

Here's a list of elements you can combine with your keywords when creating them within a worker:

| Type              | Description                                                                          | Example keyword                | Result                                                                           |
| ----------------- | :----------------------------------------------------------------------------------- | :----------------------------- | ----------------------------------------------------------------------------------- |
| Hashtag           | Terms referenced with the # symbol                                                     | #pepsi                         | returns posts that contain the hashtag (#) pepsi                                     |
| Mention           | Users referenced with the @ symbol                                                      | @cocacola                      | returns posts in which @cocacola has been tagged/mentioned                   |
| Specific Hashtag  | Search for specific hashtags                                                           | #openai                        | returns posts that contain the hashtag (#) openai                                 |

## Reserved Characters in Search Keywords

> The reserved characters are: + - = & | > < ! ¡ () {} [] ^ " ~ * ¿ ?: \ / ' -

# Contact

If you have any questions, need assistance, or want to contract or expand your services, please contact us.

**SAT (Technical Support):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20TikTok)

**SAC (Administrative Support):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales (Sales Support):**
* [Sales Email](mailto:sales@trawlingweb.com)
