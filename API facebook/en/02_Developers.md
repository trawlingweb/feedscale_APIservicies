# Facebook API - Things Every Developer Should Know

## Data Integrity

Data integrity refers to the accuracy, consistency, and reliability of data over its entire lifecycle. To ensure the integrity of data provided by our API, Trawlingweb implements the following practices:

* **Continuous Verification**: Data is continuously verified during the processing stage to ensure its accuracy and consistency.
* **Error Correction**: Any inconsistency or error detected in the data is immediately corrected to maintain its reliability.
* **Regular Updates**: Data is regularly updated to reflect the most recent and relevant information, minimizing the risk of outdated data.
* **Source Maintenance**: Periodic maintenance of media sources is conducted to ensure that processed data is high-quality and current.

Implementing these measures helps our clients maintain the integrity and reliability of the data processed by Trawlingweb.

## REST API

Trawlingweb.com operates as a REST API, meaning that while data is intended to be consumed as a data stream, continuous API calls are necessary to receive batches of data.

## Authentication

Authentication is confirmed through a unique access token passed in the API call URL along with the Worker ID to ingest. You can find your access token and Worker IDs in the control panel.

## Rate Limit

All Facebook API plans include a single main unique access token along with the specific ID of each Worker. A request rate limit of one request every 5 seconds is enforced. Requests to exceed this limit must be specifically requested.

## Output Formats

We provide data in the following output format:

| Format | Description                |
| ------ | :------------------------- |
| JSON   | JavaScript Object Notation |

## HTTP / HTTPS Security Support API

Trawlingweb.com supports both HTTP and HTTPS (SSL) endpoint calls.

## GET Requests

You can make API calls using GET requests. If making lengthy calls to the API, split them into shorter queries.

## HTTP Status Codes

| Code | Description                                    |
| ---- | :--------------------------------------------- |
| 200  | Success!                                        |
| 401  | Unauthorized user or no available tokens        |
| 404  | Syntax error                                    |
| 500  | Query execution failed                          |
| 503  | Service temporarily unavailable                 |
| 429  | Exceeded rate limit                             |

NOTE: Detailed error explanation is provided in the request response.

# Contact
If you have any questions, need assistance, want to subscribe or expand your services, please contact us.

**Technical Support (SAT):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://docs.trawlingweb.com)

**Administrative Support (SAC):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales Support (Sales):**
* [Sales Email](mailto:sales@trawlingweb.com)
