class Gl:
    def __init__(self, pos, known, axes, dt_value=None, force=0, force_known=False, fix=False):
        self.pos = float(pos)
        self.axes = axes
        self.known = known
        self.dt_value = float(dt_value) if not isinstance(dt_value, type(None)) else None
        self.force = force
        self.force_known = force_known
        self.fix = fix

    def __repr__(self):
        return f"{self.pos} {self.axes} {self.known}"
