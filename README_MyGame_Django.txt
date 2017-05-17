Requirements to run the Rock Paper Scissor game WebApp:
	Python 3.x
	Django version tested and working - 1.10.5
	Browsers tested - Chrome and Safari
	Terminal or command line - to run the Django Web-app

Playing the game:
1. Running the Django server:
   a. Goto "MyGame" folder from the repository.
   b. run command "python manage.py runserver"
   c. If you want the game to be accessed on other systems in the same network then while running the server run 
      "python manage.py runserver 0.0.0.0:8000" so that the IP of the host system is broadcasted across the network.
2. Once the server has started you can open the browser and type "http://localhost:8000/game" to open the game page. 
I have implemented all the functionalities for Rock, Paper and Scissor game along with the Status and bonus score 
tracking functionality. 
