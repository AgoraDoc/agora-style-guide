.. agora_style_guide documentation master file, created by
   sphinx-quickstart on Wed May 13 22:13:27 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2
   :numbered:
   :hidden:

   overview
   language-and-grammar
   punctuations
   formatting-and-organization
   api-reference-code-comments
   references

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Changelog

   changelog

Agora Developer Documentation Style Guide
=============================================

This document is the primary reference for technical writers on questions of grammar, style, and usage. It is broadly based on the `Google Developer Documentation Style Guide <https://developers.google.com/style/>`_. Exceptions are noted where necessary; a summary of the main differences can be found in `Exceptions <Exceptions>`_.

When investigating a style issue, consult this guide first. Refer to the Google style guide for information outside the scope of this document.

This document also contains the official spellings for Agora products and technology, as well a list of preferred spellings for related words. See :ref:`references:Word list` for details. 

For the (American) English spelling of additional terms and general vocabulary, refer to the `Merriam-Webster's Dictionary <https://www.merriam-webster.com/>`_.

For additional, in-depth study of style, grammar, and technical documentation, you can consult the following recommended sources:

English references (online)
-------------------------------

- `Apple Style Guide <https://help.apple.com/applestyleguide/>`_
- `Appledoc comments formatting style <https://github.com/tomaz/appledoc/blob/master/CommentsFormattingStyle.markdown>`_
- `How to Write Doc Comments for the Javadoc Tool <http://www.oracle.com/technetwork/articles/java/index-137868.html>`_
- `Microsoft Writing Style Guide <https://docs.microsoft.com/en-us/style-guide/welcome/>`_
- `Purdue University Online Writing Lab <https://owl.purdue.edu/owl/purdue_owl.html>`_
- `The Elements of Style (PDF) <https://faculty.washington.edu/heagerty/Courses/b572/public/StrunkWhite.pdf>`_

English references (books)
-------------------------------
- *A Manual of Style*, by University of Chicago Press (Franklin Classics Trade Press, 2018)
- *Developing Quality Technical Information: A Handbook for Writers and Editors*, by Michelle Carey et al. (IBM Press, 2014).
- *Managing your Documentation Projects*, by JoAnn Hackos (John Wiley and Sons, 1994).
- *Technical Editing*, by Judith A. Tarutz (Basic Books, 1992).
- *The Deluxe Transitive Vampire: The Ultimate Handbook of Grammar for the Innocent, the Eager, and the Doomed*, by Karen Elizabeth Gordon (Pantheon, 1993).
- *The New Well-Tempered Sentence: A Punctuation Handbook for the Innocent, the Eager, and the Doomed*, by Karen Elizabeth Gordon (Mariner Books, 2003).

Chinese references
--------------------------------

- `中文技术文档写作风格指南 <https://zh-style-guide.readthedocs.io>`_
- `泛化智能文风规范 <https://github.com/generalized-intelligence/gi-Chinese-Style-Guide/blob/master/泛化智能（gi）文风指南.md>`_
- `leengo 简体中文规范指南 <https://www.lengoo.de/documents/styleguides/lengoo_styleguide_ZH.pdf>`_
- `LeanCloud 文案风格指南 <https://open.leancloud.cn/copywriting-style-guide/>`_
- `豌豆荚文案风格指南 <https://docs.google.com/document/d/1R8lMCPf6zCD5KEA8ekZ5knK77iw9J-vJ6vEopPemqZM/edit>`_
- `中文技术文档的写作规范 <https://github.com/ruanyf/document-style-guide>`_
- `中文文案排版指北 <https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.zh-CN.md>`_

Exceptions
-------------

For those familiar with the Google style guide, this section summarizes the main differences between that document and this style guide. //TODO William I think this section should be very focused. You are trying to help people not get "tripped up" by their assumptions, but unless they are steeped in Google's style guide, this isn't broadly useful. 

Language and grammar
^^^^^^^^^^^^^^^^^^^^^

Articles
   Methods and callbacks must be specified, so when referring to a method or callback, use a leading "the" followed by "method" or "callback." For example, "The SDK triggers the Client.on(“disable-local-video”) callback." You can omit "the" and "method/callback" when the reader understands which it is from context. //TODO William Is this actually a difference from the Google guide? I can't find it in there. I suggest you delete.

Contractions
   Do not use contractions except in the headings of FAQs.

Possessives
   Do not use a possessive with a product or company name.
   
Tense
   Always put release dates in the past tense. For example, use "v3.0.0 was released on Mar 4, 2020," not "v3.0.0 is released on Mar 4, 2020." //TODO William Is this actually a difference from the Google guide? I can't find it in there (not covered in Dates and Times; Verb Tense is present vs. future). I suggest you delete.
   
Tone
   Use a formal tone in your technical documentation, with the exception of FAQs, which can be more conversational.

Verb form
   Prefer using the relative noun to a verb-…ing combination, for example say "the method that uses this parameter" instead of "the method using this parameter." //TODO William Is this actually a difference from the Google guide? I couldn't find this either? I suggest you delete.

Punctuation //TODO William I think you can delete this section (see below).
^^^^^^^^^^^^^

Colons
   No space before or after a colon when it is used to express ratios. //TODO William You should delete this; this is not a difference (Google does this too).

Slashes
   Use a slash to separate the two functions that can be realized with one method, such as, "enable/disable." The capitalization of the two words should remain consistent. //TODO William You should delete this; this is not a conflict, because Google doesn't mention this kind of case, I think? I don't think information that isn't mentioned in the Google style guide is a "difference." I think Exceptions should only mention direct contradictions.

Formatting and organization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dimensions
   When referring to resolution values, such as "1080p", or "1920 × 1080", only use commas when the number has five or more digits. For example, "width should not exceed 1920, and width × height should not exceed 1920 × 1080." Also, use the multiplication symbol rather than a lowercase x. 

Linking
   - Provide a link to the glossary at the first mention of an uncommon term. ///TODO William Is this a difference? I cannot find this in Google's guide.
   - Provide links to reference documents except in code comments. //TODO William You should delete this; this isn't a conflict.

Numbers and spacing
  - Use one space between numbers and units. Example: 256 Kbps. //TODO William You should delete this; this isn't a conflict.
  - Use spaces around mathematical symbols. Example: V = off, width x height, x < y
  - Use spaces around dimensions. Example: 3.2 x 3.6 x 0.6 mm.

Computer interfaces //TODO William This section also deosn't seem to contain conflicts (see comments below). I would like to see detailed API guidelines in the Agora style guide, but not here.
^^^^^^^^^^^^^^^^^^^^
Parameters and return values
   - For Boolean parameters use a list that includes "true" and "false," followed by corresponding functions. Do not put the words "true" and "false" in code font or quotation marks. Notice the capitalization difference across different platforms. //TODO William You should delete this; this isn't a conflict, I think?
   - For Optional or Default parameters, put (Optional) or (Default) as the first word of the description. //TODO William Is this actually a difference from the Google guide? I can't find it in there. I suggest you delete.

Callbacks //TODO William Is this a conflict? Google doesn't mention callbacks?
   - If a callback occurs when a method triggers it, start with “Occurs when…”
   - If a callback reports an error or statistics, start with “Reports…”

Code samples //TODO William Is this a conflict? Google either agrees with or doesn't mention these. 
   - Ensure that all the variants in the code samples are assigned values.
   - Code comments should be one line above the code they refer to and start with “// “.
   - Code comments should use the same indenting as the succeeding code.
   - Only use periods for complete sentences.

Word list //TODO William Delete this reference here. 
^^^^^^^^^^^
See :ref:`references:Word list` for details.
