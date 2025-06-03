weather_input= input("what is the weather like today? (sunny/rainy/cold): ").strip().lower()
if weather_input == "sunny":
    print("Wear a tshirt and sunglasses.")
elif weather_input == "rainy":
    print("Dont forget your Umbrella and rain coat.")
elif weather_input == "cold":
    print("Make sure to wear a warm coat and scarf.")
else: 
    print("Sorry! I dont have recommendations for this weather.")

