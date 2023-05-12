% agora_style_guide documentation master file, created by
% sphinx-quickstart on Wed May 13 22:13:27 2020.
% You can adapt this file completely to your liking, but it should at least
% contain the root `toctree` directive.

```{toctree}
:hidden: true
:maxdepth: 2
概述
单词表
语言和语法
标点符号
格式和架构
API 注释文档
相关参考
```

```{toctree}
:caption: Appendix
:hidden: true
:maxdepth: 2

变更历史
GitHub repo <https://github.com/AgoraDoc/agora-style-guide>
```

# 声网开发者文档风格指南

本文档是技术写作人员在语法、风格和用法方面的主要参考。它主要基于 [Google 开发者文档风格指南](https://developers.google.com/style/)。必要时会注明例外情况；可以在 [例外情况](#例外情况) 中找到主要差异的摘要。

在调查风格规范问题时，请先查阅本指南。有关本文档范围之外的信息，请参阅 Google 风格指南。

本文档还包含声网产品和技术名词的官方拼写，以及相关词的首选拼写列表。有关详细信息，请参阅{doc}`word-list`。

有关附加术语和通用词汇的（美国）英语拼写，请参阅[ Merriam-Webster 词典 ](https://www.merriam-webster.com/)。

如需进一步深入研究样式、语法和技术文档，您可以参考以下推荐资源：

## 英语参考资料（在线）

- [Apple 风格指南 ](https://help.apple.com/applestyleguide/)
- [Appledoc评论格式样式](https://github.com/tomaz/appledoc/blob/master/CommentsFormattingStyle.markdown)
- [如何为Javadoc工具编写文档注释](http://www.oracle.com/technetwork/articles/java/index-137868.html)
- [微软写作风格指南 ](https://docs.microsoft.com/en-us/style-guide/welcome/)
- [普渡大学在线写作实验室 ](https://owl.purdue.edu/owl/purdue_owl.html)
- [风格元素 (PDF) ](https://faculty.washington.edu/heagerty/Courses/b572/public/StrunkWhite.pdf)

## 英文参考资料（书籍）

- *A Manual of Style*，芝加哥大学出版社（富兰克林经典贸易出版社，2018 年）
- *开发高质量的技术信息：作家和编辑手册，米歇尔·凯莉* (Michelle Carey) 等人着。（IBM 出版社，2014 年）。
- *Managing your Documentation Projects*，作者：JoAnn Hackos（John Wiley and Sons，1994 年）。
- *技术编辑*，作者：Judith A. Tarutz（Basic Books，1992 年）。
- *The Deluxe Transitive Vampire: The Ultimate Handbook of Grammar for the Innocent, the Eager, and the Doomed*，凯伦·伊丽莎白·戈登（Karen Elizabeth Gordon）（万神殿，1993 年）。
- *The New Well-Tempered Sentence: A Punctuation Handbook for the Innocent, the Eager, and the Doomed*，凯伦·伊丽莎白·戈登 (Mariner Books, 2003)。

## 中文参考资料

- [中文技术文档写作风格指南](https://zh-style-guide.readthedocs.io)
- [泛化智能文风规范](https://github.com/generalized-intelligence/gi-Chinese-Style-Guide/blob/master/泛化智能（gi）文风指南.md)
- [leengo 简体中文规范指南](https://www.lengoo.de/documents/styleguides/lengoo_styleguide_ZH.pdf)
- [LeanCloud 文案风格指南 ](https://open.leancloud.cn/copywriting-style-guide/)
- [豆荚文案风格指南](https://docs.google.com/document/d/1R8lMCPf6zCD5KEA8ekZ5knK77iw9J-vJ6vEopPemqZM/edit)
- [中文技术文档的写作规范](https://github.com/ruanyf/document-style-guide)
- [中文案例排版指南 ](https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.zh-CN.md)

## 例外情况

对于熟悉 Google 风格指南的人，本节总结了该文档与本风格指南之间的主要区别。

### 语言和语法

缩写

：除了 FAQ 的标题外，不要使用缩写。

所有格

：不要对产品或公司名称使用所有格。

语气

：除 FAQ 外，在技术文档中使用正式的语气。FAQ 文档可以更具对话性。

### 格式和架构

分辨率

: 当提到分辨率值时，例如“1080p”或“1920 × 1080”，只有当数字有五位或更多位时才使用逗号。例如“宽度不能超过 1920，宽度 × 高度不能超过 1920 × 1080”。此外，分辨率的表达需使用乘法符号而不是小写的 x。

数字和间距
: - 在数学符号周围使用空格。示例：V = 关闭，宽度 x 高度，x \< y
: - 在尺寸数据周围使用空格。示例：3.2 x 3.6 x 0.6 毫米。