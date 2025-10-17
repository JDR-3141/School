
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
  ais16 r16 d''16 r8 cis'16 r8 gis16 dis''16 a16 a16 gis'16
}