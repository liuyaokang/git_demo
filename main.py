from get_data import parase_list
from get_urls import get_last_urls



if __name__ == "__main__":
    urls  = get_last_urls()
    u = urls
    for url in urls:
        parase_list(url)
        break

