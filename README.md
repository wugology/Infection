##Read Me!
--------------------------------
If a student or coach gets infected, then all the people in the class will get infected too! Some students and coaches are in multiple classes, so the infection can spread from class to class. This repo contains programs to simulate the spread of the infection.

###infection.py
Running `infection.py` will allow you to use the `Coach` class and the function `total_infection(user)`, `getUserList()`, and `limited_infection(number)`. 

###Coach
The `Coach` class is a group of users who are assigned to either be a coach or a student. After you have run `infection.py`, the `Coach` class can be assigned as follows:

```
>>> calculus = Coach("Sal")
>>> calculus.add_student(["Jane", "Sophia", "Juan"])
>>> french = Coach("Pierre")
>>> french.add_student(["Mohammed", "Jane", "Yossi"])
>>> history = Coach("Maria")
>>> history.add_student(["Pat", "Lee", "Alex"])
```    
As you can see, Jane is in both Calculus and French! If anyone in either of those classes gets infected, they all will! Luckily, if anyone in History class gets infected, the disease will stay confined to there.

Future implementations of `Coach` may include other attributes like whether or not the entire class has been infected.

###coachList
Once you have created a few classes you must make a `coachList` which contains all the classes, like this:

```
>>> coachList = [calculus, french, history]
```
Once you have created the `coachList`, you can use the other functions `getUsers()`, `total_infection(user)`, and `limited_infection(number)`.

###getUserList()
Simply run the command `getUserList()` and it will return a list of all users, including students and coachs. This function does not take any parameters.
```
>>> getUserList()
['Sal', 'Jane', 'Sophia', 'Juan', 'Pierre', 'Mohammed', 'Yossi', 'Maria', 'Pat', 'Lee', 'Alex']
```

###total_infection(user)
The `total_infection(user)` function will return a list of all users who will get infected if the input user is infected. To use the `total_infection(user)` function, type the name of a user (in quotes) like this:

```
>>> total_infection("Jane")
['Jane', 'Sal', 'Sophia', 'Juan', 'Pierre', 'Mohammed', 'Yossi']
```

A number of test cases for `total_infection(user)` can be found in `infection_test.py`.

###limited_infection(number)
The `limited_infection(number)` function will return a list of users who can be infected initially, where the outcome of the infection spread is less than or equal to the input number. For example:
```
>>> limited_infection(3)
Infecting any of the following users will limit the infection to 3 or fewer users: []
```
As we can see, there are no users we can infect who will limit the spread of the disease to 3 users. This is because the smallest class, history, contains three students and one coach. Let's try 4:
```
>>> limited_infection(4)
Infecting any of the following users will limit the infection to 4 or fewer users: ['Maria', 'Pat', 'Lee', 'Alex']
```
We can infect anyone from the history class, and the infection will be contained to 4 users!

A number of test cases for `limited_infection(number)` can be found in `limit_infection_test.py`.

-----------------------------
###Data Visualization
A simple visualization of this infection algorithm can be seen [here](https://wugology.shinyapps.io/Infection/). A sample situation similar to the one in `infection_test.py` is given. You can choose who to infect first. You can also choose what color the plot will display in!

The code for this visualization is contained in `ui.r` and `server.r`. Please note that this visualization comes pre-loaded with the answers, given the conditions in the sample situation. It does not actually implement the above algorithms, and therefore will not work under other conditions. However, it has a simple, user-friendly interface, and serves as a visual example of the infection spread.

In the future, I would like this visualization to run using the above algorithms, so that it can be updated with various test cases on the fly. I would also like it to be animated, showing the spread from patient zero to all their classmates, and from those classmates to all *their* classmates, and so on.