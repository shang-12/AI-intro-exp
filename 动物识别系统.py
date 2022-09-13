'''
    实验一：动物识别系统
    根据输入的事实及规则库，识别虎、金钱豹、斑马、长颈鹿、企鹅、鸵鸟、信天翁等七种动物
    input: 事实特征
    output: 推理过程及结果
    @author: shang-12
    @date: 2022年9月13日
'''
# 特征
dic = { 1:"有毛发", 2:"有奶", 3:"有羽毛", 4:"会飞", 5:"会下蛋", 6:"吃肉", 7:"有犬齿", 8:"有爪", 9:"眼盯前方",
        10:"哺乳动物", 11:"鸟", 12:"食肉动物", 13:"有蹄类动物",
        14:"有蹄", 15:"反刍动物", 16:"黄褐色", 17:"有暗斑点", 18:"有黑色条纹",
        19:"有长脖子", 20:"有长腿", 21:"不会飞", 22:"黑白二色", 23:"会游泳", 24:"善飞",
        25:"虎", 26:"金钱豹", 27:"斑马", 28:"长颈鹿", 29:"企鹅", 30:"鸵鸟", 31:"信天翁"}

'''
    规则库：
    r1: 1 -> 10
    r2: 2 -> 10
    r3: 3 -> 11
    r4: 4, 5 -> 11
    r5: 6 -> 12
    r6: 7, 8, 9 -> 12
    r7: 10, 14 -> 13
    r8: 10, 15 -> 13
    r9: 10, 12, 16, 17 -> 26
    r10: 10, 12, 16, 18 -> 25
    r11: 13, 19, 20, 17 -> 28
    r12: 13, 18 -> 27
    r13: 11, 19, 20, 21, 22 -> 30
    r14: 11, 23, 21, 22 -> 29
    r15: 11, 24 -> 31
'''
'''
    根据规则库进行推理
    para: l(事实)
    return: none
'''
def judge(l: list):
    if 1 in l:
        print(dic[1] + " -> " + dic[10])
        if 10 not in l:
            l.append(10)
    elif 2 in l:
        print(dic[2] + " -> " + dic[10])
        if 10 not in l:
            l.append(10)

    if 3 in l:
        print(dic[3] + " -> " + dic[11])
        if 11 not in l:
            l.append(11)
    elif 4 in l and 5 in l:
        print(dic[4] + ", " + dic[5] + " -> " + dic[11])
        if 11 not in l:
            l.append(11)

    if 6 in l:
        print(dic[6] + " -> " + dic[12])
        if 12 not in l:
            l.append(12)
    elif 7 in l and 8 in l and 9 in l:
        print(dic[7] + ", " + dic[8] + ", " + dic[9] + " -> " + dic[12])
        if 12 not in l:
            l.append(12)

    if 10 in l and 14 in l:
        print(dic[10] + ", " + dic[14] + " -> " + dic[13])
        if 13 not in l:
            l.append(13)
    elif 10 in l and 15 in l:
        print(dic[10] + " -> " + dic[15])
        if 13 not in l:
            l.append(13)

    if 10 in l and 12 in l and 16 in l and 17 in l:
        print(dic[10] + ", " + dic[12] + ", " + dic[16] + ", " + dic[17] + " -> " + dic[26])
        print("该动物为：" + dic[26])
    elif 10 in l and 12 in l and 16 in l and 18 in l:
        print(dic[10] + ", " + dic[12] + ", " + dic[16] + ", " + dic[18] + " -> " + dic[25])
        print("该动物为：" + dic[25])
    elif 13 in l and 17 in l and 19 in l and 20 in l:
        print(dic[13] + ", " + dic[17] + ", " + dic[19] + ", " + dic[20] + " -> " + dic[28])
        print("该动物为：" + dic[28])
    elif 13 in l and 18 in l:
        print(dic[13] + ", " + dic[18] + " -> " + dic[27])
        print("该动物为：" + dic[27])
    elif 11 in l and 19 in l and 20 in l and 21 in l and 22 in l:
        print(dic[11] + ", " + dic[19] + ", " + dic[20] + ", " + dic[21] + ", " + dic[22] + " -> " + dic[30])
        print("该动物为：" + dic[30])
    elif 11 in l and 21 in l and 22 in l and 23 in l:
        print(dic[11] + ", " + dic[21] + ", " + dic[22] + ", " + dic[23] + " -> " + dic[29])
        print("该动物为：" + dic[29])
    elif 11 in l and 24 in l:
        print(dic[11] + ", " + dic[24] + " -> " + dic[31])
        print("该动物为：" + dic[31])
    else:
        print("根据现有规则暂时无法识别该动物！")
while 1:
    print("***************************************************************************")
    print("*1:有毛发     |2:有奶   |3:有羽毛   |4:会飞     |5:会下蛋   |6:吃肉       *")
    print("*7:有犬齿     |8:有爪   |9:眼盯前方 |10:哺乳动物|11:鸟      |12:食肉动物  *")
    print("*13:有蹄类动物|14:有蹄  |15:反刍动物|16:黄褐色  |17:有暗斑点|18:有黑色条纹*")
    print("*19:有长脖子  |20:有长腿|21:不会飞  |22:黑白二色|23:会游泳  |24:善飞      *")
    print("***************************************************************************")
    print("请输入事实(数字，用空格分隔)：")
    try:
        num_input = [int(i) for i in input().split(" ")]
    except:
        print("输入信息有误，请重新输入！")

    flag = False
    for i in num_input:
        if i < 1 or i > 24:
            flag = True
            break
    if flag:
        print("请输入1~24之间的数字")
        continue
    judge(num_input)
    print("输入0退出系统，输入1继续")
    if int(input()) == 0:
        break