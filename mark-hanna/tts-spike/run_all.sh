#!/usr/bin/env bash
# Run all TTS punctuation tests. Each generates a wav + measures silences.
# Output: results.txt with structured data per test.
set -e
cd "$(dirname "$0")"

# Test definitions: NAME|TEXT
TESTS=(
# === SENTENCE GAP TESTS — same content, different terminators ===
"gap_period|He came home. He left."
"gap_question|He came home? He left."
"gap_exclaim|He came home! He left."
"gap_ellipsis|He came home... He left."
"gap_emdash|He came home — He left."
"gap_semicolon|He came home; he left."
"gap_period_double_space|He came home.  He left."
"gap_period_newline|He came home.
He left."
"gap_period_blank_line|He came home.

He left."

# === MID-SENTENCE PAUSE TESTS ===
"mid_comma|He paused, then he spoke."
"mid_emdash|He paused — then he spoke."
"mid_ellipsis|He paused... then he spoke."
"mid_semicolon|He paused; then he spoke."
"mid_period|He paused. Then he spoke."
"mid_no_punct|He paused then he spoke."

# === YEAR / NUMBER READING ===
"year_bare|And in 1896 he did it."
"year_comma|And in 1896, he did it."
"year_with_word_year|And in the year 1896 he did it."
"year_apostrophe|It happened in '96."
"year_spelled|And in eighteen ninety-six he did it."
"year_other_1880|By 1880 he was rich."
"year_other_1837|Born in 1837."
"year_period_end|He left in 1896."

# === LIST-AS-FRAGMENT (Coal/Iron problem) ===
"list_two_capitalised|His business: Coal, iron."
"list_two_no_caps|His business: coal, iron."
"list_two_with_and|His business: coal and iron."
"list_three|His business: coal, iron, steel."

# === J.P. / INITIALS ===
"initials_dotted|J.P. Morgan paid."
"initials_no_dots|JP Morgan paid."
"initials_spaced|J. P. Morgan paid."
"initials_lower|j.p. Morgan paid."

# === LEADING WORD + COMMA (Banks problem) ===
"opener_word_comma|Banks, assessed at a quarter percent."
"opener_word_no_comma|Banks assessed at a quarter percent."
"opener_word_emdash|Banks — assessed at a quarter percent."
)

OUT=results.txt
echo "# TTS Punctuation Spike Results" > "$OUT"
echo "# Voice: bm_george (Kokoro 82M via hyperframes CLI)" >> "$OUT"
echo "# Generated: $(date)" >> "$OUT"
echo "" >> "$OUT"

i=1
total=${#TESTS[@]}
for test in "${TESTS[@]}"; do
    name="${test%%|*}"
    text="${test#*|}"
    echo "[$i/$total] $name"
    
    # Render
    echo "$text" > "${name}.txt"
    npx --yes hyperframes@latest tts "${name}.txt" --voice bm_george --output "${name}.wav" 2>/dev/null > /dev/null || { echo "  ERR" ; i=$((i+1)); continue; }
    
    # Measure
    DUR=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "${name}.wav")
    SILENCES=$(ffmpeg -hide_banner -i "${name}.wav" -af "silencedetect=noise=-40dB:d=0.05" -f null - 2>&1 | grep "silence_duration" | sed 's/.*silence_duration: //' | sed 's/^/    /')
    GAPS_INNER=$(ffmpeg -hide_banner -i "${name}.wav" -af "silencedetect=noise=-40dB:d=0.05" -f null - 2>&1 | grep "silence_duration" | sed 's/.*silence_duration: //' | head -n -1 | tail -n +2 | xargs)
    
    {
        echo "## $name"
        echo "TEXT: $text"
        echo "DURATION: ${DUR}s"
        echo "INNER_SILENCES: $GAPS_INNER"
        echo ""
    } >> "$OUT"
    
    i=$((i+1))
done

echo ""
echo "Done. Results in $OUT"
