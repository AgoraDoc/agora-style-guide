# Agora Developer Documentation Style Guide

This repo hosts the content for Agora Developer Documentation Style Guide. You can browse the guide on [this website](https://agoradoc-style-guide.readthedocs.io/en/latest/), which is built with Sphinx.

## Contribute to the guide

To make updates to this guide, follow the instructions in this section.

### Prerequisites

- Basic knowledge of Git
- A [GitHub](https://github.com) account
- A code editing tool, such as [Visual Studio Code](https://code.visualstudio.com)
- A command line tool

### Make updates

The `master` branch is published to Read the Docs as the latest version. To make updates, do the following:

1. Create a new branch from `master` and update the Markdown file. Each section of the guide corresponds to a Markdown file in `_content`. 

2. Create a pull request to merge your commits to `master`.

> The source files are written in markdown, and use the MyST parser to support Sphinx features. For the MyST syntax, see [The MyST Syntax Guide](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html).

### Open an issue for discussion

Feel free to propose something for discussion by opening an issue.

1. Open the [Issues](https://github.com/AgoraDoc/Agora_style_guide/issues) page.
2. Click the **New Issue** button.
3. Edit the title and comments, and then click **Submit new issue**.

## Build the documentation locally

If you want to view the website locally before pushing your changes to GitHub, follow the instructions below.

1. Install Sphinx.

   ```bash
   $ pip install sphinx
   ```

2. Install the following packages for Markdown support.

   ```bash
   $ pip install myst-parser
   ```

3. Install the theme.

   ```bash
   $ pip install furo
   ```
   
4. Build the website locally.

   ```bash
   // Navigate to the _content folder on your PC
   $ cd /Users/jie/Agora_style_guide/_content
   // Build the website
   $ make html
   ```

If everything goes well, you should see something like this in the command line output:

```bash
build succeeded, 1 warning.
```

The output is in `/_content/__build`.