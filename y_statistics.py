#
#   Scrapes Video Links from user Playlist
#   and Tests Youtube functionality on Google Chrome
#   Also Downloads audio using youtube-dl
#
# Modules
import sys
import urllib.request, urllib.response, urllib.error
from bs4 import BeautifulSoup
import re
from apiclient.discovery import build
from oauth2client.tools import argparser
class SoupScrape:
    #
    def GetStats(self, code):
        #
        video_url = 'http://www.youtube.com/watch?v=' + code
        startpage = urllib.request.urlopen(video_url)
        soup = BeautifulSoup(startpage.read(), "lxml")
        # Get Number of Views
        rawview_data = soup.find('div', {'class': 'watch-view-count'})
        view_number = rawview_data.contents[0]
        view_number = re.sub('[^0-9]', '', view_number)
        # Get Number of Likes and Dislikes
        raw_like = soup.find('button', {'class': 'like-button-renderer-like-button'})
        raw_dislike = soup.find('button', {'class': 'like-button-renderer-dislike-button'})
        # Likes
        likes = raw_like.contents[0]
        for data in likes:
            num_of_likes = data

        # Dislikes
        dislikes = raw_dislike.contents[0]
        for data in dislikes:
            num_of_dislikes = data
        #video name
        raw_name=soup.find('span', {'class': 'watch-title'})
        video_name=raw_name.contents[0]
        video_name=video_name.replace('\n', '')
        print(video_name,"-","VIEWS",view_number, "-", "LIKES", num_of_likes, "-","DISLIKES", num_of_dislikes,'\n')


DEVELOPER_KEY = "AIzaSyBz8CStqmIgMBC_-RvQrBh9Is3m2aaM7Iw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"



#   Youtube Search Functions 

def youtube_search(search_string, max_results=25):
    input = search_string.q
    print(input)
    outfile = open('temp.txt', 'w')
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(q=search_string.q, part="id,snippet", maxResults=max_results).execute()
    videos = []
    # Add each result to the appropriate list, and then display the lists of
    # matching videos
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))

    for x in range(0, len(videos)):
        outfile.write(videos[x] + '\n')

    outfile.close()


def search(artist):
    argparser.add_argument("--q", help="Search term", default=artist)
    argparser.add_argument("--max-results", help="Max results", default=5)
    args = argparser.parse_args()
    youtube_search(args)


# Main Program

if __name__ == "__main__":
    #
    # Youtube Search
    #
    artist = sys.argv[1]
    search(artist)

    stat_fetch = SoupScrape()
    songcode_list = []
    video_file = open('temp.txt', 'r')
    video_list = video_file.readlines()
    for line in video_list:
        song = line
        begin = (len(song) - 2) - 11
        end = begin + 11
        song_code = song[begin:end]
        songcode_list.append(song_code)
    for code in songcode_list:
        stat_fetch.GetStats(code)
    video_file.close()
