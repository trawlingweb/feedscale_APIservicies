# Telegram API - POST Method /create

Allows creating new Workers with their keywords.

## What is a Worker?

A Worker in TrawlingWeb is a user-configured entity to perform specific searches over the captured messages from public Telegram channels and groups using Keywords. These Keywords are search terms configured within the Worker and are based on the contracted credits (1 credit = 1 Keyword).

## Creation and Configuration of Workers

Users can create and define search terms for each Worker directly on the dashboard ([https://dashboard.trawlingweb.com/workers](https://dashboard.trawlingweb.com/workers)) or using the method provided by the API. Once a Worker is created, it starts filtering the stream of captured messages according to its keywords (results become available almost immediately).

## Workers Functionality

* **Keywords**: Workers function as a list of keywords. They use the configured Keywords to filter the stream of public messages captured from Telegram.
- **Search Process**: Workers apply keywords against the `text`, `user_name`, and `user_screen_name` fields of each message.
- **Delivery Process**: Each time the client calls the Worker, it uses the list of Keywords to launch the search against the database of messages captured by TrawlingWeb and retrieve only those results matching the list of Keywords (combinable with boolean filters via `q=`).

Implementing and managing Workers efficiently allows users to maximize the relevance and accuracy of the processed data, tailored to the specific needs of their Telegram analysis and monitoring.

# POST Parameters

Let's examine the structure of the example query:

```
https://telegram.trawlingweb.com/create/?token={APIKEY}
```

## PATH Parameters:

| Element  | Description                                  |
| :------- | :------------------------------------------- |
| protocol | Can be either **http** or **https**          |
| domain   | API address telegram.trawlingweb.com         |
| method   | create                                       |

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

The `words` parameter must be sent as a **JSON array** of text strings, where each array element represents a Keyword. Each Keyword can be a simple term, a quoted phrase, or a mention (@username).

### Example body in JSON format:

```json
{
    "description": "Example Worker for brand monitoring",
    "words": [
        "cocacola",
        "\"coca cola\"",
        "@cocacola"
    ]
}
```

In this example, the Worker is created with 3 Keywords:
1. A simple term: "cocacola"
2. An exact phrase: "coca cola"
3. A mention: "@cocacola"

Each element in the `words` array consumes 1 credit (1 credit = 1 Keyword).

# Output Response - RESPONSE

Upon making a request to the Telegram API, it will return a structured response as follows:

## Status 200 - Return Data

| Field  | Description                              |  Type  |
| ------ | ---------------------------------------- | :----: |
| worker | Identifier of the created Worker.        | String |
| msg    | Description indicating successful action | String |

## Example response in JSON format:

```json
"response" : {
    "worker" : "...",
    "msg" : "created"
}
```
## Status 400 - Return Data

| Field | Description           |  Type  |
| ----- | --------------------- | :----: |
| error | Error description     | String |

## Example response in JSON format:
```json
"response" : {
    "error" : "..."
}
```

# Enhanced Searches with Telegram Syntax

Unlike networks with structured hashtags, Telegram is mostly plain text — so the effective syntax for defining keywords centers on exact terms, quoted phrases, and mentions. This syntax allows filtering results by terms, phrases, account mentions, and date ranges. When defining keywords for a Worker, this syntax maximizes the efficiency and relevance of the data processed by each Worker.

Here's a list of elements you can combine with your keywords when creating them within a worker:

| Type              | Description                                                                          | Example keyword                | Result                                                                           |
| ----------------- | :----------------------------------------------------------------------------------- | :----------------------------- | ----------------------------------------------------------------------------------- |
| Exact term        | Single word without special characters                                                | cocacola                       | returns messages containing the word **cocacola** in the text                       |
| Exact phrase      | Multi-word phrase enclosed in double quotes                                           | "coca cola"                    | returns messages containing the exact phrase **coca cola**                          |
| Mention           | Accounts referenced with the @ symbol                                                | @cocacola                      | returns messages in which @cocacola has been tagged/mentioned                       |

## Reserved Characters in Search Keywords

> The reserved characters are: + - = & | > < ! ¡ () {} [] ^ " ~ * ¿ ?: \ / ' -

# Contact

If you have any questions, need assistance, or want to contract or expand your services, please contact us.

**SAT (Technical Support):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20Telegram)

**SAC (Administrative Support):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales (Sales Support):**
* [Sales Email](mailto:sales@trawlingweb.com)
