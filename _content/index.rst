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

The Agora Developer Documentation Style Guide is the primary reference for technical writers to improve the quality and consistency of Agora documentation.

.. hint:: 
   If you would like to contribute technical content to the Agora community, please follow the `Google Developer Documentation Style Guide <https://developers.google.com/style/>`_ with the `exceptions <Exceptions>`_, and consult the :ref:`references:Word list` for commonly used terms in Agora documentation.

This document provides important guidelines on grammar, punctuation, and style for Agora technical writers. It is broadly based on the `Google Developer Documentation Style Guide <https://developers.google.com/style/>`_. Exceptions are noted where necessary. 

The `Merriam-Webster's Dictionary <https://www.merriam-webster.com/>`_ is the department’s reference for (American) English spelling. 

Generally speaking, consult this guide first, then consult the Google style guide for information outside the scope of this document.

For additional in-depth grammar information or company-specific vocabulary and usage, consult the following:

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

This section lists the differences between Agora and Google style guides for a quick reference.

Language and grammar
^^^^^^^^^^^^^^^^^^^^^

Articles
   Methods and callbacks must be specified, so when referring to a method or callback, use a leading “the” followed by “method” or “callback”. For example “the SDK triggers the Client.on(“disable-local-video”) callback”. Omit “the” and “method” when the reader will understand that it is a method by context. 

Contractions
   Do not use contractions except in FAQs.

Possessives
   Do not use a possessive with a product name, or with the company name.

Tense
   Always frame the release date in the past tense, as that tense will only be correct on the day of release. For example, use “v3.0.0 was released on Mar 4, 2020”, not “v3.0.0 is released on Mar 4, 2020”.

Verb form
   Prefer using the relative noun to a verb-…ing combination, for example say “the method that uses this parameter” instead of “the method using this parameter”.

Punctuations
^^^^^^^^^^^^^

Colons
   No space before or after a colon when it is used to express ratios.

Slashes
   Use a slash to separate the two functions that can be realized with one method, such as, “enable/disable”. The capitalization of the two words should remain consistent.

Formatting and organization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dimensions
   When referring to resolution values, such as "1080p", or "1920 × 1080", only use commas when the number has five or more digits. For example, "width should not exceed 1920, and width × height should not exceed 1920 × 1080."

Linking
   - Provide a link to the glossary at the first mention.
   - Provide links to reference documents except in code comments.

Spaces
  - Use one space between numbers and units. Example: 256 Kbps.
  - Use spaces around mathematical symbols. Example: V = off, width x height, x < y
  - Use spaces around dimensions. Example: 3.2 x 3.6 x 0.6 mm.

Computer interfaces
^^^^^^^^^^^^^^^^^^^^
Parameters and return values
   - For Boolean parameters use a list that includes “true” and “false”, followed by corresponding functions. Do not put the words “true” and “false” in code font or quotation marks. Notice the capitalization difference across different platforms.
   - For Optional or Default parameters, put (Optional) or (Default) as the first word of the description.

Callbacks
   - If a callback occurs when a method triggers it, start with “Occurs when…”
   - If a callback reports an error or statistics, start with “Reports…”

Code samples
   - Ensure that all the variants in the code samples are assigned values.
   - Code comments should be one line above the code they refer to and start with “// “.
   - Code comments should use the same indenting as the succeeding code.
   - Only use periods for complete sentences.

Word list
^^^^^^^^^^^
See :ref:`references:Word list` for details.