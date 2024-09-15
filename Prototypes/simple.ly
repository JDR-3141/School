
\version "2.12.3"
\new Voice \with {
  \remove Note_heads_engraver
  \consists Completion_heads_engraver
  \remove Rest_engraver
  \consists Completion_rest_engraver
}
{
  \clef treble
  \time 4/4
  c'2. f'4. g'1 c'2..
}
