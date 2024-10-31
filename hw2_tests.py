import data
from data import Point, Rectangle, Duration, Song
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        point1 = data.Point(3, 3)
        point2 = data.Point(10, 10)
        rectangle = hw2.create_rectangle(point1, point2)
        self.assertEqual(rectangle.top_left.x, 3)
        self.assertEqual(rectangle.top_left.y, 10)
        self.assertEqual(rectangle.bottom_right.x, 10)
        self.assertEqual(rectangle.bottom_right.y, 3)

    # Part 2
    def test_shorter_duration_than1(self):
        d1 = Duration(3, 30, 0)
        d2 = Duration(4,0, 0)
        self.assertTrue(hw2.shorter_duration_than(d1, d2))
        self.assertFalse(hw2.shorter_duration_than(d2, d1))

    # Part 3
    def setUp(self):
        self.song1 = Song("Artist1", "Song A", 0), Duration(0,180, 0)
        self.song2 = Song("Artist2", "Song B", 0), Duration(0,270, 0)
        self.song3 = Song("Artist3", "Song C", 0), Duration(0,135, 0)
        self.songs = [self.song1, self.song2, self.song3]

    def test_songs_shorter_than(self):
        max_duration = Duration(0,210, 0)
        result =hw2.songs_shorter_than(self.songs, max_duration)
        self.assertEqual(result, [self.song1, self.song3])

    def test_no_songs_shorter_than2(self):
        max_duration = Duration(0, 130, 0)
        result = hw2.songs_shorter_than(self.songs, max_duration)
        self.assertEqual(result, [])

    # Part 4
    def setUp(self):
        self.song1 = Song("Artist1", "Song A"), Duration(0,180, 0)
        self.song2 = Song("Artist2", "Song B"), Duration(0,270, 0)
        self.song3 = Song("Artist3", "Song C"), Duration(0,135, 0)
        self.songs = [self.song1, self.song2, self.song3]

    def test_running_time1(self):
        playlist = [0,2,1,0]
        total_time = hw2.running_time(self.songs, playlist)
        self.assertEqual(total_time, Duration(12,45, 0))

    def test_running_time2(self):
        playlist = [0,3,-1,1]
        total_time = hw2.running_time(self.songs,playlist)
        self.assertEqual(total_time, Duration(11,15, 0))
    # Part 5
    def test_validate_route1(self):
        city_links = [['san luis obispo', 'santa maria'], ['san luis obispo', 'pismo beach'],
                                                           ['atascadero', 'santa maria'], ['atascadero', 'creston']]
        valid_route = ['san luis obsipo', 'santa maria', 'atascadero']
        invalid_route = ['san luis obispo','atascadero']
        self.assertFalse(hw2.validate_route(city_links, valid_route))
        self.assertFalse(hw2.validate_route(city_links, invalid_route))


    # Part 6
    def test_longest_repetition1(self):
        self.assertEqual(hw2.longest_repetition([3,3,3,2,2,2,3]), 0)


    def test_longest_repetition2(self):
        self.assertIsNone(hw2.longest_repetition([]))




if __name__ == '__main__':
    unittest.main()
