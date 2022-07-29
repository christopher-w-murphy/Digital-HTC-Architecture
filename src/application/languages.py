from typing import Dict


deepl_source_languages: Dict[str, str] = {
    'Bulgarian': 'BG',
    'Czech': 'CS',
    'Danish': 'DA',
    'German': 'DE',
    'Greek': 'EL',
    'English': 'EN',
    'Spanish': 'ES',
    'Estonian': 'ET',
    'Finnish': 'FI',
    'French': 'FR',
    'Hungarian': 'HU',
    'Indonesian': 'ID',
    'Italian': 'IT',
    'Japanese': 'JA',
    'Lithuanian': 'LT',
    'Latvian': 'LV',
    'Dutch': 'NL',
    'Polish': 'PL',
    'Portuguese': 'PT',
    'Romanian': 'RO',
    'Russian': 'RU',
    'Slovak': 'SK',
    'Slovenian': 'SL',
    'Swedish': 'SV',
    'Turkish': 'TR',
    'Chinese': 'ZH'
}


deepl_target_languages: Dict[str, str] = {
    'Bulgarian': 'BG',
    'Czech': 'CS',
    'Danish': 'DA',
    'German': 'DE',
    'Greek': 'EL',
    'English (British)': 'EN-GB',
    'English (American)': 'EN-US',
    'Spanish': 'ES',
    'Estonian': 'ET',
    'Finnish': 'FI',
    'French': 'FR',
    'Hungarian': 'HU',
    'Indonesian': 'ID',
    'Italian': 'IT',
    'Japanese': 'JA',
    'Lithuanian': 'LT',
    'Latvian': 'LV',
    'Dutch': 'NL',
    'Polish': 'PL',
    'Portuguese (Brazilian)': 'PT-BR',
    'Portuguese (European)': 'PT-PT',
    'Romanian': 'RO',
    'Russian': 'RU',
    'Slovak': 'SK',
    'Slovenian': 'SL',
    'Swedish': 'SV',
    'Turkish': 'TR',
    'Chinese (simplified)': 'ZH'
}


tesseract_languages: Dict[str, str] = {
    'Afrikaans': 'afr',
    'Amharic': 'amh',
    'Arabic': 'ara',
    'Assamese': 'asm',
    'Azerbaijani': 'aze',
    'Azerbaijani - Cyrilic': 'aze_cyrl',
    'Belarusian': 'bel',
    'Bengali': 'ben',
    'Tibetan': 'bod',
    'Bosnian': 'bos',
    'Breton': 'bre',
    'Bulgarian': 'bul',
    'Catalan; Valencian': 'cat',
    'Cebuano': 'ceb',
    'Czech': 'ces',
    'Chinese simplified': 'chi_sim',
    'Chinese traditional': 'chi_tra',
    'Cherokee': 'chr',
    'Corsican': 'cos',
    'Welsh': 'cym',
    'Danish': 'dan',
    'German': 'deu',
    'Dhivehi': 'div',
    'Dzongkha': 'dzo',
    'Greek, Modern, 1453-': 'ell',
    'English': 'eng',
    'English, Middle, 1100-1500': 'enm',
    'Esperanto': 'epo',
    'Math / equation detection module': 'equ',
    'Estonian': 'est',
    'Basque': 'eus',
    'Persian': 'fas',
    'Faroese': 'fao',
    'Filipino': 'fil',
    'Finnish': 'fin',
    'French': 'fra',
    'Frankish': 'frk',
    'French, Middle, ca.1400-1600': 'frm',
    'West Frisian': 'fry',
    'Scottish Gaelic': 'gla',
    'Irish': 'gle',
    'Galician': 'glg',
    'Greek, Ancient, to 1453': 'grc',
    'Gujarati': 'guj',
    'Haitian; Haitian Creole': 'hat',
    'Hebrew': 'heb',
    'Hindi': 'hin',
    'Croatian': 'hrv',
    'Hungarian': 'hun',
    'Armenian': 'hye',
    'Inuktitut': 'iku',
    'Indonesian': 'ind',
    'Icelandic': 'isl',
    'Italian': 'ita',
    'Italian - Old': 'ita_old',
    'Javanese': 'jav',
    'Japanese': 'jpn',
    'Kannada': 'kan',
    'Georgian': 'kat',
    'Georgian - Old': 'kat_old',
    'Kazakh': 'kaz',
    'Central Khmer': 'khm',
    'Kirghiz; Kyrgyz': 'kir',
    'Kurdish Kurmanji': 'kmr',
    'Korean': 'kor',
    'Korean vertical': 'kor_vert',
    'Lao': 'lao',
    'Latin': 'lat',
    'Latvian': 'lav',
    'Lithuanian': 'lit',
    'Luxembourgish': 'ltz',
    'Malayalam': 'mal',
    'Marathi': 'mar',
    'Macedonian': 'mkd',
    'Maltese': 'mlt',
    'Mongolian': 'mon',
    'Maori': 'mri',
    'Malay': 'msa',
    'Burmese': 'mya',
    'Nepali': 'nep',
    'Dutch; Flemish': 'nld',
    'Norwegian': 'nor',
    'Occitan post 1500': 'oci',
    'Oriya': 'ori',
    'Orientation and script detection module': 'osd',
    'Panjabi; Punjabi': 'pan',
    'Polish': 'pol',
    'Portuguese': 'por',
    'Pushto; Pashto': 'pus',
    'Quechua': 'que',
    'Romanian; Moldavian; Moldovan': 'ron',
    'Russian': 'rus',
    'Sanskrit': 'san',
    'Sinhala; Sinhalese': 'sin',
    'Slovak': 'slk',
    'Slovenian': 'slv',
    'Sindhi': 'snd',
    'Spanish; Castilian': 'spa',
    'Spanish; Castilian - Old': 'spa_old',
    'Albanian': 'sqi',
    'Serbian': 'srp',
    'Serbian - Latin': 'srp_latn',
    'Sundanese': 'sun',
    'Swahili': 'swa',
    'Swedish': 'swe',
    'Syriac': 'syr',
    'Tamil': 'tam',
    'Tatar': 'tat',
    'Telugu': 'tel',
    'Tajik': 'tgk',
    'Thai': 'tha',
    'Tigrinya': 'tir',
    'Tonga': 'ton',
    'Turkish': 'tur',
    'Uighur; Uyghur': 'uig',
    'Ukrainian': 'ukr',
    'Urdu': 'urd',
    'Uzbek': 'uzb',
    'Uzbek - Cyrilic': 'uzb_cyrl',
    'Vietnamese': 'vie',
    'Yiddish': 'yid',
    'Yoruba': 'yor'
}