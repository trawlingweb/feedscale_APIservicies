# Trawlingweb.com Reddit API

Welcome to the Trawlingweb.com Reddit API documentation. Our API provides access to structured data from **public Reddit posts and comments**. Our advanced systems analyze, process, and structure this data for on-demand querying, offering an efficient and tailored solution for your forum analytics needs.

## Key Features:

* **Credit-Based Subscription**: Service subscription based on credit plans redeemable for keyword searches, where 1 credit = 1 keyword. This allows clients to choose the number of credits they wish to purchase, enabling them to create and monitor keywords within Reddit.
* **Keywords**: A Keyword is a search term configured within a "worker". The number of Keywords you can register depends on the credits purchased (1 credit = 1 Keyword). Workers use these keywords to filter the captured Reddit posts and comments and gather specific data, which is stored and available for query and download via REST API. Therefore, workers function as a list of keywords.

    Examples of keywords and credits required for creation:

|     Keyword     | Number of Elements | Credits Required (c1) |                          Executable Search                          |
|-----------------|--------------------|-----------------------|---------------------------------------------------------------------|
|   u/cocacola    |         1          |           1           | Mentions of a user or what a user posts containing other keywords    |
|    cocacola     |         1          |           1           | Exact term in post/comment text                                       |
|   "coca cola"   |         1          |           1           | Exact phrase in post/comment text                                     |

* **Structured Access to Reddit Data**: Obtain organized public Reddit posts and comments for analysis and further processing.
* **Subreddit Search**: Filter by the subreddit where content appears (`subreddit` field indexed and searchable).
* **Advanced Analysis Technology**: We employ state-of-the-art systems that ensure precise and up-to-date analysis of captured data.
* **On-Demand Storage and Query**: Processed data is stored in monthly indices (`reddit_YYYY_MM`) to enable quick and flexible queries as per your needs.
* **Versatility and Optimization**: Combine the worker's keyword list with boolean / Lucene queries via the `q=` parameter to refine results without consuming additional credits.

### Benefits for Businesses:

* **Public Forum Monitoring**: Facilitates tracking of conversations and trends on Reddit, providing valuable insights into brand perception, community dynamics, and emerging topics.
* **Sentiment Analysis**: Allows detailed analysis of sentiment in discussion threads, aiding in better understanding of public opinion and reactions to specific events.
* **Identification of Relevant Communities**: Detect the subreddits where your brand, product, or category is most discussed.
* **Marketing Strategies**: Supports the development of marketing strategies based on real discussion and engagement data on Reddit.

Our Reddit API is designed to be a powerful and versatile tool, tailored to the diverse forum and online community analysis needs of our users. We invite you to explore the documentation and discover how you can leverage our advanced capabilities in analyzing and processing Reddit data to the fullest.

---

# Contact
If you have any questions, need assistance, wish to subscribe or expand your services, please contact us.

**Technical Support (SAT):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20Reddit)

**Administrative Support (SAC):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales Support (Sales):**
* [Sales Email](mailto:sales@trawlingweb.com)
