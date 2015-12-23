
class Part(object):

    def __init__(self, part_id, element_id, qty):
        self.part_id = part_id
        self.element_id = element_id
        self.qty = qty

    def __str__(self):
        output = '{part_id},{element_id},{qty}\n'
        return output.format(**self.__dict__)


class Set(object):

    def __init__(self, set_id, description, parts):
        self.set_id = set_id
        self.description = description
        self._parts = parts

    def __str__(self):
        output = 'part_id,element_id, qty\n'
        for part in self.parts:
            output += str(part)
        return output

    @property
    def parts(self):
        def part_id(p):
            return p.part_id
        return sorted(self._parts, key=part_id)

    @property
    def parts_file(self):
        return './' + self.set_id + '_parts.csv'

    @property
    def bricklink_file(self):
        return './' + self.set_id + '_bricklink.csv'


class Listing(object):

    def __init__(self, part_id, element_id, qty, price, name, link):
        self.part_id = part_id
        self.element_id = element_id
        self.qty = qty
        self.price = price
        self.name = name
        self.link = 'http://bricklink.com' + link

    def __str__(self):
        output = '{part_id},{element_id},{qty},{price},"{name}",{link}\n'
        return output.format(**self.__dict__)
