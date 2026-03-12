# API NEWS & BLOGS - Filtering parameters

Filters are attributes assigned by TrawlingWeb to each element during its source and result auditing process. These filters allow you to specify detailed criteria to obtain only the data you need. By applying these filters in your queries, you can refine the results to better match your specific requirements. The available filters are described below:

| Filter        | Description                                                                                                                           |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------ |
| site          | Website from which we want data (or not)                                                                                              |
| domain        | Internet domain from which we want data (or not)                                                                                      |
| title         | Words and expressions that must be present (or not) in the titles of returned publications                                            |
| text          | Words and expressions that must be present (or not) in the body text of returned publications                                         |
| language      | Natural language of the required (or refused) publications. See language codes [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1)   |
| site_language | Website's language of the required (or refused) publications: en (english), es (spanish), fr (french), ...                            |
| site_country  | Website's country of the required (or refused) publications. See country codes [ISO-3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) |
| site_region   | Website region. See [ISO-3166-2](https://es.wikipedia.org/wiki/ISO_3166-2)                                                            |
| author        | Author of the publication. For example, "Shakespeare"                                                                                 |
| published     | Publishing timestamp in miliseconds. [Conversor](http://www.onlineconversion.com/unix_time.htm)                                       |
| crawled       | Indexing timestamp in miliseconds. [Conversor](http://www.onlineconversion.com/unix_time.htm)                                         |
| site_type     | Type of website: general, news, blog or discussion                                                                                    |

## How to build a filter expression

    q = "(filter1: value1) operator (filter2: value2) operator ... (filterN: valueN__)"

> The spaces between the parts of the expression have been added only in order to gain clarity.

## More Information on Combination and Search Capabilities
For more information on Lucene operators and syntax, you can refer to [Section 07: Best Practices](#section07_best_practices). You can also consult the complete Lucene syntax manual [here](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html), as it is the basis of our search engine.


## Scaping special characters

Some characters are part of the query syntax: \+ \- \* && || ! () [] {} ^ " ? ~ : \\ \/

In order to avoid confusions they must be preceded by the "**\\**" character in the query expression. To search (1+1):2 we have to build the querry as it follows: **\\(1\\+1\\)\\:2**.

Let's see another example: to search the URL https://www.linkedin.com we must rewrite as **url:https \:\ / \ / www.linkedin.com**.

## Examples of Filters and Booleans within **q=**

As explained in Section 03 Queries, the TrawlingWeb APIs accept boolean queries combined with Lucene syntax expressions.

The `q=` parameter allows for filtering and optimizing the query to obtain the best possible results. Within `q=`, you can use filtering parameters (see ), which are attributes assigned by TrawlingWeb to each element, as well as boolean expressions that are characteristics of the indexed information.

Remember that in Section 03 Queries, there is a more complete list of boolean expressions that you can combine with filters within `q=`. Below are some examples of filtering parameters.


| Example                                                               | Explanation                                                                                                           |
| :-------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| ```(site: elpais.com OR site: lavanguardia.com)```                          | Retrieve publications from the websites elpais.com or lavanguardia.com or from the both.                              |
| ```NOT (site:yahoo.com AND site:google.com)```                              | Retrieve publications from all the websites excepts from the yahoo.com and google.com websites.                       |
| ```((title:rajoy AND (text:España OR text:Morales)) NOT title:españoles)``` | Retrieve publications where title includes the words "rajoy" and (or "españa" or "morales") and excludes "españoles". |
| ```(language:es OR language:es)```                                          | Retrieve only publications in spanish or french languages.                                                            |
| ```(site_language:es OR site_language:fr)```                                | Retrieve publications from spanish or french websites.                                                                |
| ```NOT (site_language:es) OR NOT (site_language:fr)```                      | Don't retrieve publications from spanish or french websites.                                                          |
| ```author:Pedrolo```                                                        | Retrieve only Manuel de Perolo's publications.                                                                        |
| ```(site_type:news OR site_type:blogs)```                                   | Retrieve publications from news websites or blog websites.                                                            |
| ```NOT (site_type:news)```                                                  | Don't retrieve publication from news websites.                                                                        |

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