import time
import logging

from utilities.now_hsi import index_data
from utilities.tg_wrapper import TGBot
from config import TelegramCredential
from utilities.utils import get_current_unix_ts, convert_date_str

logging.basicConfig(filename='./hsi_updater.log', encoding='utf-8',
                    level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

tg_bot = TGBot(token=TelegramCredential.token_id, chat_id=TelegramCredential.channel_id)
index_list = index_data()

if __name__ == '__main__':
    ref_ts = get_current_unix_ts()
    logging.debug('Starts.')

    while True:
        logging.debug('Get update index.')
        try:
            update_index = index_list.get_update(ref_ts=ref_ts)
            if len(update_index) != 0:
                update_index.reverse()
                for dat in update_index:
                    contents = f'{"code: " + dat["code"]}' \
                               f'\n{"date: " + dat["sysdate"]}' \
                               f'\n{"index: " + dat["index"]}' \
                               f'\n{"volume: " + dat["volume"]}' \
                               f'\n{"============================="}'
                    tg_bot.send_message(text=contents, thread_id=TelegramCredential.thread_id)
            # contents = f'{ref_ts}: Helloworld'
            print(contents)
            tg_bot.send_message(text=contents, thread_id=TelegramCredential.thread_id)
        except Exception as e:
            logging.error(e.__str__())
        finally:
            ref_ts = get_current_unix_ts()
            time.sleep(60)