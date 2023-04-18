def get_formatted_name(first: str, last: str):
    """生成简洁的姓名"""
    full_name = f"{first} {last}"
    return full_name.title()


def get_formatted_name(first: str, last: str, middle: str = ''):
    """生成简洁的姓名"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
