![Heroku](http://heroku-badge.herokuapp.com/?app=foroba-blon)

# Foroba Blon - Simple Poll System
This repository holds the _Foroba Blon Simple Poll_ system prototype project. It was part of the project assignment of a seven-week Master course called "ICT4D: Information and Communication Technology for Development" at the Vrije Universiteit (https://www.vu.nl/).

This project is based on Foroba Blon, which is part of W4RA (https://w4ra.org/w4ra/) and tries to use computer science to help sustainable rural development. Foroba Blon tries to help rural communities to allow citizen journalism, with a voice-based/phone-based service, to call to the radio station (https://w4ra.org/foroba-blon-community-radio-in-africa-and-the-web/) and allow people to vote, or leave voice messages. The project uses Kasadaka to accomplish this; more information about Kasadaka can be found in the section called Kasadaka.

## Context
The project is done for people in rural areas. In these areas, literacy is not always high, and digital literacy can even be lower. Therefore the solution is made in such a way that it would fit these needs.

# Video
[![Foroba-Blon-SPS](https://i.imgur.com/D2mJKFh.png)](https://www.youtube.com/watch?v=sUhDYByVE2s "Foroba-Blon-SPS Demo - Click to Watch!")

# Participants
The names of the participants are:
- [Markus Funke](https://github.com/FunkeMT) 
- [Wouter Kok](https://github.com/wkokgit)
- [Sven Preng](https://github.com/mrthefastfender)
- [Pjotr Scholtze](https://github.com/pjotrscholtze)

# Kasadaka
Kasadaka is a Django based solution for managing voice-based services. Kasadaka is made explicitly for ICT4D, and generates VXML documents that contain the voice menus, references, and links back to Kasadaka to create new and dynamic documents. We extended the Kasadaka platform for our project with new features. The project is forked from the original Kasadaka repository: https://github.com/abaart/KasaDaka-VSDK

# How does it work
The project allows two actors to operate with the platform, the radio host, and the listener. The radio host sets up a question, and the callers can call to our platform. The system will answer the call, and then the caller can vote with the keypad of their phone and leave a message. The radio host can see the results on a webpage and can playback individual voice messages.

# License
The MIT License (MIT)

Copyright (c) 2020 Markus Funke, Sven Preng, Wouter Kok, Pjotr Scholtze

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




