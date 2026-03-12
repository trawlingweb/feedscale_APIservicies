# FeedScale API - GET /posts Method

This method allows you to retrieve indexed FeedScale posts from BigQuery. Temporal delimiters can be used to narrow the returned content.

## GET Parameters

The API call is built from the basic structure:

```
https://feedscale.trawlingweb.com/posts?token={APIKEY}
```

### QUERY Parameters

| Parameter | Description | Default | Example |
| :-------- | :---------- | :------ | :------ |
| token | APIKEY to validate and access the system. Each user has their own individual and non-transferable APIKEY. | Required value | `?token=1234` |
| ts | Initial temporal delimiter (past time). Unix Time format in milliseconds. Results are ordered from past to present (ASC). | Delimits to 1 month in the past from the request | `&ts=1518472804000` |
| tsi | Final temporal delimiter (present time). Unix Time format in milliseconds. | Delimits with the request date | `&tsi=1524818189854` |
| size | Number of results per page | 500 (maximum: 500) | `&size=100` |

**Note**: `apiKey` is also accepted as an alternative to `token`, and `TS`/`TSI` in uppercase for compatibility.

---

## Pagination

Each API request can return a maximum of **500 posts** matching your query. However, there may be many more results that match your filter parameters. To consume all data, you must continue making calls to the URL indicated in the **next** parameter of each request's output.

**Result order**: Results are ordered in ascending order (ASC), from past (`ts`) to present (`tsi`). Older posts appear first, and newer posts at the end of each page.

### Pagination Output Example

```json
{
  "response": {
    "data": [...],
    "totalResults": 7940,
    "restResults": 7435,
    "next": "https://feedscale.trawlingweb.com/posts?token=1234&ts=1766312910631&tsi=1768866612000&size=500"
  }
}
```

### Pagination Fields

| Field | Description |
| ----- | ----------- |
| totalResults | Total number of results matching the query |
| restResults | Number of remaining results to consume |
| next | URL to get the next page of results. `null` when there are no more results |

### Modify Number of Results per Page

By default, the API returns 500 results per request. If you need to receive fewer results per call, you can adjust this number using the `size=n` parameter.

**Examples:**
- `size=100` - Will return 100 results per page
- `size=50` - Will return 50 results per page
- Without `size` - Will return 500 results (maximum)

---

## Call Examples

### Basic Query (Last month, 500 results per page)

```
https://feedscale.trawlingweb.com/posts?token=1234
```

### With Result Limit

```
https://feedscale.trawlingweb.com/posts?token=1234&size=100
```

### Last 24 Hours with Pagination

```
https://feedscale.trawlingweb.com/posts?token=1234&ts=1768818277820&tsi=1768904677820&size=100
```

---

## How to Calculate Timestamps

Timestamps must be in **Unix Time in milliseconds**.

### JavaScript

```javascript
const now = Date.now();

// Last 24 hours
const last24Hours = now - (24 * 60 * 60 * 1000);

// Last 7 days
const last7Days = now - (7 * 24 * 60 * 60 * 1000);

// Last month (30 days)
const last30Days = now - (30 * 24 * 60 * 60 * 1000);

// Example URL with pagination
const url = `https://feedscale.trawlingweb.com/posts?token=1234&ts=${last24Hours}&tsi=${now}&size=100`;
```

### Python

```python
import time

now = int(time.time() * 1000)  # milliseconds
last24hours = now - (24 * 60 * 60 * 1000)

url = f"https://feedscale.trawlingweb.com/posts?token=1234&ts={last24hours}&tsi={now}&size=100"
```

### Conversion Table

| Period | Milliseconds |
|--------|--------------|
| 1 hour | 3,600,000 |
| 24 hours | 86,400,000 |
| 7 days | 604,800,000 |
| 30 days | 2,592,000,000 |

---

## Consume All Results (Example)

### JavaScript

```javascript
async function consumeAllResults(initialUrl) {
  let url = initialUrl;
  let allResults = [];

  while (url) {
    const response = await fetch(url);
    const data = await response.json();
    
    allResults = allResults.concat(data.response.data);
    console.log(`Retrieved: ${allResults.length} / ${data.response.totalResults}`);
    
    url = data.response.next; // Next page or null if finished
  }

  console.log(`Total retrieved: ${allResults.length}`);
  return allResults;
}

// Usage
const url = 'https://feedscale.trawlingweb.com/posts?token=1234&size=500';
consumeAllResults(url);
```

### Python

```python
import requests

def consume_all_results(initial_url):
    url = initial_url
    all_results = []

    while url:
        response = requests.get(url)
        data = response.json()
        
        all_results.extend(data['response']['data'])
        print(f"Retrieved: {len(all_results)} / {data['response']['totalResults']}")
        
        url = data['response']['next']  # Next page or None if finished

    print(f"Total retrieved: {len(all_results)}")
    return all_results

# Usage
url = 'https://feedscale.trawlingweb.com/posts?token=1234&size=500'
results = consume_all_results(url)
```

---

## Output Response - RESPONSE

### Response Structure

```json
{
  "response": {
    "data": [
      {
        "id": 123,
        "c_noticia": 456,
        "published": "2025-12-21 10:00:00",
        "autor": "User",
        "marca": "Ueno",
        "origen": "twitter",
        "audiencia": 1000,
        "likes": 50,
        "retweet": 10,
        "comentarios": 5,
        "text": "Post text...",
        "url": "https://x.com/user/status/123",
        "tono": "Positive"
      }
    ],
    "totalResults": 7940,
    "restResults": 7440,
    "next": "https://feedscale.trawlingweb.com/posts?token=1234&ts=...&tsi=...&size=500"
  }
}
```

### Post Data

| Field | Description | Type |
| ----- | ----------- | ---- |
| id | Identification code assigned to each post | Integer |
| c_noticia | News code | Integer |
| published | Post publication date (format: YYYY-MM-DD HH:mm:ss) | String |
| autor | Author name | String |
| marca | Related brand | String |
| origen | Post origin (twitter, instagram, facebook, etc.) | String |
| audiencia | Estimated audience | Integer |
| likes | Number of likes | Integer |
| retweet | Number of retweets | Integer |
| comentarios | Number of comments | Integer |
| reproducciones | Number of reproductions | Integer |
| interacciones | Total interactions | Integer |
| sentimiento | Sentiment value | Integer |
| tono | Message tone (Positive, Negative, Neutral) | String |
| lang | Detected language | String |
| title | Post title | String |
| url | Post URL | String |
| text | Post text | String |

---

## HTTP Status Codes

| Code | Description |
| ------ | ----------- |
| 200 | Success! |
| 400 | Syntax error or invalid parameters |
| 401 | Unauthorized user or missing token |
| 403 | Invalid or unauthorized API Key |
| 500 | Query could not be executed |

---

## Health Check

To verify that the server is running:

```
https://feedscale.trawlingweb.com/health
```

Response:
```json
{
  "status": "ok",
  "timestamp": "2026-01-20T10:00:00.000Z",
  "service": "FeedScale API"
}
```

---

## Examples with cURL

```bash
# Basic (500 results)
curl "https://feedscale.trawlingweb.com/posts?token=1234"

# With limit of 100 results per page
curl "https://feedscale.trawlingweb.com/posts?token=1234&size=100"

# Last 24 hours with pagination
NOW=$(date +%s)000
LAST24H=$((NOW - 86400000))
curl "https://feedscale.trawlingweb.com/posts?token=1234&ts=${LAST24H}&tsi=${NOW}&size=100"
```
