# API Twitter - POST Method /create

Allows creating new Workers with their words.

# What is a Worker?

A Worker in TrawlingWeb is an entity configured by the user to perform specific searches on social networks using Keywords. These Keywords are search terms configured within the Worker and are based on the credits purchased (1 credit = 1 Keyword).

## Creating and Configuring Workers

The user can create and define search terms for each Worker directly in the dashboard ([https://dashboard.trawlingweb.com/workers](https://dashboard.trawlingweb.com/workers)) or using the method provided by the API. Once a Worker is created, it begins its deployment to start its configuration process, which can take up to an hour.

## Functionality of Workers

- **Keywords**: Workers function as a list of keywords. They use the configured Keywords to perform searches on social networks.
- **Search Process**: Workers deliver the Keywords to TrawlingWeb's spiders to execute their searches on the social network.
- **Delivery Process**: Each time the client calls the Worker, it uses the list of Keywords to launch the search against the database of results obtained by TrawlingWeb and retrieve only those results that are related to the list of Keywords.

Implementing and managing Workers efficiently allows users to maximize the relevance and accuracy of the data processed, adapting to the specific needs of their social media analysis and monitoring.

# POST Parameters

Let's see the structure of the example query:

```
https://twitter.trawlingweb.com/create/?token={APIKEY}
```

## PATH Parameters:

| Element  | Description                         |
| :------- | :---------------------------------- |
| protocol | Can be either **http** or **https** |
| domain   | API address twitter.trawlingweb.com |
| method   | create                              |

## QUERY Parameters:

| Parameter | Description                                       | Default         | Example         |
| :-------- | :------------------------------------------------ | :-------------- | :-------------- |
| token     | Client's access APIKEY to the TrawlingWeb system. | Mandatory value | ?token={APIKEY} |

## BODY Parameters:

| Parameter   | Description                            | Default         | Limits                                               |
| :---------- | :------------------------------------- | :-------------- | :--------------------------------------------------- |
| description | Description that the Worker must have. | Mandatory value | String not exceeding 200 characters                  |
| words       | Search words.                          | Mandatory value | The number of words must not exceed the agreed limit |

### Structure of the words parameter

The `words` parameter must be sent as a **JSON array** of text strings, where each array element represents a Keyword. Each Keyword can contain advanced Twitter syntax (hashtags, mentions, boolean operators, filters, etc.).

**Important recommendation for searches with `from:`**: When you need to search for tweets from multiple accounts, you can chain up to a maximum of 10 accounts using the OR operator within a single expression. This allows you to optimize credit usage by grouping multiple accounts into a single Keyword.

### Example body in JSON format:

```json
{
  "description": "Example Worker for brand monitoring",
  "words": [
    "from:cocacola OR from:pepsi OR from:trawlingweb",
    "cocacola",
    "#pepsi",
    "cocacola lang:fr",
    "itau geocode:-25.2867,-57.647,250km OR ueno geocode:-25.2867,-57.647,250km OR basa geocode:-25.2867,-57.647,250km",
    "itau geocode:-25.2867,-57.647,250km min_faves:200",
    "cocacola filter:videos min_faves:100",
    "itau geocode:-25.2867,-57.647,250km min_faves:50 -from:itauparaguay"
  ]
}
```

In this example, the Worker is created with 8 Keywords:

1. A complex search with multiple accounts using the OR operator (maximum 10 accounts per expression)
2. A simple word: "cocacola"
3. A hashtag: "#pepsi"
4. A word with language filter: "cocacola lang:fr"
5. A chained geographic search with multiple terms using geocode and OR
6. A combination of word, geocoding, and popularity filter: "itau geocode:-25.2867,-57.647,250km min_faves:200"
7. A viral video search: "cocacola filter:videos min_faves:100"
8. A search with official account exclusion: "itau geocode:-25.2867,-57.647,250km min_faves:50 -from:itauparaguay"

Each element in the `words` array consumes 1 credit (1 credit = 1 Keyword).

# Output Response - RESPONSE

Once a request is sent to the Twitter API, it will return a response structured as follows:

## Status 200 - Return Data

| Field  | Description                              |  Type  |
| ------ | ---------------------------------------- | :----: |
| worker | Identifier of the created Worker.        | String |
| msg    | Description indicating successful action | String |

## Example response in json format:

```json
"response" : {
    "worker" : "...",
    "msg" : "..."
}
```

## Status 400 - Return Data

| Field | Description              |  Type  |
| ----- | ------------------------ | :----: |
| error | Description of the error | String |

## Example response in json format:

```json
"response" : {
    "error" : "..."
}
```

## Better searches with Twitter syntax

Twitter uses its own advanced syntax to perform specific and detailed searches within its platform. This syntax allows filtering results by keywords, hashtags, mentions, locations, and dates, among other parameters. Additionally, when defining keywords for a Worker, this same syntax can be used to launch precise queries against Twitter's search engine. This maximizes the efficiency and relevance of the data processed by each Worker, facilitating more effective monitoring and analysis of Twitter conversations.

Here is a list of elements you can combine with your keywords when creating them within a worker, organized by categories:

## Basic and Precision Searches

These elements allow you to refine and precisely target your searches by content type, location, accounts, language, and other specific filters:

| Type                                        | Description                                                                                                                                                      | Example keyword                     | Result                                                                                                                             |
| ------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Hashtag                                     | Terms referenced with the hashtag #                                                                                                                              | #pepsi                              | returns posts that contain hashtag (#) pepsi                                                                                       |
| At                                          | Users referenced with the at @                                                                                                                                   | @cocacola                           | returns posts in which @cocacola has been tagged/mentioned                                                                         |
| Simple String                               | Word with alphanumeric terms without special characters                                                                                                          | Studio54                            | returns posts that contain the word "Studio54"                                                                                     |
| Complex String                              | Words with alphanumeric terms without special characters separated by spaces                                                                                     | Cocoa Cola 2019                     | returns any post that contains some or all of these words from the example                                                         |
| Exact Search                                | Specific words or phrases in quotes                                                                                                                              | "cocacola with ice"                 | returns posts that contain exactly the phrase "cocacola with ice"                                                                  |
| OR Search                                   | Multiple words separated by OR to broaden results                                                                                                                | Cocacola OR Pepsi                   | returns posts that contain "Cocacola" or "Pepsi" (or both)                                                                         |
| Without words (NOT)                         | Exclude specific words from the search                                                                                                                           | Cocacola -pepsi                     | returns posts that contain "Cocacola" but excludes those that contain "pepsi"                                                      |
| Specific Hashtag                            | Search for specific hashtags                                                                                                                                     | #openai                             | returns posts that contain the hashtag (#) openai                                                                                  |
| From an account                             | Search for tweets sent by a specific account. Up to 10 accounts can be chained with OR within a single expression                                                | from:cocacola                       | returns posts published by the @cocacola account. Example with multiple: `from:account1 OR from:account2 OR ... OR from:account10` | 
| From an account mentioning specific content | Search for tweets sent by a specific account when the account mentions the word. In this case, accounts should not be chained with OR within a single expression | from:cocacola supermercados         | returns posts published by the @cocacola account only when it uses the word "supermercados".                                       |
| To an account                               | Search for tweets sent to a specific account                                                                                                                     | to:pepsi                            | returns posts directed to the @pepsi account                                                                                       |
| Mention of account                          | Search for tweets that mention a specific account                                                                                                                | @cocacola                           | returns posts in which @cocacola has been tagged/mentioned                                                                         |
| Geocoding (Most precise)                    | Search for tweets within a specific radius using exact GPS coordinates. This is the most precise method for geographic searches                                  | itau geocode:-25.2867,-57.647,250km | returns posts that contain "itau" sent within a radius of 250km from the specified coordinates (Asunción, Paraguay)                |
| Question                                    | Search for tweets that contain questions                                                                                                                         | pepsi ?                             | returns posts that contain "pepsi" and that are questions                                                                          |
| With links                                  | Search for tweets that contain links                                                                                                                             | cocacola filter:links               | returns posts that contain "cocacola" and that include links                                                                       |
| Video filter                                | Search for tweets that contain videos                                                                                                                             | cocacola filter:videos              | returns posts that contain "cocacola" and that include videos                                                                      |
| Image filter                                | Search for tweets that contain images                                                                                                                             | pepsi filter:images                 | returns posts that contain "pepsi" and that include images                                                                         |
| Specific source                             | Search for tweets published from a specific source                                                                                                               | pepsi source:twitterfeed            | returns posts that contain "pepsi" published from the twitterfeed source                                                           |
| Word with specific language                 | Search for tweets published in a specific language. Must be in ISO Alpha II                                                                                      | pepsi lang:fr                       | returns posts that contain "pepsi" published in French (ISO Alpha II: fr)                                                          |
| Account exclusion                           | Excludes tweets from a specific account using the minus prefix (-). Useful for seeing what real people say excluding official accounts                          | cocacola -from:cocacola             | returns posts that contain "cocacola" but excludes those published by the official @cocacola account                                |

## Popularity Searches

These elements allow you to filter results by number of likes (favorites), useful for finding viral or popular content:

| Type                                             | Description                                                                                                                               | Example keyword                                                                     | Result                                                                                                                             |
| ------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Popularity filter (min_faves)                    | Search for tweets with a minimum number of likes (favorites). Useful for finding viral or popular content                                | cocacola min_faves:200                                                              | returns posts that contain "cocacola" with at least 200 likes                                                                       |
| Combination: word + geocode + min_faves          | Combines word search, geographic location, and popularity filter. Spaces act as implicit AND                                            | itau geocode:-25.2867,-57.647,250km min_faves:200                                   | returns posts about "itau" within a 250km radius from Asunción with at least 200 likes                                            |
| Combination: viral videos                        | Combines word search, video filter, and popularity filter                                                                                 | itau geocode:-25.2867,-57.647,250km min_faves:200 filter:videos                     | returns viral videos about "itau" in Paraguay with at least 200 likes                                                             |
| Combination: exclusion + geocode + min_faves      | Combines account exclusion, geographic location, and popularity filter                                                                     | itau geocode:-25.2867,-57.647,250km min_faves:50 -from:itauparaguay                 | returns posts about "itau" in Paraguay with at least 50 likes, excluding the official account                                     |

## Time Freshness Searches

These elements allow you to filter results by specific dates or time ranges:

| Type                                             | Description                                                                                                                               | Example keyword                                                                     | Result                                                                                                                             |
| ------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Since date                                       | Search for tweets sent since a specific date                                                                                              | cocacola since:2022-02-17                                                           | returns posts that contain "cocacola" published since February 17, 2022                                                           |
| Until date                                       | Search for tweets sent until a specific date                                                                                               | pepsi until:2022-02-17                                                              | returns posts that contain "pepsi" published until February 17, 2022                                                               |
| Combination: date range + min_faves              | Combines word search, date range, and popularity filter                                                                                   | itau geocode:-25.2867,-57.647,250km min_faves:100 until:2024-01-01 since:2023-01-01 | returns posts about "itau" in Paraguay in 2023 with at least 100 likes                                                            |

### Combining Multiple Expressions

One of the most powerful features of Twitter syntax is the ability to combine multiple expressions and filters in a single Keyword. **X (Twitter) interprets each space as an implicit AND operator**, meaning you can chain different filters simply by separating them with spaces.

#### Important rules for combining expressions:

1. **Separation by spaces (implicit AND)**: Each space between expressions acts as an "AND also". For example:

   - `itau geocode:-25.2867,-57.647,250km min_faves:200` means: "itau" AND geocoded in that location AND with at least 200 likes.

2. **No spaces after colons**: It is critical that there are no spaces after the colons in commands:

   - ✅ Correct: `min_faves:200`
   - ❌ Incorrect: `min_faves: 200`

3. **Combining content filters**: You can combine content type filters with other parameters:

   - `filter:videos` - Only tweets with videos
   - `filter:images` - Only tweets with images
   - `filter:links` - Only tweets with links

4. **Exclusions with minus prefix (-)**: You can exclude accounts, words, or terms using the minus prefix:
   - `-from:account` - Excludes tweets from that account
   - `-word` - Excludes tweets containing that word

#### Practical examples of combinations:

**Search for viral videos in a specific location:**

```
itau geocode:-25.2867,-57.647,250km min_faves:200 filter:videos
```

Searches for videos about "itau" in Paraguay with at least 200 likes.

**Search excluding official accounts:**

```
itau geocode:-25.2867,-57.647,250km min_faves:50 -from:itauparaguay
```

Searches for mentions of "itau" in Paraguay with at least 50 likes, excluding the official account.

**Search within a date range with popularity filter:**

```
itau geocode:-25.2867,-57.647,250km min_faves:100 until:2024-01-01 since:2023-01-01
```

Searches for mentions of "itau" in Paraguay during 2023 with at least 100 likes.

**Search for images in a specific language:**

```
cocacola lang:es filter:images min_faves:20
```

Searches for images about "cocacola" in Spanish with at least 20 likes.

#### Note on min_faves and result ordering:

When using `min_faves:` with a high number, X usually shows results in the "Top" tab automatically. If you switch to "Latest", you'll see tweets that reached that number of likes sorted by date.

**Recommendation**: If no results appear with a high `min_faves:`, try lowering the number (for example, `min_faves:20` or `min_faves:50`) to verify that the syntax is correct and that content is available.

### Important notes on geographic searches

**Geocoding (`geocode:`)**: X (Twitter) does not support the `country:` command or a direct syntax by country code (such as `country:es`). The most accurate method to filter results by geographic location is to use `geocode:` with exact GPS coordinates.

**Geocode syntax:**

- Format: `geocode:latitude,longitude,radius`
- Example: `itau geocode:-25.2867,-57.647,250km` searches for mentions of "itau" within a 250km radius from Asunción, Paraguay.
- Coordinates must be in decimal format (latitude,longitude).
- The radius can be specified in kilometers (`km`) or miles (`mi`).

**Chaining multiple searches with OR:**
You can combine multiple search terms with geocoding using the OR operator within a single Keyword. This allows you to optimize credit usage by grouping related searches into a single Keyword:

```json
{
  "description": "Worker for geographic search of multiple terms in Paraguay",
  "words": [
    "itau geocode:-25.2867,-57.647,250km OR ueno geocode:-25.2867,-57.647,250km OR basa geocode:-25.2867,-57.647,250km"
  ]
}
```

This example searches for mentions of "itau", "ueno", or "basa" within a 250km radius from Asunción, Paraguay, using only 1 credit.

**Comparison of geographic methods:**

- `geocode:` - Most accurate, requires exact GPS coordinates. Recommended for professional searches.
- `near:` + `within:` - Less accurate, works with city names but can be less precise.
- `lang:` - Filters by tweet language, not by physical location. Useful when the goal is to filter by language rather than location.

**Important note**: Geographic filters only work with tweets from users who have location enabled in their posts or public profile.

### Table of capital city coordinates for geographic searches

Below is a table with GPS coordinates of the main capitals of Latin America and Europe, along with search examples using `geocode:` and the recommended radius to cover most of each country's territory:

#### Latin American Capitals

| Country            | Capital        | Coordinates (lat,lon) | Recommended radius | Search example                          |
| :----------------- | :------------- | :-------------------- | :----------------- | :-------------------------------------- |
| Argentina          | Buenos Aires   | -34.6037,-58.3816     | 800km              | `mochi geocode:-34.6037,-58.3816,800km`  |
| Bolivia            | La Paz         | -16.5000,-68.1500     | 600km              | `mochi geocode:-16.5000,-68.1500,600km`  |
| Brazil             | Brasília       | -15.7942,-47.8822     | 1200km             | `mochi geocode:-15.7942,-47.8822,1200km` |
| Chile              | Santiago       | -33.4489,-70.6693     | 800km              | `mochi geocode:-33.4489,-70.6693,800km`  |
| Colombia           | Bogotá         | 4.7110,-74.0721       | 600km              | `mochi geocode:4.7110,-74.0721,600km`    |
| Costa Rica         | San José       | 9.9281,-84.0907       | 200km              | `mochi geocode:9.9281,-84.0907,200km`    |
| Cuba               | Havana         | 23.1136,-82.3666      | 400km              | `mochi geocode:23.1136,-82.3666,400km`   |
| Ecuador            | Quito          | -0.1807,-78.4678      | 300km              | `mochi geocode:-0.1807,-78.4678,300km`   |
| El Salvador        | San Salvador   | 13.6929,-89.2182      | 150km              | `mochi geocode:13.6929,-89.2182,150km`   |
| Guatemala          | Guatemala City | 14.6349,-90.5069      | 250km              | `mochi geocode:14.6349,-90.5069,250km`   |
| Honduras           | Tegucigalpa    | 14.0723,-87.1921      | 250km              | `mochi geocode:14.0723,-87.1921,250km`   |
| Mexico             | Mexico City    | 19.4326,-99.1332      | 800km              | `mochi geocode:19.4326,-99.1332,800km`   |
| Nicaragua          | Managua        | 12.1364,-86.2514      | 300km              | `mochi geocode:12.1364,-86.2514,300km`   |
| Panama             | Panama City    | 8.9824,-79.5199       | 200km              | `mochi geocode:8.9824,-79.5199,200km`    |
| Paraguay           | Asunción       | -25.2867,-57.647      | 250km              | `mochi geocode:-25.2867,-57.647,250km`   |
| Peru               | Lima           | -12.0464,-77.0428     | 600km              | `mochi geocode:-12.0464,-77.0428,600km`  |
| Dominican Republic | Santo Domingo  | 18.4861,-69.9312      | 300km              | `mochi geocode:18.4861,-69.9312,300km`   |
| Uruguay            | Montevideo     | -34.9011,-56.1645     | 300km              | `mochi geocode:-34.9011,-56.1645,300km`  |
| Venezuela          | Caracas        | 10.4806,-66.9036      | 500km              | `mochi geocode:10.4806,-66.9036,500km`   |

#### European Capitals

| Country        | Capital    | Coordinates (lat,lon) | Recommended radius | Search example                       |
| :------------- | :--------- | :-------------------- | :----------------- | :----------------------------------- |
| Germany        | Berlin     | 52.5200,13.4050       | 500km              | `mochi geocode:52.5200,13.4050,500km` |
| Austria        | Vienna     | 48.2082,16.3738       | 300km              | `mochi geocode:48.2082,16.3738,300km` |
| Belgium        | Brussels   | 50.8503,4.3517        | 150km              | `mochi geocode:50.8503,4.3517,150km`  |
| Denmark        | Copenhagen | 55.6761,12.5683       | 300km              | `mochi geocode:55.6761,12.5683,300km` |
| Spain          | Madrid     | 40.4168,-3.7038       | 500km              | `mochi geocode:40.4168,-3.7038,500km` |
| Finland        | Helsinki   | 60.1699,24.9384       | 400km              | `mochi geocode:60.1699,24.9384,400km` |
| France         | Paris      | 48.8566,2.3522        | 500km              | `mochi geocode:48.8566,2.3522,500km`  |
| Greece         | Athens     | 37.9838,23.7275       | 300km              | `mochi geocode:37.9838,23.7275,300km` |
| Hungary        | Budapest   | 47.4979,19.0402       | 250km              | `mochi geocode:47.4979,19.0402,250km` |
| Ireland        | Dublin     | 53.3498,-6.2603       | 200km              | `mochi geocode:53.3498,-6.2603,200km` |
| Italy          | Rome       | 41.9028,12.4964       | 500km              | `mochi geocode:41.9028,12.4964,500km` |
| Norway         | Oslo       | 59.9139,10.7522       | 500km              | `mochi geocode:59.9139,10.7522,500km` |
| Netherlands    | Amsterdam  | 52.3676,4.9041        | 200km              | `mochi geocode:52.3676,4.9041,200km`  |
| Poland         | Warsaw     | 52.2297,21.0122       | 400km              | `mochi geocode:52.2297,21.0122,400km` |
| Portugal       | Lisbon     | 38.7223,-9.1393       | 300km              | `mochi geocode:38.7223,-9.1393,300km` |
| United Kingdom | London     | 51.5074,-0.1278       | 400km              | `mochi geocode:51.5074,-0.1278,400km` |
| Czech Republic | Prague     | 50.0755,14.4378       | 300km              | `mochi geocode:50.0755,14.4378,300km` |
| Romania        | Bucharest  | 44.4268,26.1025       | 400km              | `mochi geocode:44.4268,26.1025,400km` |
| Sweden         | Stockholm  | 59.3293,18.0686       | 600km              | `mochi geocode:59.3293,18.0686,600km` |
| Switzerland    | Bern       | 46.9481,7.4474        | 200km              | `mochi geocode:46.9481,7.4474,200km`  |

**Note**: The recommended radii are calculated to cover most of each country's territory. You can adjust the radius according to your specific search needs.

## Reserved characters in search words

> Reserved characters are: + - = & | > < ! ¡ () {} [] ^ " ~ \* ¿ ?: \ / ' -

# Contact

If you have any questions, need assistance, want to hire or expand your services, please contact us.

**Technical Support (SAT):**

- [Email SAT](mailto:support@trawlingweb.com)
- [Official Documentation](https://docs.trawlingweb.com)

**Administrative Support (SAC):**

- [Email SAC](mailto:gestion@trawlingweb.com)

**Sales Support:**

- [Email Sales](mailto:sales@trawlingweb.com)
