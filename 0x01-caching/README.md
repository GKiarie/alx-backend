0x01. Caching

************
Resources
***********
* https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29
* https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29
* https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29
* https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29
* https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29

Objectives
What a caching system is
What FIFO means
What LIFO means
What LRU means
What MRU means
What LFU means
What the purpose of a caching system
What limits a caching system have

************************
Note
Parent class BaseCaching
All your classes must inherit from BaseCaching
base_caching.py
*************************************************
******************
Tasks
******************
******************
0. Basic dictionary
********************
Create a class BasicCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
guillaume@ubuntu:~/0x01$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))

guillaume@ubuntu:~/0x01$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
guillaume@ubuntu:~/0x01$ 
Repo:

GitHub repository: alx-backend
Directory: 0x01-caching
File: 0-basic_cache.py


******************************
1. FIFO caching
******************************
Create a class FIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
guillaume@ubuntu:~/0x01$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
guillaume@ubuntu:~/0x01$ 
Repo:

GitHub repository: alx-backend
Directory: 0x01-caching
File: 1-fifo_cache.py


*****************************
2. LIFO Caching
*****************************
Create a class LIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
guillaume@ubuntu:~/0x01$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./2-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
guillaume@ubuntu:~/0x01$



**********************************
3. LRU Caching
*********************************
Create a class LRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least recently used item (LRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
guillaume@ubuntu:~/0x01$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
LRUCache = __import__('3-lru_cache').LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./3-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: B
Current cache:
C: Street
F: Mission
G: San Francisco
H: H
DISCARD: C
Current cache:
F: Mission
G: San Francisco
H: H
I: I
DISCARD: F
Current cache:
G: San Francisco
H: H
I: I
J: J
DISCARD: G
Current cache:
H: H
I: I
J: J
K: K
guillaume@ubuntu:~/0x01$ 
Repo:

GitHub repository: alx-backend
Directory: 0x01-caching
File: 3-lru_cache.py



***************************
4. MRU Caching
****************************
Create a class MRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
guillaume@ubuntu:~/0x01$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
MRUCache = __import__('4-mru_cache').MRUCache

my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./4-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: B
Current cache:
A: Hello
C: Holberton
D: School
E: Battery
Current cache:
A: Hello
C: Street
D: School
E: Battery
Hello
None
Street
DISCARD: C
Current cache:
A: Hello
D: School
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco
DISCARD: G
Current cache:
A: Hello
D: School
E: Battery
H: H
DISCARD: H
Current cache:
A: Hello
D: School
E: Battery
I: I
DISCARD: I
Current cache:
A: Hello
D: School
E: Battery
J: J
DISCARD: J
Current cache:
A: Hello
D: School
E: Battery
K: K
guillaume@ubuntu:~/0x01$ 
Repo:

GitHub repository: alx-backend
Directory: 0x01-caching
File: 4-mru_cache.py



**********************
5. LFU Caching
**********************
Create a class LFUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
guillaume@ubuntu:~/0x01$ cat 100-main.py
#!/usr/bin/python3
""" 100-main """
LFUCache = __import__('100-lfu_cache').LFUCache

my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./100-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: F
Current cache:
B: World
C: Street
G: San Francisco
H: H
DISCARD: G
Current cache:
B: World
C: Street
H: H
I: I
I
H
I
H
I
H
DISCARD: B
Current cache:
C: Street
H: H
I: I
J: J
DISCARD: J
Current cache:
C: Street
H: H
I: I
K: K
DISCARD: K
Current cache:
C: Street
H: H
I: I
L: L
DISCARD: L
Current cache:
C: Street
H: H
I: I
M: M
guillaume@ubuntu:~/0x01$ 
Repo:

GitHub repository: alx-backend
Directory: 0x01-caching
File: 100-lfu_cache.py


**************
End
**************



A caching system is a technology or mechanism used to store and manage frequently accessed data in a temporary and fast-access memory location, called a cache.

The primary purpose of a caching system is to improve the overall performance and efficiency of a computer system, software application, or website by reducing the need to fetch data from slower, long-term storage locations, such as disk drives or databases.

Caches work based on the principle of exploiting the locality of reference, which means that if data is accessed once, it is likely to be accessed again in the near future. By keeping a copy of frequently accessed data in a cache, subsequent requests for that data can be served much faster since it doesn't need to be fetched from the original data source.

Caching systems are commonly used in various computing scenarios, including:

1.Web Caching: In web applications, caching systems can store frequently accessed web pages, images, CSS, and other static assets to reduce the load time for users, resulting in a better user experience.

2.CPU Caches: Modern CPUs have multiple levels of caches (L1, L2, L3), which temporarily store frequently accessed data from main memory. This helps speed up CPU operations as accessing data from caches is faster than fetching it from RAM.

3.Database Caching: Database systems often utilize caching to store query results, frequently accessed data, or precomputed aggregations, reducing the need to repeatedly execute complex queries.

4.Content Delivery Networks (CDNs): CDNs use caching to replicate and serve content from servers located closer to end-users, reducing latency and improving content delivery performance.

5.Application-Level Caching: In software applications, caching can be used to store results of computationally expensive operations, reducing the need to recompute the same results repeatedly.

Caching systems need to be carefully managed to ensure that cached data remains consistent with the underlying data source. Strategies like cache expiration, cache eviction/replacement policies, and cache invalidation mechanisms are employed to handle data updates and changes appropriately.

Overall, caching systems play a crucial role in optimizing performance and response times in various computing environments, leading to improved efficiency and a better user experience.

******************************
Cache replacement policies 
******************************
Cache replacement policies dictate how a caching system decides which items to remove (evict) from the cache when new items need to be stored and the cache is full.

The choice of a cache replacement policy affects the cache's efficiency, hit rate, and overall performance. There are several common cache replacement policies:

1.First-In-First-Out (FIFO):
FIFO replaces the oldest item in the cache, based on the order in which items were added. It operates on the principle of discarding the item that has been in the cache for the longest time. However, FIFO may not always be a good choice, as it doesn't take into account how frequently or recently an item was accessed.

2.Last-In-First-Out (LIFO):
Using this algorithm the cache behaves in the same way as a stack and opposite way as a FIFO queue. The cache evicts the block added most recently first without any regard to how often or how many times it was accessed before.

3.Least Recently Used (LRU):
LRU replaces the least recently accessed item from the cache. It assumes that the items that have not been accessed for the longest time are the least likely to be accessed again soon. LRU is often considered a good choice when the access pattern exhibits temporal locality, meaning that recently accessed items are more likely to be accessed again in the near future.

4.Most Recently Used (MRU):
MRU replaces the most recently accessed item from the cache. It assumes that the items accessed most recently are more likely to be accessed again soon. MRU is suitable when the access pattern shows a high frequency of repeated accesses to the same items.

5.Least Frequently Used (LFU):
LFU replaces the item that has been accessed the least number of times. It assumes that items that are accessed less frequently are less likely to be needed in the future. LFU can work well in situations where there are some items that are heavily accessed and others that are rarely accessed.

6.Random Replacement:
Random replacement selects a random item from the cache to evict when space is needed. It is simple to implement and may perform reasonably well under certain circumstances. However, it may not be efficient for all types of access patterns and can lead to poor cache utilization.

7.Adaptive Replacement Cache (ARC):
ARC is a hybrid policy that combines aspects of LRU and LFU. It dynamically adjusts the cache size to better adapt to changing access patterns. It aims to strike a balance between recent and frequent accesses.

*******************************
Limits of a caching system
*******************************
While caching systems offer significant benefits in terms of performance and efficiency, they also have some limitations that need to be considered during their design and implementation. Here are some common limitations of caching systems:

Limited Cache Size: Caching systems have a finite amount of memory allocated for caching data. When the cache reaches its maximum capacity, it needs to evict some items to make room for new ones. Choosing an appropriate cache size is crucial as a cache that is too small may not provide significant performance improvements, while a cache that is too large may consume excessive memory resources.

Cache Invalidation and Data Consistency: Maintaining data consistency between the cache and the underlying data source can be challenging. When the original data changes, the cached data becomes stale. Implementing effective cache invalidation mechanisms or using time-based expiration policies is essential to ensure that the cached data remains up-to-date.

Cold Start Problem: When a caching system is initially empty or has just been restarted, it suffers from the "cold start" problem. During this phase, cache misses are prevalent, and the system may not immediately benefit from caching until the cache is warmed up by repeated accesses.

Eviction Policies: The choice of cache replacement policy can have a significant impact on cache performance. No single eviction policy is universally optimal for all scenarios, and choosing the right policy depends on the specific access patterns and workload.

Cache Thrashing: Cache thrashing occurs when the caching system frequently evicts and replaces items in the cache, resulting in a high rate of cache misses. This situation can lead to reduced cache efficiency and degraded overall performance.

Key Hotspots: In some cases, certain keys or items may be accessed much more frequently than others, leading to key hotspots. This can cause contention for cache space and disproportionately affect the cache performance.

Cache Coherency: In distributed systems with multiple cache instances or nodes, maintaining cache coherency becomes crucial. Ensuring that all cache copies have consistent data can be complex and may require additional coordination mechanisms.

Cache Wastage: Some items cached may be accessed only once or a few times before being evicted. This can lead to cache wastage, where the resources used for caching these short-lived items could have been better utilized for more frequently accessed data.

Memory Overhead: Caching systems require memory resources for maintaining cache metadata, eviction data structures, and other management overhead. This memory overhead should be considered when determining the cache size and the overall memory requirements of the system.