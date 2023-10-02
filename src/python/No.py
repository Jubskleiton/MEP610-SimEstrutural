class No:
    def __init__(self, pos, conhecido=(False, False), gl_dx=None, gl_dy=None):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.gl_x_conhecido = conhecido[0]
        self.gl_y_conhecido = conhecido[1]
        self.gl_conhecido = conhecido
        self.gl_dx = gl_dx
        self.gl_dy = gl_dy
