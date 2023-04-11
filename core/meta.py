

class Meta(type):
    def __new__(cls, *args, **kwargs):
        x = super().__new__(cls, *args, **kwargs)
        return x