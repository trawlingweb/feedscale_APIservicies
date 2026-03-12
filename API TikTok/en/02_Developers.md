# TikTok API - Things Every Developer Should Know

## Data Integrity

Data integrity refers to the accuracy, consistency, and reliability of data over its entire lifecycle. To ensure the integrity of data provided by our API, Trawlingweb implements the following practices:

* **Continuous Verification**: Data is continuously verified during the analysis process to ensure accuracy and consistency.
* **Error Correction**: Any detected inconsistency or error in the data is promptly corrected to maintain reliability.
* **Regular Updates**: Data is regularly updated to reflect the latest and most relevant information, minimizing the risk of outdated data.
* **Source Maintenance**: Periodic maintenance of media sources ensures that processed data is of high quality and current.

Implementing these measures helps our clients maintain the integrity and reliability of data processed by Trawlingweb.

## REST API

Trawlingweb.com provides a RESTful API, where data is meant to be consumed as a data stream. Continuous API calls are necessary to receive batches of data.

## Authentication

Authentication is done via a unique access token passed in the API call URL along with the Worker ID to ingest. You can find your access token and Worker IDs in the control panel.

## Rate Limit

All TikTok API plans include a single unique main access token along with the particular IDs of each Worker. A request rate limitation is set for one every 5 seconds. To exceed this limit, you will have to specifically solve.

## Output Formats

We provide data in the following output format:

| Format | Description                |
| ------ | :------------------------- |
| JSON   | JavaScript Object Notation |

## HTTP/HTTPS Security Support API

Twalingwerb.com supports both HTTP and HTTPS (SSL) endpoint calls.

## GET Requests

You can call the API using GET requests. If you make very long calls to the API, split them into several shorter queries.

## HTTP Status Codes

| Code | Description                                    |
| ---- | :--------------------------------------------- |
| 200  | Success!                                        |
| 401  | Unauthorized user or no tokens available        |
| 404  | Syntax error                                    |
| 500  | Query execution failed                          |
| 503  | Service temporarily unavailable                 |
| 429  | Exceeded rate limit                             |

NOTE: Error details explained in the request return.

---

# Contact
If you have any questions, need assistance, wish to subscribe or expand your services, please contact us.

**Technical Support (SAT):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20TikTok)

**Administrative Support (SAC):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales Support (Sales):**
* [Sales Email](mailto:sales@trawlingweb.com)
