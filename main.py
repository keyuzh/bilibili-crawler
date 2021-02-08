import atexit
from crawl import Crawl

# max uid 703222999
MAX_UID = 703222999

if __name__ == '__main__':
    crawler = Crawl()
    atexit.register(crawler.save_data)

    start_id = input("start uid[1]: ")
    if not start_id:
        start_id = 1
    else:
        start_id = int(start_id)

    end_id = input("end uid[MAX]:")
    if not end_id:
        end_id = MAX_UID
    else:
        end_id = int(end_id)

    show_status = input("show requests?(yes/[no]):")
    if not show_status or show_status == 'no':
        show_status = False
    else:
        show_status = True

    crawler.start_crawling(start_id, min(end_id, MAX_UID), show_status)
