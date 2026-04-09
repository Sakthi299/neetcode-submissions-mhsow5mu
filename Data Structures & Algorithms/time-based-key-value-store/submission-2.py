class TimeMap:

    def __init__(self):
        self.valuemap = {} # dict contains key - [[value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # all set calls will be strictly incresing order, 
        # then its already sorted
        if key not in self.valuemap:
            self.valuemap[key] = []
        self.valuemap[key].append([value, timestamp])

        print(self.valuemap)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.valuemap.get(key, [])
        if values:
            l, r = 0, len(values)-1

            while l <= r:
                mid = l+(r-l)//2

                if values[mid][1] <= timestamp:
                    res = values[mid][0]
                    l = mid + 1
                elif values[mid][1] > timestamp:
                    r = mid - 1

        return res

        
