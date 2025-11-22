from LRUCache import LRUCache

class LRUCacheDemo:
    @staticmethod
    def main():
        cache: LRUCache[str, int] = LRUCache(3)

        cache.put("1", 1)
        cache.put("2", 2)
        cache.put("3", 3)
        print(cache.get("1"))

        cache.put("4", 4)
        print(cache.get("2"))
        print(cache.get("3"))
        print(cache.get("4"))

if __name__ == "__main__":
    LRUCacheDemo.main()