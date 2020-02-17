class GEDError(ValueError):
    def __init__(self, arg):
        self.args = arg


class LegalError(GEDError):
    def __init__(self, arg):
        self.args = arg


