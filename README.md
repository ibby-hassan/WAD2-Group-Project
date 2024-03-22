# WAD2-Group-Project
UofG WAD2 Group Project
Team 12B

web application - insQuire works as expected
users are able to read through questions and answers when they are not logged in, they are also able to 
search through questions with the search functionality at the nav bar.

when users are logged in, they are able to answers questions and also vote on the questions as well.

Instructions
1. please use python 3.9
2. pip install -r requirements.txt
3. you will need to do "$ python manage.py makemigrations"
4. then "$ python manage.py migrate"
5. then run "$ python population_script.py"
6. to run the server "$ python manage.py runserver"
7. and when you run the server, everything will work as expected

Contributors
1. Zhen Yao Heng (2840506H)
2. Qiuran Bian (2795305B)
3. Ibrahim Hassan (2667185H)


the below reference is used when implementing ajax
1. https://testdriven.io/blog/django-ajax-xhr/
2. https://docs.djangoproject.com/en/3.0/ref/csrf/#ajax

the below reference is used to solve a small problem that we met in question.html
1. https://stackoverflow.com/questions/42080864/set-in-a-queryset-object-indjango#:~:text=blog%20to%20access%20the%20related,django%20puts%20in%20for%20you.&text=The%20reason%20the%20reverse%20is,the%20reverse%20is%20a%20queryset. 
