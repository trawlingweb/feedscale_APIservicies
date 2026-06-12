# Trawlingweb.com Telegram API

Welcome to the Trawlingweb.com Telegram API documentation. Our API provides access to structured data from **public Telegram channels and public groups messages**. Our advanced systems analyze, process, and structure this data for on-demand querying, offering an efficient and tailored solution for your public messaging analytics needs.

## Key Features:

* **Credit-Based Subscription**: Service subscription based on credit plans redeemable for keyword searches, where 1 credit = 1 keyword. This allows clients to choose the number of credits they wish to purchase, enabling them to create and monitor keywords within Telegram.
* **Keywords**: A Keyword is a search term configured within a "worker". The number of Keywords you can register depends on the credits purchased (1 credit = 1 Keyword). Workers use these keywords to filter the captured Telegram messages and gather specific data, which is stored and available for query and download via REST API. Therefore, workers function as a list of keywords.

    Examples of keywords and credits required for creation:

|   Keyword   | Number of Elements | Credits Required (c1) |                          Executable Search                          |
|-------------|--------------------|-----------------------|---------------------------------------------------------------------|
|  @cocacola  |         1          |           1           | Mentions of an account or what an account posts containing other keywords |
|  cocacola   |         1          |           1           | Exact term in the message text                                       |
| "coca cola" |         1          |           1           | Exact phrase in the message text                                     |

* **Structured Access to Telegram Data**: Obtain organized public Telegram messages from channels and public groups for analysis and further processing.
* **Advanced Analysis Technology**: We employ state-of-the-art systems that ensure precise and up-to-date analysis of captured data.
* **On-Demand Storage and Query**: Processed data is stored in monthly indices (`telegram_YYYY_MM`) to enable quick and flexible queries as per your needs.
* **Multilingual Coverage**: Messages in multiple languages, with extended coverage on public channels relevant to brand monitoring, reputation, and intelligence.
* **Versatility and Optimization**: Combine the worker's keyword list with boolean / Lucene queries via the `q=` parameter to refine results without consuming additional credits.

### Benefits for Businesses:

* **Public Messaging Monitoring**: Facilitates tracking of conversations on public Telegram channels and groups, providing valuable insights into brand perception, campaigns, crises, and emerging topics.
* **Sentiment Analysis**: Allows detailed analysis of sentiment in messages, aiding in better understanding of public opinion and reactions to specific events.
* **Early Detection**: Supports early detection of critical mentions, leaks, alerts, and disinformation circulating on public channels.
* **Intelligence and Risk**: Useful for reputation, compliance, and corporate security teams who need visibility over what is said on Telegram.

Our Telegram API is designed to be a powerful and versatile tool, tailored to the diverse public messaging analysis needs of our users. We invite you to explore the documentation and discover how you can leverage our advanced capabilities in analyzing and processing Telegram data to the fullest.

---

# Contact
If you have any questions, need assistance, wish to subscribe or expand your services, please contact us.

**Technical Support (SAT):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20Telegram)

**Administrative Support (SAC):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales Support (Sales):**
* [Sales Email](mailto:sales@trawlingweb.com)
