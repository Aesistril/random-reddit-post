import random
import base36
import requests
import multiprocessing

process_count = 30
loop_count = int(int(input('how many post ids do you need to generate:'))/process_count)
if (loop_count == 0): loop_count = 1
manager = multiprocessing.Manager()
posts = manager.list()

def generator(posts):
    i = 0
    while i < loop_count:
        random.seed(random.randint(1,900000))
        random_number = random.randint(100000000,999999999)
        url = 'https://reddit.com/'+str(base36.dumps(random_number))
        req = requests.get(url)
        if (str(req) == '<Response [429]>'):
            print(url)
            posts.append(url)
        i += 1

if (input(str(loop_count*process_count) + ' random post ids will be generated and checked. '+ 'Do you want to continue?(y/n)')) == 'y':
    processes = []
    for i in range(process_count):
        process = multiprocessing.Process(target=generator, args=(posts,))
        processes.append(process)
        process.start()

    for proc in processes:
        proc.join()
    print(str(loop_count*process_count) + ' random post ids checked. Found these posts. If you see a page says Whoa There Partner, It means you need to wait a few minutes before running the code')
else:
    pass

while True:
    try:
        out = open(input('File name to save:')+'.txt', 'x')
        break
    except:
        print('file already exists')
for link in posts:
    out.write(link + '\n')
out.close()