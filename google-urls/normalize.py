from urllib.parse import urlparse
from sys import stdin

def main():
        for line in stdin:
            if not 'http' in line:
                continue

            # Fix http //foo.com -> http://foo.com
            line = line.replace("http //", "http://")
            line = line.replace("https //", "https://")

            # Fix http//foo.com -> http://foo.com
            line = line.replace("http//", "http://")
            line = line.replace("https//", "https://")

            ## Fix http foo.com -> http://foo.com
            line = line.replace("http ", "http://")
            line = line.replace("https ", "https://")
            
            # Fix foo. com -> foo.com
            line = line.replace(". com", ".com")

            # Fix foo .com -> foo.com
            line = line.replace(" .com", ".com")

            # Fix (foo.com) -> foo.com
            line = line.strip('()')

            # Fix bar http://foo.com
            line = line[line.index("http"):]

            # Finally, parse the URL and throw out anything without a hostname
            parsed = urlparse(line)
            if parsed.netloc == '':
                continue

            print(line.strip())

if __name__ == '__main__':
    main()