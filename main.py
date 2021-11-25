Have left out some validation checking
#Brief didn't specify parameters on lockdown
#Given more time I would also add a game beginning message and ending message

#Function to print the current infected percentage and lockdown status
def print_details(country_name, country_infected_percent, country_in_lockdown):
  details = "" + country_name + " currently has " + str(country_infected_percent) + " percent infected, and "
  if country_in_lockdown == True:
    details += "is in lockdown."
  else:
    details += "is not in lockdown."
  return details

#List to hold all country objects
country_names = []
country_infected_percents = []
country_in_lockdown = []

#Function which receives country data
def add_countries_to_game():
    country_to_add = ""
    #Loop keeps adding countries until user is done
    while True:
        country_to_add = input("Type the name of the country you would like to add and then press enter. If you are done adding countries, type \"done\" and click enter.")
        #If the user has entered a valid country, create the country and add it to the list
        if country_to_add != "done":
            #I would also add validation here to check that the user is inputting an int
            infected_percent = int(input("Type the current percentage of infected people for " + country_to_add + " and then press enter."))
            country_names.append(country_to_add)
            country_infected_percents.append(infected_percent)
            country_in_lockdown.append(False)
        #If the user is done, break out of  function
        else:
            break
        

#Function to ask the user which country to help
def ask_which_country_to_help():
    #Create a string to display to the user which each option
    ask_country = "Which country would you like to help? Choose from the following:"
    for country in country_names:
        ask_country += "\n" + country
    #Check that selected option is valid
    while True:
        country_to_help = input(ask_country)
        #Check list of countries to see if it is a valid country
        for country in country_names:
            if country_to_help == country:
                #Return the name of the country if it is valid
                return country_to_help
        #Print an error message and return to the top of the loop if the entry is invalid
        print("Invalid input, please try again.")

#Function runs every new day. Requires argument of the country to help.
def advance_day(country_to_help):
    print("*** NEW DAY ***")
    list_index = 0
    for country in country_names:
        #If the country is helped the percentage of infected is subtracted 40%
        #If the country is already at 40% or below, there is no way have less than 0% infected
        if country == country_to_help:
            if country_infected_percents[list_index] >= 40:
                country_infected_percents[list_index] = country_infected_percents[list_index] - 40
            else:
                country_infected_percents[list_index] = 0
        #If the country is not the percentage of infected is plus 20%
        #If the country is already at 80% or above, there is no way have more than 100% infected
        else:
            if country_infected_percents[list_index] >= 80:
                country_infected_percents[list_index] = 100
            else:
                country_infected_percents[list_index] = country_infected_percents[list_index] + 20
        #Print the current status of the country
        print(print_details(country_names[list_index], country_infected_percents[list_index], country_in_lockdown[list_index]))
        list_index += 1
    print("*** END DAY ***")
    

#Main

#Create Country Test Objects (In final development, these would be removed)

#main code
add_countries_to_game()
for i in range(0, 5):
    advance_day(ask_which_country_to_help())

