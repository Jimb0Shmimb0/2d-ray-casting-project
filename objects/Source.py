from matplotlib import axes
import matplotlib.patches as patches
import constants
from .Object import Object


class Source(Object):

    def __init__(self, x1: float, y1: float, ax: axes.Axes):
        super().__init__(x1, y1, ax)

        self.detection_line_coordinates = [
            (x1 - constants.SOURCE_CIRCLE_RADIUS, y1, x1, y1 + constants.SOURCE_CIRCLE_RADIUS),
            (x1, y1 + constants.SOURCE_CIRCLE_RADIUS, x1 + constants.SOURCE_CIRCLE_RADIUS, y1),
            (x1 - constants.SOURCE_CIRCLE_RADIUS, y1, x1, y1 - constants.SOURCE_CIRCLE_RADIUS),
            (x1, y1 - constants.SOURCE_CIRCLE_RADIUS, x1 + constants.SOURCE_CIRCLE_RADIUS, y1)
        ]

        self.radius = constants.SOURCE_CIRCLE_RADIUS
        self.is_currently_a_sink = True
        self.sound_record_array = []

    def draw(self) -> None:
        self.ax.add_patch(patches.Circle((self.x1, self.y1), radius=constants.SOURCE_CIRCLE_RADIUS, fill=False, edgecolor='black', linewidth=2))
        for coord in self.detection_line_coordinates:
            x_start, y_start, x_end, y_end = coord
            self.ax.plot([x_start, x_end], [y_start, y_end], color='blue', linewidth=0.5)

