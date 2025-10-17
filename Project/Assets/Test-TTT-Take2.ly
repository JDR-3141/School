
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
  d'4~ d'16 cis16 c'16 r16 ais'8. a'16 a'4 ais'8. r16 c'8. c16 ais'4
}