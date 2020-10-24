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