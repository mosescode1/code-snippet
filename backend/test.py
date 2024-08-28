from api import code_app, db
from api.models.models import User, Snippet

code_app.app_context().push()
db.drop_all()
db.create_all()

user1 = User("JohnDoe", "johndoe", "password123",
             email="johndoe@example.com")
user1.hash_password("password123")
user1.save()

user2 = User("JaneSmith", "janesmith", "securepass456",
             email="janesmith@example.com")
user2.hash_password("securepass456")
user2.save()

user3 = User("MikeBrown", "mikebrown", "mikepass789",
             email="mikebrown@example.com")
user3.hash_password("mikepass789")
user3.save()

user4 = User("EmilyDavis", "emilydavis", "emilysecure101",
             email="emilydavis@example.com")
user4.hash_password("emilysecure101")
user4.save()

user5 = User("ChrisJohnson", "chrisjohnson", "chrispass202",
             email="chrisjohnson@example.com")
user5.hash_password("chrispass202")
user5.save()

user6 = User("SarahMiller", "sarahmiller", "sarahpass303",
             email="sarahmiller@example.com")
user6.hash_password("sarahpass303")
user6.save()

user7 = User("DavidWilson", "davidwilson", "davidpass404",
             email="davidwilson@example.com")
user7.hash_password("davidpass404")
user7.save()

user8 = User("LauraMartinez", "lauramartinez", "laurapass505",
             email="lauramartinez@example.com")
user8.hash_password("laurapass505")
user8.save()

user9 = User("JamesLee", "jameslee", "jamespass606",
             email="jameslee@example.com")
user9.hash_password("jamespass606")
user9.save()

user10 = User("AnnaGarcia", "annagarcia", "annapass707",
              email="annagarcia@example.com")
user10.hash_password("annapass707")
user10.save()


snippet1_1 = Snippet("Python", """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
""", user_id=1)

snippet1_2 = Snippet("Python", """
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0
""", user_id=1)

snippet1_3 = Snippet("Python", """
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
""", user_id=1)

snippet1_4 = Snippet("Python", """
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
""", user_id=1)

snippet1_5 = Snippet("Python", """
import random

def generate_random_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = "".join(random.choice(characters) for _ in range(length))
    return password
""", user_id=1)


snippet2_1 = Snippet("JavaScript", """
                     class Calculator {
                         add(a, b) {
                             return a + b
                         }

                         subtract(a, b) {
                             return a - b
                         }

                         multiply(a, b) {
                             return a * b
                         }

                         divide(a, b) {
                             if (b == = 0) {
                                 throw new Error("Division by zero")
                             }
                             return a / b
                         }
                     }
    """, user_id=2)

snippet2_2 = Snippet("JavaScript", """
                     function debounce(func, wait) {
                         let timeout
                         return function(...args) {
                             const context = this
                             clearTimeout(timeout)
                             timeout= setTimeout(() = > func.apply(context, args), wait)
                         }
                     }
    """, user_id=2)

snippet2_3 = Snippet("JavaScript", """
                     const fetchData=async (url)=> {
                         try {
                             const response = await fetch(url)
                             if (!response.ok) {
                                 throw new Error('Network response was not ok')
                             }
                             const data = await response.json()
                             return data
                         } catch(error) {
                             console.error(
                                 'There has been a problem with your fetch operation:', error)
                         }
                     }
    """, user_id=2)

snippet2_4 = Snippet("JavaScript", """
                     class Person {
                         constructor(firstName, lastName) {
                             this.firstName= firstName
                             this.lastName= lastName
                         }

                         getFullName() {
                             return `\${this.firstName} \${this.lastName}\`
                         }
                     }

                     const john=new Person('John', 'Doe')
                     console.log(john.getFullName())
    """, user_id=2)

snippet2_5 = Snippet("JavaScript", """
                     const throttle=(func, limit)= > {
                         let inThrottle
                         return function() {
                             const args= arguments
                             const context= this
                             if (!inThrottle) {
                                 func.apply(context, args)
                                 inThrottle= true
                                 setTimeout(()=> inThrottle = false, limit)
                             }
                         }
                     }
    """, user_id=2)


