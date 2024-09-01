import os
import requests
import telegram
from random import randint
from pathlib import Path
from dotenv import load_dotenv
from retry import retry


def fetch_comics_entity(comics_number):
    """Скачать комикс по номеру"""
    url = f'https://xkcd.com/{comics_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_and_save(image_url, path_to_image):
    """Скачать картинку по указанному адресу и записать по указанному пути."""
    response = requests.get(image_url)
    response.raise_for_status()
    with open(path_to_image, 'wb') as file:
        file.write(response.content)


@retry(exceptions=telegram.error.NetworkError, delay=20)
def send_comics_and_comment(bot, tg_chat_id, path_to_image, comment):
    """Опубликовать комикс с комментарием."""
    with open(path_to_image, 'rb') as image:
         bot.send_document(chat_id=tg_chat_id, document=image, caption=comment)


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]

    bot = telegram.Bot(token=tg_token)

    Path('images').mkdir(parents=True, exist_ok=True)
    current_comics = fetch_comics_entity('')
    current_comics_number = current_comics['num']
    comics_number = randint(1, current_comics_number)

    comics = fetch_comics_entity(comics_number)
    comics_url = comics['img']
    comment = comics['alt']

    path_to_image = Path('images', f'comics_{comics_number}.png')

    try:
        fetch_and_save(comics_url, path_to_image)
        send_comics_and_comment(bot, tg_chat_id, path_to_image, comment)
    except:
        print("Комикс опубликовать не удалось")
    finally:
        Path(path_to_image).unlink(missing_ok=True)


if __name__ == "__main__":
    main()
