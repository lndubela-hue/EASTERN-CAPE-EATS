import streamlit as st
import random

def recommend_eateries(cuisine=None, location="Eastern Cape", budget=None):
    """
    Recommends eateries in the Eastern Cape based on cuisine, location, and budget.

    Args:
        cuisine (str, optional): The desired cuisine (e.g., "Seafood", "African", "Italian"). Defaults to None.
        location (str, optional): The specific location within the Eastern Cape (e.g., "East London", "Gqeberha"). Defaults to "Eastern Cape".
        budget (str, optional): The desired budget (e.g., "Budget-friendly", "Mid-range", "Fine dining"). Defaults to None.

    Returns:
        list: A list of dictionaries, where each dictionary represents an eatery
              and contains its name, cuisine, location, budget, and a short description.
              Returns an empty list if no eateries match the criteria.
    """
    eateries = [
        {
            "name": "The Beach Break",
            "cuisine": "Seafood",
            "location": "East London",
            "budget": "Mid-range",
            "description": "Fresh seafood with stunning ocean views."
        },
        {
            "name": "Ginger & Co.",
            "cuisine": "African",
            "location": "Gqeberha",
            "budget": "Mid-range",
            "description": "Modern African cuisine with a focus on local ingredients."
        },
        {
            "name": "Guido's",
            "cuisine": "Italian",
            "location": "East London",
            "budget": "Mid-range",
            "description": "Authentic Italian dishes in a cozy atmosphere."
        },
        {
            "name": "The Highlander",
            "cuisine": "Pub Fare",
            "location": "East London",
            "budget": "Budget-friendly",
            "description": "Classic pub food and a wide selection of beers."
        },
        {
            "name": "Sage Restaurant",
            "cuisine": "Fine Dining",
            "location": "Gqeberha",
            "budget": "Fine dining",
            "description": "Elegant dining experience with innovative dishes."
        },
        {
            "name": "Kukula Restaurant",
            "cuisine": "African",
            "location": "Mthatha",
            "budget": "Budget-friendly",
            "description": "Traditional Xhosa cuisine."
        },
        {
            "name": "The Grill Room",
            "cuisine": "Steakhouse",
            "location": "East London",
            "budget": "Mid-range",
            "description": "Excellent steaks and grills."
        },
        {
            "name": "Ciao Bella",
            "cuisine": "Italian",
            "location": "Gqeberha",
            "budget": "Mid-range",
            "description": "Delicious Italian food."
        },
        {
            "name": "The Coffee Shop",
            "cuisine": "Cafe",
            "location": "East London",
            "budget": "Budget-friendly",
            "description": "Great coffee and light meals."
        },
        {
            "name": "The Seafood Shack",
            "cuisine": "Seafood",
            "location": "Port Alfred",
            "budget": "Mid-range",
            "description": "Fresh seafood with a view of the ocean."
        }
    ]

    filtered_eateries = eateries

    if cuisine:
        filtered_eateries = [e for e in filtered_eateries if cuisine.lower() in e["cuisine"].lower()]
    if location and location.lower() != "eastern cape":
        filtered_eateries = [e for e in filtered_eateries if location.lower() in e["location"].lower()]
    if budget:
        filtered_eateries = [e for e in filtered_eateries if budget.lower() in e["budget"].lower()]

    if not filtered_eateries:
        return []

    num_recommendations = min(3, len(filtered_eateries))
    recommendations = random.sample(filtered_eateries, num_recommendations)

    return recommendations

def main():
    st.set_page_config(page_title="Eastern Cape Eatery Recommender", page_icon="🍽️")
    st.title("Eastern Cape Eatery Recommender")
    st.markdown("Find the best places to eat in the Eastern Cape!")

    # Input fields
    cuisine = st.text_input("Enter desired cuisine (e.g., Seafood, African, Italian) or leave blank for any:", "")
    location = st.text_input("Enter location (e.g., East London, Gqeberha) or leave blank for the whole Eastern Cape:", "")
    budget = st.text_input("Enter budget (e.g., Budget-friendly, Mid-range, Fine dining) or leave blank for any:", "")

    # Search button
    if st.button("Get Recommendations"):
        recommendations = recommend_eateries(cuisine, location, budget)
        if recommendations:
            st.subheader("Your Recommendations:")
            for eatery in recommendations:
                st.markdown(f"- **{eatery['name']}** ({eatery['cuisine']}) - {eatery['location']} - {eatery['budget']}: {eatery['description']}")
        else:
            st.error("Sorry, no eateries found matching your criteria.")

    st.markdown("---")
    st.write("Thank you for using the Eastern Cape Eatery Recommender!")

if __name__ == "__main__":
    main()