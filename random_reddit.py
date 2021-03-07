import random
import base36
import multiprocessing

loop_count = int(input('how many post ids do you need to generate:'))
process_count = int(input('how many processes do you need to run:'))

def generator():
    i = 0
    while i < loop_count:
        random.seed(random.randint(1,900000))
        random_number = random.randint(100000000,999999999)
        print(base36.dumps(random_number))
        i += 1

if (input(str(loop_count*process_count) + ' random post ids will be generated. Do you need to continue?(y/n)')) == 'y':
    processes = []
    for i in range(process_count):
        process = multiprocessing.Process(target=generator)
        processes.append(process)
        process.start()

    for proc in processes:
        proc.join()
else:
    pass