# DjangoBlog
A Blogging WebApp Made on the Python Djang Framework

Install the following packages: OR Use the Virtual Environment ZIP for Linux
pip install django
pip install channels
pip install channels_redis
pip install Django==1.11
pip install django-crispy-forms

Ensure Your Pip List Has the Following Packages Before Runnning The Program
Package             Version
------------------- -------
aioredis            1.1.0  
asgiref             2.3.2  
async-timeout       3.0.0  
attrs               18.1.0 
autobahn            18.7.1 
Automat             0.7.0  
channels            2.1.2  
channels-redis      2.2.1  
constantly          15.1.0 
daphne              2.2.1  
Django              2.0.7  
django-crispy-forms 1.7.2  
django-filter       2.0.0  
hiredis             0.2.0  
hyperlink           18.0.0 
idna                2.7    
incremental         17.5.0 
msgpack             0.5.6  
pip                 18.0    
pytz                2018.5 
setuptools          40.0.0 

Twisted             18.7.0 
txaio               18.7.1 
wheel               0.31.1 
------------------- -------
Run the Redis Server using The Command:<br />
sudo docker run -p 6379:6379 -d redis:2.8<br />
After That,<br />
python manage.py runserver<br />
And the WebApp Should be active at<br /> 127.0.0.1:8000

Features:<br />
.........<br />
Sign Up for new users <br />
Authentication using Login and Logout <br />
ADMIN PANEL <br />
View Blogs <br />
Search Blogs for Content<br />
Add Blogs <br />
Edit Blogs <br />
Delete Blogs <br />
Each Blog has Comments and Likes <br />
Chat System With Both Group Chat as well as Personal CHATROOM Chat <br />
Profile Page to display profile INFO <br />
