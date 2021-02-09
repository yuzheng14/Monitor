import time

def log(message):
    with open('log.out','a') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\t'+message+'\n')