# Super Mario for Terminal
Super Mario game for terminal without using in-built pygame libraries.

## Controls
W - JUMP
A - MOVE LEFT
D - MOVE RIGHT

## Objects on screen

* Mario
* Clouds
* Bridges
* Pillars
* Normal enemies
* Boss enemies
* Coins

## External dependencies

* Numpy
* Colorama

## Install dependencies
``` pip -r requirements.txt ```

## Play the game
``` python3 main.py ```

## Directory structure
```
├── classes.py  
├── collision.py  
├── creator.py  
├── generator.py  
├── input.py  
├── main.py  
├── README.md  
├── requirements.txt  
└── sounds  
    ├── smb_1-up.wav  
    ├── smb_coin.wav  
    ├── smb_flagpole.wav  
    ├── smb_gameover.wav  
    ├── smb_jump-small.wav  
    └── smb_mariodie.wav  
```
## Additional Notes

* There are 3 levels in total
* Level is increased based on the score attained
* Mario has 3 lives to start with
* Once a final score is reached in the final level, game exits

## License
The MIT License https://rohanc.mit-license.org/  
Copyright &copy; 2019 Rohan Chacko <rohanchacko007@gmail.com>
