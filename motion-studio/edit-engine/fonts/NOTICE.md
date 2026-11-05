# Caption fonts

TTF copies of the WOFF2 files already in the repo, renamed to unique family names so libass finds them by name. All
of them are under the SIL Open Font License 1.1 (https://openfontlicense.org), which allows commercial use,
embedding and modification. A renamed modified version may not use the original Reserved Font Name.

| File | Family name used in captions | Original | Source in repo |
|---|---|---|---|
| Montserrat-900.ttf | Montserrat Black | Montserrat (Julieta Ulanovsky et al.) | projects/straightscale-03/assets/fonts |
| Montserrat-800.ttf | Montserrat ExtraBold | Montserrat | same |
| Montserrat-600.ttf | Montserrat SemiBold | Montserrat | same |
| PlayfairDisplay-900-italic.ttf | Playfair Black Italic | Playfair Display (Claus Eggers Sørensen) | same |
| Inter-700.ttf | Inter Bold | Inter (Rasmus Andersson) | .claude/skills/talking-head-recut/assets/fonts |
| Caveat-700.ttf | Caveat Bold | Caveat (Impallari Type) | same |

The files are Latin subsets. For other scripts (Cyrillic, Greek, Hebrew, Arabic and so on), add a full TTF here.
To add a brand font, convert it to TTF, give it a unique family name (nameIDs 1 and 4), and use that name in the
style's `captions.font`.
