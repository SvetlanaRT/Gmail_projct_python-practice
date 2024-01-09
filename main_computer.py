def main_computer(Data):
    # Const
    Data['Const']['BrakeDistance'] = 5

    # Init
    Data['ErrorCode'] = 'Null'
    Data['current_Index'] = 0
    Data['OutPos'] = {'x': [], 'y': []}

    # Drive
    while Data['ErrorCode'] == 'Null':
        Data['current_Index'] += 1
        Data = Drive(Data)

    return Data


def Drive(Data):
    if Data['current_Index'] == len(Data['pos']['x']) - 1:
        Data['ErrorCode'] = 'End of trajectory'
        return Data

    Data['curr_Pos']['x'] = Data['pos']['x'][Data['current_Index'] + 1]
    Data['curr_Pos']['y'] = Data['pos']['y'][Data['current_Index'] + 1]
    Data['OutPos']['x'].append(Data['curr_Pos']['x'])
    Data['OutPos']['y'].append(Data['curr_Pos']['y'])
    Data = CheckCollision(Data)

    return Data


def CheckCollision(Data):
    diffX = Data['Const']['Obstacle'][0] - Data['curr_Pos']['x']
    diffY = Data['Const']['Obstacle'][1] - Data['curr_Pos']['y']
    Range = (diffX ** 2 + diffY ** 2) ** 0.5

    if Range < Data['Const']['BrakeDistance']:
        Data['Obstacle'] = True
        Data['ErrorCode'] = 'Hit Obstacle'
        return Data
    else:
        Data['Obstacle'] = False

    return Data


# Usage
# Assuming you have already read the trajectory file and initialized Data
# Data = {'pos': {'x': [values], 'y': [values]}, 'curr_Pos': {'x': 0, 'y': 0}, 'Const': {'Obstacle': [30, 30]}}
# main_computer(Data)
# print(Data['OutPos'])

