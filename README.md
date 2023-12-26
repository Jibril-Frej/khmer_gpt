# khmer_gpt

A small tutorial to know the basics to start marking a Language Model in Khmer

## Prerequisites

conda

## Download Khmer Wikipedia

```bash
wget https://dumps.wikimedia.org/kmwiki/20231220/kmwiki-20231220-pages-articles.xml.bz2
```

```bash
wget bzip2 -dk kmwiki-20231220-pages-articles.xml.bz2
```

Use wikiextractor to get the text from XML dump. The argument -b sets the maximum file size, here we set it ot 200M to have a single file to analyse.

```bash
python -m wikiextractor.WikiExtractor kmwiki-20231220-pages-articles.xml --json -b 200M
```
