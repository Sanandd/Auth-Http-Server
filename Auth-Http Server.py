import requests,sys,argparse
requests.packages.urllib3.disable_warnings()
from multiprocessing import Pool

def main():
    parse =argparse.ArgumentParser(description="信息泄露")
    parse.add_argument('-u','--url',dest='url',type=str,help='输入url')
    parse.add_argument('-f','--file',dest='file',type=str,help='输入file')
    args = parse.parse_args()
    pool = Pool(20)
    try:
        if args.url:
            check(args.url)
        else:
            targets = []
            f = open(args.file,'r+')
            for target in f.readlines():
                target = target.strip()
                targets.append(target)
            pool.map(check,targets)
    except Exception as e:
        print(e)
def check(target):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
    }
    responses = requests.get(target,headers=headers,verify=False)
    try:
        if responses.status_code == 200:
            print(f"[*] {target} 存在")
        else:
            print(f"[!] {target} 不存在")
    except Exception as e:
        print(f"[Error] {target} TimeOut")

if __name__ == '__main__':
    main()