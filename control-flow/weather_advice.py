weather= input("what is the weather like today? (sunny/rainy/cold): ").strip().lower()

if weather == "sunny":
    print("Wear a tshirt and sunglasses.")
elif weather == "rainy":
    print("Dont forget your Umbrella and rain coat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and scarf.")
else: 
    print("Sorry! I dont have recommendations for this weather.")

