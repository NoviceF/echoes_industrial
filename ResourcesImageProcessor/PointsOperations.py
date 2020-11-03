import math


class PointsCollections:
    def __init__(self):
        self._pointsByX = dict()

    def add_point(self, x, y):
        if x not in self._pointsByX:
            self._pointsByX[x] = list()

        if y not in self._pointsByX[x]:
            self._pointsByX[x].append(y)

    def count_points(self):
        if not self._pointsByX:
            return 0

        threshold = 10

        iterator = iter(self._pointsByX.items())

        result_points = list()

        last_pointX, last_pointY = next(iterator)
        result_points.append((last_pointX, last_pointY[0]))

        for pointX, pointY in iterator:
            pointY = pointY[-1]
            last_pointX = result_points[-1][0]
            last_pointY = result_points[-1][1]

            if (math.fabs(pointX - last_pointX) > threshold or
                    math.fabs(pointY - last_pointY) > threshold):

                if self.is_point_already_saved(
                        pointX, pointY, result_points, threshold):
                    continue

                result_points.append((pointX, pointY))

        return len(result_points)

    def is_point_already_saved(self, pointX, pointY, result_points, threshold):
        for x, y in result_points:
            if (math.fabs(x - pointX) < threshold and
                    math.fabs(y - pointY) < threshold):
                return True

        return False


