# .wav-sample-extractor
## What is it?
This python script makes use of the [aubio](https://aubio.org/) python library to extract sample data from a .wav file.

## How does it work?
For my specific use, it extracts the data from a .wav file that I composed in [Ableton Live](https://www.ableton.com/en/live/what-is-live/) and converts the resulting ***numpy.array*** into an array of ***floats***, due to the less than precise nature of extracting sample data from a .wav file, some of the data required additional processing including normalization, and manual bounds adjustment. 
<br/>
This is then output to a .csv or .txt file for other use cases.

## Why?
I made this script to use music sample data for a Unity game project I am working on for the 2022 [inclusive coding festival](https://www.inclusivecodingfestival.org/)! My plan is to use this data to maniplate the physical appearance of in-game objects in sync with the music that is playing. I decided to use this approach to avoid the resource usage involved with real time data processing during game execution.

