#importing all required modules
from uagents import Agent, Context
import requests
from helper import warn_mssg #import from .src/helper.py
from decouple import Config

config = Config(".env")

# Access environment variables
weather_api = config.get("weather_api")

#Initialise agent
agent = Agent(name="WeatherWarner",seed="WWseed")

@agent.on_event("startup")
async def introduce_agent(ctx: Context):

    #Let the agent introduce itself
    ctx.logger.info(f"Hello, I'm agent {ctx.name} and I will warn you about extreme temperatures.\n")

    #Taking in the user input for temperature threshold range
    minT=int(input("Enter the Minimum threshold in °C: "))
    maxT=int(input("Enter the Maximum threshold in °C: "))

    #Assesrting that the min temp threshold is smaller than the max temothreshold
    assert maxT>=minT, "Maximum threshold should be greater than or equal to Minimum threshold!"

    #Taking in the user input for location
    loca=input("Enter your location: ")

    #Using agent storage to store the thresholds as well as the location
    ctx.storage.set("min_thresh",minT)
    ctx.storage.set("max_thresh",maxT)
    ctx.storage.set("loc",loca)

#Agent will perform this function at the interval of every 10 seconds
@agent.on_interval(period=10.0)
async def Check_temp(ctx: Context):

    #Get the location stored by the agent
    local=ctx.storage.get("loc")

    #Define the request parameters for the Weatherstack API
    params = {
    'access_key': weather_api,
    'query': {local}
    }

    #send a http request to weatherstack
    response = requests.get("http://api.weatherstack.com/current", params)
    res=response.json()

    #Get the thresholds stored by the agent
    maxt=ctx.storage.get("max_thresh")
    mint=ctx.storage.get("min_thresh")

    location=res['request']['query']

    #If the current temperature of the location specified is outside of the threshold range, then alert the user 
    if (res['current']['temperature']>maxt):
        ctx.logger.warning(f"TEMPERATURE IS ABOVE {maxt} °C in {location}")
        warn_mssg(f"TEMPERATURE IS ABOVE {maxt} °C in {location}")

    elif (res['current']['temperature']<mint):
        ctx.logger.warning(f"TEMPERATURE IS BELOW {mint} °C in {location}")
        warn_mssg(f"TEMPERATURE IS BELOW {mint} °C in {location}")

if __name__ == "__main__":
    agent.run()
