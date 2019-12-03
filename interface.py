#Author:
#Jordan Sze

#Professor Alvin Lam provided general template

import pymysql

host = "localhost" 
username = "YAll6"  
password = "123456"  
database = "Movies" 

con = pymysql.connect(host,username,password,database)

#Database functions
def databaseFetchOne(query): #This function will return only ONE row the top/first row
    cur = con.cursor()
    cur.execute(query)
    return cur.fetchone()

def databaseFetchAll(query):
    cur = con.cursor()
    cur.execute(query)
    return cur.fetchall()

def databaseRunQuery(query):
    cur = con.cursor()
    amount = cur.execute(query)
    con.commit()
    return amount

#Queries to create tables Directors, Movies, and Actors
table_directors = "CREATE TABLE IF NOT EXISTS Directors(name VARCHAR(30), age INT, awards VARCHAR(30));"
table_movies = "CREATE TABLE IF NOT EXISTS Movies(title VARCHAR(50), year INT, rating INT);"
table_actors = "CREATE TABLE IF NOT EXISTS Actors(name VARCHAR(30), age INT, gender VARCHAR(10));"

#Runs queries
databaseRunQuery(table_directors)
databaseRunQuery(table_movies)
databaseRunQuery(table_actors)

#Functional functions

#Inserts inputted data into tables
def insert():
    #Prompts the user if they want to insert an entry in Directors
    ask_insert_directors = input("Do you want to insert an entry into Directors? (Enter Yes/Y for Yes or any other character for No)\n")
    
    #If yes then executes insert,
    #otherwise skips insert for Directors
    if ask_insert_directors == "Yes" or ask_insert_directors == "Y" or ask_insert_directors == "yes" or ask_insert_directors == "y":
        
        #Input director data
        insert_directors = input("Input director name, age, and awards (separated by space): ")

        #Parses director data input
        director_data = insert_directors.split(" ")
        director_name = director_data[0]
        director_age = director_data[1]
        director_awards = director_data[2]

        #If the input for director data is incorrectly inputted, repeats until it is correctly inputted
        while director_name.isdigit() or director_age.isalpha() or director_awards.isdigit():
            print("Faulty input for director data, try again")
            #Input director data
            insert_directors = input("Input director name, age, and awards (separated by space): ")

            #Parses director data input
            director_data = insert_directors.split(" ")
            director_name = director_data[0]
            director_age = director_data[1]
            director_awards = director_data[2]
        
        #Runs insert query Directors and prints the data that is inputted
        databaseRunQuery("INSERT INTO Directors VALUES (\'" + director_name + "\'" + ',' + director_age + ',' + "\'" + director_awards + "\'" + ");")
        print("Created new row data for table Directors: " + insert_directors)
            
    else:
        pass
    
    
    #Prompts the user if they want to insert an entry in Movies
    ask_insert_movies = input("Do you want to insert an entry into Movies? (Enter Yes/Y for Yes or any other character for No)\n")
    
    #If yes then executes insert,
    #otherwise skips insert for Movies
    if ask_insert_movies == "Yes" or ask_insert_movies == "Y" or ask_insert_movies == "yes" or ask_insert_movies == "y":
        
        #Input movie data
        insert_movies = input("Input movie title, year, and rating (separated by space): ")

        #Parses movie data input
        movie_data = insert_movies.split(" ")
        movie_title = movie_data[0]
        movie_year = movie_data[1]
        movie_rating = movie_data[2]

        #If the input for movie data is incorrectly inputted, repeats until it is correctly inputted
        while movie_title.isdigit() or movie_year.isalpha() or movie_rating.isalpha():
            print("Faulty input for movie data, try again")
            #Input movie data
            insert_movies = input("Input movie title, price, and rating (separated by space): ")

            #Parses movie data input
            movie_data = insert_movies.split(" ")
            movie_title = movie_data[0]
            movie_price = movie_data[1]
            movie_rating = movie_data[2]
            
        #Runs insert query Movies and prints the data that is inputted
        databaseRunQuery("INSERT INTO Movies VALUES (\'" + movie_title + "\'" +  ',' + movie_year + ',' + movie_rating + ");")
        print("Created new row data for table Movies: " + insert_movies)
            
    else:
        pass
    
    #Prompts the user if they want to insert an entry in Actors
    ask_insert_actors = input("Do you want to insert an entry into Actors? (Enter Yes/Y for Yes or any other character for No)\n")
    
    #If yes then executes insert,
    #otherwise skips insert for Actors
    if ask_insert_actors  == "Yes" or ask_insert_actors  == "Y" or ask_insert_actors  == "yes" or ask_insert_actors == "y":
        #Input actor data
        insert_actors = input("Input actor name, age, gender (separated by space): ")

        #Parses actor data input
        actors_data = insert_actors.split(" ")
        actor_name = actors_data[0]
        actor_age = actors_data[1]
        actor_gender = actors_data[2]

        #If the input for actor data is incorrectly inputted, repeats until it is correctly inputted
        while actor_name.isdigit() or actor_age.isalpha() or actor_gender.isdigit():
            print("Faulty input for actor data, try again")
            #Input actor data
            insert_actors = input("Input actor name, age, gender (separated by space): ")

            #Parses actor data input
            actors_data = insert_actors.split(" ")
            actor_name = actors_data[0]
            actor_age = actors_data[1]
            actor_gender = actors_data[2]
            
        #Runs insert query Actors and prints the data that is inputted
        databaseRunQuery("INSERT INTO Actors VALUES (\'" + actor_name + "\'" + ',' + actor_age + ',' + "\'" + actor_gender + "\'" + ");") 
        print("Created new row data for table Actors: " + insert_actors)
        
    else:
        pass
    

  
