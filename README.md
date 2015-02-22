##Read Me!
--------------------------------
If a student or teacher gets infected, then all the people in the class will get infected too! Some students and teachers are in multiple classes, so the infection can spread from class to class. This repo contains programs to simulate the spread of the infection.

###infection.py
Running `infection.py` will allow you to use the `Mentor` class as well as the function `infect(user)`. 

The `Mentor` class is a group of users who are assigned to either be a teacher or a student. After you have run `infection.py`, the `Mentor` class can be assigned as follows:

```
calculus = Mentor("Sal")
calculus.add_student(["Jane", "Sophia", "Juan"])
french = Mentor("Pierre")
french.add_student(["Mohammed", "Jane", "Yossi"])
history = Mentor("Maria")
history.add_student(["Pat", "Lee", "Alex"])
```    
As you can see, Jane is in both Calculus and French! If anyone in either of those classes gets infected, they all will! Luckily, if anyone in History class gets infected, the disease will stay confined to there.

To use the `infect(user)` function, you must first make a `mentorList` which contains all the classes, like this:

```
mentorList = [calculus, french, history]
```

Next, you can infect any user from the class list, like this:

```
>>> infect("Jane")
['Jane', 'Sal', 'Sophia', 'Juan', 'Pierre', 'Mohammed', 'Yossi']
```

A number of test cases for `infection.py` can be found in `infection_test.py`.


###limit_infection.py
`limit_infection.py` will take take a maximum number of infections and try to find a patient zero with the smallest amount of infection spread. 


###Data Visualization
A simple visualization of this infection algorithm can be seen [here](https://wugology.shinyapps.io/Infection/).

Please note that this visualization comes pre-loaded with the answers, given the conditions shown at the bottom. It does not actually implement the above algorithms, and therefore will not work under other conditions. However, it has a simple, user-friendly interface, and serves as a visual example of the infection spread.

In the future, I would like this visualization to run using the above algorithms. I would also like it to be animated, showing the spread from patient zero to all their classmates, and from those classmates to all *their* classmates, and so on.