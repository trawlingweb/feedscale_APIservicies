## What is a Worker?

A **Worker** in TrawlingWeb is a key entity that allows users to perform automated and specific searches over the captured posts and comments from Reddit, using Keywords. These Workers are configured by users to monitor, analyze, and process content in real time or at set intervals, according to their specific needs.

### How Workers Work

- **Keywords:** Each Worker is associated with one or more Keywords, which are search terms defined by the user. These terms can include mentions (u/username), subreddit names, exact terms, quoted phrases, or any word or phrase relevant to monitoring Reddit content. The effectiveness of a Worker depends on the precision and relevance of the configured Keywords.

- **Credits:** The number of Keywords a user can configure within a Worker depends on the credits available in their TrawlingWeb account. In TrawlingWeb, 1 credit equals 1 Keyword. Therefore, if a user has 10 credits, they can configure up to 10 Keywords across one or multiple Workers.

- **Crawling and Results:** Once configured, the Worker filters the continuous stream of posts and comments captured by our Reddit crawlers, looking for content matching the specified Keywords. Matching content (text, author, subreddit, date, etc.) is processed and stored in monthly indices `reddit_YYYY_MM`, allowing the user to access the data, analyze it, and generate detailed reports.

- **Search Intervals:** Users can query their Workers as often as needed, adjusting the call frequency according to the level of detail and timeliness required. This is particularly useful for real-time monitoring campaigns, where the immediacy of the information is crucial.

- **Customization:** Workers in TrawlingWeb allow combining configured Keywords with additional boolean / Lucene queries through the `q=` parameter, filtering by subreddit in the query, and bounding temporal ranges with `ts` and `tsi`. This customization ensures that the obtained results are highly relevant and specific to the user's needs.

### Example of Use

Suppose a brand wants to monitor in real time how a product launch is being discussed on Reddit. They configure a Worker in TrawlingWeb with Keywords such as the product name, the brand, and mentions of the official account (u/brand). As Trawlingweb crawlers capture posts and comments, the Worker analyzes and stores the matches, enabling the brand to analyze overall sentiment, identify relevant subreddits, and respond quickly to interactions.

### Benefits of Using Workers in TrawlingWeb

- **Efficiency:** Workers automate the search and monitoring process on Reddit, saving the user time and effort.
- **Scalability:** Users can adjust the number of Workers and Keywords according to their needs and available credits.
- **Precision:** By customizing Keywords and combining them with `q=` (including `subreddit:` filters) on each call, the results are highly relevant, enabling more effective analysis.
- **Immediacy:** Ideal for campaigns that require real-time information, such as crisis management, community monitoring, or product launches.

In summary, a Worker in TrawlingWeb is a powerful tool for managing and analyzing large volumes of Reddit posts and comments, providing valuable insights that can guide strategic decisions in real time.
