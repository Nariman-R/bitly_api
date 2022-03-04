import argparse
import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, url):
    headers = {"Authorization": "Bearer {}".format(token)}
    long_url = {"long_url": url}
    response = requests.post(
                    "https://api-ssl.bitly.com/v4/shorten",
                    json=long_url,
                    headers=headers,
              )
    response.raise_for_status()
    decoded_response = response.json()
    if 'error' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['error'])
    return decoded_response["link"]


def is_bitlink(token, url):
    parsed_url = urlparse(url)
    url = "https://api-ssl.bitly.com/v4/bitlinks/{}{}".format(
        parsed_url.netloc,
        parsed_url.path
    )
    headers = {"Authorization": "Bearer {}".format(token)}
    response = requests.get(url, headers=headers)
    return response.ok


def count_clicks(token, url):
    parsed_url = urlparse(url)
    headers = {"Authorization": "Bearer {}".format(token)}
    params = {"unit": "month", "units": "-1"}
    url = "https://api-ssl.bitly.com/v4/bitlinks/{}{}/clicks/summary".format(
        parsed_url.netloc,
        parsed_url.path
    )
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    decoded_response = response.json()
    if 'error' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['error'])
    return decoded_response["total_clicks"]


def main():
    load_dotenv()
    bitly_token = os.environ["BITLY_TOKEN"]
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='Ссылка')
    args = parser.parse_args()
    try:
        if is_bitlink(bitly_token, args.link):
            print("Количество переходов по ссылке: ", count_clicks(bitly_token, args.link))
        else:
            print("Битлинк ", shorten_link(bitly_token, args.link))
    except requests.exceptions.HTTPError:
        print("Ссылка неверная")

if __name__ == "__main__":
    main()
