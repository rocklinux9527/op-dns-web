import subprocess
import re


def main():
    # 获取域名的 IP 地址
    command = "dig ops-dns-mysql +short"
    ip_address = runcmd(command)

    # 将域名替换为 IP 地址
    filename = "./tools/config.py"
    with open(filename, "r") as f:
        content = f.read()

    content_new = re.sub(r"ops-dns-mysql", ip_address, content)

    with open(filename, "w") as f:
        f.write(content_new)


def main2():
    print("start python table init")
    command = "python table.py"
    print("end python table init")
    table_result = runcmd(command) 
    print(table_result)


def runcmd(command):
    try:
       result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       std = result.stdout.decode().strip()
       return std
    except Exception  as e:
       print(str(e))


if __name__ == '__main__':
    main()
    main2()

