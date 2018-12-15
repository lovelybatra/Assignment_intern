This is simple HTTP Proxy service in python Django Framework
Requirements:
	To run this application python 3.6 and Django 2.1.4 is required following is the guidelines to install Django on windows.
	Once your system has Python 3 and pip installed you  can follow following steps:
	Open up the command promote on the location where you want to install Django.
	Type the following command.

		 pip install Django==2.1.4

	Make sure that your machine has internet connection. Once the download complete you can go
	Further
	To create a new project in Django create a new directory with the name of project , open the 
	Cmd in that directory and type the following command.

		Django-admin startproject project_name

	Proect_name canbe valid name of project.
	Once the project has been created you can test your server now by typing the following
	Command
	Goto the newly created directory with the name of project_name and type 

		python manage.py runserver 

	Now Server is started you can test by open the following URL

		http://localhost:8000

	From this URL Server Hello World page will open.
After Installing Django in your machine you need to add this project in your newly created project to do this follow the following steps.
1.	Copy the Webapp directory in to project_name Directory 
2.	Open the urls.py file and add this line within urlpatterns 

		url(r'^webapp/', include('webapp.urls')),    

3.	Now open the browser and type the Base_URL as follows 

		http://localhost:8000/webapp

	Once you open this URL Proxy service will run 
	Yu can now test by adding param and values or query string to this URL it will respond with as close to an exact copy of resulting response as possible.



