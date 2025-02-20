import requests
from datetime import datetime, timezone
import xmltodict
import math


response = requests.get(url='https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')



def data_range(response: str) -> None:
    '''
    This functions purpose is to give the data range for the epochs from the first to last one

    Arguments:

    reponse: the xml converted string file we are using to pull the data from. The XML file was created from the ISS data found in the nasa website

    Returns:

    It is supposed to return a statement which contains the date range which is present for the whole datset. If there is an error then it is supposed to return an "error" message.

    '''

    epochs = [line.strip() for line in response.split('\n') if '<EPOCH>' in line]

    if epochs:
        first_epoch = epochs[0].split('>')[1].split('<')[0]
        last_epoch = epochs[-1].split('>')[1].split('<')[0]


        first_time = datetime.strptime(first_epoch, "%Y-%jT%H:%M:%S.%fZ")
        last_time = datetime.strptime(last_epoch, "%Y-%jT%H:%M:%S.%fZ")

        print(f"Data range is from {first_time} to {last_time}")
    else:
        print("Error")






def current_epoch(response: str) -> None:
    '''

    This function is used to output the epoch which is closest in time to when the program is run. It will change everytime the program is run.

    Arguments:    

response: variable under which we stored the xml data which we pulled from NASA website. Used xmltodict to parse through the data.

    Returns:

    The output of this function is to print out the whole epoch which is closest to the time which the program is run.

    '''

    data = xmltodict.parse(response)

    state_vector = data['ndm']['oem']['body']['segment']['data']['stateVector']

    current_time = datetime.now(timezone.utc)
    close_epoch = min(state_vector, key=lambda x: abs((datetime.strptime(x['EPOCH'], "%Y-%jT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc) - current_time).total_seconds()))

    for i, j in close_epoch.items():
        if i in ['X', 'Y', 'Z']:
            print(f"{i}: {j} km")
        elif i in ['X_DOT', 'Y_DOT', 'Z_DOT']:
            print(f"{i}: {j}")
        else:
            print(f"{i}: {j}")


def average_speed(response: str) -> None:
    data = xmltodict.parse(response)
    state_vector = data['ndm']['oem']['body']['segment']['data']['stateVector']


    overall_speed = []
    all_epochs = []
    all_speed = []


    for i in state_vector:
        speed = math.sqrt(float(i['X_DOT']['#text'])**2 + float(i['Y_DOT']['#text'])**2 + float(i['Z_DOT']['#text'])**2)
        all_speed.append(speed)

        all_epochs.append(datetime.strptime(i['EPOCH'], "%Y-%jT%H:%M:%S.%fZ"))

        overall_speed += all_speed


    average_speed = sum(overall_speed) / len(all_speed)
    print(f"Average speed for the dataset: {average_speed}")

    current_time = datetime.now(timezone.utc)
    close_epoch = min(range(len(all_epochs)), key=lambda x: abs((all_epochs[x].replace(tzinfo=timezone.utc) - current_time).total_seconds()))

    instant_speed = all_speed[close_epoch]

    print(f"Instataneous Speed: {instant_speed}")



def main():
    print(data_range(response.text))
    print(current_epoch(response.text))
    print(average_speed(response.text))



if __name__ == '__main__':
    main()
