#! usr/bin/python3
message = 'the movie is about to begin, we recommed '
print(' what is you conn speed in mbps?')
connection = float(input())
if connection >= 25:
    message = message + 'setting vid to 4k'
elif connection >= 5:
    message = message + 'setting vid to 1080p'
elif connection >=2:
    message = message + 'setting vid to 720p'
else: 
    message = message + 'finding another access network.'
    
print(message)

