"""
This module provides asynchronous functions to fetch data from an API endpoint using aiohttp.
Functions:
```python
fetch_api(
    route: str, 
    access_token: str, 
    method: str = "GET", 
    data: dict = None) -> tuple[Response, int]:
```
-   Fetches data from an API endpoint using the specified HTTP method.

```python
bot_request(
    route: str, 
    method: str = "GET", 
    data: dict = None) -> tuple[Response, int]:
```
-   Makes an asynchronous HTTP request to a specified route with the given access token and method.

"""


import aiohttp, config
from flask import  Response


async def fetch_api(route:str, access_token:str, method:str="GET", data:dict=None)->tuple[Response, int]:
    """
    Fetches data from an API endpoint using the specified HTTP method.
    Args:
        route (str): The API route to fetch data from.
        access_token (str): The access token for authorization.
        method (str, optional): The HTTP method to use (default is "GET").
        data (dict, optional): The data to send in the request body for POST requests (default is None).
    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    Raises:
        requests.exceptions.RequestException: If an error occurs while making the HTTP request.
    """

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (https://discord.com, v1)",
        "Accept": "application/json"
    }
    _endpoint:str = config.BASE_API+route
    async with aiohttp.ClientSession(headers=headers) as session:
        if method.upper() == "GET":
            async with session.get(_endpoint) as response:
                return await response.json(), response.status
        elif method.upper() == "POST":
            async with session.post(_endpoint, json=data) as response:
                return await response.json(), response.status
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")




async def bot_request(route: str, method: str = "GET", data: dict = None) -> tuple[Response, int]:
    """
    Makes an asynchronous HTTP request to a specified route with the given access token and method.
    
    Args:
        route (str): The API route to send the request to.
        method (str, optional): The HTTP method to use for the request (default is "GET").
        data (dict, optional): The data to send with the request if the method is "POST" (default is None).
        
    Returns:
        tuple: A tuple containing the JSON response and the status code.
    """
    headers = {
        "Authorization": f"Bot {config.TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (https://discord.com, v1)",
        "Accept": "application/json"
    }
    _endpoint: str = config.BASE_API + route

    async with aiohttp.ClientSession(headers=headers) as session:
        if method.upper() == "GET":
            async with session.get(_endpoint) as response:
                return await response.json(), response.status
        elif method.upper() == "POST":
            async with session.post(_endpoint, json=data) as response:
                return await response.json(), response.status
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
