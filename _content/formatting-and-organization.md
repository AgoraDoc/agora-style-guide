## Formatting and organization

### Headings and titles

Headings assist the reader in scanning content, helping them discover exactly what they are seeking. They provide structure and are visual points of reference for the reader.

Use headers to help outline your draft content. Some other points for consideration:

- Use sentence case for headings.
- Capitalize doc titles.
- Be descriptive and concise.
- Each heading should cover a specific topic.
- Focus on what the reader needs to know and what they can accomplish.
- Use ampersands or other symbols only if they appear in a UI or product name.
- Do not conclude a heading with a period. (An exception are FAQs whose titles are often phrased as a conversation with the reader).
- Do not skip levels of the heading hierarchy. For example, put an `<h3>` only under an `<h2>`.

### Lists

In most cases, the phrase before the list must be a complete sentence, not a partial one that is completed by the list items. The sentence can end with a colon or a period; usually a colon if it immediately precedes the list, or a period if there is more material (such as a note paragraph) between the introduction and the list.

:::{caution}
Never use a semicolon to end a list item.
:::

### Tables

Always introduce a table with a complete sentence and end it with a full stop, not a partial one that is completed by the table.

#### Table headings

- Use table headings for the first column and the first row only.
- Use sentence case.
- When referencing something specific (such as a unit of measure) in a table header, do not repeat it in the cells in that column. For example, if a table column header uses “Kbps”, there is no need to repeat it in the cells for that column.
- Write concise headings and omit articles (*a*, *an*, *the*).
- Do not end with punctuation, including a period, an ellipsis, or a colon.

#### Multi-paragraph table cells

To create multiple paragraphs, use the `<p>` element rather than using the `<br>` element.

### Notes

A note provides the reader with important or useful information that is not part of the regular flow of text.

Do not use Markdown's native ">" to create a note, as the visual effect it produces is poor. Instead, use HTML code format as outlined below for each note type.

:::{admonition} Exception
">" can be used in API Reference (code comments).
:::

Agora has three styles of notes, designed to convey a different level of importance depending on the circumstance.

#### Information

Provides supplemental information that is useful for the reader to know.

In Agora's online editor, wrap the notes in `<div class="alert info"></div>`.

:::{admonition} Example
![Example of info](img/notes-info.png)
:::

#### Note

Provides supplemental information that may not apply to all readers, but is important for those specific readers to know. In the following example, the context for the note only applies to those who have a firewall.

In Agora's online editor, wrap the notes in `<div class="alert note"></div>`.

:::{admonition} Example
![Example of note](img/notes-note.png)
:::

#### Warning

Designed to guide the reader away from a circumstance that poses some form of problem or hazard.

In Agora's online editor, wrap the notes in `<div class="alert warning"></div>`.

:::{admonition} Example
![Example of warning](img/notes-warning.png)
:::

### Numbers

Spell out all ordinal numbers in text. For example, first, fifth, twelfth, forty-third.

Do not start a sentence with a numeral. Add a modifier before the number, or spell the number out if you cannot rewrite the sentence.

:::{admonition} Exception
List items or table cells can start with numerals.
:::

In general, spell out the following:

- Numbers from zero through nine. An exception is when a number appears in a title.
- A number that starts a sentence. In some cases it is better to rearrange the sentence so that the number appears later.
- A number that is followed by a numeral.
- Indefinite and casual numbers.

In general, use numerals for the following:

