# IBM Embeddable AI - Watson NLP Keyword Extraction from PDF file

Clone project repository from GitHub

```sh
git clone https://github.com/IraAngeles-IBM/watson-nlp-keyword-extraction-pdf.git
```

Change to **watson-nlp-keyword-extraction-pdf** directory

```sh
cd watson-nlp-keyword-extraction-pdf
```

Install Python libraries

```sh
pip install -r requirements.txt
```

Ensure you have the Watson NLP Server URL before you run the program

```sh
export SERVER_URL=<watson nlp server URL>
```

To execute the program

```sh
python pdf_keyword_extract.py <pdf-filename> <csv-filename> <number_of_keywords>
```


