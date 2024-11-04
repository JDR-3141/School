
\version "2.25.12"
\new Voice \with {
  \remove Note_heads_engraver
  \consists Completion_heads_engraver
  \remove Rest_engraver
  \consists Completion_rest_engraver
}
{
  \clef treble
   \time 3/4
  \key ees \major
  d'4. ees'8 d'8 ees'8 d'8 bes8 g2 d'8 ees'8 d'8 ees'8 d'8 ees'8 g'4. ees'8 d'8 ees'8 d'8 bes8 g1~ 1~ g2.
}