from homework2_modify.TongLao import TongLao


class XuZhu(TongLao):

    def __init__(self, blood, power):
        super(XuZhu, self).__init__(blood, power)

    def read(self):
        print("罪过罪过")