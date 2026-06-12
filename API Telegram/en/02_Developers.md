# Telegram API - Things every developer should know

## Data Integrity

Data integrity refers to the accuracy, consistency, and reliability of data over time. To guarantee the integrity of the data provided by our API, Trawlingweb implements the following practices:

* **Continuous Verification**: Data is continuously verified during analysis to ensure accuracy and consistency.
* **Error Correction**: Any inconsistency or error detected in the data is corrected immediately to maintain reliability.
* **Regular Update**: Data is updated regularly to reflect the most recent and relevant information, minimizing the chance of stale data.
* **Source Maintenance**: Periodic maintenance is performed on the public channels and groups tracked to ensure that the processed data is of high quality and current.

Implementing these measures helps our clients maintain the integrity and reliability of the data processed by Trawlingweb.

## REST API

`telegram.trawlingweb.com` is a REST API, so although the data is meant to be consumed as a stream, you need to call the API continuously to receive the data batches.

## Authentication

Authentication is confirmed via a unique access token passed in the API URL together with the Worker ID to ingest.
You can find your access token and your Worker IDs in the dashboard.

## Rate Limit

All Telegram API plans include a single primary access token along with the specific identifier of each Worker.
A rate limit of one request every 5 seconds is applied. To exceed this limit, a specific request must be made.

## Output Formats

We provide the data in the following output format:

| Format | Description                |
| ------ | :------------------------- |
| JSON   | JavaScript Object Notation |

## HTTP / HTTPS support

`telegram.trawlingweb.com` supports both HTTP and HTTPS (SSL) endpoint calls. HTTPS is always recommended.

## GET Requests

You can call the API using GET requests. If you make very long queries, split them into shorter ones (using `ts` and `tsi` to bound the temporal range).

## HTTP Status Codes

| Code | Description                                  |
| ---- | :------------------------------------------- |
| 200  | Success!                                     |
| 400  | Missing params or malformed query            |
| 401  | Unauthorized user or no available tokens     |
| 404  | Syntax error                                 |
| 429  | Rate limit exceeded                          |
| 500  | Could not execute the query                  |
| 503  | Service temporarily unavailable              |

NOTE: Error details explained in the response payload.

# Contact
If you have any questions, need assistance, or want to subscribe or expand your services, please contact us.

**SAT (Technical Support):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20Telegram)

**SAC (Administrative Support):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales (Sales Support):**
* [Sales Email](mailto:sales@trawlingweb.com)
