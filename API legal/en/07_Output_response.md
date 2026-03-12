# Legal API - Output Response

Once a request is made to the API, it will return a response with two distinct types of data:

## News Data

| Field           | Description                                                                                   | Filterable |  Type   |           Format            |
| --------------- | --------------------------------------------------------------------------------------------- | :--------: | :-----: | :-------------------------: |
| id              | Identification code assigned by Trawlingweb to each tracked publication                       |     No     | String  |                             |
| site_type       | Type of publication                                                                           |     No     | String  |                             |
| profile         | Publication profile                                                                           |     No     | String  |                             |
| edition_url     | Web address of the bulletin edition                                                           |     No     | String  |                             |
| edition_url_pdf | Address of the bulletin edition PDF file                                                      |     No     | String  |                             |
| edition_id      | Bulletin identifier                                                                           |    Yes     | String  |                             |
| edition_name    | Bulletin acronym                                                                              |    Yes     | String  |                             |
| edition_number  | Bulletin edition number                                                                       |    Yes     | Integer |                             |
| published       | Publication date                                                                              |    Yes     |  Date   |        ISO 8601-UTC         |
| crawled         | Processing date. Time zone is GMT +1                                                             |    Yes     | Integer | UNIX Timestamp milliseconds |
| language        | Publication language                                                                          |    Yes     | String  |          ISO 639-1          |
| section         | Publication language                                                                          |    Yes     | String  |                             |
| subsection      | Subsection                                                                                    |    Yes     | String  |                             |
| department      | Department                                                                                    |    Yes     | String  |                             |
| topic           | Associated terms                                                                              |     No     | String  |                             |
| Reference       | Publication identifier                                                                        |     No     | String  |                             |
| title           | Publication title                                                                             |    Yes     | String  |                             |
| text            | Publication text                                                                              |    Yes     | String  |                             |
| text_raw        | Indicates if the obtained text belongs to the complete page (true) or the publication (false) |     No     | Boolean |                             |
| url_html        | Web address of the publication                                                                |     No     | String  |                             |
| url_pdf         | Address of the publication PDF file                                                           |     No     | String  |                             |
| url_epob        | Address of the publication EPUB file                                                          |     No     | String  |                             |
| url_doc         | Address of the publication DOC file                                                           |     No     | String  |                             |
| url_xml         | Address of the publication XML file                                                           |     No     | String  |                             |

## Datos de petición

| Data         | Description                                         |  Type   |
| :----------- | :-------------------------------------------------- | :-----: |
| requestLeft  | Total queries pending from the subscription         | Integer |
| totalResults | Total results found by the query                    | Integer |
| restResults  | Total pending results for delivery                  | Integer |
| next         | URL to continue pagination and retrieve all results | String  |

## Example JSON Response:

```
"json"
"response" : {
    "data" : [{
        "id" : "...",
        "site_type" : "...",
        "profile" : "...",
        "edition_url" : "...",
        "edition_url_pdf" : "...",
        "edition_id" : "...",
        "edition_name" : "...",
        "edition_number" : "...",
        "published" : "...",
        "crawled" : "...",
        "language" : "...",
        "section" : "...",
        "subsection" : "...",
        "department" : "...",
        "topic" : "...",
        "Reference" : "...",
        "title" : "...",
        "text" : "...",
        "text_raw" : "...",
        "url_pdf" : "...",
        "url_html" : "...",
        "url_epob" : "...",
        "url_doc" : "...",
        "url_xml" : "..."
    }],
    "requestLeft" : "...",
    "totalResults" : "...",
    "restResults" : "...",
    "next" : "..."
}
```
