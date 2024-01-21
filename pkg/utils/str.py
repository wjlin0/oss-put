import random
import string


def generate_random_string(length=10) -> str:
    # 字符集包括所有字母和数字
    characters = string.ascii_letters + string.digits
    # 使用 random.choice 从字符集中随机选择字符
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string
