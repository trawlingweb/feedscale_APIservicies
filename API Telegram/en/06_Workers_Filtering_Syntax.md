# Using Basic Boolean Queries in the TrawlingWeb Telegram API

The TrawlingWeb APIs accept boolean queries combined with Lucene syntax expressions. Below are some practical examples that will help you have a better experience and optimize your searches and results when using the Telegram API.

Remember that these boolean expressions can only be used within the `q=` parameter in the API call and must be combined with the required filters and PATH parameters.

## Always inside `q=`
Boolean queries and Lucene syntax parameters must always be used inside the `q=` parameter in the API call URL structure. The elements within `q=` constitute the entire query attached to the API call.

## Essential Boolean Operators AND, OR, and NOT

Boolean queries allow combining keywords or phrases using specific operators. Below are the available operators and some useful examples:

|  Operator   | Usage                                                                                                  |       Example        |
| :---------: | :----------------------------------------------------------------------------------------------------- | :------------------: |
| x **AND** y | "**x**" and "**y**" will both appear in the retrieved documents.                                       | "Messi" AND "Girona" |
| x **OR** y  | In the retrieved documents, "**x**", "**y**", or both will appear. Parentheses are recommended.        | ("Messi" OR "Girona")|
|  **NOT** x  | Documents containing "**x**" will not be retrieved.                                                    |      NOT "Messi"     |

### Parentheses

Use parentheses to encapsulate OR statements and ensure search engines run the query correctly. The OR operator is interpreted as "I would like at least one of these terms."

For example: _(Barcelona OR Madrid OR Paris)_

### Quotes

Quotes must be used to search for exact phrases of more than one word. Without quotes, you could get messages with the words split into individual components.

For example: _White House_

Without quotes, results might include messages containing _White_ and _House_ but not necessarily together. Using quotes, you tell the system to only return messages containing the exact phrase in that order.

For example: _"White House"_

# Using Lucene Query Syntax

The TrawlingWeb APIs allow queries that may contain boolean operators combined with Lucene syntax expressions, offering a powerful tool to perform complex and precise searches. Lucene's query syntax is designed to be intuitive and expressive.

Below are some key features and useful examples to optimize your user experience:


1.  **Term Query**: Searches for a specific term.

    ```
    cocacola
    ```

2.  **Phrase Query**: Searches for an exact phrase by enclosing it in double quotes.

    ```
    "coca cola cherry flavor"
    ```

3.  **Wildcard Query**: Use `?` to replace a single character or `*` to replace zero or more characters.

    ```
    - ambigu?  : (returns ambiguOus or ambiguIty)
    - ejem*    : (returns, among others, results containing words like ejemPLO, ejemPLOS, ejemPLAR, etc.)
    - *finance : (returns, among others, results containing words like "microfinance", "finance", "macrofinance", etc.)
    ```

4.  **Boolean Operators**
    Use `AND`, `OR`, and `NOT` to combine multiple terms or phrases.

        Examples

        AND: Used to find records containing both terms or phrases.

        Mcdonalds AND "Burger King"

        OR: Used to find records containing at least one of the terms or phrases.

        Mcdonalds OR "Burger King"

        NOT: Used to exclude records containing the following term or phrase.

        Mcdonalds AND NOT "Burger King"

5. **Field-Specific Queries**: Specify a field to search in particular parts of the message. In Telegram, searchable fields are `text`, `user_name`, and `user_screen_name`.
   ```
   text:"exact phrase"
   user_screen_name:publicchannel
   ```

   ***Remember: Boolean queries or Lucene syntax parameters must always be used within the q= parameter in the API call URL structure. The elements within q= constitute the entire query attached to the API call.***

### Useful examples for grouping search elements

(...) Use parentheses to group clauses and form subqueries.

```
(cocacola OR pepsi) AND (campaign NOT crisis)
```

### Examples of the most common Lucene queries used by our clients

Here are some examples of queries to illustrate the use of Lucene syntax in our Telegram API:

* Search for messages containing the word "technology":

  ```
  technology
  ```

* Search for messages with the exact phrase "artificial intelligence":

  ```
  "artificial intelligence"
  ```

* Search for messages with "change" in the text from the channel "news":

  ```
  user_screen_name:news AND text:change
  ```

* Search for messages mentioning "economy" but not "recession":
  ```
  economy NOT recession
  ```

### More Information

For more details, see the full Lucene syntax manual ([here](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html)), which is the basis of our search engine.

## Conclusion and More Information

Using the Lucene query syntax with TrawlingWeb's Telegram API allows you to create precise and complex searches, ensuring you retrieve the most relevant data. For a more complete understanding of Lucene's query syntax, see the [official Lucene documentation](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html).

If you have any questions or need further assistance, please contact our support team.

---

# Contact
If you have any questions, need assistance, or want to contract or expand your services, please contact us.

**SAT (Technical Support):**
* [SAT Email](mailto:support@trawlingweb.com)
* [Official Documentation](https://github.com/trawlingweb/APIservicies/tree/main/API%20Telegram)

**SAC (Administrative Support):**
* [SAC Email](mailto:gestion@trawlingweb.com)

**Sales (Sales Support):**
* [Sales Email](mailto:sales@trawlingweb.com)
