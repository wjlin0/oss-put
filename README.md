<h4 align="center"> oss-put 是一个用python编写的检查存储桶是否存在任意写入文件的脚本。这是一个非常简单的工具。</h4>
<p align="center">
<a href="https://github.com/wjlin0/oss-put/releases/"><img src="https://img.shields.io/github/release/wjlin0/oss-put" alt=""></a> 
<a href="https://github.com/wjlin0/oss-put" ><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/wjlin0/oss-put"></a>
<a href="https://github.com/wjlin0/oss-put/releases"><img src="https://img.shields.io/github/downloads/wjlin0/oss-put/total" alt=""></a> 
<a href="https://github.com/wjlin0/oss-put"><img src="https://img.shields.io/github/last-commit/wjlin0/oss-put" alt=""></a> 
<a href="https://blog.wjlin0.com/"><img src="https://img.shields.io/badge/wjlin0-blog-green" alt=""></a>
</p>

# 特征
- 快速发现存储桶任意文件写入漏洞
- 支持使用HTTP/SOCKS5代理

# 安装oss-put
```shell
git clone https://github.com/wjlin0/oss-put.git
cd oss-put
pip install -r requirements.txt
./oss-put.py
```
# 用法
oss-put 用法简单，只需要指定一个URL即可，例如：
```shell
./oss-put.py -u https://example.com
```
```text

                                                  __ 
  ____    _____   _____           ____   __  __  / /_
 / __ \  / ___/  / ___/ ______   / __ \ / / / / / __/
/ /_/ / (__  )  (__  ) /_____/  / /_/ // /_/ / / /_  
\____/ /____/  /____/          / .___/ \__,_/  \__/  
                              /_/  
                                                
                            wjlin0.com         
    
慎用。你要为自己的行为负责
开发者不承担任何责任，也不对任何误用或损坏负责。

[INF] targets: 2, thread: 10, debug: False, proxy: None
[SUC] https://example.com is vulnerable
[INF] success: 1, failed: 1
```
oss-put 支持使用代理，例如：
```shell
./oss-put.py -u https://example.com -p http://127.0.0.1:7890
```
```text

                                                  __ 
  ____    _____   _____           ____   __  __  / /_
 / __ \  / ___/  / ___/ ______   / __ \ / / / / / __/
/ /_/ / (__  )  (__  ) /_____/  / /_/ // /_/ / / /_  
\____/ /____/  /____/          / .___/ \__,_/  \__/  
                              /_/  
                                                
                            wjlin0.com         
    
慎用。你要为自己的行为负责
开发者不承担任何责任，也不对任何误用或损坏负责。

[INF] targets: 2, thread: 10, debug: False, proxy: http://127.0.0.1:7890
[SUC] https://example.com is vulnerable
[INF] success: 1, failed: 1
```
oss-put 支持结果输出到文件，例如：
```shell
./oss-put.py -u https://example.com -o output.txt
```
```text

                                                  __ 
  ____    _____   _____           ____   __  __  / /_
 / __ \  / ___/  / ___/ ______   / __ \ / / / / / __/
/ /_/ / (__  )  (__  ) /_____/  / /_/ // /_/ / / /_  
\____/ /____/  /____/          / .___/ \__,_/  \__/  
                              /_/  
                                                
                            wjlin0.com         
    
慎用。你要为自己的行为负责
开发者不承担任何责任，也不对任何误用或损坏负责。

[INF] targets: 2, thread: 10, debug: False, proxy: None
[SUC] https://example.com is vulnerable
[INF] success: 1, failed: 1
```
oss-put 也支持调试查看，例如：
```shell
./oss-put.py -list url.txt -debug
```
```text

                                                  __ 
  ____    _____   _____           ____   __  __  / /_
 / __ \  / ___/  / ___/ ______   / __ \ / / / / / __/
/ /_/ / (__  )  (__  ) /_____/  / /_/ // /_/ / / /_  
\____/ /____/  /____/          / .___/ \__,_/  \__/  
                              /_/  
                                                
                            wjlin0.com         
    
慎用。你要为自己的行为负责
开发者不承担任何责任，也不对任何误用或损坏负责。

[INF] targets: 2, thread: 10, debug: True, proxy: None
[SUC] https://example.com is vulnerable
[ERR] https://wjlin0.com HTTPSConnectionPool(host='wjlin0.com', port=443): Max retries exceeded with url: /pXxio7Uhn7.txt (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x102088a00>: Failed to resolve 'wjlin0.com' ([Errno 8] nodename nor servname provided, or not known)"))
[INF] success: 1, failed: 1
```
oss-put 当然也可以所有参数写入config.yaml中：
```yaml
# url 目标 eg: https://example.com/
url: https://example.com/

# list 目标列表（文件）eg: url.txt
list: 

# proxy 代理 eg: http://127.0.0.1:7890
proxy: 

# output 输出路径 eg: output.txt
output: 

# thread 线程数 eg: 10
thread: 0

# debug 调试模式 eg: True
debug: False

# nocolor 关闭颜色 eg: True
nocolor: False
```
```shell
python oss-put.py 
```
