import yaml


class Options:
    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Options, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self.url = ''
            self.list = ''
            self.proxy = ''
            self.output = ''
            self.thread = 0
            self.debug = False
            self.nocolor = False
            self._is_initialized = True

    # yaml序列化
    def to_yaml(self, filename):
        help_dict = self.docs()
        yaml_data = ""
        yaml_data += f"# url {help_dict['url']}\n"
        yaml_data += f"url: {self.url}\n\n"
        yaml_data += f"# list {help_dict['list']}\n"
        yaml_data += f"list: {self.list}\n\n"
        yaml_data += f"# proxy {help_dict['proxy']}\n"
        yaml_data += f"proxy: {self.proxy}\n\n"
        yaml_data += f"# output {help_dict['output']}\n"
        yaml_data += f"output: {self.output}\n\n"
        yaml_data += f"# thread {help_dict['thread']}\n"
        yaml_data += f"thread: {self.thread}\n\n"
        yaml_data += f"# debug {help_dict['debug']}\n"
        yaml_data += f"debug: {self.debug}\n\n"
        yaml_data += f"# nocolor {help_dict['nocolor']}\n"
        yaml_data += f"nocolor: {self.nocolor}\n\n"
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(yaml_data)

    def from_yaml(self, filename):
        """从YAML文件反序列化为类实例"""
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
            for key, value in data.items():
                setattr(self, key, value)

    def __repr__(self):
        return f"Options(url={self.url}, list={self.list}, proxy={self.proxy}, output={self.output}, thread={self.thread}, debug={self.debug}, nocolor={self.nocolor})"
    @staticmethod
    def docs():
        return dict(
            url='目标 eg: https://example.com/',
            list='目标列表（文件）eg: url.txt',
            proxy='代理 eg: http://127.0.0.1:7890',
            output='输出路径 eg: output.txt',
            thread='线程数 eg: 10',
            debug='调试模式 eg: True',
            nocolor='关闭颜色 eg: True'
        )

    def validate(self):
        if self.url is None and self.list is None:
            return "[-] url and list cannot be both empty"

        if self.thread is not None and isinstance(self.thread, str) and not self.thread.isdigit():
            return "[-] thread must be a number"
        if self.thread == 0:
            self.thread = 10
        return True
