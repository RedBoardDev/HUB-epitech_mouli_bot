import requests

def r_get_json_request(link:str):
    return (requests.get(link).json())

def r_get_last_project(link:str):
    r = r_get_json_request("https://intra.epitech.eu/planning/load?format=json")[-1]
    return (r)