#Looks up singular data values in tables
def lookupOne():
    #Prompts the user if they want to look up an entry in Directors
    ask_lookup_directors = input("Do you want to look up an entry in Directors? (Enter Yes/Y for Yes or any other character for No)\n")
    
    #If yes then executes look up,
    #otherwise skips look up for directors
    if ask_lookup_directors == "Yes" or ask_lookup_directors == "Y" or ask_lookup_directors == "yes" or ask_lookup_directors == "y":
        lookup_directors = input("Which entry do you want to look up in Directors? ")
        directors_tuple = databaseFetchOne("SELECT * FROM Directors WHERE name = " + "\'" + lookup_directors + "\'")
        #If input not found in Directors, prints not found
        #otherwise prints the tuple of the input
        if directors_tuple == None:
            print(lookup_directors + " not found in Directors")
        else:
            print(directors_tuple[0], directors_tuple[1], directors_tuple[2])
    
    else:
        pass
        
    #Prompts the user if they want to look up an entry in Movies   
    ask_lookup_movies = input("Do you want to look up an entry in Movies? (Enter Yes/Y for Yes or any other character for No)\n")
    
    #If yes then executes look up,
    #otherwise skips look up for movies
    if ask_lookup_movies == "Yes" or ask_lookup_movies == "Y" or ask_lookup_movies == "yes" or ask_lookup_movies == "y":
        lookup_movies = input("Which entry do you want to look up in Movies? ")
        movies_tuple = databaseFetchOne("SELECT * FROM Movies WHERE title = " + "\'" + lookup_movies + "\'")
        #If input not found in Movies, prints not found
        #otherwise prints the tuple of the input
        if movies_tuple == None:
            print(lookup_movies + " not found in Movies")
        else:
            print(movies_tuple[0], movies_tuple[1], movies_tuple[2])
        
    else:
        pass
     
    #Prompts the user if they want to look up an entry in Actors  
    ask_lookup_actors = input("Do you want to look up an entry in Actors? (Enter Yes/Y for Yes or any other character for No)\n")
    
    #If yes then executes look up,
    #otherwise skips look up for actors
    if ask_lookup_actors == "Yes" or ask_lookup_actors == "Y" or ask_lookup_actors== "yes" or ask_lookup_actors == "y":
        lookup_actors = input("Which entry do you want to look up in Actors? ")
        actors_tuple = databaseFetchOne("SELECT * FROM Actors WHERE name = " + "\'" + lookup_actors + "\'")
        #If input not found in Actors, prints not found
        #otherwise prints the tuple of the input
        if actors_tuple == None:
            print(lookup_actors + " not found in Actors")
        else:
            print(actors_tuple[0], actors_tuple[1], actors_tuple[2])
        
    else:
        pass
    
  
