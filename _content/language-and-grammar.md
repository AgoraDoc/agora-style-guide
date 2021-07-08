## Language and grammar

### Abbreviations, acronyms, and initialisms

**Quick reference:**
- Do not use abbreviations. Exceptions: Units of measure with numbers, and "Ltd." or "Inc."
- Capitalize acronyms.
- Do not use periods after the letters in acronyms. Exception: "U.S." when it is used as an adjective.
- Spell out uncommon acronyms the first time they appear. Example: "A New Acronym (ANA)."
- Do not use Latin abbreviations such as "e.g." or "etc."
_________

Abbreviations are a shortened version of a word used to represent the whole. Examples include "s" for "seconds" or "approx." for "approximately." 

As a general rule, only use abbreviations in technical documentation for units of measure, and then only when they are joined with a number. For example, "15 s" is acceptable, but "The interval is measured in s." is not. Do not use a period after an abbreviated unit of measure. For more information, see [Units of Measurement](formatting-and-organization.md#units-of-measurement). 

In most other cases (such as "approx."), spell out the word. The only obvious exceptions are "Ltd." or "Inc." in a company's name.

Note that some short forms have entered common speech and are now accepted as words themselves, such as "app" or "demo." If you are unsure if a short form is in common use, you can check the dictionary or consult with other writers.

Acronyms and initialisms are a type of abbreviation formed from the initial letters of other words. The difference between them is in pronunciation; acronyms are pronounced like words, whereas with initialisms each letter is pronounced individually. Examples of acronyms include "GIF" for "Graphics Interchange Format" and "RAM" for "random-access memory." Examples of initialisms include "SDK" for "Software Development Kit" and "API" for "Application Programming Interface."

The pronunciation is important when choosing which form of the indefinite article to use. For more information, see [Articles](language-and-grammar.md#articles-a-an-the). 

Some words can be considered either acronyms or initialisms depending on personal preference, such as "FAQ." In such cases, check the department's word list first for the preferred choice. If there is none, choose one and make sure you use it consistently afterwards. For example, Agora treats FAQ as an intialism, so you would write "an FAQ" (that is, "an eff-ay-cue") rather than "a FAQ" ("a fack").

Always capitalize every letter in an acronym or initialism unless it is a company-specific spelling (for example, "macOS").

Do not use periods after the letters of acronyms or initialisms. The only exception is "U.S." when used as an adjective (you should spell out the noun). 

:::{admonition} Example
Servers located in the United States provide services to U.S. users.
:::

Note that some acronyms have evolved into words (for example, "modem") and are now treated as words, meaning they are not capitalized.

Many abbreviations and acronyms/initialisms can be considered understood by average readers and do not need to be spelled out. If a term is new or uncommon, however, spell out the first mention of it in the text, followed immediately by the abbreviation in parentheses. Use the abbreviated form for all subsequent references.

:::{admonition} Example
The communication between the user and the Agora server is protected by transmission protocols, such as the Agora private transmission protocol, Transport Layer Security (TLS), and Web Socket Secure (WSS). Consult the API guide for guidelines on implementing TLS and WSS on your project.
:::

#### Latin abbreviations

Do not use abbreviations derived from Latin. Always use their English equivalents. 

| Do this... | ...instead of this |
| :---------| :------- |
| For example | e.g. (for ""exempli gratia") | 
| In other words   | i.e. (for "id est")   |
| and so on   | etc. (for "et cetera")   |

#### Abbreviations at the end of a sentence

If a sentence ends with an abbreviation, the period used for the abbreviation also serves as the period for the sentence.

:::{admonition} Example
For more information, contact Agora Inc.
:::

### Active voice

**Quick reference:**
- Favor the active voice where possible.
_________

Generally speaking, with the active voice the subject of a sentence performs the action, whereas with the passive voice the subject is acted upon by something else.

The active voice sounds immediate and clear. The passive voice usually sounds more wordy and can obscure the subject, making it difficult for readers to fully understand your meaning. 

| Recommended                       | Not recommended                         |
| :-------------------------------- | :-------------------------------------- |
| This method gets the user ID. | This method is used to get the user ID. |
| The callback provides troubleshooting information | Troubleshooting information is provided by the callback. |

This is not a hard and fast rule. The passive voice can be used to emphasize the object of the action or the action itself. Also, it may not always be possible to phrase your sentence with an active voice, such as in status code explanations. For example, "This method is not implemented."

### Anthropomorphism

**Quick reference:**
- Do not attribute human qualities to software, hardware, or companies/brands.
_________

Anthropomorphism is the attribution of human traits or characteristics to non-human things. This is too metaphorical and informal in the context of technical writing.

| Do this...                                               | ...instead of this                                              |
| :-------------------------------------------------------- | :----------------------------------------------------------- |
| A Delimiter object specifies where to split a string. | A Delimiter object tells the splitter where a string should be broken. |
| The PC detects a new device.                          | The PC sees a new device.                                    |

:::{admonition} Example
Combine the teacher's video with each of the students' videos.
:::

### Articles (a, an, the)

**Quick reference:**
- Singular countable nouns must have an article or similar determiner.
- Plural countable nouns can have a definite article or no article.
- Do not use an article with proper nouns or uncountable (mass) nouns.
- Use a definite article plus "method" or "callback" to specify its function unless it is obvious from context.
- Do not normally use a leading article with "mode." Example: "Put the device into silent mode."
_________

Articles are a type of word called a determiner. Determiners are parts of noun phrases that provide information about specificity, quantity, or possession. 

"A" and "an" are indefinite articles. They are used before a singular countable noun when referring to any member of a group. For example, "Download a text editor." means any text editor will do.

Note that "countable" nouns are called that because they can be separated from a group and counted. For example, "channels" or "users."

"The" is a definite article. It is used before a singular countable noun when referring to a particular member of a group. For example, "Download the text editor from the sample folder." means you need a specific text editor. 

A plural countable noun can also be specified with a definite article. For example, "Extract the script files to your project folder." points you to some specific files.

Note that singular countable nouns *require* an article or some other type of determiner, such as "one," "your," or "this." They cannot exist on their own. 

| Do this...                                           | ...instead of this                                    |
| :--------------------------------------------------- | :---------------------------------------------------- |
| You need a token (or *the* token, or *your* token) to access the channel. | You need token to access the channel. | 

Some types of nouns do not take articles. For example, non-specific plural nouns ("Script files can be useful."), proper nouns ("Agora is a wonderful company."), and uncountable or mass nouns ("Planning is crucial to success.").

Note that many nouns can shift between "countable" and "uncountable" based on context, and they may therefore sometimes require an article and sometimes not. For example, "Information can be lost to user error. Be sure to back up the information in your project folder regularly."

#### Choosing "a" or "an"

When using an indefinite article, the sound of a word or acronym when it is spoken determines whether "a" or "an" precedes it. Use "a" before a word that starts with a consonant *sound*, and "an" for words that begin with a vowel *sound*. For example, "a URL" and "an SDK".

#### Articles and internal agreement

Methods and callbacks must be specified, so when referring to a method or callback, use a leading "the" followed by "method" or "callback". For example "the SDK triggers the Client.on("disable-local-video") callback".


You can omit "the" and "method" or "callback" when the reader will understand what it is through context.

:::{admonition} Example
The CheckPermission method is used to request access to the microphone. You do not need to call CheckPermission for earlier versions.
:::


(the)=

#### Use of "the" before a type of mode

In most cases, do not use a leading article for "modes." The exception to this is modes that have multiple options.

For example, the following modes do not require an article:

- silent mode
- dual-stream mode
- individual recording mode
- render mode
- video display mode
- mirror mode

The following are modes that have several options, so the article is needed: 

- the recording mode
- the rendering mode

### Capitalization

**Quick reference:**
- Use title case for document titles.
- Use sentence case for headings and captions. Exception: Also capitalize the first word after a colon.
- Use sentence case for all table elements, including column headings.
- Capitalize the first word after a colon in a sentence if it follows a label such as "Caution," "Note," or "Example."  
- Use the official capitalization of products, companies, and so on.
- Do not use all-caps for emphasis. Use italics instead.
- Use sentence case for list items.
- Capitalize only the first word in a hyphenated phrase. Example: "Random-access memory"
_________

In document titles, use title case, where you capitalize the first word and then every word except for the verb "to be," short prepositions or conjunctions, and articles. Capitalize words after a colon, but only the first word in a hyphenated phrase.

| Do this...                                           | ...instead of this                                    |
| :--------------------------------------------------- | :---------------------------------------------------- |
| Authenticate Your Users with Tokens | Authenticate your users with tokens | 
| Real-time Messaging: A Beginner's Guide | Real-Time Messaging: a Beginner's Guide |

In document headings, use sentence case, where you capitalize only the first word, plus any proper nouns (such as names, trademarks, keywords, and other terms that are normally capitalized). You should also capitalize the first word after a colon.

:::{admonition} Example
Step one: Generate a builderToken for your users
:::

Use the official capitalization for the names of brands, companies, software, products, services, and so on. When in doubt, visit the offical web site of the company.

:::{admonition} Example
Copy the Microsoft Word files to your iOS project folder.
:::

Do not use capitalization for emphasis, as this comes across as shouting to a native English reader. Use italics instead. Note: You should use emphasis sparingly.

| Do this...                                           | ...instead of this                                    |
| :--------------------------------------------------- | :---------------------------------------------------- |
| Do *not* share your token. | Do NOT share your token. | 

Use sentence case for all of the following:

- Image and table captions
- All other elements of a table, such as headings, labels, and cell contents
- Items in all types of lists

When a hyphenated word is capitalized (as the first word in a sentence or heading, for example), capitalize only the first element in the word.  

| Do this...                                           | ...instead of this                                    |
| :--------------------------------------------------- | :---------------------------------------------------- |
| Real-time multimedia streaming is optional. | Real-Time multimedia streaming is optional. | 

Note that proper nouns in hyphenated words are always capitalized.

### Clause order

**Quick reference:**
- Provide the context before you provide the information.
- If a clause has a causal relationship, put the cause first, followed by the effect.
- Use "that" with restrictive clauses and "which" with non-restrictive clauses.
_________

Generally speaking, it is helpful to put the most important information at the beginning of a sentence, followed by what the user can do with that information.

Provide the context or objective before you provide the information. This allows someone skimming the document to skip that section if it does not apply to their needs.

If your sentence describes a cause-and-effect relationship, always put the cause first.

| Do this...                                               | ...instead of this                                              |
| :-------------------------------------------------------- | :----------------------------------------------------------- |
| To obtain a user ID, use the following procedure: | Use the following procedure to obtain a user ID:    |
| If the operation completes without errors, the system returns a status code of 200. | The system returns a status code of 200 if the operation completes without errors. |

#### That vs. which

"That" is used to introduce restrictive clauses. A restrictive clause provides information that is crucial to a sentence. For example, "Download the sample project that corresponds to your operating system." If you remove the clause "that corresponds to your operating system," the sentence lacks information that the reader needs (specifying which sample project to download vs. any others). Restrictive clauses are not set off with commas.

"Which" is used to introduce non-restrictive clauses. A non-restrictive clause provides information that is useful, but not crucial to a sentence. For example, "Download the sample project, which you can find on GitHub." If you remove the clause "which you can find on GitHub," the sentence still conveys its main point (the directive to "Download the sample project"). Restrictive clauses are set off with commas.

### Contractions

**Quick reference:**
- Do not use contractions except in FAQ titles and headers.
_________

A contraction is a word or phrase that is shortened by dropping one or more letters. Examples include "let's" for "let us" and "can't" for "cannot." While native English readers understand them, they add unnecessary complexity for non-native readers. For example, contractions that end with the letter "s" can be mistaken for possessive nouns. In technical documentation, the use of contractions is discouraged because it sets an informal tone.

The more conversational nature of an FAQ allows for the use of contractions, but restrict them to titles and headers.

### Expletives

**Quick reference:**
- Avoid using "filler" or unnecessary words or phrases. 
- Avoid using "please" and "thank you."
_________

Expletives (also called "filler" words or "empty" words) are words or phrases that can add emphasis to a sentence but are normally unnecessary. If a word or phrase can be removed without changing the sentence's meaning, it is probably an expletive. They may creep into writing because they are often heard in conversation. Because technical documentation is more formal, expletives should be used sparingly or avoided altogether.

The most common expletives are "there is/are" and "it is/they are". While these can be used intentionally for emphasis, avoiding them is better. Using them too often also results in boring writing.

| Do this...                          | ...instead of this                       |
| :----------------------------------- | :---------------------------------------- |
| The live broadcast has 17 hosts. | There are 17 hosts in the live broadcast. |
| Do not store the key in plaintext.  | It is important not to store the key in plaintext. |

The following are other expletives to watch out for:

- Indeed
- At this time
- Most
- Actually
- Very
- Perhaps

Words may become unnecessary in context. For example, you do not need to use "new" after "create," because "new" is implied.

| Do this...          | ...instead of this      |
| :------------------- | :------------------- |
| Create a folder. | Create a new folder. |

Note: The term "expletives" also commonly refers to swear words, which it could be argued also add unnecessary emphasis to sentences.

#### "Polite" words

Avoid using the words "please" and "thank you" in technical documentation, because they do not set the proper tone.

| Do this...          | ...instead of this      |
| :------------------- | :------------------- |
| Download the sample code. | Please download the sample code. |

### Present tense

**Quick reference:**
- Use the present tense in most situations.
- Use the past tense only for release dates, fixed issues in release notes, or events that were completed a significant period of time in the past.
- Use the present perfect tense for actions that happened in past and continue into the present. 
- Avoid the future tense. 
_________

Use the present tense when writing your technical documentation, as it creates concise sentences and provides a tone of immediacy, as if things are occuring sequentially at the moment they are read (and always will). It also conveys a sense of truth or fact. 

| Do this...          | ...instead of this      |
| :------------------- | :------------------- |
| Click on the Open button. A pop-up window opens. | Once you have clicked on the Open button, a pop-up window will open. |

#### Exceptions to using the present tense
The past tense is used for events that have happened definitively in the past and are unlikely to repeat. For Agora technical documenation, this is generally reserved for two situations: release dates and fixed issues.

Always frame a product's release date in the past tense, as the present tense is only correct on the day of release. 

Fixed issues described in release notes should also be written in the past tense to emphasize that the issues have been addressed.

| Do this...          | ...instead of this      |
| :------------------- | :------------------- |
| v3.0.0 was released on Mar 4, 2020. | v3.0.0 is released on Mar 4, 2020. |
| Fixed an issue where disconnecting the microphone caused the audio to freeze. | Fixed an issue where disconnecting the microphone causes the audio to freeze. |

Avoid using the future tense if at all possible. In most cases, the present tense works equally well.

| Do this...          | ...instead of this      |
| :------------------- | :------------------- |
| The token expires in 24 hours. | The token will expire in 24 hours. |
| If the network connection is lost, the system attempts to reconnect automatically. | If the network connection is lost, the system will attempt to reconnect automatically. |

The present prefect tense is used to emphasize a past event that has consequences that continue into the present. For example, "Before calling this method, ensure that you have integrated the `libagora_segmentation_extension.dll` dynamic library into the project folder." 

The corresponding Chinese is 已经. 

### Possessives

**Quick reference:**
- Do not use possessives with company or product names.
_________

For singular nouns, add "'s" to the end of the word to form a possessive. 

For plural nouns that end in "s" (like most English plurals), add an apostrophe on the end without an additional "s". 

For plural nouns that do not end in "s", add "'s" to the end of the word. 

:::{admonition} Example
Combine the teacher's video with each of the students' videos on the children's channel.
:::

Do not use a possessive with a product or company name. This is due to matters of trademark, because the "'s" may be mistaken for a part of the name, and because trademarks are often considered adjectives rather than nouns. 

| Do this...                                           | ...instead of this                                    |
| :--------------------------------------------------- | :---------------------------------------------------- |
| The MP4 support of the Media Streaming Server SDK... | The Media Streaming Server SDK's MP4 support... | 
| Install the latest version of iOS from Apple. (or "of Apple iOS") | Install Apple's latest iOS version   |
| Output by the Agora server   | Output by Agora's server  |


### Second person

**Quick reference:**
- Use the second person when writing technical documentation.
- If you need to use the third person, use gender-neutral language.
- Use the imperative mood for task steps.
- When writing references describing methods, use the third person (what it does) rather than the second person (what a developer would do with it).
- Use the first person for FAQ questions.

_________

Using the second person ("you") addresses your text to the reader, which is why it is also called direct address. Second person is more engaging to readers than third person. However, when using the second person you must make sure you are clear who your intended audience is.

Use the second person rather than including yourself by using the first person ("we"). Remember who your audience is and that you are in a different role. In Chinese documents, use "你" instead of "您". 

| Do this...                                          | ...instead of this                           |
| :--------------------------------------------------- | :---------------------------------------- |
| You can get an App ID using Agora Console.        | Developers can get an App ID using Agora Console.         |
| Once in GitHub, you can download the sample project. | Once in GitHub, we can download a sample project. |

If you are describing something in the third person, avoid using "his," "her," or "he/she". You can rephrase the sentence, use the singular "they," or refer to the relevant role instead (in singular or plural form). 

| Do this...                                                  | ...instead of this                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| A user joins a channel and receives the onChannelJoined callback. | Once a user joins a channel, he/she receives the onChannelJoined callback. |
| When a user joins a channel, they receive the onChannelJoined callback. | Once a user joins a channel, he receives the onChannelJoined callback.  |
| Users joining a channel receive the onChannelJoined callback.   | Once a user joins a channel, she receives the onChannelJoined callback.   |

When necessary, given the typical audience for Agora technical documentation, use "a developer" or "developers" to refer to readers in the third person. 

:::{admonition} Example
To improve data security, developers can encrypt users' media streams during the real-time engagement.
:::

For glossary terms, avoid using any person where possible; otherwise, use "developers."  

:::{admonition} Example
Agora Console
: Agora Console is a site for developers to manage Agora projects and services.
:::

#### Imperative mood

The imperative mood is an implied second-person voice that takes the form of a command or request. The imperative mood keeps the content concise and sounds like you are giving instructions. Use the imperative mood when describing steps in a task, as if you were walking someone through the procedure.

| Do this...                                          | ...instead of this                          |
| :--------------------------------------------------- | :---------------------------------------- |
| Download the Agora SDK. | The Agora SDK can be downloaded.          |
| Define your variables in the header file. | You should define your variables in the header file. |

#### Third person with methods in reference documentation

When writing reference documentation for a method, phrase the main method description in terms of what it does (for example, "gets" or "creates") rather than what a developer would use it to do ("get" or "create). The subject is the method. 

#### First person with FAQs

When writing the questions for FAQs (but *not* the answers), use first person, as if someone were asking you the question.


:::{admonition} Example


How do I obtain a temporary token?
:::
