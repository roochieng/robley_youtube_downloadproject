# Youtube Downloader project

import requests

from pytube import YouTube
from pytube.streams import Stream

YouTube("https://www.youtube.com/watch?v=DPnqb74Smug").streams.get_highest_resolution().download()

# This should work