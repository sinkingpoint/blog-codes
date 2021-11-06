from collections import defaultdict
from sys import stdin, argv
from urllib.parse import urlparse
from urllib.request import urlopen

def tsv(items):
    items = sorted([(k, v) for (k, v) in items.items()], key=lambda x: x[1])
    for k, v in items:
        print("{}\t{}".format(k, v))

def try_visit(url):
    try:
        req = urlopen(url, timeout=5)
        return req.status < 400
    except:
        return False

def main(type):
    counts = defaultdict(lambda: 0)
    for line in stdin:
        url = urlparse(line)
        if type == 'paths':
            counts[url.path] += 1
        elif type == 'hosts':
            counts[url.netloc] += 1
        elif type == 'visit':
            counts[line] = try_visit(line)

    tsv(counts)

if __name__ == '__main__':
    if len(argv) < 2 or argv[1] not in ['paths', 'hosts', 'visit']:
        print("Supply 'hosts' or 'paths' as the argument to count")
        exit(1)
    main(argv[1])