import os

import requests


def lambda_handler(event, context):
    client_id = 'BO_n7nTIlMljdvU6kRRB3g'
    redirect_uri = 'https://auth.asf.alaska.edu/login'
    state = 'https://s1qc.asf.alaska.edu/aux_poeorb/S1A_OPER_AUX_POEORB_OPOD_20240301T070741_V20240209T225942_20240211T005942.EOF'
    url = f'https://urs.earthdata.nasa.gov/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&state={state}'

    auth = (os.environ['USERNAME'], os.environ['PASSWORD'])

    response = requests.get(url, auth=auth)
    response.raise_for_status()
