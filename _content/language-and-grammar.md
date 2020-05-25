## Language and grammar

### Abbreviations and acronyms

Abbreviations are the shortened version of a word or phrase used to represent the whole. Examples include "s" for "seconds,” "approx." for "approximately," and "e.g." for "exempli gratia" (meaning "for example"). 

Acronyms are a type of abbreviation formed from the initial letters of other words. Examples include "SDK" for "Software Development Kit", "API" for "Application Programming Interface", and "URL" for "Uniform Resource Locator". 

Abbreviations and acronyms can affect the clarity of Agora content for the reader. While many are understood by our readers and do not need to be spelled out, for new or novel terms always spell out the first mention of an abbreviated term in the text, followed immediately by the abbreviation in parentheses. Use the abbreviated form for all subsequent references of the abbreviation.

``` admonition:: Example

   The communication between the user and the Agora server is protected by transmission protocols, such as the Agora private transmission protocol, Transport Layer Security (TLS) and Web Socket Secure (WSS). You can also use Advanced Encryption Standard (AES) or a customized encryption algorithm for end-to-end encryption of audio and video data.
```

#### Latin abbreviations

Do not use Latin abbreviations in your technical writing.

There are several abbreviations derived from Latin that are used in written English. Examples include "e.g." for "exempli gratia" (meaning "for example"), "i.e." for "id est" (meaning "in other words"), and "etc." for "et cetera" (meaning "and the other things").

Plain language principles suggest avoiding these abbreviated terms and spell them out instead.

#### Abbreviations ending a sentence

If a sentence ends with an abbreviation (like "U.S.", or "Agora Inc."), the period used for the abbreviation also serves as the period for the sentence.

#### Contractions

Do not use contractions except in FAQs.

A contraction is a word or phrase that is shortened by dropping one or more letters. Examples include "aren't" for "are not", "let's" for "let us", and "can’t” for “cannot”. While any native English reader understands them, they add unnecessary complexity for non-native readers. For example, contractions that end with the letter "s" can be mistaken for possessive nouns. In business communication, the use of contractions is frowned upon as they make the tone of the writing too informal.

The only exception to this rule is when you are writing content for an FAQ. The more conversational tone of an FAQ allows for the use of contractions in their titles and headers.

### Possessives

Do not use a possessive with a product name, or with the company name. 

| Recommended                                          | Not recommended                                       |
| :--------------------------------------------------- | :---------------------------------------------------- |
| The Agora Media Streaming Server SDK supports MP4... | The Agora Media Streaming Server SDK's MP4 support... |
| ...Agora RTC SDK                                     | ...Agora's RTC SDK                                    |
| Output by the Agora server                           | Output by Agora's server                              |

In general, to form a possessive of a singular or a plural noun that doesn't end in "s", add "'s" to the end of the word. For a plural noun that does end in "s", add an apostrophe but no additional "s". 

``` admonition:: Example

   Combine the teacher's video with each of the students' videos.
```

### Articles (a, an, the)

"A" and "an" are indefinite articles and are used before a singular countable noun. They refer to any member of a group. "The" is a definite article. It is used before singular and plural nouns and refers to one or more particular members of a group.

#### Sound rule for using "a" and "an"

The way a word or acronym is spoken determines whether "a" or "an" precedes it. Use "a" before a word that starts with a consonant sound, and "an" for words that begin with a vowel sound. For example "a URL", and "an SDK".

#### Articles and internal agreement

- There is no need to use "the" or even "method" when describing what a method does, as the reader will understand that it is a method by context. For example: "Call CheckPermission to request access…" and not "Call the CheckPermission method to request access…" 
- Callbacks must be specified, so when referring to a callback, use a leading "the" followed by "callback". For example "the SDK triggers the Client.on("disable-local-video") callback".

#### Use of "the" before a type of mode

The general trend in technical writing is to drop the use of the article "the" before a type of mode. The Agora style drops the leading article for modes that do not have multiple options, and retains the article for modes that do have multiple options.

Do not use "the" before the following:

- dual-stream mode
- individual recording mode
- render mode
- video display mode

Use "the" for modes with several options, such as the following:

- the mirror mode
- the recording mode
- the rendering mode

### Capitalization

