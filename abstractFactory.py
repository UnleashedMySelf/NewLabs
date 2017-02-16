class Shop(object):
    def __init__(self, item_factory = None):
        self.item_factory=item_factory

    def get_item_description(self):
        item=self.item_factory.get_item()
        print("Item model ",self.item_factory.model())
        print("Item name ",item.name())
        print("Item color ",self.item_factory.color())

class Jacket(object):
    def name(self):
        return "Jacket"
    def __str__(self):
        return "Jacket"

class Gadget(object):
    def name(self):
        return "Apple"
    def __str__(self):
        return "Apple"

class JacketFactory(object):
    def get_item(self):
        return Jacket()
    def model(self):
        return "Wrangler"
    def color(self):
        return "Dark blue"

class GadgetFactory(object):
    def get_item(self):
        return Gadget()
    def model(self):
        return "iPad Pro"
    def color(self):
        return "Space Gray"

shopJacket=Shop(JacketFactory())
shopJacket.get_item_description()
print("*"*30)
shopGadget=Shop(GadgetFactory())
shopGadget.get_item_description()