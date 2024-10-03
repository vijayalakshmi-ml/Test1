
def gzk(shm):
    for foo in range(len(shm)-1):
        bar = foo
        for xyz in range(foo+1, len(shm)):
            if shm[xyz] < shm[bar]:
                bar = xyz  # Fix here
        ukr = shm[foo]
        shm[foo] = shm[bar]
        shm[bar] = ukr

my_list = [43, 40, 20, 57, 62, 34, 44, 18, 54, 59, 49,15, 30,14, 14, 48, 61, 56, 50, 38, 46]
gzk(my_list)
print(my_list)
