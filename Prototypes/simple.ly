
\version "2.12.3"
\new Voice \with {
  \remove Note_heads_engraver
  \consists Completion_heads_engraver
  \remove Rest_engraver
  \consists Completion_rest_engraver
}
{
  \clef treble
  \time 3/8
  c'8. f'2 g'4..
}
