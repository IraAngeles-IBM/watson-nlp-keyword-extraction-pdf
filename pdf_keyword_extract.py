import os
import pandas as pd
import requests
import json
import csv
import typer

from PyPDF2 import PdfReader
from typing import Optional

SERVER_URL = os.getenv("SERVER_URL")

headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
    }

main_app = typer.Typer()

# extracts keywords from text using library API

def extract_keywords(text, limit):
    REQ_URL = SERVER_URL+'/v1/watson.runtime.nlp.v1/NlpService/KeywordsPredict'
    MODEL_STOCK = 'keywords_text-rank-workflow_lang_en_stock'

    payload = {
       'rawDocument': {
            'text': text
        },
        'limit': limit
    }

    headers['grpc-metadata-mm-model-id'] = MODEL_STOCK
    response = requests.post(REQ_URL, headers=headers, data=json.dumps(payload))
    response_json = response.json()
    keywords_list = response_json['keywords']
    key_list = []
    for i in range(len(keywords_list)):
        dict_list = {}
        dict_list['phrase'] = keywords_list[i]['text']
        dict_list['relevance'] = keywords_list[i]['relevance']
        key_list.append(dict_list)
    return (key_list)


@main_app.command()
def extract(soure_pdf: str, target_csv: str, kw_limit: Optional[int] = typer.Argument(None, help="")):
    reader = PdfReader(soure_pdf)
    numpages = len(reader.pages)
    page = reader.pages[0]

    if not kw_limit:
        kw_limit = 100

    print("Extracting Text from PDF file.")

    text = ""
    for i in range(numpages):
        page = reader.pages[i]
        text += page.extract_text()


    k_key_list = extract_keywords(text, kw_limit)
    print("Extracting keywords using Watson NLP.")

    df = pd.DataFrame(k_key_list)


    print(f"Saving the extracted keywords to {target_csv} CSV file.")
    df.to_csv(target_csv, index=False)


if not SERVER_URL:
    print("Error: SERVER_URL not found.\n   please type export SERVER_URL=<server url>")
    exit(1)


if __name__ == "__main__":
    main_app()