snippet3_1 = Snippet("HTML", """
                     <!DOCTYPE html >
                     < html lang="en" >
                     < head >
                     < meta charset="UTF-8" >
                     < meta name="viewport" content="width=device-width, initial-scale=1.0" >
                     < title > Simple Form < /title >
                     < / head >
                     < body >
                     < h1 > Contact Us < /h1 >
                     < form action="/submit" method="POST" >
                     < label for ="name" > Name: < /label >
                     < input type="text" id="name" name="name" > <br > <br >
                     < label for ="email" > Email: < /label >
                     < input type="email" id="email" name="email" > <br > <br >
                     < label for ="message" > Message: < /label > <br >
                     < textarea id="message" name="message" rows="4" cols="50" > </textarea > <br > <br >
                     < input type="submit" value="Submit" >
                     < / form >
                     < / body >
                     < / html > """, user_id=3)

snippet3_2 = Snippet("HTML", """
                     <!DOCTYPE html >
                     < html lang="en" >
                     < head >
                     < meta charset="UTF-8" >
                     < meta name="viewport" content="width=device-width, initial-scale=1.0" >
                     < title > Product List < /title >
                     < / head >
                     < body >
                     < h1 > Our Products < /h1 >
                     < ul >
                     < li > Product A < /li >
                     < li > Product B < /li >
                     < li > Product C < /li >
                     < / ul >
                     < / body >
                     < / html > """, user_id=3)

snippet3_3 = Snippet("HTML", """
                     <!DOCTYPE html >
                     < html lang="en" >
                     < head >
                     < meta charset="UTF-8" >
                     < meta name="viewport" content="width=device-width, initial-scale=1.0" >
                     < title > Login Page < /title >
                     < / head >
                     < body >
                     < h1 > Login < /h1 >
                     < form action="/login" method="POST" >
                     < label for ="username" > Username: < /label >
                     < input type="text" id="username" name="username" > <br > <br >
                     < label for ="password" > Password: < /label >
                     < input type="password" id="password" name="password" > <br > <br >
                     < input type="submit" value="Login" >
                     < / form >
                     < / body >
                     < / html > """, user_id=3)

snippet3_4 = Snippet("HTML", """
                     <!DOCTYPE html >
                     < html lang="en" >
                     < head >
                     < meta charset="UTF-8" >
                     < meta name="viewport" content="width=device-width, initial-scale=1.0" >
                     < title > Profile Card < /title >
                     < / head >
                     < body >
                     < div class ="profile-card" >
                     < img src="profile.jpg" alt="Profile Picture" >
                     < h2 > John Doe < /h2 >
                     < p > Web Developer < /p >
                     < p > Lorem ipsum dolor sit amet, consectetur adipiscing elit. < /p >
                     < / div >
                     < / body >
                     < / html > """, user_id=3)

snippet3_5 = Snippet("HTML", """
                     <!DOCTYPE html >
                     < html lang="en" >
                     < head >
                     < meta charset="UTF-8" >
                     < meta name="viewport" content="width=device-width, initial-scale=1.0" >
                     < title > Responsive Navbar < /title >
                     < style >
                     .navbar {
                         display: flex
                         background-color:  # 333;
                         justify-content: space-around
                         padding: 1rem
                     }

                     .navbar a {
                         color: white
                         text-decoration: none
                         padding: 14px 20px
                     }

                     .navbar a: hover {
                         background-color:  # ddd;
                         color: black
                     }
                     < /style >
                     < / head >
                     < body >
                     < div class ="navbar" >
                     < a href="#home" > Home < /a >
                     < a href="#about" > About < /a >
                     < a href="#services" > Services < /a >
                     < a href="#contact" > Contact < /a >
                     < / div >
                     < / body >
                     < / html > """, user_id=3)

snippet4_1 = Snippet("CSS", """
                     body {
                         font-family: Arial, sans-serif
                         margin: 0
                         padding: 0
                         background-color:  # f4f4f4;
                     }

                     h1 {
                         color:  # 333;
                         text-align: center
                         padding: 20px
                     }
                     """, user_id=4)

snippet4_2 = Snippet("CSS", """
                     .container {
                         width: 80 %
                         margin: 0 auto
                         background-color:  # fff;
                         padding: 20px
                         box-shadow: 0 0 10px rgba(0, 0, 0, 0.1)
                     }

                     .container p {
                         line-height: 1.6
                         color:  # 666;
                     }
    """, user_id=4)

