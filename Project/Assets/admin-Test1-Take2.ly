
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
  \key c \major
  c'4 c'8 g8 c'4 c'8 d'8 e'8 d'16 d'16 c'8 d'8 c'2
}