import data
from typing import List, Optional
from data import Point, Rectangle,Duration, Song
# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1:Point, point2:Point) -> Rectangle:
    top_left_x = min(point1.x, point2.x)
    top_left_y = max(point1.y, point2.y)

    bottom_right_x = max(point1.x, point2.x)
    bottom_right_y = min(point1.y, point2.y)

    return Rectangle(Point(top_left_x, top_left_y), Point(bottom_right_x, bottom_right_y))

# Part 2
def shorter_duration_than(d1:Duration, d2:Duration) -> bool:
    total_seconds1 = d1.minutes * 60 + d1.seconds
    total_seconds2 = d2.minutes * 60 + d2.seconds

    return total_seconds1 < total_seconds2

# Part 3
def songs_shorter_than(songs:list[Song], max_duration:Duration) -> list[Song]:
    return [song for song in songs if song.duration.total_seconds() < max_duration.total_seconds()]


# Part 4
def running_time(songs:list[Song], playlist:list[int]) -> Duration:
    total_seconds = 0
    for idx in playlist:
        if 0 <= idx < len(songs):
            total_seconds += songs[idx].duration.total_seconds()
    minutes, seconds = divmod(total_seconds, 60)
    return Duration(minutes, seconds)
# Part 5
def validate_route(city_links:list[list[str]], route:list[str]) -> bool:
    if len(route) <=1:
        return True
    for i in range(len(route) - 1):
        if not any(route[i] in link and route[i + 1] in link for link in city_links):
            return False
    return True

# Part 6
def longest_repetition(nums:list[int]) -> Optional[int]:
    if not nums:
        return None
    max_index = 0
    max_length = 1
    current_length = 1
    current_index = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i -1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_index = current_index
            current_length = 1
            current_index = i
    if current_length > max_length:
        max_index = current_index
    return max_index if max_length > 1 else None
