# API NEWS & BLOGS - Things that every developer should know

## API REST

Trawlingweb.com API NEWS & BLOGS is an API REST, so although the data is intended to be consumed as a data stream, it is necessary to call the API continuously in order to receive the data batches.

## Data Integrity

Data integrity refers to the accuracy, consistency, and reliability of data over time. To ensure the integrity of the data provided by our API, Trawlingweb implements the following practices:

* **Continuous Verification**: Data is continuously verified during the indexing process to ensure its accuracy and consistency.
* **Error Correction**: Any inconsistencies or errors detected in the data are promptly corrected to maintain its reliability.
* **Regular Updates**: Data is regularly updated to reflect the most recent and relevant information, minimizing the possibility of outdated data.
* **Source Maintenance**: Periodic maintenance of media sources is performed to ensure that the indexed data is of high quality and up-to-date.

Implementing these measures helps our clients maintain the integrity and reliability of the data indexed by Trawlingweb.

## URL Structure

### The URL query call has three parts:

- Authentication
- The HTTP GET parameters string to set the timestamp, size of page and reception format file.
- The query string to set up the pairs **filters:value** that specifies the wanted data.

## Authentication

Authentication is effective with an unique valid access token included in the URL API call. Client can find his access token in his client control pannel.

## Rate limit

All API plans include a single unique access token, with a built-in querying limitation of one request per second. To overcome this limit, a second plan must be added.

## Output formats

Two file formats are avaiable in order to receive the response to the query:

| Format | Description                |
| ------ | :------------------------- |
| JSON   | JavaScript Object Notation |
| XML    | eXtensible Markup Language |

## HTTP / HTTPS security support API

Twalingwerb.com supports both HTTP and HTTPS (SSL) endpoint calls.

## GET requests

API is called with GET requests. In order to optimeze the requests, it's better to make several short queries than a very long single query.

## HTTP status codes

| Code | Description                                     |
| ---- | :---------------------------------------------- |
| 200  | Success!                                        |
| 401  | Unauthorized user or without available tokens   |
| 404  | Syntax error                                    |
| 500  | The query could not be executed: internal error |
| 503  | Service temporarily unavailable                 |
| 429  | Exceeds rate limit                              |

NOTE: Detail of the error explained in the return of the request.

---
**Contact Us:**
If you have any questions, need assistance, want to hire or expand your services, please contact us.

**Technical Support (SAT):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://docs.trawlingweb.com)

**Administrative Support (SAC):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales Support (Sales):**
* [Sales Email](mailto:sales@trawlingweb.com)