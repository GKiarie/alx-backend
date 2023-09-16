0x00. Pagination
**************************
Resources
**************************
* https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination
* https://en.wikipedia.org/wiki/HATEOAS

*****************
Objectives
*****************
How to paginate a dataset with simple page and page_size parameters
How to paginate a dataset with hypermedia metadata
How to paginate in a deletion-resilient manner

********************
Popular_Baby_Names.csv
***********************

Paginating a dataset involves breaking the data into smaller, manageable chunks or pages to make it easier to display or process. It is commonly used in web applications to handle large datasets and display them in a user-friendly manner, showing a limited number of items per page.

The two main parameters for pagination are:
page: The page number that the user wants to view. It represents which page of data to retrieve. Page numbers are typically 1-indexed, meaning the first page is page 1.

page_size: The number of items or records to display per page. It determines how many items will be shown on each page.

To paginate a dataset using these parameters, you can follow these steps:

1.Calculate Start and End Indexes:

First, calculate the start index for the current page using the formula (page - 1) * page_size.
Next, calculate the end index using the formula start_index + page_size.

2.Slice the Dataset:

Once you have the start and end indexes, you can use them to extract the relevant portion of the dataset for the current page. This can be achieved using list slicing in Python.

3.Display the Paginated Data:

Display the extracted data to the user. This could involve showing the data in a table, list, or any other suitable format.

4.Handle Out-of-Range Pages:

It's essential to handle cases where the user requests a page number that is out of range for the dataset. In such cases, return an empty list or an appropriate message indicating that the page is not available.

def paginate_dataset(dataset, page, page_size):
    total_items = len(dataset)
    total_pages = math.ceil(total_items / page_size)

    if page < 1 or page > total_pages:
        return []  # Page is out of range, return an empty list

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return dataset[start_index:end_index]

In this example, dataset is the entire dataset you want to paginate. The function calculates the total number of items and the total number of pages using len() and math.ceil() functions, respectively.

The function then checks if the requested page is within a valid range (between 1 and total_pages). If the requested page is out of range, it returns an empty list.

Otherwise, it calculates the start and end indexes for the current page and returns the appropriate slice of the dataset containing the items for that page.

Remember that the pagination logic may vary depending on the specifics of your application, such as the data source, framework used, or specific user interface requirements. The provided example serves as a general guideline for implementing pagination with simple page and page_size parameters.


*****************************************************
How to paginate a dataset with hypermedia metadata
*****************************************************
When paginating a dataset with hypermedia metadata, we add additional information to the paginated results that provide links or references to other related pages in the dataset. This allows clients to navigate through the paginated data efficiently, following the hypermedia links provided.

The process of paginating a dataset with hypermedia metadata involves the following steps:

Calculate Start and End Indexes:

Calculate the start and end indexes of the current page using the same approach as in the simple pagination method (using (page - 1) * page_size and start_index + page_size).
Slice the Dataset and Extract Metadata:

Slice the dataset to get the paginated data for the current page, just like in the simple pagination method.
Additionally, generate hypermedia metadata that includes links or references to other pages, such as the first page, last page, next page, previous page, etc.
Include Hypermedia Metadata in the Response:

Include both the paginated data and the hypermedia metadata in the response to the client.
Handle Out-of-Range Pages:

As in the simple pagination method, handle cases where the user requests a page number that is out of range for the dataset. In such cases, return an empty list or an appropriate message.
Here's an example of a paginated dataset with hypermedia metadata using Python:

import math

def paginate_dataset_with_metadata(dataset, page, page_size):
    total_items = len(dataset)
    total_pages = math.ceil(total_items / page_size)

    if page < 1 or page > total_pages:
        return {"data": [], "metadata": {"total_pages": total_pages}}, 404

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paginated_data = dataset[start_index:end_index]

    metadata = {
        "total_pages": total_pages,
        "current_page": page,
        "next_page": page + 1 if page < total_pages else None,
        "prev_page": page - 1 if page > 1 else None,
        "first_page": 1,
        "last_page": total_pages
    }

    return {"data": paginated_data, "metadata": metadata}, 200

In this example, the paginate_dataset_with_metadata function returns a dictionary containing both the paginated data and the hypermedia metadata. The metadata includes the total number of pages, the current page, links to the next and previous pages, and links to the first and last pages.

The status code is also included in the response (e.g., 200 for success and 404 for an out-of-range page).

By providing hypermedia metadata, the client can navigate through the paginated data more efficiently. For example, if the client wants to access the next page, it can follow the link provided in the "next_page" field in the metadata rather than manually calculating the next page number. Similarly, the client can use the links for the first, last, and previous pages.

