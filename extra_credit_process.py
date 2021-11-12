log_file = open("um-server-01.txt")


def melon_reports(log_file):
    melon_arr = []
    for line in log_file:
        line = line.rstrip()
        values = line.split(',')
        print (line)
    #     if (float(values[0]) >= 10 and values[3] == 'Melon'):
    #         melon_arr.append(line)
    # return melon_arr
        
melon_reports(log_file)
# print (melon_reports(log_file))