import random
import base36
import requests
import multiprocessing
from os import environ

process_count = int(input('how many processes do you need to run(its recommended to not going above 300):'))
loop_count = int(input('how many post ids do you need to generate per process:'))
subreddit = input("Subreddit filter (leave blank if you don't need to filter by subreddit, TYPE NAME OF SUB WITHOUT r/ SECTION!):")
if subreddit == '':
    pass
else:
    subreddit = 'r/'+ subreddit +'/comments/'

def generator():
    i = 0
    while i < loop_count:
        random.seed(random.randint(1,900000))
        random_number = random.randint(100000000,999999999)
        url = 'https://reddit.com/'+ subreddit +str(base36.dumps(random_number))
        req = requests.get(url)
        if (str(req) == '<Response [429]>'):
            print(url)
        i += 1

if (input(str(loop_count*process_count) + ' random post ids will be generated and checked. '+ 'Do you want to continue?(y/n)')) == 'y':
    processes = []
    for i in range(process_count):
        process = multiprocessing.Process(target=generator)
        processes.append(process)
        process.start()

    for proc in processes:
        proc.join()
    print(str(loop_count*process_count) + ' random post ids checked. Found these posts. If you see a page says Whoa There Partner, It means you need to wait a few minutes before running the code')
else:
    pass