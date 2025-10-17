
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
  d'4. ees'8 d'8 ees'8 d'8 bes'8 g2 d'8 ees'8 d'8 ees'8 d'8 ees'8 g'4. ees'8 d'8 ees'8 d'8 bes'8 g2 g16 g16 g'8 g'4 g'4 g'8. g'16 r16 g'16 g'16 g'16 r16 g'16 g'16 g'16 r16 g'16 g'16 r8. g'16 g'16
}