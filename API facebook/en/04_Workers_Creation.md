# API Facebook - POST Method /create

Allows creating new Workers with their keywords.

## What is a Worker?

A Worker in TrawlingWeb is an entity configured by the user to perform specific searches on social networks using Keywords. These Keywords are search terms configured within the Worker and are based on contracted credits (1 credit = 1 Keyword).

## Creation and Configuration of Workers

Users can create and define search terms for each Worker directly on the dashboard ([https://dashboard.trawlingweb.com/workers](https://dashboard.trawlingweb.com/workers)) or using the method provided by the API. Once a Worker is created, it begins its deployment to start its configuration task, which may take up to an hour.

## Functionality of Workers

- **Keywords**: Workers operate as a list of keywords. They use configured Keywords to perform searches on social networks.

* **Search process**: Workers deliver the keywords to TrawlingWeb spiders to execute searches on the social network.
* **Delivery process**: Each time the client calls the Worker, it uses the list of keywords to launch the search against the database of results obtained by TrawlingWeb and retrieve only those results related to the list of keywords.

Efficiently implementing and managing Workers allows users to maximize the relevance and accuracy of processed data, adapting to the specific needs of their social media analysis and monitoring.

# POST Parameters

Let's examine the structure of the example query:

```
https://facebook.trawlingweb.com/create/?token={APIKEY}
```

## PATH Parameters:

| Element  | Description                                 |
| :------- | :------------------------------------------ |
| protocol | Can be either **http** or **https**         |
| domain   | Address of the API Facebook.trawlingweb.com |
| method   | create                                      |

## QUERY Parameters:

| Parameter | Description                                       | Default         | Example         |
| :-------- | :------------------------------------------------ | :-------------- | :-------------- |
| token     | Client's APIKEY for access to TrawlingWeb system. | Mandatory value | ?token={APIKEY} |

## BODY Parameters:

| Parameter   | Description                | Default         | Limits                                     |
| :---------- | :------------------------- | :-------------- | :----------------------------------------- |
| description | Description of the Worker. | Mandatory value | String not exceeding 200 characters        |
| words       | Search keywords.           | Mandatory value | Number of words not exceeding agreed limit |

### Structure of the words parameter

The `words` parameter must be sent as a **JSON array** of text strings, where each array element represents a Keyword. Each Keyword can contain advanced Facebook syntax (hashtags, mentions, boolean operators, etc.).

### Example body in JSON format:

```json
{
  "description": "Example Worker for brand monitoring",
  "words": [
    "cocacola",
    "#pepsi",
    "@cocacola",
    "Cocacola (__) Pepsi",
    "\"cocacola with ice\""
  ]
}
```

In this example, the Worker is created with 5 Keywords:

1. A simple word: "cocacola"
2. A hashtag: "#pepsi"
3. A mention: "@cocacola"
4. An OR search using (**): "Cocacola (**) Pepsi"
5. An exact search in quotes: "cocacola with ice"

Each element in the `words` array consumes 1 credit (1 credit = 1 Keyword).

# Output Response - RESPONSE

Upon making a request to the Facebook API, it will return a structured response as follows:

## Status 200 - Return Data

| Field  | Description                              |  Type  |
| ------ | ---------------------------------------- | :----: |
| worker | Identifier of the created Worker.        | String |
| msg    | Description indicating successful action | String |

## Example response in json format:

```
json
"response" : {
    "worker" : "...",
    "msg" : "..."
}
```

## Status 400 - Return Data

| Field | Description              |  Type  |
| ----- | ------------------------ | :----: |
| error | Description of the error | String |

## Example response in json format:

```
json
"response" : {
    "error" : "..."
}
```

# Enhanced Search with Facebook Syntax

Facebook employs its own advanced syntax for executing specific and detailed searches within its platform. This syntax allows filtering results by keywords, hashtags, mentions, locations, dates, among other parameters. Furthermore, when defining keywords for a Worker, this syntax can be used to launch precise queries against Facebook's search engine. This maximizes the efficiency and relevance of the data processed by each Worker, facilitating more effective monitoring and analysis of conversations on Facebook.

Here is a list of elements you can combine with your keywords when creating them within a worker:

| Type             | Description                                                                  | Example keyword       | Result                                                                     |
| ---------------- | :--------------------------------------------------------------------------- | :-------------------- | -------------------------------------------------------------------------- |
| Hashtag          | Terms referenced with the # symbol                                           | #pepsi                | returns posts that contain the hashtag (#) pepsi                           |
| Mention          | Users referenced with the @ symbol                                           | @cocacola             | returns posts in which @cocacola has been tagged/mentioned                 |
| Simple String    | Words with alphanumeric terms without special characters                     | Studio54              | returns posts that contain the word "Studio54"                             |
| Complex String   | Words with alphanumeric terms without special characters separated by spaces | Cocoa Cola 2019       | returns any post that contains some or all of these words from the example |
| Exact Search     | Specific words or phrases enclosed in quotation marks                        | "cocacola with ice"   | returns posts that contain exactly the phrase "cocacola with ice"          |
| OR Search        | Multiple words separated by (\_\_) to expand results                         | Cocacola (\_\_) Pepsi | returns posts that contain "Cocacola" or "Pepsi" (or both)                 |
| Specific Hashtag | Search for specific hashtags                                                 | #openai               | returns posts that contain the hashtag (#) openai                          |

## Reserved Characters in Search Words

> Reserved characters include: + - = & | > < ! ¡ () {} [] ^ " ~ \* ¿ ?: \ / ' -

# Contact

If you have any questions, need assistance, want to hire or expand your services, please contact us.

**Technical Support (SAT):**

- [SAT Email](mailto:support@trawlingweb.com)
- [Official Documentation](https://docs.trawlingweb.com)

**Administrative Support (SAC):**

- [SAC Email](mailto:gestion@trawlingweb.com)

**Sales Support (Sales):**

- [Sales Email](mailto:sales@trawlingweb.com)
