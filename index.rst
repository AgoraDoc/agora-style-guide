.. agora_style_guide documentation master file, created by
   sphinx-quickstart on Wed May 13 22:13:27 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Agora Documentation Style Guide
=============================================


--------------------------------------
 1. Introduction
--------------------------------------

The Agora Technical Document Style Guide is a reference for Technical Writers to improve the writing and consistency of the Agora documentation. This document only provides important guidelines targeting Agora's technical writers. You can find detailed style, usage, and grammar in the following references.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.1 English style guide references
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* `Apple Style Guide <https://help.apple.com/applestyleguide/>`_
* `Appledoc comments formatting style <https://github.com/tomaz/appledoc/blob/master/CommentsFormattingStyle.markdown>`_
* `Google Developer Documentation Style Guide <https://developers.google.com/style/>`_
* `How to Write Doc Comments for the Javadoc Tool <http://www.oracle.com/technetwork/articles/java/index-137868.html>`_
* *Managing your Documentation Projects*, by JoAnn Hackos (John Wiley and Sons, 1994).
* `Merriam-Webster's Dictionary <https://www.merriam-webster.com/>`_
* `Microsoft Writing Style Guide <https://docs.microsoft.com/en-us/style-guide/welcome/>`_
* *Technical Editing*, by Judith A. Tarutz (Perseus Books, 1992). 
* `The Chicago Manual of Style <http://www.chicagomanualofstyle.org/home.html>`_
* `The Elements of Style (PDF) <https://faculty.washington.edu/heagerty/Courses/b572/public/StrunkWhite.pdf>`_
* *The Transitive Vampire: A Handbook of Grammar for the Innocent, the Eager, and the Doomed*, by Karen Elizabeth Gordon (Times Books, 1984).

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.2 Chinese style guide references
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* `泛化智能文风规范 <https://github.com/generalized-intelligence/gi-Chinese-Style-Guide/blob/master/%E6%B3%9B%E5%8C%96%E6%99%BA%E8%83%BD%EF%BC%88gi%EF%BC%89%E6%96%87%E9%A3%8E%E6%8C%87%E5%8D%97.md>`_
* `leengo 简体中文规范指南 <https://www.lengoo.de/documents/styleguides/lengoo_styleguide_ZH.pdf>`_
* `LeanCloud 文案风格指南 <https://open.leancloud.cn/copywriting-style-guide/>`_
* `豌豆荚文案风格指南 <https://docs.google.com/document/d/1R8lMCPf6zCD5KEA8ekZ5knK77iw9J-vJ6vEopPemqZM/edit>`_
* `中文技术文档的写作规范 <https://github.com/ruanyf/document-style-guide>`_
* `中文文案排版指北 <https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.zh-CN.md>`_

------------------------------------------
2. Overview
------------------------------------------

This chapter describes the purpose of the Agora documentation and the top editing principles for our team.

^^^^^^^^^^^^^^^^^^
2.1 Purpose
^^^^^^^^^^^^^^^^^^

The primary goal of this guide is to codify and record decisions the Agora technical communication team make about style. The guide can help you avoid making decisions about the same issue over and over again, provide editorial assistance on structuring and writing your documentation, and help you keep your documentation consistent with our other documentation.

^^^^^^^^^^^^^^^^^^
2.2 Our audience
^^^^^^^^^^^^^^^^^^

Our technical documentation is aimed primarily at programmers working with our SDKs to create apps. The programmers visiting our website have all levels of experience, ranging from domain experts to junior programmers working on their first project. Keep in mind that most programmers visiting our website have a specific goal in mind: to find the information they need to get their app working. While we cannot write our content to cater to all levels of programmers, we can best serve them all by ensuring our content is concise, clear, and correct.

^^^^^^^^^^^^^^^^^^
2.2.1 Concise
^^^^^^^^^^^^^^^^^^

Keep your writing short and to the point.

Most readers will be scanning rather than reading our content, seeking only the information they need to do their job. You need to get your ideas across to our audience quickly. Concise writing does not always mean fewer words but enough to convey an idea effectively.

^^^^^^^^^^^^^^^^^^
2.2.2 Clear
^^^^^^^^^^^^^^^^^^

Think about what you are trying to communicate to the reader. Then use plain language to convey the information to our audience.

If you do not fully understand what you are writing about, that will come across to the reader. 

^^^^^^^^^^^^^^^^^^
2.2.3 Correct
^^^^^^^^^^^^^^^^^^

Our content must be technically and grammatically correct.

Incorrect content causes our audience to lose trust in our content and brand. If you are unsure if your content is technically correct, check with a developer before publication.

