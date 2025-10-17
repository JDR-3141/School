
\version "2.25.12"
\new Voice \with {
  \remove Note_heads_engraver
  \consists Completion_heads_engraver
  \remove Rest_engraver
  \consists Completion_rest_engraver
}
{
  \clef treble
   \time 4/4
  \key bes \major
  d'4. c'8 ais4 a4 ais4 c'4 ais2
}