## Punctuations

### Colons

The first word after the colon should be in uppercase.

#### Colons preceding lists

When a colon introduces a list, the phrase before the colon must be a complete sentence. 

A colon cannot be placed between a verb and its object or a preposition and its object. See **Lists**.

``` admonition:: Incorrect

   The methods are:
```

``` admonition:: Correct

   The SDK uses the following methods:

    - joinChannel
    - leaveChannel
    - renewToken
```

#### Colon use within sentences

Do not use colons within sentences. In most cases, splitting the two clauses into separate sentences reads better and is more clear.

#### Colon use in ratios

No space before or after a colon when it is used to express ratios.

### Commas

General rules to follow:

- In a series of three or more items, use a comma before the final "and" or "or." (This is the house editing style of Oxford Press, hence the term "[Oxford comma](https://www.lexico.com/definition/oxford_comma)").

  ``` admonition:: Example

      Adds support for the macOS, Windows x86, and Windows x86_64 platforms.
  ```
  
- In general, place a comma after an introductory word or phrase like “occasionally”, or “otherwise”. 

  ``` admonition:: Example

      Occasionally, the SDK does not automatically reconnect after being disconnected from the servers for pushing and pulling streams.
  ```
- When a coordinating conjunction ("for", "and", "nor", "but", "or", "yet", and "so") separates two independent clauses (where each clause could stand as an independent sentence), insert a comma after the first clause before the conjunction. For example: “The recorded files are stored on your server only, and Agora has no access to them." An exception is when both clauses are very short. For example: "Enables or disables image enhancement and sets the options."

- Commas also enclose the following and similar phrases: "and so forth," "for example," "namely," and "that is,".

| Recommended                                                  | Not recommended                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Unity renders 3D objects by default, such as Cube, Cylinder**,** and Plane. (note comma after "Cylinder") | Unity renders 3D objects by default, such as Cube, Cylinder and Plane. |
| Finally, only groups that contain parameters appear in this list. | Finally only groups that contain parameters appear in this list. |
| The libraries not only make feed creation easier, but they also ensure that only valid feeds are produced. | The libraries not only make feed creation easier but they also ensure that only valid feeds are produced. |

### Ampersands

Do not use ampersands ("&") unless they are part of a name, UI string, or in a piece of code.

### Exclamation marks

Do not use exclamation marks unless they are part of a code example.

### Periods

General rules to follow: 

- Use a period to end a complete sentence.
- Do not use a period at the end of a sentence fragment, such as an item in a list that is not a complete sentence, or in a heading title. 
- Do not use a period in a title or heading.
- List items that are complete sentences end with a period.
- List items that are incomplete sentences do not end with a period. However, when a list includes one item that requires a period, all the list items should have a period for consistency.
- For table items, use complete sentences and end them with a period.

### Slashes

Use a slash to separate the two functions that can be realized with one method, such as, "enable/disable". The capitalization of the two words should remain consistent.

Do not use slashes to separate alternatives. For example use "audio or video calls" instead of "audio/video calls".

``` hint::

    "a and/or b" is only acceptable when the meaning is a or b or both.
```

### Hyphens

In appearance, a hyphen is shorter than both the em dash (“—”), and the en dash (“–”).

- All words following a hyphen are in lowercase, even if the word is at the beginning of a sentence. For example, "32-bit", "Open-source", or "Multi-threaded".
- Use a hyphen to form a compound adjective which is an adjective made up of more than one word. Examples include, "A 25-minute interval", "16-bit color", "state-of-the-art technology", "a six-figure price".
- Use a hyphen to indicate a common second element. For example, "a 10- to 11-digit number", "a six- or seven-hour delay", "a two-, three-, or fourfold increase".
- Many common prefixes, such as "co", "de", "pre", "pro", "re", and "sub" do not need a hyphen.
- Do not use a hyphen when forming a compound adjective with an adverb that ends in "ly".

| Recommended               | Not recommended       |
| :------------------------ | :-------------------- |
| **A badly written book.** | A badly-written book. |

### Semicolons

The semicolon has the following uses:

- To unite sentences that are closely associated

  ``` admonition:: Example
  
      The people on the fourth floor work with product development; those on the fifth work with deployment.
  ```

- To create a stronger division in a sentence that already includes divisions using commas

  ``` admonition:: Example

      The people on the fourth floor, who work with product development, are to continue with the project until Friday; but the following Monday, when their equipment has been moved, they resume work on the sixth floor.
  ```

- To create stronger divisions in a list

  ``` admonition:: Example

      The visitors are to be received by the managing director, Daphne Jones; the head of security, Fred Smith; and the union representative, Howard Brown.
  ```

``` caution::

    The previous examples only demonstrate the semicolon usage and are not typical of technical writing style.
```

### Spaces

General rules to follow:

- Add a space before an opening parenthesis (. *Example: Basic Methods (RTCEngine)*
- Use only one space after full stops. *Example: Add a space. One after the full stop.*
- Use one space between numbers and units. *Example: 256 Kbps.*
- Use spaces around mathematical symbols. *Example: V = off, width x height, x < y*
- Use spaces around dimensions. *Example: 3.2 x 3.6 x 0.6 mm.*


``` admonition:: Exception

    There is no space before a parenthesis when writing a function call. For example:
    
    - `muteRemoteAudioStream`(true)
    - `enableLocalVideo`(false)
    - `CHANNEL_PROFILE_COMMUNICATION`(0)
```
