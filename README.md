# gifmaker
Upload your facebook picture and create an #AllinOnClimate gif.

## Instructions

First, clone this repository:

```
git clone git@github.com:ClimateVoice/gifmaker.git
cd gifmaker
```

Now put your facebook profile picture in this folder as a .PNG and rename it to 1.png (replace the existing image in there!). Note that LinkedIn images are the ideal dimensions here for this program.

![](https://github.com/ClimateVoice/gifmaker/blob/master/1.png)

Next, run the script:

```
virtualenv myenv
source myenv/bin/activate
pip install -r requirements.txt
python3 create_gif.py
```

Now you have a gif like the one below (Gif-2020-43-07-16-43-07.png).

![](https://github.com/ClimateVoice/gifmaker/blob/master/Gif-2020-43-07-16-43-07.gif?raw=true)

Lastly, make this your new Twitter, LinkedIn, or Facebook profile picture to help spread the word!! :)

## Alternative using giphy

Alternatively, you could use the [gifmaker on giphy](https://giphy.com/create/gifmaker). Just upload your three images (profile picture, 2.png, 3.png) and it will create/host the gif for you! If you pursue this option, here are the other 2 pictures you need:

![](https://github.com/ClimateVoice/gifmaker/blob/master/2.png)
![](https://github.com/ClimateVoice/gifmaker/blob/master/3.png)

## A bit more about ClimateVoice
Our mission is to mobilize the voice of the workforce to urge companies to go "all in" on climate, both in business practices and policy advocacy. More info @ https://climatevoice.org 

## References
* [ClimateVoice website](https://climatevoice.org)
* [Protea](http://protea.earth)
