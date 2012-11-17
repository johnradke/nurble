nurble
======

Changes all the nouns in English text to "nurble" using the Natural Language Toolkit. The concept comes from webcomic artist Zach Weiner, who initially brainstormed the idea in [this](https://twitter.com/ZachWeiner/status/261101946151260160) [series](https://twitter.com/ZachWeiner/status/261839516795551744) of [tweets](https://twitter.com/ZachWeiner/status/261840134218063873), and later made a [webcomic](http://www.smbc-comics.com/index.php?db=comics&id=2779#comic) out of the idea.

This script uses the Natural Language Toolkit to parse the sentences and tag the parts-of-speech of words in order to replace everything besides the nouns with "nurble".

To Run
======

1. Ensure Python is installed.
2. Install the Natural Language Toolkit from here: http://nltk.org/install.html
3. Run the Python interpreter, and type the following commands:

    import nltk
    nltk.download()

4. Once the "NLTK Downloader" GUI opens, go to the Models tab and download the "punkt" model.
5. Close the NLTK Downloader and exit the Python interpreter.
6. Run the following to nurble-ize the provided example (Ezekiel 25:17, better known as Samuel L. Jackson's speech from *Pulp Fiction*):

    python nurble.py example.txt
