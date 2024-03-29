% agora_style_guide documentation master file, created by
% sphinx-quickstart on Wed May 13 22:13:27 2020.
% You can adapt this file completely to your liking, but it should at least
% contain the root `toctree` directive.

```{toctree}
:hidden: true
:maxdepth: 2

overview
word-list
language-and-grammar
punctuations
formatting-and-organization
api-reference-code-comments
references
```

```{toctree}
:caption: Appendix
:hidden: true
:maxdepth: 2

changelog
GitHub repo <https://github.com/AgoraDoc/agora-style-guide>
```

# Agora Developer Documentation Style Guide

This document is the primary reference for technical writers on questions of grammar, style, and usage. It is broadly based on the [Google Developer Documentation Style Guide](https://developers.google.com/style/). Exceptions are noted where necessary; a summary of the main differences can be found in [Exceptions](#exceptions).

When investigating a style issue, consult this guide first. Refer to the Google style guide for information outside the scope of this document.

This document also contains the official spellings for Agora products and technology, as well a list of preferred spellings for related words. See {doc}`word-list` for details.

For the (American) English spelling of additional terms and general vocabulary, refer to the [Merriam-Webster's Dictionary](https://www.merriam-webster.com/).

For additional, in-depth study of style, grammar, and technical documentation, you can consult the following recommended sources:

## English references (online)

- [Apple Style Guide](https://help.apple.com/applestyleguide/)
- [Appledoc comments formatting style](https://github.com/tomaz/appledoc/blob/master/CommentsFormattingStyle.markdown)
- [How to Write Doc Comments for the Javadoc Tool](http://www.oracle.com/technetwork/articles/java/index-137868.html)
- [Microsoft Writing Style Guide](https://docs.microsoft.com/en-us/style-guide/welcome/)
- [Purdue University Online Writing Lab](https://owl.purdue.edu/owl/purdue_owl.html)
- [The Elements of Style (PDF)](https://faculty.washington.edu/heagerty/Courses/b572/public/StrunkWhite.pdf)

## English references (books)

- *A Manual of Style*, by University of Chicago Press (Franklin Classics Trade Press, 2018)
- *Developing Quality Technical Information: A Handbook for Writers and Editors*, by Michelle Carey et al. (IBM Press, 2014).
- *Managing your Documentation Projects*, by JoAnn Hackos (John Wiley and Sons, 1994).
- *Technical Editing*, by Judith A. Tarutz (Basic Books, 1992).
- *The Deluxe Transitive Vampire: The Ultimate Handbook of Grammar for the Innocent, the Eager, and the Doomed*, by Karen Elizabeth Gordon (Pantheon, 1993).
- *The New Well-Tempered Sentence: A Punctuation Handbook for the Innocent, the Eager, and the Doomed*, by Karen Elizabeth Gordon (Mariner Books, 2003).

## Chinese references

- [中文技术文档写作风格指南](https://zh-style-guide.readthedocs.io)
- [泛化智能文风规范](https://github.com/generalized-intelligence/gi-Chinese-Style-Guide/blob/master/泛化智能（gi）文风指南.md)
- [leengo 简体中文规范指南](https://www.lengoo.de/documents/styleguides/lengoo_styleguide_ZH.pdf)
- [LeanCloud 文案风格指南](https://open.leancloud.cn/copywriting-style-guide/)
- [豌豆荚文案风格指南](https://docs.google.com/document/d/1R8lMCPf6zCD5KEA8ekZ5knK77iw9J-vJ6vEopPemqZM/edit)
- [中文技术文档的写作规范](https://github.com/ruanyf/document-style-guide)
- [中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.zh-CN.md)

## Exceptions

For those familiar with the Google style guide, this section summarizes the main differences between that document and this style guide.

### Language and grammar

Contractions

: Do not use contractions except in the headings of FAQs.

Possessives

: Do not use a possessive with a product or company name.

Tone

: Use a formal tone in your technical documentation, with the exception of FAQs, which can be more conversational.

### Formatting and organization

Dimensions

: When referring to resolution values, such as "1080p", or "1920 × 1080", only use commas when the number has five or more digits. For example, "width should not exceed 1920, and width × height should not exceed 1920 × 1080." Also, use the multiplication symbol rather than a lowercase x.

Numbers and spacing
: - Use spaces around mathematical symbols. Example: V = off, width x height, x \< y
  - Use spaces around dimensions. Example: 3.2 x 3.6 x 0.6 mm.
