"""
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""
# 定义一个TelPhone类


class TelPhone:

    # 构造函数
    def __init__(self, color):
        self.color = color

    def phone_call(self):
        print("具有打电话的功能")

    def send_message(self):
        print("具有发短信的功能")


class SmartPhone(TelPhone):

    def paly(self):
        print("具有玩游戏的功能")


iphone12 = SmartPhone("green")
iphone12.paly()

# 定义一个Car类


class Car:
    wheel_num = 4

    def __init__(self, color):
        self.color = color

    def type(self, energy):
        print(f"我的动能是{energy}")


Tesla = Car("pink")
Tesla.type("电能")

# 定义一个Human类


class Human:

    def __init__(self, color, height, weight, age, sex):
        self.color = color
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex

    def skill(self, sk):
        print(f"我会{sk}")

    def hobby(self, ho):
        print(f"我的爱好是{ho}")


Zhangsan = Human("black", "2.5", "10kg", "1", "female")
Zhangsan.skill("闪电")
Zhangsan.hobby("瘦瘦瘦，瘦成一道闪电")

# 定义一个Noodles类


class Noodles:

    def __init__(self, width):
        self.width = width

    def des(self, area):
        print(f"我是{self.width}面")
        print(f"我来自{area}")


Spaghetti = Noodles("粗面")
Spaghetti.des("意大利")

# 定义一个培训机构类


class Train:

    def __init__(self, slogan):
        self.slogan = slogan

    def name(self, nam):
        print(f"培训机构名称是{nam}")

    def field(self, fi):
        print(f"培训领域是{fi}")

    def price(self, pri):
        print(f"培训费用是{pri}")


Hogwarts = Train("测试人的清华大学")
Hogwarts.name("霍格沃兹学院")
Hogwarts.field("测试开发")
Hogwarts.price("只要6888，买了不吃亏，买了不上当")
