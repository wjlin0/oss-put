import pkg.utils

NoColor = False


def color_print(color, msg):
    if pkg.utils.NoColor:
        return msg
    else:
        return '\033[1;{}m{}\033[0m'.format(color, msg)


def INF(msg):
    c = color_print(34, 'INF')
    print(f"[{c}] {msg}")


def SUCCESS(msg):
    c = color_print(32, 'SUC')
    print(f"[{c}] {msg}")


def WAR(msg):
    c = color_print(33, 'WAN')
    print(f"[{c}] {msg}")


def DEBUG(msg):
    c = color_print(34, 'DBG')
    print(f"[{c}] {msg}")


def ERR(msg):
    c = color_print(31, 'ERR')
    print(f"[{c}] {msg}")
