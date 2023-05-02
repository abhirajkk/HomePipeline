import maya.cmds as mc


class AttrFn:
    def __init__(self):
        pass

    @classmethod
    def lock_attr(cls, node, value, attrs):
        if value:
            for att in attrs:
                mc.setAttr(f'{node}.{att}', lock=True, e=True)
                mc.setAttr(f'{node}.{att}', e=True, k=False, cb=False)

        else:
            for att in attrs:
                mc.setAttr(f'{node}.{att}', lock=False, e=True, cb=True)

    @classmethod
    def lock_translate(cls, node, value):
        if isinstance(value, bool):
            AttrFn.lock_attr(node, value, ['tx', 'ty', 'tz'])
        elif isinstance(value, list):
            AttrFn.lock_attr(node, value, value)
        else:
            pass
