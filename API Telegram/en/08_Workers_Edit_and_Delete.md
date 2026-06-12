# Telegram API - GET Method /delete

If a Worker is no longer useful to you, you can delete it and free space to create a new one.

# GET Parameters

Let's examine the structure of the example query:

```
https://telegram.trawlingweb.com/delete/xxxxxxxxxxxxx?token={APIKEY}
```

> Note: this endpoint also accepts the HTTP **DELETE** method with the same structure.

## PATH Parameters:

| Element  | Description                                  |
| :------- | :------------------------------------------- |
| protocol | Can be either **http** or **https**          |
| domain   | API address telegram.trawlingweb.com         |
| method   | delete                                       |
| id       | Identifier of the Worker to delete           |

## QUERY Parameters:

| Parameter | Description                                              | Default           | Example         |
| :-------- | :------------------------------------------------------- | :---------------- | :-------------- |
| token     | Client's APIKEY access to TrawlingWeb system.            | Required value    | ?token={APIKEY} |

# Output Response - RESPONSE

Upon making a request to the Telegram API, it will return a structured response as follows:

## Status 200 - Return Data

| Field  | Description                              |  Type  |
| ------ | ---------------------------------------- | :----: |
| worker | Identifier of the deleted Worker.        | String |
| msg    | Description indicating successful action | String |

## Example response in JSON format:

```json
"response" : {
    "worker" : "...",
    "msg" : "deleted"
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

# Worker characteristics

Captured data is stored in monthly indices `telegram_YYYY_MM` with the retention agreed in the client's plan (typically the last months queryable via `ts`/`tsi`).

Users can delete a specific Worker. This deletion destroys the Worker's configuration. Historical data associated with the Worker can no longer be queried through it once removed.

When a Worker is deleted, the consumer's available Workers counter is incremented again (as long as it does not exceed the plan's `counter_limit`).
