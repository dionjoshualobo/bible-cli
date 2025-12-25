"""Book metadata: full names, accepted abbreviations, and printable lists.

This module centralizes the book name mapping and the printed
Old/New Testament tuples so the main CLI can import them without
dumping a very long list in `bible`.
"""

# Standard Bible book abbreviations mapping
# Format: 'Book Name': [list of accepted abbreviations]
BOOK_ABBREVIATIONS = {
    # Old Testament
    'Genesis': ['gen', 'gn', 'genesis'],
    'Exodus': ['ex', 'exo', 'exod', 'exodus'],
    'Leviticus': ['lev', 'lv', 'leviticus'],
    'Numbers': ['num', 'nm', 'numb', 'numbers'],
    'Deuteronomy': ['deut', 'dt', 'deu', 'deuteronomy'],
    'Joshua': ['josh', 'js', 'jos', 'joshua'],
    'Judges': ['judg', 'jud', 'jdg', 'judges'],
    'Ruth': ['ruth', 'rt', 'rut'],
    '1 Samuel': ['1sam', '1sm', '1samuel', '1 sam', '1 samuel'],
    '2 Samuel': ['2sam', '2sm', '2samuel', '2 sam', '2 samuel'],
    '1 Kings': ['1kgs', '1ki', '1kings', '1 kings', '1 kgs'],
    '2 Kings': ['2kgs', '2ki', '2kings', '2 kings', '2 kgs'],
    '1 Chronicles': ['1chr', '1ch', '1chronicles', '1 chronicles', '1 chr'],
    '2 Chronicles': ['2chr', '2ch', '2chronicles', '2 chronicles', '2 chr'],
    'Ezra': ['ezra', 'ezr'],
    'Nehemiah': ['neh', 'ne', 'nehemiah'],
    'Esther': ['esth', 'et', 'est', 'esther'],
    'Job': ['job'],
    'Psalms': ['ps', 'psa', 'psalm', 'psalms'],
    'Proverbs': ['prov', 'prv', 'pro', 'proverbs'],
    'Ecclesiastes': ['eccl', 'ec', 'ecc', 'ecclesiastes'],
    'Song of Solomon': ['song', 'so', 'sos', 'songofsolomon', 'song of solomon'],
    'Isaiah': ['isa', 'is', 'isaiah'],
    'Jeremiah': ['jer', 'jr', 'jeremiah'],
    'Lamentations': ['lam', 'lm', 'lamentations'],
    'Ezekiel': ['ezek', 'ez', 'eze', 'ezekiel'],
    'Daniel': ['dan', 'dn', 'daniel'],
    'Hosea': ['hos', 'ho', 'hosea'],
    'Joel': ['joel', 'jl', 'joe'],
    'Amos': ['amos', 'am'],
    'Obadiah': ['obad', 'ob', 'oba', 'obadiah'],
    'Jonah': ['jonah', 'jon'],
    'Micah': ['mic', 'mi', 'micah'],
    'Nahum': ['nah', 'na', 'nahum'],
    'Habakkuk': ['hab', 'hk', 'habakkuk'],
    'Zephaniah': ['zeph', 'zp', 'zep', 'zephaniah'],
    'Haggai': ['hag', 'hg', 'haggai'],
    'Zechariah': ['zech', 'zc', 'zec', 'zechariah'],
    'Malachi': ['mal', 'ml', 'malachi'],
    # New Testament
    'Matthew': ['matt', 'mt', 'mat', 'matthew'],
    'Mark': ['mark', 'mk', 'mar'],
    'Luke': ['luke', 'lk', 'luk'],
    'John': ['john', 'jo', 'joh', 'jn'],
    'Acts': ['acts', 'act', 'ac'],
    'Romans': ['rom', 'rm', 'romans'],
    '1 Corinthians': ['1cor', '1co', '1corinthians', '1 corinthians', '1 cor'],
    '2 Corinthians': ['2cor', '2co', '2corinthians', '2 corinthians', '2 cor'],
    'Galatians': ['gal', 'gl', 'galatians'],
    'Ephesians': ['eph', 'ephesians'],
    'Philippians': ['phil', 'ph', 'php', 'philippians'],
    'Colossians': ['col', 'cl', 'colossians'],
    '1 Thessalonians': ['1thess', '1ts', '1th', '1thessalonians', '1 thessalonians', '1 thess'],
    '2 Thessalonians': ['2thess', '2ts', '2th', '2thessalonians', '2 thessalonians', '2 thess'],
    '1 Timothy': ['1tim', '1tm', '1ti', '1timothy', '1 timothy', '1 tim'],
    '2 Timothy': ['2tim', '2tm', '2ti', '2timothy', '2 timothy', '2 tim'],
    'Titus': ['titus', 'tt', 'tit'],
    'Philemon': ['philem', 'phm', 'phlm', 'philemon'],
    'Hebrews': ['heb', 'hb', 'hebrews'],
    'James': ['james', 'jm', 'jas', 'jam'],
    '1 Peter': ['1pet', '1pe', '1pt', '1peter', '1 peter', '1 pet'],
    '2 Peter': ['2pet', '2pe', '2pt', '2peter', '2 peter', '2 pet'],
    '1 John': ['1john', '1jo', '1jn', '1 john'],
    '2 John': ['2john', '2jo', '2jn', '2 john'],
    '3 John': ['3john', '3jo', '3jn', '3 john'],
    'Jude': ['jude', 'jd'],
    'Revelation': ['rev', 're', 'revelation'],
}

# To avoid duplicating book names/ordering, we keep explicit testament
# ordering here and derive the printable abbreviations from
# `BOOK_ABBREVIATIONS` (the single source of truth).
OT_ORDER = [
    'Genesis','Exodus','Leviticus','Numbers','Deuteronomy','Joshua','Judges',
    'Ruth','1 Samuel','2 Samuel','1 Kings','2 Kings','1 Chronicles','2 Chronicles',
    'Ezra','Nehemiah','Esther','Job','Psalms','Proverbs','Ecclesiastes',
    'Song of Solomon','Isaiah','Jeremiah','Lamentations','Ezekiel','Daniel',
    'Hosea','Joel','Amos','Obadiah','Jonah','Micah','Nahum','Habakkuk',
    'Zephaniah','Haggai','Zechariah','Malachi',
]

NT_ORDER = [
    'Matthew','Mark','Luke','John','Acts','Romans','1 Corinthians','2 Corinthians',
    'Galatians','Ephesians','Philippians','Colossians','1 Thessalonians','2 Thessalonians',
    '1 Timothy','2 Timothy','Titus','Philemon','Hebrews','James','1 Peter','2 Peter',
    '1 John','2 John','3 John','Jude','Revelation',
]


def _format_abbrevs(name, max_items=3):
    """Return a printable abbreviation string for a book name.

    Uses the first `max_items` abbreviations from `BOOK_ABBREVIATIONS`
    and title-cases them for display.
    """
    abbrevs = BOOK_ABBREVIATIONS.get(name, [])
    if not abbrevs:
        return ''
    # pick up to max_items and title-case them for readability
    picked = abbrevs[:max_items]
    return ', '.join(a.title() for a in picked)


# Derived printable lists for help output
OT_BOOKS = [(name, _format_abbrevs(name)) for name in OT_ORDER]
NT_BOOKS = [(name, _format_abbrevs(name)) for name in NT_ORDER]
