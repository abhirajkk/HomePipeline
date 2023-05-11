import maya.cmds as mc


class AttrFn:
    def __init__(self):
        pass

    @classmethod
    def lock_attr(cls, node, attrs):
        if attrs:
            for att in attrs:
                mc.setAttr(f'{node}.{att}', lock=True, e=True)
                mc.setAttr(f'{node}.{att}', e=True, k=False, cb=False)

    @classmethod
    def unlock_attr(cls, node, value, attrs):
        if value:
            for att in attrs:
                mc.setAttr(f'{node}.{att}', lock=False, e=True, cb=True)

