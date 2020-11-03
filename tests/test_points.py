from ResourcesImageProcessor.PointsOperations import PointsCollections


def test_points():
    collection = PointsCollections()
    collection.add_point(392, 65)
    collection.add_point(392, 65)
    collection.add_point(393, 65)
    collection.add_point(394, 65)
    collection.add_point(395, 65)

    assert collection.count_points() == 1

    collection.add_point(739, 65)
    collection.add_point(740, 65)
    collection.add_point(741, 65)
    collection.add_point(742, 65)

    assert collection.count_points() == 2

    collection.add_point(740, 65)
    collection.add_point(740, 66)
    collection.add_point(740, 67)
    collection.add_point(740, 67)

    assert collection.count_points() == 2

    collection.add_point(740, 231)
    collection.add_point(740, 232)
    collection.add_point(740, 233)
    collection.add_point(740, 234)
    collection.add_point(740, 235)
    collection.add_point(740, 236)
    collection.add_point(740, 237)

    assert collection.count_points() == 3

    collection.add_point(6, 236)
    collection.add_point(7, 236)
    collection.add_point(8, 236)
    collection.add_point(9, 236)
    collection.add_point(10, 236)
    collection.add_point(11, 236)
    collection.add_point(12, 236)

    assert collection.count_points() == 4

    collection.add_point(391, 66)
    collection.add_point(392, 66)
    collection.add_point(393, 66)
    collection.add_point(394, 66)
    collection.add_point(742, 66)
    collection.add_point(743, 66)
    collection.add_point(391, 67)
    collection.add_point(392, 67)
    collection.add_point(739, 67)
    collection.add_point(740, 67)
    collection.add_point(741, 67)
    collection.add_point(742, 67)
    collection.add_point(743, 67)
    collection.add_point(744, 67)
    collection.add_point(392, 68)
    collection.add_point(393, 68)
    collection.add_point(394, 68)
    collection.add_point(395, 68)
    collection.add_point(396, 68)
    collection.add_point(397, 68)

    assert collection.count_points() == 4
