# https://pypi.org/project/lilypond/
import subprocess
import lilypond
text = """
\\version "2.12.3"
\\new Voice \\with {
  \\remove Note_heads_engraver
  \\consists Completion_heads_engraver
  \\remove Rest_engraver
  \\consists Completion_rest_engraver
}
{
  \\clef treble
  \\time 3/8
  c'8. f'2 g'4..
}
"""
# 1 "'" is middle c upwards, remove "'" means octave below, from there add "'" and "," to change octaves
f = open("c:/Users/jdraj/OneDrive/Documents/GitHub/School/Prototypes/simple.ly","w")
f.write(text)
f.close()
subprocess.run([lilypond.executable(), "c:/Users/jdraj/OneDrive/Documents/GitHub/School/Prototypes/simple.ly"])