- Use an uppercase letter to begin the first word of the text immediately following a colon.
- Do not use all-uppercase for emphasis, as it comes across as shouting to a native English reader.
- Use sentence case for captions and other figure-related text.
- When a hyphenated word is the first word in a sentence or in a heading, capitalize only the first element in the word, unless a subsequent element is a proper noun or proper adjective.
- Use sentence case for items in all types of lists.
- Use sentence case for all the elements in a table: contents, headings, labels, and captions.

For the names of brands, companies, software, products, services, and the like, follow the official capitalization.

In document titles and page headings, use sentence case. That is, capitalize only the first word. The exceptions are for proper nouns, trademarks, keywords, and other terms that are always capitalized a certain way, use the standard capitalization for the term.

``` admonition:: Example

  .. image:: img/sentence-case.png
```
### Ornamental words

Avoid placeholder phrases such as "current", "currently", "please", "at this time", "now", "still", "most", or "commonly".

An expletive is an added word or phrase that does not contribute meaning to the sentence. The most common expletives are "there are" and "there is".

| Recommended                          | Not recommended                           |
| :----------------------------------- | :---------------------------------------- |
| **The live broadcast has 17 hosts.** | There are 17 hosts in the live broadcast. |

Do not use "new" after "create", as "new" is implied.

| Recommended          | Not recommended      |
| :------------------- | :------------------- |
| **Create a folder.** | Create a new folder. |

### Active voice

Use active voice where possible as it is more direct.

Sentences phrased with passive voice are usually wordy. This is not a hard rule, as it may not always be possible to phrase things with an active voice (such as in status code explanations for example), but aim for active voice when possible.

| Recommended                       | Not recommended                         |
| :-------------------------------- | :-------------------------------------- |
| **This method gets the user ID.** | This method is used to get the user ID. |

### Direct address or imperative mood

Use the imperative mood for task steps.

The imperative mood keeps the content concise. The direct address is more personal.

| Recommended                                          | Not recommended                           |
| :--------------------------------------------------- | :---------------------------------------- |
| **Download the Agora SDK. (Imperative Mood)**        | The Agora SDK can be downloaded.          |
| **You can download the Agora SDK. (Direct Address)** | The developer can download the Agora SDK. |

### Gender-neutral

- Avoid using "his" or "her", or "he/she".
- Use the second person, "you", or the collective noun.

| Recommended                                                  | Not recommended                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| **A user joins a channel and receives the onChannelJoined callback.** | Once a user joins a channel, he/she receives the onChannelJoined callback. |

### Present tense

- Use the present tense as it creates concise sentences and provides a tone of immediacy. An exception to this rule is the release date of an SDK or other product. Always frame the release date in the past tense, as that tense will only be correct on the day of release. For example, use "v3.0.0 **was** released on Mar 4, 2020", not "v3.0.0 **is** released on Mar 4, 2020".
- Avoid using *will* and *can*.
- Use future tense if there is a significant time delay that matters in the context. 
- Only use the present prefect tense to emphasize a past event that has present consequences (The corresponding Chinese is 已经). 

| Recommended                                  | Not recommended                                     |
| :------------------------------------------- | :-------------------------------------------------- |
| **Press Enter, a message appears.**          | When you have pressed Enter, a message will appear. |
| **When you press Enter, a message appears.** |                                                     |

### Anthropomorphism

Do not attribute human qualities to software or hardware.

| Recommended                                               | Not recommended                                              |
| :-------------------------------------------------------- | :----------------------------------------------------------- |
| A Delimiter object **specifies** where to split a string. | A Delimiter object tells the splitter where a string should be broken. |
| The PC **detects** a new device.                          | The PC sees a new device.                                    |

### Second person

In general, use second person "you" (sometimes implicit) in your docs rather than first person "we." In Chinese documents, use "你" instead of "您"。

In glossary terms, avoid using person where possible and use "developer" to refer to the reader if necessary.

### Verb forms in reference documentation

When you are writing reference documentation for a method, phrase the main method description in terms of what it does ("Gets," "Lists," "Creates," "Searches"), rather than what the developer would use it to do ("Get," "List," "Create," "Search").

In documentation (like step-by-step instructions) that is aimed at *implementors* of an API, it may make more sense to use the imperative form without the "-s" (in other words, "Set" instead of "Sets", or "Initialize" instead of "Initializes").

### Clause order

- Put the most important information at the beginning of a sentence, followed by what the user can do with that information. 
- Provide the context before you provide the instruction; that way, the reader can skip the additional information if it does not apply to their circumstance. 
- If clauses have a causal relationship, put the cause first, followed by the effect.