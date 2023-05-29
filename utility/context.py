from functools import wraps
from maya import cmds


def undo(func):
    """ Puts the wrapped `func` into a single Maya Undo action, then
        undoes it when the function enters the finally: block """
    @wraps(func)
    def _undofunc(*args, **kwargs):
        try:
            # start an undo chunk
            cmds.undoInfo(ock=True)
            return func(*args, **kwargs)
        finally:
            # after calling the func, end the undo chunk and undo
            cmds.undoInfo(cck=True)
            cmds.undo()

    return _undofunc