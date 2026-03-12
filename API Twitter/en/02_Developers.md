# Twitter API - Things Every Developer Should Know

## Data Integrity

Data integrity refers to the accuracy, consistency, and reliability of data over time. To ensure the integrity of the data provided by our API, Trawlingweb implements the following practices:

* **Continuous Verification**: Data is continuously verified during the analysis process to ensure its accuracy and consistency.
* **Error Correction**: Any inconsistencies or errors detected in the data are corrected immediately to maintain its reliability.
* **Regular Updates**: Data is updated regularly to reflect the most recent and relevant information, minimizing the possibility of obsolete data.
* **Source Maintenance**: Periodic maintenance of media sources is performed to ensure that the processed data is high-quality and up-to-date.

Implementing these measures helps our clients maintain the integrity and reliability of the data processed by Trawlingweb.

## REST API

Trawlingweb.com is a REST API, so although the data is intended to be consumed as a data stream, it is necessary to call the API continuously in order to receive data batches.

## Authentication

Authentication is confirmed through a unique access token passed in the API call URL along with the Worker ID to ingest.
You can find your access token and Worker IDs in the control panel.

## Rate Limit

All Twitter API plans include a single main unique access token along with the specific identifier of each Worker.
A rate limit of one request every 5 seconds is established. To exceed this limit, a specific request must be made.

## Output Formats

We provide data in the following output format:

| Format | Description                |
| ------ | :------------------------- |
| JSON   | JavaScript Object Notation |

## HTTP/HTTPS Security Support

Trawlingweb.com supports both HTTP and HTTPS (SSL) endpoint calls.

## GET Requests

You can call the API using GET requests. If you make very long API calls, split them into multiple shorter queries.

## HTTP Status Codes

| Code | Description                                    |
| ---- | :--------------------------------------------- |
| 200  | Success!                                       |
| 401  | Unauthorized user or no tokens available       |
| 404  | Syntax error                                   |
| 500  | Query execution failed                         |
| 503  | Service temporarily unavailable                |
| 429  | Rate limit exceeded                            |

NOTE: Error details explained in the request return.

# Contact

If you have any questions, need assistance, want to hire or expand your services, please contact us.

**Technical Support (SAT):**
* [Email SAT](mailto:support@trawlingweb.com)
* [Official Documentation](https://docs.trawlingweb.com)

**Administrative Support (SAC):**
* [Email SAC](mailto:gestion@trawlingweb.com)

**Sales Support:**
* [Email Sales](mailto:sales@trawlingweb.com)
