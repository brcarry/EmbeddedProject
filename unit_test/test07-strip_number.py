def convert_number_to_chinese(num):
    num = int(num)
    units = ['', '十', '百', '千']
    nums = '零一二三四五六七八九'
    result = []

    if num < 10:
        return nums[num]

    num_str = str(num)
    num_len = len(num_str)

    for i, n in enumerate(num_str):
        if n == '0':
            if result and result[-1] != '零':
                result.append('零')
        else:
            result.append(nums[int(n)])
            result.append(units[num_len - i - 1])

    return ''.join(result).rstrip('零')


import re


def replace_numbers_with_chinese(text):
    def replace(match):
        number = match.group(0)
        return convert_number_to_chinese(number)

    return re.sub(r'\d+', replace, text)


text = "今天傍晚到前半夜阴有时多云，后半夜到明天早晨阴天，偶有小雨；明天上午起阴转多云到晴；后天晴到少云。今天傍晚偏 北风4-5级阵风6级，夜里到明天3-4级阵风5级。明天白天最高气温22度，明天早晨最低气温14度，明天平均相对湿度70。"
result = replace_numbers_with_chinese(text)
print(result)
