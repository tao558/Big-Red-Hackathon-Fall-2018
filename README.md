# Big-Red-Hacks-Fall-2018

## What are we doing?

Big-Red-Hacks-Fall-2018

### Cornell University, October 19-21
Contributors:
* Carter Nesbitt
* Tom Osika

## What are we doing?

We are making a program in Python to both encode and decode hidden messages in images. This is a specific type of cryptography called steganography.

## How does steganography work?

There are many different ways to embed messages inside images. That being said, we are using the least significant bit method. This works by modifying the least significant bits of the various red, green and blue components of each pixel in an image. As long the encoding and decoding algorithms know which bits to look at, and in the correct order of encryption, then messages can successfully be sent through images. 

## Does the image look any different after encryption?

Technically, yes. However, in reality, if encrypted correctly, humans should not be able to notice any difference between the encoded image and the original. This is mainly as a result of the significance of the bits that are being modified. There are eight bits to each of the three components of a standard pixel, which can be represented in decimal as an integer with a range from 0 to 255. If the last two bits of this value are being modified, then the decimal value of a given component can be changed by at most 3.

## How do I encrypt and decrypt an image using this program?

First, clone this repository. Next, put the image you want to encrypt or decrypt in the working repository, and run the command [python3 encryption.py] or [python3 decryption.py] from the terminal, respectively. You will be prompted to enter the image name, the message to be encrypted (if you are running encryption.py), and the password. If you enter the incorrect password when decrypting the image, you will not obtain the correct message.

## What does the password change about the encryption process?

The password that is used works as a key to the program. The program knows where to look for the first bit of the message based on the password. This is why the output message is nonsense if the incorrect password is given when decrypting. If you see a message when decrypting along the lines of "There were 'x' encoding errors.", this is a sign that you may have entered the incorrect password. However, the actual output of the decryption might be a pretty good indicator of this.

## Why are you doing this?

Why not? Have you never wanted to send a super secret message to someone via an image?
