import requests
import time
import signal
import sys
import os
from concurrent.futures import ProcessPoolExecutor, as_completed

class SessionWithHeaderRedirection(requests.Session):
    AUTH_HOST = 'urs.earthdata.nasa.gov'

    def __init__(self, username, password):
        super().__init__()
        self.auth = (username, password)
 
    def rebuild_auth(self, prepared_request, response):
        headers = prepared_request.headers
        url = prepared_request.url

        if 'Authorization' in headers:
            original_parsed = requests.utils.urlparse(response.request.url)
            redirect_parsed = requests.utils.urlparse(url)

            if (original_parsed.hostname != redirect_parsed.hostname) and \
                    redirect_parsed.hostname != self.AUTH_HOST and \
                    original_parsed.hostname != self.AUTH_HOST:
                del headers['Authorization']
        return

def upload(i, url, filename):
    username = "Hardik5247" 
    password= "3993Np76zZZagKi"
    session = SessionWithHeaderRedirection(username, password)

    try:
        response = session.get(url)
        print(response.status_code)
        response.raise_for_status()  

        with open(f"C:\\Users\\Hardik\\Downloads\\data\\srtm30m\\{filename}", 'wb') as fd:
            fd.write(response.content)
        print(i, "Done")
    except Exception as e:
        print(e)

def signal_handler(signal, frame):
    print(2)
    [f.cancel() for f in futures]
    # Accessing protected member of a class here (could fail in future versions)
    try:
        for pid, proc in executor._processes.items():
            if proc.is_alive():
                proc.terminate()
        executor.shutdown()
    finally:
        sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_handler)

    url_list = None
    with open("srtm30m_urls.txt", "r") as f:
        url_list = f.read().split("\n")
    print(len(url_list))

    already_downloaded = set(list(list(os.walk("C:\\Users\\Hardik\\Downloads\\data\\srtm30m"))[0])[2])
    executor = ProcessPoolExecutor(max_workers=20)
    futures = []

    n_range = {"N08", "N09"}.union({f'N{str(i)}' for i in range(10, 36)})
    e_range = {f'E0{str(i)}' for i in range(68, 98)}

    for i, url in enumerate(url_list):
        filename = url[url.rfind('/') + 1:]
        x = filename.split(".")[0]
        if "N" in x and "E" in x:
            if x[0:3] in n_range and x[3:] in e_range and filename not in already_downloaded:
                future = executor.submit(upload, i, url, filename)
                futures.append(future)

    print(len(futures))
    try:
        for future in as_completed(futures):
            future.result()
    finally:
        print(1)
        [f.cancel() for f in futures]
        for pid, proc in executor._processes.items():
            if proc.is_alive():
                proc.terminate()
        executor.shutdown()
    