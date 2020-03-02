class GEDError(Exception):
    def __init__(self, *args, **kwargs):
        pass


class LegalError(GEDError):
    def __init__(self, arg):
        self.args = arg


class PossibleError(GEDError):
    def __init__(self, arg):
        self.args = arg
