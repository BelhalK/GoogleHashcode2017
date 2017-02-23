#main.py

def read_data(title):
    # reads title
    # returns lists
    # LD_list[i] is the LD of user i
    # K_list[i] is the K of user i
    # caches_list[i] is a list of the cacheserver values (id,latency)
    # RV_list[i] is the video id of request i
    # RE_list[i] is the endpoint id of request i
    # RN_list[i] is the number of requests of request i

    file = open(title,'r')

    LD_list = []
    K_list = []
    caches_list = []
    RV_list = []
    RE_list = []
    RN_list = []

    lines = file.readlines()
    i = 0
    V,E,R,C,X = [int(str) for str in lines[i].split()]
    i+= 1
    video_sizes = [int(str) for str in lines[i].split()]
    i += 1

    for e in range(E):
        LD,K = [int(str) for str in lines[i].split()]
        LD_list += [LD]
        K_list += [K]
        i += 1
        caches = []
        for l in range(K):
            c,Lc = [int(str) for str in lines[i].split()]
            caches += [(c,Lc)]
            i += 1
        caches_list += [caches]
    for r in range(R):
        RV,RE,RN = [int(str) for str in lines[i].split()]
        RV_list += [RV]
        RE_list += [RE]
        RN_list += [RN]
        i += 1



    return LD_list,K_list,caches_list,RV_list,RE_list,RN_list


def write_sub(name,N,cacheserver_list):
    file = open(name,'w')
    file.write(str(N)+'\n')
    for i in range(N):
        cacheserver = cacheserver_list[i]
        idx = cacheserver.idx
        vids = cacheserver.videos
        towrite = str(idx)
        for vid in vids:
            towrite += ' ' + str(vid.idx)
        towrite += '\n'
        file.write(towrite)
