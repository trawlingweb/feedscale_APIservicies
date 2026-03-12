# Legal API - Filtering Parameter

The following filters allow you to obtain only the data you need.

| Filter       | Description                                                                                                                                          |
| :----------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| site         | Website from which we want or do not want to retrieve data.                                                                                          |
| domain       | Domain from which we want or do not want to retrieve data.                                                                                           |
| title        | Words or phrases that should or should not appear in the titles of desired publications.                                                             |
| text         | Words that should or should not appear in the desired publications.                                                                                  |
| language     | Language of the publications we want to include or exclude in the retrieval. See language codes[ISO 639-1](https://es.wikipedia.org/wiki/ISO_639-1). |
| site_country | Country of the website. See country codes according to [ISO-3166-2](https://es.wikipedia.org/wiki/ISO_3166-2).                                       |
| crawled      | Indexing date (in milliseconds). [Converter](http://www.onlineconversion.com/unix_time.htm)                                                             |

## How to Assign a Filter Expression

    q = "(_filtro1_: __valor1__) operador (_filtro2_ : valor2) operador ... (_filtroN_ : valorN)"

> In this expression, spaces have been added between terms for clarity, but you should avoid them when making queries.

## More Information on Combination and Search Possibilities

For more information, you can refer to the complete Lucene query syntax manual ( [aquí](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html) ) which is the basis of our search engine.

## Escaping Reserved Characters

If you need to use any of the characters that function as operators in your own query (and not as operators), then you must escape them with an initial backslash.
For example, to search for url: url:https://www.linkedin.com, you need to write your query as url:https \:\ / \ / www.linkedin.com.

> The reserved characters are: + - = && || > <! () {} [] ^ "~ \*?: \ /

Failure to escape these special characters correctly could result in a syntax error that prevents the query from executing correctly.

## Examples of **q** Filters

| Example                                                               | Explanation                                                                                                               |
| :-------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| (site: elpais.com OR site: lavanguardia.com)                          | Retrieve only publications from the websites elpais.com or lavanguardia.com or both.                                      |
| NOT (site:yahoo.com AND site:google.com)                              | Retrieve publications from all websites except yahoo.com and google.com.                                                  |
| ((title:rajoy AND (text:España OR text:Morales)) NOT title:españoles) | Retrieve only publications whose title includes the words "rajoy" and (or "españa" or "morales") and exclude "españoles". |
| (language:es OR language:cat)                                         | Retrieve only publications in Spanish or Catalan.                                                                         |
| (site_language:es OR site_language:cat)                               | Retrieve only publications from websites whose language is Spanish or Catalan.                                            |
| NOT (site_language:es OR site_language:cat)                           | Retrieve all publications except those published on websites whose language is Spanish or Catalan.                        |
