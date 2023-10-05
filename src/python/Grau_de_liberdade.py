class Gl:
    def __init__(self, pos, known, axes, dt_value=None, force=0, fix=False):
        self.pos = pos
        self.axes = axes
        self.known = known
        self.dt_value = dt_value
        self.force = force
        self.fix = fix

    def __repr__(self):
        return f"{self.pos} {self.axes} {self.known}"
