import random
import os
import requests
import time

# HTTP Proxies
proxies = {
    "http": "http://",
}
# NUMBER OF YOU NEED
numb = 1000
# YOUR TARGET URL
url = "https://"


headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
last_str_time = time.time()

files_list = []
for files in os.listdir("./codes"):
    if os.path.splitext(files)[1] == '.png':
        files_list.append(files)

for i in range(len(files_list), numb + 1):

    time.sleep(random.randint(1, 2))

    print("downloading %d.png" % i)
    r = requests.get(url, proxies=proxies, headers=headers)
    with open('./codes/%s.png' % i, 'wb') as f:
        f.write(r.content)

    if list(str(i))[-1] == "0":
        print(
            "Downloading 10 pictures takes %d minutes, %d minutes left." % (
                (time.time() - last_str_time), (((time.time() - last_str_time) * int(numb / 10)) / 60)
            )
        )
