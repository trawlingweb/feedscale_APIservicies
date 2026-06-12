## What is a Worker?

A **Worker** in TrawlingWeb is a key entity that allows users to perform automated and specific searches over the captured messages from public Telegram channels and groups, using Keywords. These Workers are configured by users to monitor, analyze, and process content in real time or at set intervals, according to their specific needs.

### How Workers Work

- **Keywords:** Each Worker is associated with one or more Keywords, which are search terms defined by the user. These terms can include mentions (@username), exact terms, quoted phrases, or any word or phrase relevant to monitoring Telegram messages. The effectiveness of a Worker depends on the precision and relevance of the configured Keywords.

- **Credits:** The number of Keywords a user can configure within a Worker depends on the credits available in their TrawlingWeb account. In TrawlingWeb, 1 credit equals 1 Keyword. Therefore, if a user has 10 credits, they can configure up to 10 Keywords across one or multiple Workers.

- **Crawling and Results:** Once configured, the Worker filters the continuous stream of messages captured by our Telegram crawlers, looking for content matching the specified Keywords. Matching content (message text, author, channel, date, etc.) is processed and stored in monthly indices `telegram_YYYY_MM`, allowing the user to access the data, analyze it, and generate detailed reports.

- **Search Intervals:** Users can query their Workers as often as needed, adjusting the call frequency according to the level of detail and timeliness required. This is particularly useful for real-time monitoring campaigns, where the immediacy of the information is crucial.

- **Customization:** Workers in TrawlingWeb allow combining configured Keywords with additional boolean / Lucene queries through the `q=` parameter, as well as bounding temporal ranges with `ts` and `tsi`. This customization ensures that the obtained results are highly relevant and specific to the user's needs.

### Example of Use

Suppose a brand wants to monitor in real time how a product launch is being discussed on public Telegram channels. They configure a Worker in TrawlingWeb with Keywords such as the product name, the brand, and mentions of the official account. As Trawlingweb crawlers capture messages from public channels, the Worker analyzes and stores the matches, enabling the brand to analyze overall sentiment, identify relevant channels, and respond quickly to interactions.

### Benefits of Using Workers in TrawlingWeb

- **Efficiency:** Workers automate the search and monitoring process on Telegram, saving the user time and effort.
- **Scalability:** Users can adjust the number of Workers and Keywords according to their needs and available credits.
- **Precision:** By customizing Keywords and combining them with `q=` on each call, the results are highly relevant, enabling more effective analysis.
- **Immediacy:** Ideal for campaigns that require real-time information, such as crisis management, leak monitoring, or product launches.

In summary, a Worker in TrawlingWeb is a powerful tool for managing and analyzing large volumes of public Telegram messages, providing valuable insights that can guide strategic decisions in real time.
