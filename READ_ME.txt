This application has been created using Flask micro framework.

To run the application firstly make sure to have pip and flask installed. Flask can be installed with the following command:
$ pip install Flask

Once Flask has been installed the application can be run with the following command:
$ python index.py

The index page of the application can be viewed via: http://localhost:5000

When the user first opens the application type the database will contain no transactions. 
To add new transaction please press the green button (in the right bottom corner of the screen). A window should be displayed where you can fill in transaction details. 
Unfortunetly due to time constrains I have stored "formatted_transactions = []" globally, this means that although the database is updated upon addition of the new transaction, the API is only updated upon restarting the app. Hence, in order to continue restart the app. 

Now that the data has been added you can display the data in two ways:
	1) By clicking the green search button (with no input into the search bar)
	2) or via: http://localhost:5000/get_api

You can further search for specific Transactions by either:
	1) Typing transaction id into the search bar 
	2) Via: http://localhost:5000/get_api/? where the ? should be replaced with the id you are looking for

You can also delete transactions via: http://localhost:5000/delete_api/? where once again the question mark should be replaced with the id of the transaction you wish to delete. If the transaction was successfully deleted you'll see a success message. Due to autoincrementing the transaction_id value in the database some errors may occur when trying to access indivitual transactions via: http://localhost:5000/get_api/? (the search bar method remains reliable)

Given more time, I would've:
-Sanatised the data before inputing it into the database
-Ensured API is updated without the need to restart the app
-Use string as a transaction id instead of an integer
-Allow users to search for specific transactions using number of other varibles, such as the date of transaction, merchant or amount
