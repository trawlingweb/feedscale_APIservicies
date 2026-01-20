# FeedScale API by Trawlingweb.com

Welcome to the FeedScale API documentation by Trawlingweb.com. Our API provides access to a structured repository of posts captured from multiple social media and digital media sources. Data is stored in BigQuery and available for on-demand queries through a REST API, offering an effective and scalable solution for your content analysis and brand monitoring needs.

## What is GeriAI?

**GeriAI** is the cognitive artificial intelligence engine developed by Trawlingweb that automatically processes and analyzes posts captured in the FeedScale repository. GeriAI is an advanced Fine Tuning system that uses Natural Language Processing (NLP), Machine Learning, Deep Learning, Sentiment Analysis, Named Entity Recognition (NER), Text Classification, Topic Analysis (LDA, BERT), Semantic Embeddings, and Transfer Learning techniques to transform unstructured content into intelligent and actionable data.

### GeriAI Multidimensional Analysis

GeriAI enriches each post with cognitive analysis across **9 standard dimensions**:

1. **Message Intent**: Classifies the communicative purpose (advertising, complaint, denunciation, praise, recommendation, etc.)
2. **Country of Origin**: Determines the most likely country of the author based on linguistic and cultural indicators
3. **Author Profile**: Identifies the author's role (consumer, affected, collaborator, executive, media, influencer, etc.)
4. **Author Gender**: Identifies the apparent gender based on linguistic indicators
5. **Age Range**: Estimates the author's age range (15-20, 21-30, 31-40, 41-55, 56+)
6. **Sensitive Topics**: Identifies critical sector-specific topics that require special attention
7. **Message Tone**: Analyzes the communicative style (official, personal, critical, supportive, neutral, emotional, etc.)
8. **Appeal Type**: Identifies the persuasive strategy (emotional, logical, authority, urgency, social)
9. **Ecosystem Focal Entity**: Classifies the sectorial or thematic context of the content

### Additional Analysis

In addition to the standard dimensions, GeriAI provides:

- **Sentiment Analysis**: Automatic sentiment classification (positive, negative, neutral) with precise numerical values (`sentimiento`, `tono_positivo`, `tono_neutro`, `tono_negativo`)
- **Thematic Categorization**: Automatic classification into up to 20 different thematic categories (`categoria1` to `categoria20`), enabling granular content analysis
- **Language Detection**: Automatic identification of the language of each post (`lang`)
- **Brand Analysis**: Detection and classification of brand mentions, including main brand (`marca_principal`) and related brands (`marcas_relacion`)

### Automatic Processing

All these analyses are automatically performed by GeriAI during the capture and storage process in BigQuery. The data you obtain through this API already includes these cognitive artificial intelligence enrichments, ready to be used directly in your analyses, reports, and KPI generation without additional processing.

## Main Features:

- **Structured Access to FeedScale Data**: Get post data in an organized and accessible format from BigQuery for analysis and subsequent processing. Data includes detailed information about posts from Twitter, Instagram, Facebook, and other sources.

- **Advanced Storage Technology**: We use Google BigQuery as the storage and query engine, ensuring scalability, performance, and the ability to handle large volumes of historical data.

- **On-Demand Queries**: Captured data is efficiently stored in BigQuery, allowing fast and flexible queries according to your specific analysis needs.

- **Smart Pagination**: The API implements a pagination system that allows efficient consumption of large data volumes, with a maximum of 500 results per request to ensure server performance.

- **Flexible Temporal Filtering**: Use temporal delimiters (`ts` and `tsi`) to narrow your queries to specific date ranges, from the last few hours to complete historical periods.

- **API Key Authentication**: Secure authentication system through individual and non-transferable tokens, linked to your services and specific characteristics.

### Benefits for Businesses:

- **Brand Monitoring**: Enables companies to track mentions and conversations about their brands across multiple platforms, providing valuable insights into brand perception and market dynamics.

- **Sentiment Analysis with GeriAI**: Access pre-processed sentiment analysis by GeriAI, enabling detailed sentiment analysis of posts (positive, negative, neutral) without the need to manually process data. This helps better understand public opinion and reactions to specific events immediately.

- **Temporal Analysis**: Access historical data to perform trend analysis, temporal comparisons, and track conversation evolution over time.

- **Data-Driven Marketing Strategies**: Supports the development of marketing strategies based on real interaction and social media participation data.

- **BigQuery Integration**: Data is stored in BigQuery, allowing direct integrations with business data analysis and visualization tools.

### Data Structure:

The API provides access to a complete set of fields for each post, including:

- **Post Information**: ID, text, URL, publication date, author
- **Engagement Metrics**: Likes, retweets, comments, reproductions, total interactions
- **GeriAI Analysis**: Sentiment (numerical values), tone (positive/negative/neutral), tono_positivo, tono_neutro, tono_negativo, thematic categories (categoria1 to categoria20)
- **Metadata**: Language, origin (platform), related brand, classification categories
- **Brand Information**: Main brand, related brands, agent ID, company ID

### Response Format:

The API returns data in structured JSON format, including:

- **Post Data**: Array with posts matching your search criteria
- **Pagination Information**: Total results, remaining results, URL for the next page
- **Applied Filters**: Information about the parameters used in the query

Our FeedScale API is designed to be a powerful and versatile tool, adapted to the diverse content analysis and social media monitoring needs of our users. We invite you to explore the documentation and discover how you can make the most of our advanced query and data analysis capabilities.

---

## Quick Start

To start using the API, you will need:

1. **Access Token**: Your unique API Key provided by Trawlingweb
2. **Base Endpoint**: `http://localhost:3000/feedscaleaiposts` (or production URL)
3. **Query Parameters**: `token`, `ts`, `tsi`, `size` (optional)

### Basic Example:

```
GET http://localhost:3000/feedscaleaiposts?token=YOUR_API_KEY
```

This call will return the last 500 results from the last month, with pagination information to access more data if needed.

---

## Contact

If you have any questions, need assistance, want to contract or expand your services, please contact us.

**SAT (Technical Support):**

- [SAT Email](mailto:support@trawlingweb.com)
- [Official Documentation](https://docs.trawlingweb.com)

**SAC (Administrative Support):**

- [SAC Email](mailto:gestion@trawlingweb.com)

**Sales (Sales Support):**

- [Sales Email](mailto:sales@trawlingweb.com)