Paginating datasets with hypermedia metadata is a more powerful and flexible approach that enables clients to interact with the paginated data in a standardized and intuitive way, following hyperlinks to navigate through the results.

*************************************************
How to paginate in a deletion-resilient manner
*************************************************
Paginating in a deletion-resilient manner means handling situations where data is being deleted from the dataset while paginating without causing any inconsistencies or missing data in the paginated results. When data is deleted from the original dataset, the pagination mechanism should adapt to ensure that pages remain consistent and accurate.

To achieve deletion-resilient pagination, you can follow these steps:

1.Obtain a Stable Dataset Snapshot:

Before initiating the pagination process, obtain a stable snapshot of the dataset. This snapshot will serve as the basis for paginating without being affected by any concurrent deletions.

2.Calculate Total Pages and Adjust Page Number:

Use the stable dataset snapshot to calculate the total number of pages using the same formula as before (math.ceil(total_items / page_size)).
When calculating the total number of pages, ensure that you base it on the total number of items in the stable dataset snapshot rather than the original dataset, as the original dataset may change during pagination.

3.Handle Deletions While Paginating:

As you paginate through the data, check if the current page's data still exists in the stable dataset snapshot.
If an item has been deleted from the original dataset but is still present in the stable snapshot, skip it during pagination to avoid inconsistencies.

4.Adjust Pagination if Items are Deleted:

If an item is deleted from the dataset while paginating, and the deleted item was on the current page being fetched, adjust the pagination accordingly.
If the deleted item was on the last page, reduce the total number of pages by one.
If the deleted item was on a page before the last one, keep the total number of pages unchanged, but adjust the contents of the last page accordingly.
By following these steps, your pagination mechanism can handle deletions in a resilient manner and ensure that paginated results remain consistent even if data is being deleted from the dataset concurrently.

Keep in mind that implementing deletion-resilient pagination can be more complex and may involve trade-offs in terms of performance and resource utilization. It's essential to carefully design and test the pagination mechanism to ensure it works effectively in your specific use case. Additionally, consider using appropriate locking mechanisms or concurrency control techniques if the dataset is frequently updated during pagination to avoid data inconsistencies.

Let's demonstrate an example of paginating in a deletion-resilient manner using Python. We'll create a function that performs deletion-resilient pagination on a list of data. For this example, we'll simulate data deletions randomly during the pagination process.

import random
import math

def paginate_deletion_resilient(data, page, page_size):
    total_items = len(data)
    total_pages = math.ceil(total_items / page_size)

    # Adjust the page number if it's out of range
    page = max(min(page, total_pages), 1)

    # Create a stable snapshot of the original data
    stable_snapshot = data.copy()

    # Simulate random deletions from the original data during pagination
    for _ in range(random.randint(1, 3)):
        if stable_snapshot:
            deleted_item = random.choice(stable_snapshot)
            stable_snapshot.remove(deleted_item)

    # Calculate the start and end indexes for the current page
    start_index = (page - 1) * page_size
    end_index = min(start_index + page_size, len(stable_snapshot))

    # Return the paginated data and metadata
    paginated_data = stable_snapshot[start_index:end_index]
    metadata = {
        "total_pages": total_pages,
        "current_page": page,
        "next_page": page + 1 if page < total_pages else None,
        "prev_page": page - 1 if page > 1 else None,
        "first_page": 1,
        "last_page": total_pages
    }

    return paginated_data, metadata

# Example usage
data = [i for i in range(1, 101)]  # Sample data from 1 to 100
page_number = 3
page_size = 10

paginated_data, metadata = paginate_deletion_resilient(data, page_number, page_size)

print(f"Page {metadata['current_page']} of {metadata['total_pages']}: {paginated_data}")
print(f"Next Page: {metadata['next_page']}, Previous Page: {metadata['prev_page']}")

In this example, we first create a sample dataset (data) containing numbers from 1 to 100. We then use the paginate_deletion_resilient function to perform deletion-resilient pagination.

Inside the function, we calculate the total number of pages based on the initial length of the data (total_items). We then adjust the requested page number to ensure it falls within the valid range.

Next, we create a stable snapshot of the original data (stable_snapshot). We simulate random deletions from the stable_snapshot to mimic data deletions during the pagination process.

Finally, we calculate the start and end indexes for the current page, taking into account the length of the stable_snapshot. We return the paginated data for the current page along with metadata containing information about the total number of pages and links to the next and previous pages.

