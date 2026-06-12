# Telegram API - GET Method /workers

Allows retrieving the Workers configured by the user along with their data.

# GET Parameters

Let's examine the structure of the example query:

```
https://telegram.trawlingweb.com/workers/?token={APIKEY}
```

## PATH Parameters:

| Element  | Description                                  |
| :------- | :------------------------------------------- |
| protocol | Can be either **http** or **https**          |
| domain   | API address telegram.trawlingweb.com         |
| method   | workers                                      |

## QUERY Parameters:

| Parameter | Description                                             | Default           | Example         |
| :-------- | :------------------------------------------------------ | :---------------- | :-------------- |
| token     | Client's APIKEY access to TrawlingWeb system.           | Required value    | ?token={APIKEY} |

# Output Response - RESPONSE

Upon making a request to the Telegram API, it will return a structured response as follows:

## Data per Worker

| Field       | Description                                              | Searchable | Sortable |  Type  |   Format     |
| ----------- | -------------------------------------------------------- | :--------: | :------: | :----: | :----------: |
| id          | Worker identification code                               |     No     |    No    | String |              |
| type        | Worker type (telegram)                                    |     No     |    No    | String |              |
| subtype     | Subtype (if applicable)                                   |     No     |    No    | String |              |
| description | Description set by the user                              |     No     |    No    | String |              |
| words       | Search keywords (array)                                  |     No     |    No    | Array  |              |
| created_at  | Worker creation date                                     |     No     |    No    | Date   | ISO 8601-UTC |
| status      | Worker activity status ( 1 running , 0 stopped )         |     No     |    No    | Integer|              |

## General data

| Field       | Description                   | Searchable | Sortable |  Type  | Format |
| ----------- | ----------------------------- | :--------: | :------: | :----: | :----: |
| workersLeft | Number of Workers available   |     No     |    No    | Integer|        |
| limit       | Maximum number of Workers     |     No     |    No    | Integer|        |

## Example response in JSON format:

```json
"response" : {
    "workers" : [{
            "id" : "...",
            "type" : "telegram",
            "subtype" : "...",
            "description" : "...",
            "words" : ["cocacola", "@cocacola"],
            "created_at" : "...",
            "status" : 1
    }],
    "workersLeft" : "...",
    "limit" : "..."
}
```