snippet4_3 = Snippet("CSS", """
                     button {
                         background-color:  # 4CAF50;
                         color: white
                         padding: 15px 20px
                         border: none
                         cursor: pointer
                     }

                     button: hover {
                         background-color:  # 45a049;
                     }
                     """, user_id=4)

snippet4_4 = Snippet("CSS", """
                     .navbar {
                         overflow: hidden
                         background-color:  # 333;
                     }

                     .navbar a {
                         float: left
                         display: block
                         color:  # f2f2f2;
                         text-align: center
                         padding: 14px 16px
                         text-decoration: none
                     }

                     .navbar a: hover {
                         background-color:  # ddd;
                         color: black
                     }
                     """, user_id=4)

snippet4_5 = Snippet("CSS", """
                     @ media screen and (max-width: 600px) {
                         .navbar a {
                             float: none
                             display: block
                             text-align: left
                         }
                     }
    """, user_id=4)

snippet5_1 = Snippet("Python", """
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self, data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            last_node=self.head
            while last_node.next:
                last_node=last_node.next
            last_node.next=new_node

    def print_list(self):
        current_node=self.head
        while current_node:
            print(current_node.data)
            current_node=current_node.next
""", user_id=5)

snippet5_2 = Snippet("Python", """
def merge_sort(arr):
    if len(arr) > 1:
        mid=len(arr) // 2
        left_half=arr[:mid]
        right_half=arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i=j=k=0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k]=left_half[i]
                i += 1
            else:
                arr[k]=right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k]=left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k]=right_half[j]
            j += 1
            k += 1
""", user_id=5)

snippet5_3 = Snippet("Python", """
class BinaryTree:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left=BinaryTree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right=BinaryTree(data)
            else:
                self.right.insert(data)

    def find(self, data):
        if data < self.data:
            if self.left is None:
                return False
            return self.left.find(data)
        elif data > self.data:
            if self.right is None:
                return False
            return self.right.find(data)
        else:
            return True
""", user_id=5)

snippet5_4 = Snippet("Python", """
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot=arr[len(arr) // 2]
        left=[x for x in arr if x < pivot]
        middle=[x for x in arr if x == pivot]
        right=[x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
""", user_id=5)

snippet5_5 = Snippet("Python", """
class Graph:
    def __init__(self):
        self.graph={}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node]=[]
        self.graph[node].append(neighbor)

    def bfs(self, start_node):
        visited=set()
        queue=[start_node]
        while queue:
            node=queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(self.graph[node])
""", user_id=5)


snippet7_1 = Snippet("Python", """
class Stack:
    def __init__(self):
        self.stack=[]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
""", user_id=7)

snippet7_2 = Snippet("Python", """
class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end_of_word=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.is_end_of_word=True

    def search(self, word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node=self.root
        for char in prefix:
            if char not in node.children:
                return False
            node=node.children[char]
        return True
""", user_id=7)

snippet7_3 = Snippet("Python", """
def merge_two_sorted_lists(l1, l2):
    dummy=ListNode(0)
    current=dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next=l1
            l1=l1.next
        else:
            current.next=l2
            l2=l2.next
        current=current.next

    if l1:
        current.next=l1
    elif l2:
        current.next=l2

    return dummy.next
""", user_id=7)

snippet7_4 = Snippet("Python", """
class MinHeap:
    def __init__(self):
        self.heap=[]

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self._heapify_down(0)
        return root
      """, user_id=7)


snippet1_1.save()
snippet1_2.save()
snippet1_3.save()
snippet1_4.save()
snippet1_5.save()

snippet2_1.save()
snippet2_2.save()
snippet2_3.save()
snippet2_4.save()
snippet2_5.save()

snippet3_1.save()
snippet3_2.save()
snippet3_3.save()
snippet3_4.save()
snippet3_5.save()

snippet4_1.save()
snippet4_2.save()
snippet4_3.save()
snippet4_4.save()
snippet4_5.save()

snippet5_1.save()
snippet5_2.save()
snippet5_3.save()
snippet5_4.save()
snippet5_5.save()


snippet7_1.save()
snippet7_2.save()
snippet7_3.save()
snippet7_4.save()
