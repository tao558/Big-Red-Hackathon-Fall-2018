# Big-Red-Hacks-Fall-2018

## What are we doing?

Big-Red-Hacks-Fall-2018
___
### Cornell University, October 19-21
Contributors:
* Carter Nesbitt
* Tom Osika

## What are we doing?
___
We are making a program in Python to both encode and decode hidden messages in images. This is a specific type of cryptography called steganography.

## How does steganography work?
___
There are many different ways to embed messages inside images. That being said, we are using the least significant bit method. This works by modifying the least significant bits of the various red, green and blue components of each pixel in an image. As long the encoding and decoding algorithms know which bits to look at, and in the correct order of encryption, then messages can successfully be sent through images. 
## Does the image look any different after encryption?
___
Technically, yes. However, in reality, if encrypted correctly, humans should not be able to notice any difference between the encoded image and the original. This is mainly as a result of the significance of the bits that are being modified. There are eight bits to each of the three components of a standard pixel, which can be represented in decimal as an integer with a range from 0 to 255. If the last two bits of this value are being modified, then the decimal value of a given component can be changed by at most 3.
## Why are you doing this?
___
Why not? Have you never wanted to send a super secret message to someone via an image?
