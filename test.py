
import urllib.request, urllib.response, urllib.error
from bs4 import BeautifulSoup
import re
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
        print(video_name,"-","VIEWS",view_number, "-", "LIKES", num_of_likes, "-","DISLIKES", num_of_dislikes)


#
# Main Program
if __name__ == "__main__":
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



