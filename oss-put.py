#! /usr/bin/env python3
from opt import Options
from pkg import utils
from pkg.runner import Runner

version = '0.0.1'


def banner():
    print("""
                                                  __ 
  ____    _____   _____           ____   __  __  / /_
 / __ \\  / ___/  / ___/ ______   / __ \\ / / / / / __/
/ /_/ / (__  )  (__  ) /_____/  / /_/ // /_/ / / /_  
\\____/ /____/  /____/          / .___/ \\__,_/  \\__/  
                              /_/  
                                                
                            wjlin0.com         
    """)
    print("慎用。你要为自己的行为负责\n开发者不承担任何责任，也不对任何误用或损坏负责。\n")


# 解析命令行参数
def parse_args():
    import argparse
    parser = argparse.ArgumentParser('oss-put.py', add_help=False)
    parser.add_argument('-u', '-url', '--url', help=Options.docs()['url'])
    parser.add_argument('-l', '-list', '--list', help=Options.docs()['list'])
    parser.add_argument('-p', '-proxy', '--proxy', help=Options.docs()['proxy'])
    parser.add_argument('-o', '-output', '--output', help=Options.docs()['output'])
    parser.add_argument('-d', '-debug', '--debug', action='store_true', default=False, help=Options.docs()['debug'])
    parser.add_argument('-t', '-thread', '--thread', type=int, help=Options.docs()['thread'])
    parser.add_argument('-h', '-help', '--help', action='help', help='help info')
    parser.add_argument('-c', '-config', '--config', default='config.yaml', help='config file')
    parser.add_argument('-v', '-version', '--version', action='version', version=f'%(prog)s current version v{version}',
                        help='version')
    parser.add_argument('-nc', '-nocolor', '--nocolor', action='store_true', default=False, help='no color')
    args = parser.parse_args()
    opt = Options()
    if args.config:
        # 如果文件不存在先进行序列化
        import os
        if not os.path.exists(args.config):
            opt.to_yaml(args.config)
        opt.from_yaml(args.config)
    if args.url is not None:
        opt.url = args.url
    if args.list is not None:
        opt.list = args.list
    if args.proxy is not None:
        opt.proxy = args.proxy
    if args.output is not None:
        opt.output = args.output
    if args.debug is not None:
        opt.debug = args.debug
    if args.thread is not None:
        opt.thread = args.thread
    if args.nocolor is not None:
        opt.nocolor = args.nocolor
    if opt.url is None and opt.list is None:
        docx()
        exit(-1)
    check = opt.validate()
    if check != True:
        print(check)
        exit(-1)
    if opt.nocolor:
        utils.NoColor = True
    return opt


def docx():
    print('''运行 oss-put 单个目标
$ python3 oss-put.py -u https://wjlin0.com/

运行 oss-put 批量目标
$ python3 oss-put.py -l url.txt

运行 oss-put 批量目标并导出结果
$ python3 oss-put.py -l url.txt -o output.txt

运行 oss-put 批量目标并使用代理
$ python3 oss-put.py -l url.txt -p http://127.0.0.1:7890
''')


if '__main__' == __name__:
    banner()
    opts = parse_args()
    runner = Runner(options=opts, version=version)
    runner.run()
