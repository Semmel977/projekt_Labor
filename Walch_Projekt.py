class row():
    def __init__(self):
        self.points = ["empty","empty","empty"]
    
    def change_point(self, point, new_value):
        self.points[point] = new_value

class board():
    def __init__(self):
        self.points = []
        for i in range(24):
            self.points.append("empty")
        self.rows = {"top_top":row(),
                     "top_mid":row(),
                     "top_bottom":row(),
                     "top_out":row(),
                     "left_left":row(),
                     "left_mid":row(),
                     "left_right":row(),
                     "left_out":row(),
                     "bottom_top":row(),
                     "bottom_mid":row(),
                     "bottom_bottom":row(),
                     "bottom_out":row(),
                     "right_left":row(),
                     "right_mid":row(),
                     "right_right":row(),
                     "right_out":row()}
        self.points_dict = {
            0: [["top_top", 0], "left_left"],
            1: ["top_top", "top_out"],
            2: ["top_top", "right_right"],
            3: ["left_mid", "top_mid"],
            4: ["top_mid", "top_out"],
            5: ["right_mid", "top_mid"],
            6: ["left_right", "top_bottom"],
            7: ["top_bottom", "top_out"],
            8: ["top_bottom", "right_left"],
            9: ["left_left", "left_out"],
            10: ["left_mid", "left_out"],
            11: ["left_right", "left_out"],
            12: ["right_"]
        }                 