- Numbers including and greater than 10.
- Version numbers.
- Technical quantities, such as amounts of memory, amounts of disk space, numbers of queries, or usage limits.
- Page numbers.
- Chapter numbers, sections, pages, and so on.
- Prices.
- Numbers without units, such as numbers used in mathematical expressions.
- Numbers less than 10 when they appear in the same sentence with numbers greater than 9.
- Negative numbers.
- [Percentages](https://developers.google.com/style/numbers#percentages).
- [Dimensions](https://developers.google.com/style/numbers#dimensions).
- Decimals.
- Measurements.
- [Numbers in a range](https://developers.google.com/style/numbers#ranges-of-numbers).

#### Commas in numbers

Use a comma to separate values in this thousands, hundreds of thousands, millions, and so on. For example, "Agora gives each Agora account 10,000 charge-free minutes each month."

| Recommended | Not recommended |
| :---------- | :-------------- |
| 1,000       | 1000            |
| 10,000      | 10000           |
| 100,000     | 100000          |
| 1,000,000   | 1000000         |

:::{admonition} Exception
- When referring to resolution values, such as "1080p", or "1920 × 1080", only use commas when the number has five or more digits. For example, "`width` should not exceed 1920, and `width` × `height` should not exceed `1920` × `1080`."
- Do not use commas in page numbers, phone numbers, addresses, or on the right of decimal points.
:::

### Currency

Agora technical documentation rarely mentions currency figures, but they do occasionally come up in billing-related documentation. In English documentation, the standard currency used is in US dollars. Please keep the following in mind when writing currency information.

#### Referencing the currency

When referencing US dollars, it is not enough to use the dollar symbol ("\$"), as there are other national currencies that also use the dollar, such as the Australian or Canadian dollars. When referencing US dollars, use "\$US". So long as an article references "\$US" within the article and there are no other currencies referenced, it will be understood that "\$" will mean "\$US".

For example:

| Service type    | Pricing (\$US/1,000 minutes) |
| --------------- | ---------------------------- |
| Recording audio | \$1.49                       |
| Recording video | High-Definition (HD): \$5.99 |

If you are writing about more than one type of currency within the same article, use the official [ISO 4217 three-letter currency code](https://www.thefinancials.com/Default.aspx?SubSectionID=curformat), which is "USD". Use this same ISO standard if you need to refer to other currencies in your documentation. The currency amount immediately follows the three-letter currency code with no intervening space. For large currency amounts, things are typically rounded to the nearest dollar, so there is no need to display the dollar amount to two decimal places.

:::{admonition} Example
In Q4 the company posted a net profit of CNY1,234,567 (USD176,297).
:::

If it is understood through context that the currency is in US dollars, there is no need to use the three-letter ISO code.

:::{admonition} Example
The American division posted a net revenue of $123,456.
:::

#### Using the dollar symbol and amounts

Always place the dollar symbol at the beginning of a currency value, without any intervening space. For example: "\$0.99".

If the amount is less than a full dollar, ensure that there is a leading 0 before the decimal point. Also, when referring to the small figures that are used in billing documentation, always use two decimal places for any dollar amount. For example "\$9.90", not "​\$9.9".

### Time

If a parameter or property expresses Unix time, describe it as "Unix time (in seconds since 1 January 1970) in UTC".

### Dates

Writing dates in a clear and unambiguous way helps with reader understanding, and with writing for a global audience.

In general, express months as a word rather than an abbreviation, in *month day, year* format. For example, "v3.0.0 was released on September 3, 2019." When space is tight (such as within a table), use a three-letter abbreviation for the month. When a full date appears in the middle of a sentence, add a comma after the year. For example, "The September 3, 2019, release of..."

Avoid using numeric dates when possible. Different countries and regions in the world express numeric dates in different formats, inevitably leading to confusion. If a numeric date cannot be avoided, use the format *yyyy-mm-dd*, (for example, "2019-09-03"), which conforms to the ISO 8601 international standard for numerical dates.

### Procedures

In most cases, introduce a procedure with an introductory sentence. The sentence can end with a colon or a period; usually a colon if it immediately precedes the procedure, or a period if there is more material (such as a note paragraph) between the introduction and the procedure.

| Recommended                                   | Not recommended           |
| :-------------------------------------------- | :------------------------ |
| To customize the buttons, follow these steps: | To customize the buttons: |

Here are more guidelines:

- In general, use one step per action. However, you can combine small actions into one step, using arrows (`>`) for sequential menu selections.
- Avoid having more than two levels of steps as this makes it hard for the reader to scan and to understand.
- When a step has sub-steps, treat the step like an [introductory sentence](https://developers.google.com/style/procedures#introductory-sentences): put a colon or a period at the end of the step, as appropriate.
- Do not make the procedure too long. If it starts to feel too long, consider splitting it into two procedures.
- If the user must press **Enter** or click **OK** after a step, then include that instruction as part of the step.
- State the purpose of the action before stating the action.
- State the location of the action before stating the action. If there are multiple headings associated with a set of procedures, restate the location of the action in the first step of each procedure, even if the location is the same as in the previous procedure.
- Do not use "please."
- For an optional step, type "Optional:" as the first word of the step.
- Use concise procedures to avoid repetitiveness and overwhelming the user with too much bolding of UI elements.
- Use complete sentences.
- Use parallel structure.

### Units of measurement

When specifying a unit of measurement, use a non-breaking space ( ) between the number and the unit. This guidance applies to HTML and Markdown sources.

However, when the unit of measure is money, degrees, or percent, do not leave a space.

In some contexts, it may be appropriate to indicate thousands of something by following a number with a lowercase "k". If you do that, then follow these guidelines:

- Do not put a space between the number and "k".
- Add a noun to indicate what the number measures, and to make clear that you are not using "k" as an abbreviation for "kilobytes."

See [](ref/units).

### Linking

#### When to link

Provide a link to the glossary at the first mention.

Provide links to reference documents except in code comments for the API Reference.

In an API Reference, when referring to an advanced guide, do not create a link, just use italics instead. For Chinese, use guillemets《》to indicate the reference.

:::{admonition} Example
See *Set the Audio Profile* for details.

详见《设置音频属性》。
:::

#### Link text

When you are writing link text, use a phrase that describes what the reader will see after following the link. That can take either of two forms:

- The exact title of the linked-to page, capitalized the same way the title is capitalized.
- A description of the linked-to page, capitalized like ordinary text instead of like a title.

A couple of specific things not to do in link text:

- Do not use the phrase "click here." (It is bad for accessibility and bad for scannability.)
- Similarly, do not use phrases like "this document." (It is easy to read "this" as meaning "the one you're reading now" rather than "the one I'm pointing to.")
- Do not use a URL as link text. Instead, use the page title or a description of the page.
- Do not include punctuation in the link text.

### Code in text

This section applies to all Agora documentation except the automatically generated API Reference.

In ordinary text sentences, use code font to mark up most things that have anything to do with code. In HTML, use the `<code>` element; in Markdown, use backticks (\`\`\`).

Some specific items to put in code font:

- Language keywords.
- Class names.
- Method, function, and callback names.
- XML and HTML element names. (Also place angle brackets (`<>`) around the element name; you may have to escape the angle brackets to make them appear in the document.)
- Attribute names and values.
- Filenames and paths. Start the path with a /, for example: `/etc/app/agora.app`.
- Defined (constant) values for an element or attribute.
- User inputs, for example: "Enter `demoChannel1` as the channel name".

### Code samples

In most cases, precede a code sample with an introductory sentence or paragraph. The intro can end with a colon or a period; usually a colon if it immediately precedes the sample, usually a period if there is more material (such as a note paragraph) between the introduction and the sample, or if the introduction paragraph ends in a sentence that is not directly related to the sample.

:::{caution}
Ensure that all the variants in the code samples are assigned values.
:::

### UI elements and interaction

When referring to any UI element by name, put its name in boldface, using the `<b>` element in HTML or `**` in Markdown. This includes names for buttons, menus, dialogs, windows, list items, or any other feature in the UI that has a visible name.

Do not make an official feature name or product name bold, except when it directly refers to an element in the UI that uses the name, for example a window title or button name.
