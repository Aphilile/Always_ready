# Calculate the cost of the hotel based on the number of nights.
def hotel_cost(num_nights):
    total_cost = num_nights*700
    return total_cost
 
# Calculate the cost of the plane ticket based on the destination city. 
def plane_cost(city_flight):
    if city_flight == "cape town":
        return 900
    elif city_flight == "east london":
        return 700
    elif city_flight=="durban":
        return 500
    
# Calculate the cost of car rental based on the number of days. 
def car_rental(rental_days):
    rental_cost = rental_days*250
    return rental_cost
 
# Calculate the total holiday cost by adding up hotel, plane, and car costs.
def holiday_cost(h_cost, p_cost, c_rental):
    hotel_total = hotel_cost(h_cost)
    print("Hotel Cost for " + str(h_cost) + " day(s) is " + str(hotel_total))
    plane_total = plane_cost(p_cost)
    print("Plane Cost to " + str(p_cost) + " is " + str(plane_total))
    car_rental_total = car_rental(c_rental)
    print("Car rental Cost for " + str(c_rental) + " day(s) is "  + str(car_rental_total))
    holiday_total = hotel_total + plane_total + car_rental_total
    print("Total Holiday Cost " + str(holiday_total))
    
 # Get the name of the city the user will be flying to.   
city_flight = input("Which City are you flying to(Cape Town,East London or Durban) ? ")
city_flight_validation = city_flight.lower()
num_nights = input("How many nights you will stay in a hotel ? ")
rental_days = input("How many days you need the car hire for ? ")

if city_flight_validation =="cape town"or city_flight_validation =="durban"or city_flight_validation=="East london":
 # Check if both num_nights and rental_days are valid integers   
    if str(num_nights).isdigit() and str(rental_days).isdigit():
        
# Call the holiday_cost function with the provided inputs.
        holiday_cost(int(num_nights),city_flight_validation,int(rental_days))
        
# Print an error message if the input for nights or rental days is not valid
    else:
        print("Enter correct number of nights or car rental days")
        
# Print an error message if the city input is not one of the specified options
else:
    print("one of the inputs is not correct please check and re-enter") 

    
    