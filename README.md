# DarwinLabs
<br>
<h2>Mobile Recharge API Using Paytm</h2> 

<h4>Python Application that provide REST API to recharge Mobile Phones</h4>

<br>

<h3>Prerequisites :</h3>

1. DjangoRESTFramework - pip install djangorestframework


<br>

<h3>Installation :</h3>

In order to run this project follow the steps given below :-

1. First, Download this project or clone this project in your computer
2. After that ensure whether Django or DjangoRESTFramework package is installed in your system or not 
3. If DjangoRESTFramework is installed in your local computer then open cmd(command prompt) 
4. Go to your project directory using command prompt(cmd).
5. When you reached inside the project directory and if you see any file named as manage.py then you are at the right location
6. Now, write this command in your command prompt  to start the django development server : <br><h4 align="center">python manage.py runserver</h4>
7. when server launched then open your browser and type this url in your browser address bar: <h5 align="center"> URL:- 127.0.0.1:8000 </h5>

<br>

<h3>Working:</h3>
<br>
In order to explore functionality or working of this project follow the steps given below :
<br>
<br>
1. Open Registration URL: <h5 align="center"> 127.0.0.1:8000/register</h5> 
 <h6 align="center"> At this url you will see a form that is for registrating new users. Fill all the fields of that form in order to proceed futher </h6>
  <h6 align="center">* Note -  The field named as account_balance is just for adding money in your wallet so type how much money you want in your wallet there</h6>
 <br>
 <br>
2. After Registration Go to the Recharge URL : <h5 align="center"> 127.0.0.1:8000/phone</h5> 
 <h6 align="center"> At this url you will see a form that is required for the recharge </h6>
 <br>
 
3. When you submit the recharge form then you will see json response which provide the status of your recharge that whether it is successfully completed or not .
4. If a user dont have sufficient balance in his/her account then system will notify that "Insufficient Balance"

<br>

<h3>Built With:</h3>
<br>

* [Django Framework](http://www.django-rest-framework.org/) - The web framework used for creating the application 
* [Django REST-Framework](https://www.djangoproject.com/) - The web framework used for creating the API's for the application
* [Bootstrap](http://getbootstrap.com/) - The web framework used for creating the user-interface(UI) of the application

<br>
<h3>Authors:</h3>

* **Akash Shukla** - *Initial work* - [AkashShukla](https://github.com/akash707)



