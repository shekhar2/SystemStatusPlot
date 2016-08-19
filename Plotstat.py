import re
import sys
import os

def num_groups(regex):
    return re.compile(regex).groups

def plotGraph(inputFile, process):

    my_regex = r"^\D{3}\s+\d{1,2}\s+(\d{2}(:\d{2}){2})(.*)\s+" + process + "(.*)\s+status\s+(.*)"
    h = re.compile(my_regex)
    num_group = num_groups(my_regex)
    status = []
    time = []
    firstLine = True
    stat = ["up", "down"]


    try:
        with open(inputFile) as f:
            for line in f:
                statmatch = h.match(line.strip())

                if not statmatch:
                    continue

                if statmatch.group(num_group).lower() in stat::

                    if firstLine:
                        laststatus = statmatch.group(num_group).lower()
                        status.append(1) if laststatus == "up"  else status.append(0)
                        time.append(statmatch.group(1))
                        firstLine = False

                    else:
                        if statmatch.group(num_group).lower() !=  laststatus:
                            if laststatus == "up":
                                status.append(0)
                                laststatus = "down"
                            else:
                                status.append(1)
                                laststatus = "up"

                            time.append(statmatch.group(1))


    except  IOError:
            print ("Could not read file: %s" %(inputFile))
    print(time)
    print(status)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit('input filename missing; usage: python plot.py <input_file> processString')
    plotGraph(os.path.abspath(sys.argv[1]), sys.argv[2])