Please note that this example is a simplified simulation to demonstrate the concept of deletion-resilient pagination. In real-world scenarios, you may need to consider more sophisticated approaches to handle concurrent modifications and ensure data consistency during pagination.


************************
Tasks
************************
************************
0. Simple helper function
**************************
Write a function named index_range that takes two integer arguments page and page_size.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

bob@dylan:~$ ./0-main.py
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
bob@dylan:~$
Repo:

GitHub repository: alx-backend
Directory: 0x00-pagination
File: 0-simple_helper_function.py


*************************************
1. Simple pagination
*************************************
Copy index_range from the previous task and the following class into your code

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass
Implement a method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.

You have to use this CSV file (same as the one presented at the top of the project)
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
If the input arguments are out of range for the dataset, an empty list should be returned.
bob@dylan:~$  wc -l Popular_Baby_Names.csv 
19419 Popular_Baby_Names.csv
bob@dylan:~$  
bob@dylan:~$ head Popular_Baby_Names.csv
Year of Birth,Gender,Ethnicity,Child's First Name,Count,Rank
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Olivia,172,1
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Chloe,112,2
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sophia,104,3
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emma,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emily,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Mia,79,5
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Charlotte,59,6
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sarah,57,7
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Isabella,56,8
bob@dylan:~$  
bob@dylan:~$  cat 1-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('1-simple_pagination').Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")


print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))

bob@dylan:~$ 
bob@dylan:~$ ./1-main.py
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3']]
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']]
[]
bob@dylan:~$ 
Repo:

GitHub repository: alx-backend
Directory: 0x00-pagination
File: 1-simple_pagination.py


**********************************
2. Hypermedia pagination
**********************************
Replicate code from the previous task.

Implement a get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

You can use the math module if necessary.

bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('2-hypermedia_pagination').Server

server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))

bob@dylan:~$ 
bob@dylan:~$ ./2-main.py
{'page_size': 2, 'page': 1, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2']], 'next_page': 2, 'prev_page': None, 'total_pages': 9709}
---
{'page_size': 2, 'page': 2, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4']], 'next_page': 3, 'prev_page': 1, 'total_pages': 9709}
---
{'page_size': 3, 'page': 100, 'data': [['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Londyn', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Amirah', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'McKenzie', '14', '39']], 'next_page': 101, 'prev_page': 99, 'total_pages': 6473}
---
{'page_size': 0, 'page': 3000, 'data': [], 'next_page': None, 'prev_page': 2999, 'total_pages': 195}
bob@dylan:~$ 
Repo:

GitHub repository: alx-backend
Directory: 0x00-pagination
File: 2-hypermedia_pagination.py


*********************************************
3. Deletion-resilient hypermedia pagination
*********************************************
The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.

Start 3-hypermedia_del_pagination.py with this code:

#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
            pass
Implement a get_hyper_index method with two integer arguments: index with a None default value and page_size with default value of 10.

The method should return a dictionary with the following key-value pairs:
index: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with page_size 20, and no data was removed from the dataset, the current index should be 60.
next_index: the next index to query with. That should be the index of the first item after the last item on the current page.
page_size: the current page size
data: the actual page of the dataset
Requirements/Behavior:

Use assert to verify that index is in a valid range.
If the user queries index 0, page_size 10, they will get rows indexed 0 to 9 included.
If they request the next index (10) with page_size 10, but rows 3, 6 and 7 were deleted, the user should still receive rows indexed 10 to 19 included.
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

server.indexed_dataset()

try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")        


index = 3
page_size = 2

print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 1- request first index
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next index
print(server.get_hyper_index(res.get('next_index'), page_size))

# 3- remove the first index
del server._Server__indexed_dataset[res.get('index')]
print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 4- request again the initial index -> the first data retreives is not the same as the first request
print(server.get_hyper_index(index, page_size))

# 5- request again initial next index -> same data page as the request 2-
print(server.get_hyper_index(res.get('next_index'), page_size))

bob@dylan:~$ 
bob@dylan:~$ ./3-main.py
AssertionError raised when out of range
Nb items: 19418
{'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4']], 'page_size': 2, 'next_index': 5}
{'index': 5, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']], 'page_size': 2, 'next_index': 7}
Nb items: 19417
{'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']], 'page_size': 2, 'next_index': 6}
{'index': 5, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']], 'page_size': 2, 'next_index': 7}
bob@dylan:~$ 
Repo:

GitHub repository: alx-backend
Directory: 0x00-pagination
File: 3-hypermedia_del_pagination.py


**************
END
**************