from dataclasses import dataclass, field


@dataclass(order=True)
class DataClass:
    name: str
    component: str
    module: str
    color: int = field(default=0)
    side: str = field(default="M")
    control_hierarchy: list = field(default=('zero', 'offset', 'ctrl'))
    lock_visibility: bool = field(default=False)
    lock_translate: bool = field(default=True)
    lock_rotate: bool = field(default=True)
    lock_scale: bool = field(default=True)
    module_hierarchy: list = field(default=('inputs', 'outputs', 'controls', 'deform'))
    nodes: dict = field(default=())
    guide: list = field(default=())
    bind: list = field(default=())
    controls: list = field(default=())
    inputs: list = field(default=())
    outputs: list = field(default=())

    def __post_init__(self):
        pass



