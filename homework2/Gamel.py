"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""


class TongLao:

    def __init__(self, blood, power):
        self.blood = blood
        self.power = power

    def see_people(self, name):
        if name == 'WYZ':
            print("师弟！！！！")
        elif name == '李秋水':
            print("师弟是我的！")
        elif name == '丁春秋':
            print("叛徒！我杀了你")

    def fight_zms(self, en_hp, en_power):
        self.power *= 10
        self.blood /= 2
        print(f"我的武力增加到{self.power}, 血量减低到{self.blood}")
        while True:
            self.power = self.power - en_power
            en_power = en_hp - self.power
            if self.power > en_hp:
                print("I win")
                break
            elif self.power < en_hp:
                print("I fail, the enemy win")
                break


class XuZhu(TongLao):

    def __init__(self, blood, power):
        super(XuZhu, self).__init__(blood, power)

    def read(self):
        print("罪过罪过")


Zhouzhiruo = XuZhu(100, 500)
Zhouzhiruo.read()
Zhouzhiruo.see_people("李秋水")
Zhouzhiruo.fight_zms(50, 50)
