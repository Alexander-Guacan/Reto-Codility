import big_o
import math

class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

def compute_slope(point_A: Point2D, point_B: Point2D) -> float:
    return (point_B.y - point_A.y) / (point_B.x - point_A.x)

def compute_angle(start: Point2D, middle: Point2D, end: Point2D) -> float:
    try:
        slope_start_middle = compute_slope(start, middle)
    except ZeroDivisionError:
        try:
            slope_middle_end = compute_slope(middle, end)
            if start.y >= end.y:
                return 360 - (90 - (math.atan(slope_middle_end) * (180 / math.pi)))
            else:
                return 90 + (math.atan(slope_middle_end) * (180 / math.pi))
        except ZeroDivisionError:
            return 180

    try:
        slope_middle_end = compute_slope(middle, end)
        return math.atan((slope_middle_end - slope_start_middle) / (1 + (slope_middle_end * slope_start_middle))) * (180 / math.pi)
    except ZeroDivisionError:
        return 90 - math.atan(slope_start_middle) * (180 / math.pi)

def polygon_concavity_index(polygon: list[Point2D]) -> int:
    if len(polygon) < 3:
        return -1

    middle = 1
    end = 2

    for start in range(len(polygon)):
        angle = compute_angle(polygon[start], polygon[middle], polygon[end])
        print(start, middle, end, angle)

        if angle > 180:
            return middle

        middle = 0 if middle >= len(polygon) - 1 else middle + 1
        end = 0 if end >= len(polygon) - 1 else end + 1
    
    return -1

def test(polygon : list[Point2D]) -> None:
    # Prints the parameter to test
    print(f"Array of test: {polygon}")
    # Prints the returns of function
    print(f"Index = {polygon_concavity_index(polygon)}")

def main() -> None:
    # Testing polygon_concavity_index function
    # test([Point2D(-1, 3), Point2D(1, 2), Point2D(3, 1), Point2D(0, -1), Point2D(-2, 1)])
    # test([Point2D(-1, 3), Point2D(1, 2), Point2D(1, 1), Point2D(3, 2), Point2D(0, -1), Point2D(-2, 1), Point2D(-1, 2)])
    # test([Point2D(7, 4), Point2D(8, 2), Point2D(6, 1), Point2D(6, 3)])
    # test([1, 2, 3, 4]) # Tree with height = 1
    # test([]) # Empty array

    # # Computes algorithmic complexity of polygon_concavity_index function with the worst case specified in the 'codility' exercise
    # tree_sample = lambda n : big_o.datagen.integers(1000, -(sys.maxsize - 1), sys.maxsize)
    # best, others = big_o.big_o(polygon_concavity_index, tree_sample)

    # # Prints algorithmic complexity
    # print("Algorithmic complexity")
    # print(best)

    print(math.tan(math.pi / 2))

if __name__ == "__main__":
    main()