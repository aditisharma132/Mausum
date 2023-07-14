import requests
import streamlit as st

def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def get_precautions(weather_description):
    precautions = ""
    if "rain" in weather_description.lower():
        precautions = "Carry an umbrella or raincoat."
    elif "snow" in weather_description.lower():
        precautions = "Wear warm clothes and avoid driving unless necessary."
    elif "clouds" in weather_description.lower():
        precautions = "No specific precautions. Enjoy the day!"
    elif "thunderstorm" in weather_description.lower():
        precautions = "Stay indoors, avoid open spaces, and unplug electronic devices."
    elif "clear" in weather_description.lower():
        precautions = "Wear sunscreen and stay hydrated."
    elif "fog" in weather_description.lower():
        precautions = "Drive slowly, keep a safe distance from other vehicles, and use fog lights."
    else:
        precautions = "No specific precautions. Enjoy the day!"
    return precautions

def main():
    st.title("⛅मौsum")
    api_key = "ceca35c8292b0222e991213932cdddf1"  
    city = st.text_input("Enter city name", "London")
    if st.button("Get Weather"):
        weather_data = get_weather_data(api_key, city)
        if weather_data["cod"] == "404":
            st.error("City not found. Please enter a valid city name.")
        else:
            st.write(f"Weather in {city}:")
            temperature = weather_data["main"]["temp"]
            weather_desc = weather_data["weather"][0]["description"]
            precautions = get_precautions(weather_desc)
            st.subheader("Temperature:")
            st.write(f"{temperature} °C")
            st.subheader("Description:")
            st.write(f"{weather_desc}")
            st.subheader("Precautions:")
            st.write(f"{precautions}")

if __name__ == "__main__":
    main()
