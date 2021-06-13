
import heapq

def meeting_rooms(meetings):

    meetings.sort(key=lambda x: x[0])
    print(meetings)
    meeting_ends = []
    max_rooms = 0

    for meeting in meetings:
        # The heap[0] element also returns the smallest element each time.
        while meeting_ends and meeting_ends[0] <= meeting[0]:
            heapq.heappop(meeting_ends)
        print(meeting_ends)
        heapq.heappush(meeting_ends, meeting[1])
        print(meeting_ends)
        max_rooms = max(max_rooms, len(meeting_ends))
    return max_rooms

# print(meeting_rooms([[0, 10], [10, 20]]))
# 1

print(meeting_rooms([[20, 30], [10, 21], [0, 50]]))
# 3