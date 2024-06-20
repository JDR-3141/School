# https://pypi.org/project/lilypond/
import subprocess
import lilypond
text = """
\\version "2.12.3"
\\relative
{
    \clef treble
    \\time 4/4
    \\tempo "Swing" 4 = 100
    \key g \minor
    g'8 a bes c a4 f8 g8~
    2 r2
}"""
# 1 "'" is middle c upwards, remove "'" means octave below, from there add "'" and "," to change octaves
f = open("c:/Users/jdraj/OneDrive/Documents/GitHub/School/Prototypes/simple.ly","w")
f.write(text)
f.close()
subprocess.run([lilypond.executable(), "c:/Users/jdraj/OneDrive/Documents/GitHub/School/Prototypes/simple.ly"])
