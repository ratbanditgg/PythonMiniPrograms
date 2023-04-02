from pytube import YouTube

url = "https://www.youtube.com/watch?v=Ns4LCeeOFS4&t=320s"

yt = YouTube(url)

#Title of video
print("Title: ",yt.title)
#Number of views of video
print("Number of views: ",yt.views)
#Length of the video
print("Length of video: ",yt.length,"seconds")
#Description of video
print("Description: ",yt.description)
#Rating
print("Ratings: ",yt.rating)