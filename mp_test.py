import multiprocessing

def worker(num):
    """thread worker function"""
    name = multiprocessing.current_process().name
    print name
    return

def main():
    jobs = []
    for i in range(50):
        p = multiprocessing.Process(target=worker,args=(i,))
        jobs.append(i)
        p.start()
        p.join()
if __name__ == '__main__':
    main()