#Looks up all data in tables
def lookupAll():
    #Prompts the user which table to look up
    #If the input is not a table, repeats
    #until a valid table name is inputted
    ask_lookupall = input("Which table do you want to look up? \nDirectors\nMovies\nActors:\n\n")
    while ask_lookupall != "Directors" and ask_lookupall != "Movies" and ask_lookupall != "Actors":
        print("Faulty input, try again")
        ask_lookupall = input("Which table do you want to look up? \nDirectors\nMovies\nActors:\n\n")
    
    i = 0    
    #If the table requested is Directors,
    #prints all of its tuples
    if ask_lookupall == "Directors":
        lookupall_directors = databaseFetchAll("SELECT * FROM Directors ORDER BY name")
        print("(name, age, awards)")
        while i < len(lookupall_directors):
            print(str(lookupall_directors[i]))
            i += 1
    
    #If the table requested is Movies,
    #prints all of its tuples    
    elif ask_lookupall == "Movies":
        lookupall_movies = databaseFetchAll("SELECT * FROM Movies ORDER BY title")
        print("(title, year, rating)")
        while i < len(lookupall_movies):
            print(str(lookupall_movies[i]))
            i += 1
    
    #If the table requested is Actors,
    #prints all of its tuples    
    elif ask_lookupall == "Actors":
        lookupall_actors = databaseFetchAll("SELECT * FROM Actors ORDER BY name")
        print("(name, age, gender)")
        while i < len(lookupall_actors):
            print(str(lookupall_actors[i]))
            i += 1

#Deletes provided by inputted values
def delete():
    #Prompts the user which table to select
    #If the input is not a table, repeats
    #until a valid table name is inputted
    ask_table = input("Which table do you want to select? \nDirectors\nMovies\nActors:\n\n")
    while ask_table != "Directors" and ask_table != "Movies" and ask_table != "Actors":
        print("Faulty input, try again")
        ask_table = input("Which table do you want to select? \nDirectors\nMovies\nActors:\n\n")
       
    #If the table requested is Directors,
    #prompts user for value to delete
    #and deletes tuples with inputted value
    if ask_table == "Directors":
        ask_delete_directors = input("What do you want to delete? (name, age, or awards) ")
        #If requested value to delete is name
        if ask_delete_directors == "name" or ask_delete_directors == "Name":
            director_value = input("Enter name to be deleted: ")
            delete_directors = databaseRunQuery("DELETE from Directors WHERE name = \"" + director_value + "\"")
            if(delete_directors == 0): 
                print("Found nothing to delete")
            else:
                print("Deleted " + str(delete_directors) + " rows")
        #If requested value to delete is age
        elif ask_delete_directors == "age" or ask_delete_directors == "Age":
            director_value = input("Enter age to be deleted: ")
            delete_directors = databaseRunQuery("DELETE from Directors WHERE age = \"" + director_value + "\"")
            if(delete_directors == 0): 
                print("Found nothing to delete")
            else:
                print("Deleted " + str(delete_directors) + " rows")
        #If requested value to delete is awards
        elif ask_delete_directors == "awards" or ask_delete_directors == "Awards":
            director_value = input("Enter award to be deleted: ")
            delete_directors = databaseRunQuery("DELETE from Directors WHERE awards = \"" + director_value + "\"")
            if(delete_directors == 0): 
                print("Found nothing to delete")
            else:
                print("Deleted " + str(delete_directors) + " rows")
        else:
            print("Faulty input")
    #If the table requested is Movies,
    #prompts user for value to delete
    #and deletes tuples with inputted value  
    elif ask_table == "Movies":
        ask_delete_movies = input("What do you want to delete? (title, year, or rating) ")
        #If requested value to delete is title
        if ask_delete_movies == "title" or ask_delete_movies == "Title":
            movie_value = input("Enter title to be deleted: ")
            delete_movies = databaseRunQuery("DELETE from Movies WHERE title = \"" + movie_value + "\"")
            if(delete_movies == 0): 
                print("Found nothing to delete")
            else:
                print("Deleted " + str(delete_movies) + " rows")
        #If requested value to delete is year
        elif ask_delete_movies == "year" or ask_delete_movies == "Year":
            movie_value = input("Enter year to be deleted: ")
            delete_movies = databaseRunQuery("DELETE from Movies WHERE year = \"" + movie_value + "\"")
            if(delete_movies == 0): 
                print("Found nothing to delete")
            else:
                print("Deleted " + str(delete_movies) + " rows")
        #If requested value to delete is rsting
        elif ask_delete_movies == "rating" or ask_delete_directors == "Rating":
            movie_value = input("Enter rating to be deleted: ")
            delete_movies = databaseRunQuery("DELETE from Movies WHERE rating = \"" + movie_value + "\"")
            if(delete_movies == 0): 
                print("Found nothing to delete")
            else:
                print("Deleted " + str(delete_movies) + " rows")
        else:
            print("Faulty input")
    
    #If the table requested is Actors,
    #prompts user for value to delete
    #and deletes tuples with inputted value   
    elif ask_table == "Actors":
        ask_delete_actors = input("What do you want to delete? (name, age, or awards) ")
        #If requested value to delete is name
        if ask_delete_actors == "name" or ask_delete_actors == "Name":
            actor_value = input("Enter name to be deleted: ")
            delete_actors = databaseRunQuery("DELETE from Actors WHERE name = \"" + actor_value + "\"")
            if(delete_actors == 0): 
                print("Found nothing to delete")
            else:
                print("Deleted " + str(delete_actors) + " rows")
        #If requested value to delete is age
        elif ask_delete_actors == "age" or ask_delete_actors == "Age":
            actor_value = input("Enter age to be deleted: ")
            delete_actors = databaseRunQuery("DELETE from Actors WHERE age = \"" + actor_value + "\"")
            if(delete_actors == 0): 
                print("Found nothing to delete")
            else:
                print("Deleted " + str(delete_actors) + " rows")
        #If requested value to delete is gender
        elif ask_delete_actors == "gender" or ask_delete_actors == "Gender":
            actor_value = input("Enter gender to be deleted: ")
            delete_actors = databaseRunQuery("DELETE from Actors WHERE gender = \"" + actor_value + "\"")
            if(delete_actors == 0): 
                print("Found nothing to delete")
            else:
                print("Deleted " + str(delete_actors) + " rows")
        else:
            print("Faulty input")
    
    
