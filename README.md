# Planet Builder

Planet Builder is a command line script that will generate equirectangular textures from a specified spaceengine texture pack.

### Prerequisites

Planet Builder requires a few external python modules.
Make sure to install the requirements before running the script.
`$> pip install -r .\requirements.txt` 

You will also need to install the wanted texture pack from [Solar System HD](http://spaceengine.org/download/official-addons/solar-system-hd/) or [Solar System Ultra](http://spaceengine.org/download/official-addons/solar-system-uhd/)

## Docs

Running the planet builder script is relatively easy.

-h | *help:* Shows a list of all avaliable commands.

-s | *source:* Path to parent folder containing the folders "pos_x", "neg_y"...

-r | *resolution:* Resolution of the LOD. To check all possibles resolution, navigate into your textures folder and check the first character of your files. (eg. '5_0_0.png', 5). If no resolution is specified then the script will use the highest resolution avaliable.

### Examples
See a list of avaliable commands.
`$> main.py -h`

Example of using the script.
`$> main.py -s "C:/Users/user/Downloads/Earth-Surface-PBC-128k-1/textures/planets/Earth/Surface-PBC" -r 5`

*Warning: The time it takes for the script to run is entirely dependant on the resolution (16k, 32k...). Times can vary from a couple minutes to a couple hours.*

## Built With

* [Visual Studio Code](https://code.visualstudio.com/)

## Author

* **Christopher Hosken** - *Initial work* - [Christopher-Hosken](https://github.com/Christopher-Hosken)

## Acknowledgements

c2e converter from [py360convert](https://github.com/sunset1995/py360convert)
