import re
from moviepy.editor import VideoFileClip, concatenate

video = VideoFileClip("C:/Users/owner/Desktop/greppy/Thundercats1.mp4")

cuts = re.findall("mutants",text) != []

def assemble_cuts(cuts, outfile):
    final = concatenate([video.subclip(start,end)
                       for (start,end) in cuts])
    final.to_videofile(outfile)

assemble_cuts(cuts, "mut.mp4")
# shame such an awesome library isn't working right
