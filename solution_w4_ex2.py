"""Descriptor that makes a value with a commission"""
class Value:
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value, commission):
        return value - value * commission

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        #print(instance.__dict__)
        commission = instance.__dict__['commission']
        self.value = self._prepare_value(value, commission)