Grammatically incorrect writing confuses our readers and reflects poorly on our professionalism. If you are questioning the wording of your content, speak to another writer, or contact a technical editor for help.

^^^^^^^^^^^^^^^^^^^^^^^
2.3 General principles
^^^^^^^^^^^^^^^^^^^^^^^^

""""""""""""""""""""""""""""
2.3.1 Style and tone
""""""""""""""""""""""""""""

Best practices to adopt:

* Plan what to write before you write.
* Always keep your audience in mind when you write.
* Use active voice when possible.
* Write for scannability; use bullet points, short paragraphs, and sections/headers to break up your content.
* Be brief.
* Oxford comma: In a list of three or more items, add a comma before the conjunction (for example: "Android, iOS, and Windows").
* Spell check your content.
* Be friendly by using "you". And remember that Agora can "recommend" courses of action.
* Review your content. Edit out any information your reader does not need to know.
* Use parallel structures to tell the reader how related concepts are different and how they are similar.
* Place essential information in the main clause, as you cannot assume the reader will read the whole sentence.
* Remove ambiguity by choosing words whose meaning is clear.
* Use the relative pronoun "that" where you might otherwise omit it, and prefer using it to a noun-...ing combination, for example say "the method that uses this parameter" instead of "the method using this parameter".

Avoid the following:

* Buzzwords or technical jargon.
* Adding unwarranted humor.
* Ableist language or figures of speech.
* Placeholder phrases like "please note" and "at this time."
* Convoluted or overly-long sentences.
* Starting all sentences with the same phrase (such as "You can" or "To do").
* Current pop-culture references.
* Jokes.
* Exclamation marks, except in code examples. 
* Wackiness, zaniness, and goofiness.
* Phrasing that denigrates, insults, or discriminates against any group of people.
* Using phrases like "simply" or "it is that simple" or "it is easy" in a procedure.
* Internet slang, or other internet abbreviations such as "tl;dr" or "ymmv".
* Do not use dangling modifiers. A modifier "dangles" when the sentence is not clear about what is being modified.

""""""""""""""""""""""""""""
2.3.2 Accessible content
""""""""""""""""""""""""""""

Our audience is comprised of people who come to our website with different abilities. Some might have issues with their eyesight and magnify the content on their screen. Others may use a screen reader that speaks the text on a web page. Some people come to the Agora website for whom English is a second language, and their reading comprehension level may be low. Content aimed at U.S. readers should be in line with the Americans with Disabilities Act (ADA) and use the W3C Web Content Accessibility Guidelines as a guide. By following the best practices outlined previously, you will already be doing most of what is required, but also keep the following in mind when you write:

* Provide informative and descriptive page titles for your articles.
* Use headings to convey meaning and structure.
* Make link text meaningful, describing the target of the link target.
* Write meaningful text alternatives for images that provide information about what the image is or what function it depicts.
* Provide transcripts for videos.
* For every image, provide alt text that summarizes the intent of the image. In markdown, images should look like ![Alt text](image_url). The alt text should be in Chinese for Chinese documents.
* Tables are particularly challenging for screen readers. Do not use table unless it is the best method to present your information. Also, do not merge cells within a table.

""""""""""""""""""""""""""""""""""""""""""
2.3.3 Writing for a global audience
""""""""""""""""""""""""""""""""""""""""""

While Agora has a sizable Chinese audience, it is important to remember that the company's growth depends on having an international focus. It is essential that as Agora expands its operations worldwide, that writers keep in mind techniques that will help when we begin to translate to languages other than English.

In conjunction with the general principles outlined earlier, the following techniques will help us write for a global audience:

* Write in simple structures.
* Use simple verbs. For example, don't use words like utilize when the simpler word use conveys the same information.
* Do not use idiomatic or colloquial expressions.
* Provide context for the reader using descriptive (but still concise) text.
* Avoid making negative constructions. Do not tell the reader what they cannot do; tell them what they can do.
* Do not use double negative.
* Avoid using images with embedded text where possible.
* Keep paragraphs short. Dense pages full of text are intimidating for readers.
* Address the reader directly by using “you” instead of “the developer”.
* Put the conditional clause first. Start by mentioning a circumstance or scenario, followed the instruction.
* Be inclusive in your writing. Use gender-neutral pronouns. Avoid mentioning holidays, sports teams, or other culturally-specific things.
* Avoid using metaphors, as many are culturally specific.
* Be consistent in your word usage. Do not use the same word to mean different things.



.. toctree::
   :maxdepth: 2


