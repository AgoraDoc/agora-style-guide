## Overview

This chapter outlines the purpose of this style guide and summarizes the top editing principles of the Agora TechDocs team.

### Purpose

The primary goal of this guide is to clearly record the grammar and style standards of the Agora technical documentation team. This guide allows you to avoid having to research style issues on your own, provides editorial assistance on structuring and writing your documentation, and helps you keep your documentation consistent with our other documentation.

### Our audience

Our technical documentation is aimed primarily at programmers working with our SDKs to create apps. The programmers visiting our website have all levels of experience, ranging from domain experts to junior programmers working on their first project. Keep in mind that most programmers visiting our website have a specific goal in mind: to find the information they need to get their app working. 

While we cannot write our content to cater to all levels of programmers, we can best serve them all by ensuring our content is concise, clear, and correct.

#### Concise

Keep your writing short, direct, and to the point.

Most readers will be scanning rather than reading our content, seeking only the information they need to do their job. You need to get your ideas across to our audience quickly. Concise writing does not simply mean fewer words; it means eliminating redundancy and excess verbiage. Everything included should be necessary.

#### Clear

Think about what you are trying to communicate to the reader, then use plain language to convey that information. Organize the information is a logical fashion that progresses in the most useful way.

Provide informative examples where possible.

Make sure you fully understand what you are writing about. When in doubt, ask for clarification from subject matter experts or the other writers.

``` hint::

    It is more considerate to compile a complete list of your questions about a document before asking for help; it is less intrusive to interrupt someone once (even if it takes longer) than to keep coming back to ask multiple "quick questions."
```

#### Correct

Our content must be factually and grammatically correct.

Incorrect content causes our audience to lose trust in our documentation and brand. If you are unsure if your content is correct, check with a developer before publication.

Grammatically incorrect writing can confuse our readers and reflects poorly on our professionalism. If you are having trouble with the wording of your content, speak to another writer, or contact a technical editor for help.

### General principles

#### Style and tone

Best practices to adopt: //TODO William Are there too many? Should we simplify this or break it up? If you wanted something someone could maybe print (on one page) and put up by their workstation, this might be too much.

* Create an outline to plan what to write before you start.
* Always keep your audience's capabilites and needs in mind when you write.
* Write for scannability by using bullet points, short paragraphs, and informative section headings to break up your content.
* Keep paragraphs short. Dense pages full of text can be intimidating for readers (or hide important information from skimmers).
* Remember to be clear and concise. Replace phrases with single words where possible, and remove ambiguities.
* Favor the active voice.
* Maintain a formal tone (except for FAQs).
* Write in the second person ("you"), because it is more friendly and engaging than a third-person form (such as "developers"). Do not use "we," but remember that "Agora" can recommend courses of action. 
* Always be consistent in your word usage. Do not use the same word to mean different things (or refer to one thing using different words).
* Place essential information in the main clause, as you cannot assume the reader will read the whole sentence.
* Put conditional clauses first. Start by mentioning the objective, followed the instruction (for example, "To run the program, click Run.").
* Use the Oxford comma. That is, in a list of three or more items, add a comma before the conjunction (for example. "Android, iOS, and Windows").
* Use parallel structures to tell the reader how related concepts are different and how they are similar.
* Vary the length of your sentences.
* Use the relative pronoun "that" with a present-tense verb instead of the present participle (an "ing" ending). For example, write "the method that uses this parameter" instead of "the method using this parameter."
* Review and spell check your content before submitting it. Edit out any information your reader does not need to know.

Avoid the following:

- Buzzwords, jargon, or slang.
- Humorous or absurdist references.
- References to pop culture or the names of real people.
- [Ableist](https://developers.google.com/style/inclusive-documentation.html#ableist-language), gendered, or discriminatory language or figures of speech, such as "crazy," "crippled," or "mankind." When necessary, use the singular pronoun "they" instead of "he" or "she."
- Empty phrases, such as "please note," "for the most part," or "at this time."
- Convoluted or overly long sentences.
- Starting all sentences with the same phrase, such as "You can" or "To do."
- Exclamation marks (except in code examples).
- Judgment phrases, such as "simply" or "it is that simple" or "it is easy" in a procedure.
- Dangling modifiers. A modifier "dangles" when the sentence is not clear about what is being modified.
- Double negatives 

#### Accessible content

Our readers come to our website with different abilities. Some may have issues with their eyesight and magnify the content on their screen. Others may use a screen reader that speaks the text on a web page. For some, English is their second language, and their reading comprehension level may be low. Content aimed at U.S. readers should be in line with the Americans with Disabilities Act (ADA) and use the [W3C Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/) as a guide. By following the best practices outlined previously, you will already be doing most of what is required, but also keep the following in mind when you write:

- Provide informative and descriptive page titles for your articles.
- Use headings to convey meaning and structure.
- Make link text meaningful, describing the target of the link target.
- Write meaningful text alternatives for images that provide information about what the image is or what function it depicts.
- Provide transcripts for videos.
- For every image, provide alt text that summarizes the intent of the image. In markdown, images should look like `![Alt text](image_url)`. The alt text should be in Chinese for Chinese documents.
- Tables are particularly challenging for screen readers. Do not use a table unless it is the best method to present your information. Also, do not merge cells within a table.

#### Writing for a global audience

While Agora has a sizable Chinese audience, it is important to remember that the company's growth depends on having an international focus. It is essential that as Agora expands its operations worldwide, writers write in ways that make it easier when we begin to translate our documentation into languages other than English.

In conjunction with the general principles outlined earlier, the following techniques will help us write for a global audience:

- Write in simple structures.
- Use simple verbs. For example, do not use words such as "utilize" when the simpler word "use" conveys the same meaning.
- Do not use idiomatic or colloquial expressions, and watch out for culturally specific customs (for example, "red envelopes"), holidays, or sports teams.
- Avoid using metaphors, as many are culturally specific.
- Provide context for the reader using descriptive (but still concise) text.
- Avoid negative constructions. It is better to tell the reader what they can do rather than what they cannot.
- Do not use images with embedded text where possible.
