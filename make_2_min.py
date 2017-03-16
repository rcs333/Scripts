# This is that black magic voodoo that turns timestamps into the correct format
timestamps = open('timestamps.txt')


def det_day(pt_day, time):
    count = 1
    times = []
    f = open(pt_day + '_times.txt')
    for entry in f:
        if count % 2 == 0:
            times.append(float(entry))
        count += 1
    for x in range(1, len(times)):
        times[x] = times[x] + times[x - 1]

    count = 0
    for cum_time in times:
        if time < cum_time:
            break
        count += 1
    f.close()
    return count, times[count - 1]

d = open('fully_processed_timestamps.txt', 'w')
d.write('pt_day_vidnum,start,end,kwd\n')

for line in timestamps:
    pt = line.split()[0]
    start = float(line.split()[1]) + 0.5
    end = float(line.split()[2]) - 0.5
    kwd = line.split()[3]
    [num, time_adj] = det_day(pt, float(start))
    new_start = start - time_adj
    new_end = end - time_adj

    d.write(pt + '_' + str(num).zfill(4) + ',' + str(new_start) + ',' + str(new_end) + ',' + kwd + '\n')
