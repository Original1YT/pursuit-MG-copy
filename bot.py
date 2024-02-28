# pylint: disable=global-statement, line-too-long, invalid-name, missing-function-docstring, missing-module-docstring

import json
import random
import sys

import socketio


logger = True
engineio_logger = False

sio = socketio.Client(logger=logger, engineio_logger=engineio_logger)

my_sid = None
my_tank = None

#A bunch of variables to store Enemy's SIDs
EnemySID = [["", "", ""], ["", "", ""]]



gameUpdateMessagePublic = json 
###############################################################################
# Authentication Methods
###############################################################################

def send_authentication():
    username = sys.argv[1]
    password = sys.argv[2]
    sio.emit('authenticate', {'data': f'{username}:{password}'})


@sio.event
def connect():
    print('connected to server')
    send_authentication()


@sio.event
def auth_response(message):
    global my_sid
    global my_tank

    print(f'auth_response: {message}')
    if message['data'] == 'SUCCESSFUL':
        my_sid = message['sid']
        my_tank = message['tank']
        sio.emit('game_queue', {'data': 'queue'})

###############################################################################
# Game Update Handler
###############################################################################
try:
    game_update_message = json.loads(message['data'])
except:
    game_update_message = ""
allTankNames = [["myTank", "Tank1", "Tank2", "Tank3" ], ["my_sid", "", "", "" ]]
tEMPINPUTNUMBER = 0
tARGET_NUMBER = 0
tARGET_INPUT = ["", "", "", ""]
cONFIRMATION_TEXT = "1"
while(tEMPINPUTNUMBER < 3):
    tEMPINPUTNUMBER = tEMPINPUTNUMBER + 1
    tARGET_NUMBER = tARGET_NUMBER + 1
    print(f'Enter Target no.[{tARGET_NUMBER}]')
    tARGET_INPUT[tARGET_NUMBER] = input()
    if(tARGET_INPUT[tARGET_NUMBER] == "RANDOM"):
        print(f'please confirm that you want the rest of your target list to be random targets by typing [{cONFIRMATION_TEXT}], if you do not, and want "RANDOM" to be your target, press enter:')
        cONFIRMATION_TEXT = input()
        if(cONFIRMATION_TEXT == "1"):
            tEMPINPUTNUMBER = 3
            #break #DELETE THIS ONCE CODE IS COMPLETE
            game_update_message
            #
            # CREATE CODE FOR RANDOM TARGET SELECTION HERE
            #
            #
            #
        else:
            tARGET_INPUT[tARGET_NUMBER] = "RANDOM"


##########################################
# This is a function to break an update
# method into multiple smaller pieces
##########################################
def UpdateChunkr(game_update_message, UpdatePiece):
    #searches for an enemy's SID and assigns it to "1"
    if(UpdatePiece = "Enemy_SID_1")

@sio.event
def game_start(message):
    global my_tank
    print(f'game_start: {message}')
    my_tank = message['data']

@sio.event
def game_update(message):
    # Convert the message string to an object that you can use
    game_update_message = json.loads(message['data'])
    gameUpdateMessagePublic = game_update_message
    # So that it is easier to see your actions, this will only show your tank. Comment this out to see all tanks.
    tank = next((t for t in game_update_message['tanks'] if t['name'] == my_tank), None)
    if tank:
        print(f'game_update: {tank}')

    # Uncomment the following line to see all tanks and game world information.
    # print(f'game_update: {message}')

    # This is where you will add your code to control your tank.

    # Tank actions you can emit
    #   tank_action_change_direction
    #   tank_action_change_speed
    #   tank_action_shoot

    # Example code to move your tank randomly.
    action = random.choices(
        population=['MOVE', 'SHOOT', 'NONE'],
        weights=[0.8, 0.15, 0.05],
    )
    if action[0] == 'MOVE':
        print('action: move')
        move()
    elif action[0] == 'SHOOT':
        print('action: shoot')
        sio.emit('tank_action_shoot')
    else:   # action == 'NONE'
        print('action: none')



###############################################################################
# Action Methods
###############################################################################

def move():
    move_or_speed = random.choice(['MOVE', 'SPEED'])
    if move_or_speed == 'MOVE':
        direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        print(f'change_direction: {direction}')
        sio.emit('tank_action_change_direction', {'data': direction})
    else:   # move_or_speed == 'SPEED'
        velocity = random.randint(0, 2)
        print(f'tank_action_change_speed: {velocity}')
        sio.emit('tank_action_change_speed', {'data': velocity})


###############################################################################
# Start the Application
###############################################################################

if __name__ == '__main__':
    sio.connect('http://72.14.182.150:5000/')
    sio.wait()
