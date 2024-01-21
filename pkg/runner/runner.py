import concurrent.futures
import sys

from opt.options import Options
from pkg.requests import Requests
from pkg.utils import generate_random_string, INF, SUCCESS, ERR


class Runner:
    def __init__(self, options: Options, version):
        self.options = options
        self._targets = []
        self._version = version
        self._debug = options.debug
        if self.options.proxy:
            proxy = dict(
                http=self.options.proxy,
                https=self.options.proxy
            )
        else:
            proxy = None
        self.requests = Requests(proxy=proxy)
        self.load_targets()

    def load_targets(self):
        if self.options.url:
            if self.options.url.endswith('/'):
                self._targets.append(self.options.url[:-1])
            else:
                self._targets.append(self.options.url)

        if self.options.list:
            with open(self.options.list, 'r') as file:
                for line in file.readlines():
                    line = line.strip()
                    if line == "":
                        continue
                    if line.endswith('/'):
                        self._targets.append(line[:-1])
                    else:
                        self._targets.append(line)
        # 去重复
        self._targets = list(set(self._targets))

    def run(self):
        # 输出版本
        INF(f"current version oss-put v{self._version}")
        # 输出目标总数 和 线程数 和 运行模式
        INF(f"targets: {len(self._targets)}, thread: {self.options.thread}, debug: {self.options.debug}, proxy: {self.options.proxy}")
        success = 0
        failed = 0
        # 多线程，线程池
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.options.thread) as executor:
            futures = [executor.submit(self.exploit, target) for target in self._targets]
            # 等待每个任务完成并获取结果
            for future in concurrent.futures.as_completed(futures):
                results_lists = future.result()
                if results_lists['result']:
                    success += 1
                else:
                    failed += 1
                self.output(**results_lists)

        INF(f"success: {success}, failed: {failed}")

    def exploit(self, url) -> dict:
        headers = {
            'Content-Type': 'text/plain',
            'Accept-Encoding': 'gzip, deflate, br',
        }
        # 随机生成一个文件名
        url_ = f"{url}/{generate_random_string()}.txt"
        data = generate_random_string(20)
        try:
            resp = self.requests.put(url=url_, headers=headers, data=data)
            if resp.status_code != 200:
                return dict(url=url, result=False, error=None)
            resp = self.requests.get(url=url_)
            if data == resp.text:
                return dict(url=url, result=True, error=None)
        except Exception as e:
            return dict(url=url, result=False, error=Exception(e))
        return dict(url=url, result=False, error=None)

    def output(self, url, result, error: Exception):
        if error:
            if self._debug:
                ERR(f"{url} {error}")
            return
        if result:
            SUCCESS(f"{url} is vulnerable")
            if self.options.output:
                with open(self.options.output, 'a+', encoding='utf-8') as file:
                    file.write(f"{url}\n")
            return
        else:
            if self._debug:
                ERR(f"{url} is not vulnerable")
            return