#Looks for values in tables
#and updates them if found
def update():
    #Prompts the user which table to select
    #If the input is not a table, repeats
    #until a valid table name is inputted
    ask_table = input("Which table do you want to select? \nDirectors\nMovies\nActors:\n\n")
    while ask_table != "Directors" and ask_table != "Movies" and ask_table != "Actors":
        print("Faulty input, try again")
        ask_table = input("Which table do you want to select? \nDirectors\nMovies\nActors:\n\n")
    
    #If selected table is Directors...
    if ask_table == "Directors":
        #Prompts user for what value to update
        lookfor = input("What value would you like to update? (any value in Directors) ")
        
        #If inputted value exists in name, alters rows
        if(databaseRunQuery("SELECT * FROM Directors WHERE name = \"" + lookfor + "\"")):
            updateto = input("What value would you like it to update to? ")
            result = databaseRunQuery("UPDATE Directors SET name = \"" + updateto + "\" WHERE name = \"" + lookfor + "\"")
            print("Altered " + str(result) + " rows!")
            
        #If inputted value exists in age, alters rows
        elif(databaseRunQuery("SELECT * FROM Directors WHERE age = \"" + lookfor + "\"")):
            updateto = input("What value would you like it to update to? ")
            result = databaseRunQuery("UPDATE Directors SET age = \"" + updateto + "\" WHERE age = \"" + lookfor + "\"")
            print("Altered " + str(result) + " rows!")
                
        #If inputted value exists in awards, alters rows
        elif(databaseRunQuery("SELECT * FROM Directors WHERE awards = \"" + lookfor + "\"")):
            updateto = input("What value would you like it to update to? ")
            result = databaseRunQuery("UPDATE Directors SET awards = \"" + updateto + "\" WHERE awards = \"" + lookfor + "\"")
            print("Altered " + str(result) + " rows!")
            
        #Otherwise, prints could not find value
        else:
            print("Could not find " + lookfor)
    
    #If selected table is Movies...
    elif ask_table == "Movies":
        #Prompts user what value to update
        lookfor = input("What value would you like to update? (any value in Movies) ")
        
        #If inputted value exists in title, alters rows
        #otherwise prints cannot find inputted value
        if(databaseRunQuery("SELECT * FROM Movies WHERE title = \"" + lookfor + "\"")):
            updateto = input("What value would you like it to update to? ")
            result = databaseRunQuery("UPDATE Movies SET title = \"" + updateto + "\" WHERE title = \"" + lookfor + "\"")
            print("Altered " + str(result) + " rows!")

                
        #If inputted value exists in year, alters rows
        #otherwise prints cannot find inputted value
        elif(databaseRunQuery("SELECT * FROM Movies WHERE year = \"" + lookfor + "\"")):
                updateto = input("What value would you like it to update to? ")
                result = databaseRunQuery("UPDATE Movies SET year = \"" + updateto + "\" WHERE year = \"" + lookfor + "\"")
                print("Altered " + str(result) + " rows!")
                
        #If inputted value exists in rating, alters rows
        #otherwise prints cannot find inputted value
        elif(databaseRunQuery("SELECT * FROM Movies WHERE rating = \"" + lookfor + "\"")):
            updateto = input("What value would you like it to update to? ")
            result = databaseRunQuery("UPDATE Movies SET rating = \"" + updateto + "\" WHERE rating = \"" + lookfor + "\"")
            print("Altered " + str(result) + " rows!")
        else:
            print("Could not find " + lookfor)

    #If selected table is Actors...
    elif ask_table == "Actors":
        #Prompts user for what value to update
        lookfor = input("What value would you like to update? (any value in Actors) ")
        
        #If inputted value exists in name, alters rows
        #otherwise prints cannot find inputted value
        if(databaseRunQuery("SELECT * FROM Actors WHERE name = \"" + lookfor + "\"")):
            updateto = input("What value would you like it to update to? ")
            result = databaseRunQuery("UPDATE Actors SET name = \"" + updateto + "\" WHERE name = \"" + lookfor + "\"")
            print("Altered " + str(result) + " rows!")
                
        #If inputted value exists in age, alters rows
        #otherwise prints cannot find inputted value
        elif(databaseRunQuery("SELECT * FROM Actors WHERE age = \"" + lookfor + "\"")):
            updateto = input("What value would you like it to update to? ")
            result = databaseRunQuery("UPDATE Actors SET age = \"" + updateto + "\" WHERE age = \"" + lookfor + "\"")
            print("Altered " + str(result) + " rows!")
                
        #If inputted value exists in gender, alters rows
        #otherwise prints cannot find inputted value
        elif(databaseRunQuery("SELECT * FROM Actors WHERE gender = \"" + lookfor + "\"")):
            updateto = input("What value would you like it to update to? ")
            result = databaseRunQuery("UPDATE Actors SET gender = \"" + updateto + "\" WHERE gender = \"" + lookfor + "\"")
            print("Altered " + str(result) + " rows!")
        else:
            print("Could not find " + lookfor)
                
    else:
        print("Faulty input")

    
#Main looping interface
while(1):
        #Feel free to modify this prompt, remember that \n creates a new line
        prompt = "\nYAll6: \n"\
                 "1. Insert\n"\
                 "2. Delete\n"\
                 "3. Lookup by Name\n"\
                 "4. Lookup all data of one table\n"\
                 "5. Update\n"\
                 "Please enter a command, type q or quit to exit.\n"
	
        choice = input(prompt)
        
        #Handle the case where the user wants to quit here.                
        if(choice == 'q' or choice == "quit"):  
            con.commit()
            break
            
        #The rest is where we match up the choice with a function or code path
        if(choice == '1'):
            insert()
        if(choice == '2'):
            delete()
        if(choice == '3'):
            lookupOne()
        if(choice == '4'):
            lookupAll()
        if(choice == '5'):
            update()
        
        print()
