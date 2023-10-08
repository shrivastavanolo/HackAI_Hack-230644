## Installation of uAgents module(Python)

Install μAgents for Python 3.8, 3.9, 3.10, or 3.11:

```bash
poetry install
poetry shell
```

## Documentation

● Project Name : **WeatherWarner**

● Description :
WeatherWarner is a Temperature Alert Agent using the uAgent library. The agent allows users to set their preferred temperature thresholds and location. It periodically fetches real-time weather data from a specified location using the Weatherstack API and alerts the user when the temperature exceeds the specified maximum or falls below the specified minimum threshold. The agent runs continuously, periodically checking the temperature and issuing alerts as needed, making it a useful tool for monitoring extreme temperatures in a specific location.

● Instructions to run the project : 
To run the Temperature Alert Agent code you provided, follow these instructions:

1. **Prerequisites**:
   - Ensure you have Python installed on your system.
   - Install required Python packages [uAgents,python-decouple].
   - Create a `.env` file and set the `weather_api` environment variable with your Weatherstack API access key.

2. **Run the script**:
   - Open a terminal and navigate to the directory containing the `main.py` file.
   - Run the script using `python main.py`.
   - Make sure to be in the uagents virtual environment.

4. **Agent Configuration**:
   - The agent will introduce itself and prompt you to enter your temperature thresholds (minimum and maximum) and location.
   - Follow the prompts to input these preferences.

5. **Running the Agent**:
   - After configuring the agent, it will run and periodically check the current temperature for the specified location.
   - If the temperature goes above the maximum or below the minimum threshold, the agent will log a warning and potentially send an alert (the `warn_mssg` function).

6. **Monitoring and Alerts**:
   - Keep the terminal running to allow the agent to continue monitoring temperatures.
   - You will receive alerts when extreme temperatures are detected.

7. **Stopping the Agent**:
   - To stop the agent, you can typically press `Ctrl+C` in the terminal where the script is running. The agent should handle shutdown signals gracefully.

## API INFORMATION

Remember to replace `"YOUR_WEATHERSTACK_API_KEY"` in the `.env` file with your actual Weatherstack API access key for accurate weather data retrieval. Additionally, ensure you have the necessary environment variables and packages correctly configured to run the code successfully.

● Where to get Weatherstack API key : 
- Visit https://weatherstack.com and sign in (sign up if you don't have an account already). You should be able to see the "Your API Access Key" Heading and right under that will be the free api key.
- Endpoint used (get) : http://api.weatherstack.com/current