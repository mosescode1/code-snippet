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


def create_dummy_snippets(user, snippets):
    for title, content, code_type in snippets:
        snippet = Snippet(
            snippet_title=title,
            snippet_type=code_type,
            snippet_code=content,
            user_id=user.id,
        )
        snippet.save()


# List of users with corresponding snippets
users_with_snippets = [
    (user1, [
        ("Hello World in Python", "print('Hello, World!')", "Python"),
        ("Simple For Loop in Python", "for i in range(5): print(i)", "Python"),
        ("String Concatenation in Python",
         "greeting = 'Hello' + ' ' + 'World!'", "Python"),
        ("Basic Function in Python",
         "def greet(name):\n    return f'Hello, {name}!'", "Python")
    ]),
    (user2, [
        ("JavaScript Alert", "alert('Hello, World!');", "JavaScript"),
        ("Basic JavaScript Function",
         "function greet(name) { return 'Hello, ' + name + '!'; }", "JavaScript"),
        ("JavaScript Array Iteration",
         "let numbers = [1, 2, 3, 4, 5];\nnumbers.forEach(num => console.log(num));", "JavaScript"),
        ("DOM Manipulation",
         "document.getElementById('myElement').textContent = 'Hello, DOM!';", "JavaScript")
    ]),
    (user3, [
        ("HTML Basic Structure", "<!DOCTYPE html>\n<html>\n<head>\n<title>Page Title</title>\n</head>\n<body>\n<h1>Hello, World!</h1>\n</body>\n</html>", "HTML"),
        ("CSS Centering",
         "body { display: flex; justify-content: center; align-items: center; height: 100vh; }", "CSS"),
        ("CSS Grid Layout",
         ".container { display: grid; grid-template-columns: repeat(3, 1fr); }", "CSS"),
        ("Simple Form in HTML", "<form>\n  <input type='text' placeholder='Name'>\n  <input type='submit' value='Submit'>\n</form>", "HTML")
    ]),
    (user4, [
        ("SQL Select Statement", "SELECT * FROM users WHERE active = 1;", "SQL"),
        ("SQL Insert Statement",
         "INSERT INTO users (username, email) VALUES ('john', 'john@example.com');", "SQL"),
        ("SQL Update Statement",
         "UPDATE users SET password = 'newpass' WHERE username = 'john';", "SQL"),
        ("SQL Delete Statement", "DELETE FROM users WHERE username = 'john';", "SQL")
    ]),
    (user5, [
        ("Python List Comprehension", "[x**2 for x in range(10)]", "Python"),
        ("Python Dictionary Comprehension",
         "{x: x**2 for x in range(10)}", "Python"),
        ("Python Lambda Function", "double = lambda x: x * 2", "Python"),
        ("Python Map Function",
         "result = map(lambda x: x*2, [1, 2, 3, 4, 5])", "Python")
    ]),
    (user6, [
        ("JavaScript Fetch API", "fetch('https://api.example.com/data')\n  .then(response => response.json())\n  .then(data => console.log(data));", "JavaScript"),
        ("JavaScript Promises",
         "let promise = new Promise((resolve, reject) => {\n  resolve('Success!');\n});", "JavaScript"),
        ("JavaScript Async/Await",
         "async function fetchData() {\n  let response = await fetch('https://api.example.com/data');\n  let data = await response.json();\n  console.log(data);\n}", "JavaScript"),
        ("JavaScript Event Listener",
         "document.getElementById('myButton').addEventListener('click', () => {\n  alert('Button clicked!');\n});", "JavaScript")
    ]),
    (user7, [
        ("HTML Image Element", "<img src='image.jpg' alt='My Image'>", "HTML"),
        ("CSS Flexbox Layout",
         ".container { display: flex; justify-content: space-between; }", "CSS"),
        ("CSS Media Query",
         "@media (max-width: 600px) { .container { flex-direction: column; } }", "CSS"),
        ("HTML Anchor Element", "<a href='https://example.com'>Visit Example</a>", "HTML")
    ]),
    (user8, [
        ("SQL Join Statement", "SELECT users.username, orders.order_id FROM users JOIN orders ON users.id = orders.user_id;", "SQL"),
        ("SQL Group By Statement",
         "SELECT COUNT(*), status FROM orders GROUP BY status;", "SQL"),
        ("SQL Having Clause",
         "SELECT COUNT(*), status FROM orders GROUP BY status HAVING COUNT(*) > 5;", "SQL"),
        ("SQL Subquery", "SELECT * FROM users WHERE id IN (SELECT user_id FROM orders WHERE status = 'completed');", "SQL")
    ]),
    (user9, [
        ("Python Try/Except", "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')", "Python"),
        ("Python File Handling",
         "with open('file.txt', 'r') as file:\n    content = file.read()", "Python"),
        ("Python Class Definition",
         "class MyClass:\n    def __init__(self, name):\n        self.name = name", "Python"),
        ("Python Inheritance", "class Animal:\n    def speak(self):\n        return 'Sound'\n\nclass Dog(Animal):\n    def speak(self):\n        return 'Bark'", "Python")
    ]),
    (user10, [
        ("JavaScript Object Creation",
         "let person = {\n  name: 'John',\n  age: 30\n};", "JavaScript"),
        ("JavaScript Arrow Function",
         "let greet = name => `Hello, ${name}!`;", "JavaScript"),
        ("JavaScript Array Filter",
         "let numbers = [1, 2, 3, 4, 5];\nlet even = numbers.filter(num => num % 2 === 0);", "JavaScript"),
        ("JavaScript String Template",
         "let greeting = `Hello, ${person.name}! You are ${person.age} years old.`;", "JavaScript")
    ])
]

# Create and save dummy snippets for each user
for user, snippets in users_with_snippets:
    create_dummy_snippets(user, snippets)
