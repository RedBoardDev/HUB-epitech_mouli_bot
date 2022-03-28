from dotenv import dotenv_values

secrets = dotenv_values(".env")

def e_get_email():
    account_email = secrets["ACCOUNT_EMAIL"]
    return (account_email)

def e_get_mdp():
    account_mdp = secrets["ACCOUNT_MDP"]
    return (account_mdp)