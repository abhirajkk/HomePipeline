from dataclasses import dataclass, field


@dataclass(order=True)
class DataClass:
    color: int
    side: str
    part: str
    component: str
    module: str

