# -*- coding: utf-8 -*-
# Source data for BAMA Book 1 — Survival Kit.
# Romanization follows John Okell's system (Burmese by Ear):
#   - syllables hyphenated
#   - aspirated consonants marked with an apostrophe: p' t' k' c' s'
#   - "I" = ca.na.w (male speaker) / ca.ma. (female speaker)
#   - high & creaky tone: acute accent (á é í ó ú) — low tone: unmarked
#   - weak/reduced vowel: breve (a.)  — glottal final: -q  — nasal final: -n
#   - the ky/gy sound is written c/j, not ky/gy

UNITS = []

def U(n, letter, name, part, theme, goal, main, vocab, grammar, write):
    UNITS.append({
        "n": n, "letter": letter, "name": name, "part": part, "theme": theme,
        "goal": goal, "main": main, "vocab": vocab, "grammar": grammar, "write": write
    })

# ============== PART 1 — FOUNDATIONS ==============

U(1, "က", "ka", "Foundations", "Statements & tag questions",
  "Make a simple statement about something, and comment on it the way Burmese speakers actually open small talk — through the weather.",
  {"type":"dialogue","lines":[
    ["A","ပူတယ်နော်။","Pu-deh-naw.","Hot today, isn't it."],
    ["B","ဟုတ်ကဲ့၊ ပူပါတယ်။","Houq-keh, pu-ba-deh.","Yeah, it is."]
  ]},
  [["မင်္ဂလာပါ","mingalar-ba","hello (formal / to foreigners / service settings)"],
   ["ဘယ်သွားမလဲ","beh thwa-mha-lé","\"where are you headed?\" — real street greeting"],
   ["ထမင်းစားပြီးပြီလား","hta-min sa-pi-bi-la","\"have you eaten yet?\" — real street greeting"],
   ["ပူတယ်","pu-deh","to be hot / it's hot"],["အေးတယ်","é-deh","to be cold / it's cold"],
   ["ကောင်းတယ်","kaun-deh","to be good / it's good"],["ရတယ်","ya-deh","to be all right / it's fine"],
   ["ဟုတ်ကဲ့","houq-keh","that's right / yes (agreeing)"],["ဟုတ်တယ်","houq-teh","it's true / correct"],
   ["ကြီးတယ်","cí-deh","to be big"],["ငယ်တယ်","ngeh-deh","to be small"]],
  [{"title":"-deh — the statement ending","explain":"Every plain Burmese statement ends in -deh (or -teh after a syllable ending in -q). It's the neutral, all-purpose \"is/does\" ending — there's no separate word for \"to be.\"",
    "examples":[["ပူတယ်","Pu-deh.","It's hot."],["ကောင်းတယ်","Kaun-deh.","It's good."]]},
   {"title":"-naw — inviting agreement","explain":"Add -naw to the end of a -deh statement to turn it into a tag question — like English \"...isn't it?\" Commenting on the weather this way is one of the most common ways to open a conversation in Burmese, the same way English speakers open with \"nice day, huh?\"",
    "examples":[["ပူတယ်နော်။","Pu-deh-naw.","Hot, isn't it."],["ကောင်းတယ်နော်။","Kaun-deh-naw.","Good, isn't it."]]}],
  "The anchor loop of the whole script. Start at the top, curve down and left, close the loop back where you started — one continuous stroke."
)

U(2, "ခ", "hka", "Foundations", "Answering politely",
  "Pay someone a compliment and receive one — the polite way, with -ba-/-pa-.",
  {"type":"dialogue","lines":[
    ["A","သိပ်ကောင်းပါတယ်။","Théiq kaun-ba-deh.","This is really good."],
    ["B","ဟုတ်ကဲ့၊ ကောင်းပါတယ်။ ကျေးဇူးတင်ပါတယ်။","Houq-keh, kaun-ba-deh. Cé-zú-tin-ba-deh.","Yeah, it is. Thank you."]
  ]},
  [["ကျေးဇူးတင်ပါတယ်","cé-zú-tin-ba-deh","thank you"],["ကျေးဇူးပဲ","cé-zú-béh","thanks (casual)"],
   ["သိပ်","théiq","very / really"],["နည်းနည်း","né-né","a little"],
   ["ဟုတ်ပါတယ်","houq-pa-deh","yes, that's correct (polite)"],["စားတယ်","sa-deh","to eat"],
   ["သောက်တယ်","thauq-teh","to drink"],["ဟုတ်ကဲ့ခင်ဗျား","houq-keh khin-bya","yes sir/ma'am (very polite)"]],
  [{"title":"-ba- / -pa- — the politeness infix","explain":"Slot -ba- (or -pa- after a syllable ending in -q) between the verb and -deh to make a statement polite. Pu-deh → Pu-ba-deh. This is the single most useful upgrade you can make to any sentence.",
    "examples":[["ပူပါတယ်","Pu-ba-deh.","It's hot. (polite)"],["ကောင်းပါတယ်","Kaun-ba-deh.","It's good. (polite)"]]},
   {"title":"Théiq — \"very\"","explain":"Place théiq directly before the verb to intensify it: théiq + kaun-ba-deh = \"it's really good.\" Word order is reversed from English — the intensifier still comes before the verb, since the verb is always last.",
    "examples":[["သိပ်ကောင်းပါတယ်","Théiq kaun-ba-deh.","It's really good."]]}],
  "Same loop as က, with one extra hook curling off the top right. Draw က first, then add the hook without lifting your rhythm."
)

U(3, "ဂ", "ga", "Foundations", "Saying no",
  "Politely disagree about something everyday — like the weather, again.",
  {"type":"dialogue","lines":[
    ["A","ပူတယ်နော်။","Pu-deh-naw.","Hot, isn't it."],
    ["B","မပူပါဘူး၊ ရတယ်။","Ma-pu-ba-bú, ya-deh.","Not really, it's fine."]
  ]},
  [["ကြိုက်တယ်","caiq-teh","to like"],["မကြိုက်ဘူး","ma-caiq-pa-bú","don't like (polite negative)"],
   ["လိုချင်တယ်","lo-jin-deh","to want (something)"],["မလိုချင်ဘူး","ma-lo-jin-ba-bú","don't want"],
   ["နားလည်တယ်","na-leh-deh","to understand"],["နားမလည်ဘူး","na-ma-leh-ba-bú","don't understand"],
   ["ဟုတ်ဘူး","ma-houq-pa-bú","that's not right / no"],["ဘူး","-bú","(negative sentence ending)"]],
  [{"title":"ma-...-bú — the negative sandwich","explain":"Burmese negates by sandwiching the verb: ma- goes on the front, -bú goes on the end, and the politeness infix -ba-/-pa- sits in between. Pu-deh becomes Ma-pu-ba-bú — never just \"pu-deh + not.\"",
    "examples":[["မပူပါဘူး","Ma-pu-ba-bú.","It's not hot."],["ကြိုက်ပါဘူး","Ma-caiq-pa-bú.","I don't like it."]]},
   {"title":"Where ma- attaches on two-part verbs","explain":"Some verbs are really two syllables glued together (like ná-leh-deh, \"to understand\"). The negative ma- goes before the second syllable, not the first: ná-ma-leh-ba-bú, not Ma-ná-leh-ba-bú.",
    "examples":[["နားမလည်ဘူး","Ná-ma-leh-ba-bú.","I don't understand."]]}],
  "A closed loop with a small tail flicked off the base. Round the loop fully before you let the tail trail out to the right."
)

U(4, "ဃ", "ga (gha)", "Foundations", "Asking a plain question",
  "Point at something and genuinely ask about it — without leading the listener toward an answer.",
  {"type":"dialogue","lines":[
    ["A","ဒါစားသလား။","Da sa-tha-la.","Do you eat this?"],
    ["B","ဟုတ်ကဲ့၊ စားပါတယ်။","Houq-keh, sa-ba-deh.","Yes, I do."]
  ]},
  [["-သလား","-tha-la","(neutral question ending)"],["-လား","-la","(neutral question ending, short form)"],
   ["စားသလား","sa-tha-la","do you eat (it)?"],["ကြိုက်သလား","caiq-tha-la","do you like it?"],
   ["ရှိသလား","shi-tha-la","is there.../do you have...?"],["ဟင့်အင်း","hín-ín","no (casual)"],
   ["ဟုတ်ကဲ့","houq-keh","yes"],["ဘာ","ba","what"]],
  [{"title":"-tha-la / -dha-la — a genuine question","explain":"Unlike -naw (Unit 1), which nudges the listener to agree, -tha-la (voiced to -dha-la after most syllables) is neutral — a real yes/no question with no expected answer either way. It's the natural way to ask about something you're actually unsure of, like whether a food is familiar to someone.",
    "examples":[["ဒါစားသလား။","Da sa-tha-la.","Do you eat this?"],["ကြိုက်သလား။","Caiq-tha-la.","Do you like it?"]]}],
  "Two loops stacked — draw the lower loop first (like ဂ), then add the second loop directly above it."
)

U(5, "င", "nga", "Foundations", "Numbers 1–10",
  "Count from one to ten, and use a classifier to ask how many people are in a group.",
  {"type":"dialogue","lines":[
    ["A","ဘယ်နှစ်ယောက်လဲ။","Beh-hna-yauq-lé.","How many people?"],
    ["B","နှစ်ယောက်ပါ။","Hna-yauq ba.","Two people."]
  ]},
  [["တစ်","tiq","one"],["နှစ်","hniq","two"],["သုံး","thoun","three"],["လေး","lé","four"],
   ["ငါး","ngá","five"],["ခြောက်","c'auq","six"],["ခုနစ်","k'un-hniq","seven"],
   ["ရှစ်","shiq","eight"],["ကိုး","kó","nine"],["တစ်ဆယ်","ta-s'eh","ten"]],
  [{"title":"Counting needs a classifier","explain":"Burmese never counts a noun with a bare number — you always add a classifier (a counting word) after it. -yauq counts people: hna-yauq = \"two (people).\"",
    "examples":[["နှစ်ယောက်","hna-yauq","two people"],["သုံးယောက်","thoun-yauq","three people"]]},
   {"title":"tiq, hniq, k'un-hniq weaken before a classifier","explain":"\"One,\" \"two,\" and \"seven\" shorten their vowel to a. before most classifiers: tiq-yauq is never said — it's ta-yauq. Same for hniq → hna-, and k'un-hniq → k'un-na-.",
    "examples":[["တစ်ယောက်","ta-yauq","one person (not tiq-yauq)"],["နှစ်ယောက်","hna-yauq","two people (not hniq-yauq)"]]}],
  "A single hooked curve — no loop to close. One relaxed stroke, curling from top to bottom-left."
)

U(6, "စ", "sa (ca)", "Foundations", "Numbers & prices",
  "Ask the price of something and understand the answer.",
  {"type":"dialogue","lines":[
    ["A","Da beh-lauq-lé?","da beh-lauq-lé","How much is this?"],
    ["B","Ngá-yá caq ba.","ngá-yá caq ba","Five hundred kyats."],
    ["A","Théiq zé-cí-deh-naw?","théiq zé-cí-deh-naw","That's quite expensive, isn't it?"],
    ["B","Ma-zé-cí-ba-bú, zé-cho-ba-deh.","ma-zé-cí-ba-bú, zé-cho-ba-deh","It's not expensive, it's cheap."]
  ]},
  [["ဆယ့်တစ်","s'eh-tiq","eleven"],["နှစ်ဆယ်","hna-s'eh","twenty"],["တစ်ရာ","ta-ya","one hundred"],
   ["ကျပ်","caq","kyat (currency)"],["ဈေးကြီးတယ်","zé-cí-deh","to be expensive"],
   ["ဈေးချိုတယ်","zé-cho-deh","to be cheap"],["ဘယ်လောက်လဲ","beh-lauq-lé","how much is it?"],
   ["ဒါ","da","this / this one"]],
  [{"title":"beh-lauq-lé — asking a price or amount","explain":"Beh-lauq literally means \"how much\" and takes the -lé question ending you'll formally meet in Unit 7. It's the single most useful phrase for shopping, taxis, and markets.",
    "examples":[["ဒါဘယ်လောက်လဲ။","Da beh-lauq-lé?","How much is this?"]]},
   {"title":"The Voicing Rule","explain":"When two words join, the first consonant of the second word often \"voices\": s'eh (\"ten\") becomes -zeh in compounds like hna-s'eh (twenty, no change — after a˘) but thoun-zeh (thirty, s' voices to z). It doesn't happen after a syllable ending in -q.",
    "examples":[["သုံးဆယ်","thoun-zeh","thirty"],["ရှစ်ဆယ်","shiq-s'eh","eighty (no voicing — ends in -q)"]]}],
  "Begins like a backward c, then flicks upward at the end. Practice the upward flick on its own before joining it to the curve."
)

U(7, "ဆ", "hsa", "Foundations", "\"What\" and question words",
  "Ask an open question using a question word instead of yes/no.",
  {"type":"dialogue","lines":[
    ["A","Beh-lo-lé?","beh-lo-lé","How (is it)?"],
    ["B","Kaun-ba-deh.","kaun-ba-deh","It's good."],
    ["A","Da ba-lé?","da ba-lé","What is this?"],
    ["B","Da hta-min ba.","da hta-min ba","This is rice."]
  ]},
  [["ဘာ","ba","what"],["ဘယ်","beh","which / where (base)"],["ဘယ်သူ","beh-thu","who"],
   ["ဘယ်တော့","beh-dawh","when"],["ဘာဖြစ်လဲ","ba-p'yiq-lé","what happened? / what's wrong?"],
   ["ဘယ်လို","beh-lo","how"],["-လဲ","-lé","(question-word question ending)"],["အကြောင်း","a-caun","reason / about"]],
  [{"title":"-lé — closing a question that already has a question word","explain":"When your question already contains ba (\"what\"), beh-thu (\"who\"), or another question word, you close the sentence with -lé, not -tha-la. The two question endings are never mixed.",
    "examples":[["ဒါဘာလဲ။","Da ba-lé?","What is this?"],["ဘယ်သူလဲ။","Beh-thu-lé?","Who is it?"]]},
   {"title":"Question words stay in place","explain":"Unlike English, Burmese doesn't move the question word to the front. Ba (\"what\") sits exactly where the answer word would go: Da ba-lé, literally \"this what is?\"",
    "examples":[["ဒါဘာလဲ","Da ba-lé?","This — what — is? (What is this?)"]]}],
  "A loop with a small tail at the base. Draw the loop first, then anchor the tail underneath — like ဂ with an added foot."
)

U(8, "ဇ", "za (ja)", "Foundations", "Wanting & asking politely",
  "Say what you want, and turn any verb into a polite request.",
  {"type":"dialogue","lines":[
    ["A","Ba lo-jin-dha-lé?","ba lo-jin-dha-lé","What do you want?"],
    ["B","Yé lo-jin-ba-deh.","yé lo-jin-ba-deh","I want water."],
    ["A","Yé pé-ba.","yé pé-ba","Please give (me) water."],
    ["B","Houq-keh, ya-ba-deh.","houq-keh, ya-ba-deh","Sure, no problem."]
  ]},
  [["လိုချင်တယ်","lo-jin-deh","to want (something)"],["ချင်တယ်","-jin-deh","(suffix) \"want to\""],
   ["ပေးပါ","pé-ba","please give (me)"],["ရေ","yé","water"],["ထမင်း","hta-min","rice"],
   ["ရတယ်","ya-deh","that's fine / no problem"],["ခဏလောက်","k'a-na-lauq","just a moment"],
   ["ကျေးဇူးပြု၍","cé-zú-pyú-ywé","please (formal)"]],
  [{"title":"-jin-deh — \"want to\"","explain":"Attach -jin-deh directly to a verb to mean \"want to [verb].\" Sa-jin-deh = \"want to eat.\" It behaves exactly like any other -deh verb — it takes -ba-, -naw, -tha-la, and ma-...-bú normally.",
    "examples":[["စားချင်တယ်","Sa-jin-deh.","I want to eat."],["မစားချင်ဘူး","Ma-sa-jin-ba-bú.","I don't want to eat."]]},
   {"title":"pé-ba — the all-purpose polite request","explain":"Adding pé-ba (\"give me,\" softened) after a verb turns it into a request: \"please [verb] for me.\" You'll use this constantly — ordering food, asking for help, asking for the bill.",
    "examples":[["ရေပေးပါ။","Yé pé-ba.","Water, please."],["ကူညီပေးပါ။","Ku-nyi pé-ba.","Please help me."]]}],
  "Echoes the shape of စ with a longer tail underneath. Write စ first, then extend the tail further down."
)

# ============== PART 2 — FIRST NEEDS ==============

U(9, "ဈ", "za (jha)", "First Needs", "When you don't understand",
  "Say you don't understand, and ask someone to repeat or slow down.",
  {"type":"dialogue","lines":[
    ["A","[fast Burmese]","...","..."],
    ["B","Sáw-rí, ná-ma-leh-ba-bú.","sáw-rí, ná-ma-leh-ba-bú","Sorry, I don't understand."],
    ["B","P'yan-pyaw-pé-ba.","p'yan-pyaw-pé-ba","Please say it again."],
    ["A","Houq-keh.","houq-keh","Sure."]
  ]},
  [["ဆောရီး","sáw-rí","sorry (English loanword)"],["နားမလည်ဘူး","ná-ma-leh-ba-bú","I don't understand"],
   ["ပြန်ပြောပေးပါ","p'yan-pyaw-pé-ba","please say it again"],["နှေးနှေးပြောပေးပါ","hné-hné pyaw-pé-ba","please speak slowly"],
   ["မြန်မာလို","myan-ma-lo","in Burmese"],["အင်္ဂလိပ်လို","in-ga-leiq-lo","in English"],
   ["ဘယ်လိုပြောလဲ","beh-lo pyaw-lé","how do you say...?"],["နားလည်ပါတယ်","ná-leh-ba-deh","I understand"]],
  [{"title":"Loanwords slot in like native words","explain":"Sáw-rí (\"sorry\") is a straight loan from English, but it takes Burmese grammar exactly like any native word — you can say Sáw-rí-naw or ask Sáw-rí-tha-la, though the plain form alone is what you'll use most.",
    "examples":[["ဆောရီးနော်","Sáw-rí-naw.","Sorry (softened)."]]},
   {"title":"Building requests with pé-ba","explain":"P'yan-pyaw-pé-ba (\"say again, please\") and hné-hné pyaw-pé-ba (\"speak slowly, please\") both use the pé-ba pattern from Unit 8 — this is why that pattern is worth over-learning.",
    "examples":[["ပြန်ပြောပေးပါ။","P'yan-pyaw-pé-ba.","Please say that again."],["နှေးနှေးပြောပေးပါ။","Hné-hné pyaw-pé-ba.","Please speak slowly."]]}],
  "A less common letter today, mostly kept in older spellings. Recognize its shape — a loop with a low, extended tail — more than you'll write it."
)

U(10, "ည", "nya", "First Needs", "Getting someone's attention",
  "Politely get a stranger's attention and understand their reply.",
  {"type":"dialogue","lines":[
    ["A","A-ma!","a-ma","Excuse me! (to an older woman)"],
    ["B","Shin?","shin","Yes? (woman replying)"],
    ["A","Di-ha beh-lauq-lé?","di-ha beh-lauq-lé","How much is this?"],
    ["B","Ngá-ya caq ba.","ngá-ya caq ba","Five hundred kyats."]
  ]},
  [["အမ","a-ma","excuse me (to an older woman / \"auntie\")"],["ကို","a-ko","excuse me (to a man about your age)"],
   ["ရှင်","shin","yes? (used by/to women)"],["ဗျာ","bya","yes? (used by men)"],
   ["ဟုတ်ကဲ့","houq-keh","yes? / I'm listening"],["ဘာလဲ","ba-lé","what is it?"],
   ["ဒီဟာ","di-ha","this (thing) here"],["ဟိုဟာ","ho-ha","that (thing) over there"]],
  [{"title":"Getting attention with kin terms","explain":"Burmese doesn't have a neutral word for \"excuse me\" the way English does — instead you address a stranger with a kinship term that fits their approximate age and your gender relative to them: a-ma (\"auntie\") for an older woman, a-ko (\"older brother\") for a man near your age.",
    "examples":[["အမ။","A-ma!","Excuse me! (to an older woman)"],["အကို။","A-ko!","Excuse me! (to a man)"]]},
   {"title":"Gendered response particles","explain":"Shin and bya both mean roughly \"yes?\" as a reply to being addressed — shin is used by and to women, bya by and to men. You'll hear both constantly in shops and cafés.",
    "examples":[["ရှင်။","Shin?","Yes? (woman)"],["ဗျာ။","Bya?","Yes? (man)"]]}],
  "Sits low with a long curved tail beneath the line — give it plenty of room below the baseline before you start the next letter."
)

U(11, "ဋ", "ta", "First Needs", "Ordering at a café",
  "Order food and drink at a café or restaurant.",
  {"type":"dialogue","lines":[
    ["A","Mi-nú cí-lo ya-ma-la?","mi-nú cí-lo ya-ma-la","May I see the menu?"],
    ["B","Ya-ba-deh.","ya-ba-deh","Of course."],
    ["A","Hin-cho ta-k'weq pé-ba.","hin-cho ta-k'weq pé-ba","One bowl of soup, please."],
    ["B","Houq-keh, k'a-na-lauq saun-pa.","houq-keh, k'a-na-lauq saun-pa","Sure, one moment please."]
  ]},
  [["မီနူး","mi-nú","menu"],["ဟင်းချို","hin-cho","soup"],["ထမင်း","hta-min","rice"],
   ["ကော်ဖီ","kaw-p'i","coffee"],["ရေခဲမှုန့်","yé-gé-hmoun","ice"],["ခွက်","k'weq","bowl / cup (classifier)"],
   ["စောင့်တယ်","saun-deh","to wait"],["ငတ်တယ်","ngaq-teh","to be hungry"]],
  [{"title":"-lo ya-ma-la — \"may I...?\"","explain":"Attach -lo ya-ma-la to a verb to ask permission — literally \"if I [verb], will it be all right?\" It's the standard way to ask \"may I...?\" or \"can I...?\" in any polite setting.",
    "examples":[["ကြည့်လို့ရမလား။","Cí-lo ya-ma-la?","May I look?"],["စားလို့ရမလား။","Sa-lo ya-ma-la?","May I eat (this)?"]]},
   {"title":"Ordering with a classifier","explain":"Just like counting people needs -yauq (Unit 5), ordering food needs the right classifier: -k'weq for a bowl or cup. Number + classifier + pé-ba is the whole pattern for ordering anything.",
    "examples":[["တစ်ခွက်ပေးပါ။","Ta-k'weq pé-ba.","One bowl, please."]]}],
  "A small loop with a flag-like stroke on top — one of the letters borrowed for Pali spellings; you'll meet it more in reading than writing."
)

U(12, "ဌ", "hta", "First Needs", "Asking for the bill",
  "Ask for the check and handle a simple payment.",
  {"type":"dialogue","lines":[
    ["A","Saun-di pé-ba.","saun-di pé-ba","The bill, please."],
    ["B","Ngá-ya-ngá-zeh ba.","ngá-ya-ngá-zeh ba","It's 550."],
    ["A","Da paq-hma.","da paq-hma","Here you go."],
    ["B","Cé-zú-tin-ba-deh.","cé-zú-tin-ba-deh","Thank you."]
  ]},
  [["ဘေ့ငွေ","saun-di","the bill"],["ငွေ","ngwé","money"],["ပိုက်ဆံ","paiq-s'an","money (colloquial)"],
   ["ချွေတာ","c'wé-ta","to save (money)"],["အကြွေ","a-cwé","change (coins)"],["ငွေလက်ခံသလား","ngwé leq-k'an-tha-la","do you accept card?"],
   ["ငွေသား","ngwé-thá","cash"],["အကြွေးဝယ်","a-cwé-weh","to buy on credit"]],
  [{"title":"Numbers keep stacking the same way","explain":"550 is ngá-ya-ngá-zeh — literally \"5 hundred, 5 tens\" — built exactly like the smaller numbers from Units 5–6, just chained together. No new grammar, only more digits.",
    "examples":[["ငါးရာငါးဆယ်","Ngá-ya-ngá-zeh.","550."]]},
   {"title":"da paq-hma — handing something over","explain":"Da paq-hma (\"here it is,\" literally \"this — put — at\") is what you say while physically handing over cash or an item. It pairs naturally with cé-zú-tin-ba-deh in reply.",
    "examples":[["ဒါပါ့မှာ။","Da paq-hma.","Here you go."]]}],
  "Pairs with ဋ — another Pali-derived letter. Same small loop-and-flag shape, slightly rounder."
)

U(13, "ဍ", "da", "First Needs", "Taking a taxi",
  "Tell a taxi driver where you're going and settle the fare.",
  {"type":"dialogue","lines":[
    ["A","[place]-go thwa-jin-ba-deh.","...go thwa-jin-ba-deh","I want to go to [place]."],
    ["B","Houq-keh. Tweh-caq-caq ba.","houq-keh. tweh-caq-caq ba","Sure. It's 4000 kyats."],
    ["A","Théiq cí-ba-deh. Né-né shaw-pé-ba.","théiq cí-ba-deh. né-né shaw-pé-ba","That's a lot. A little discount, please?"],
    ["B","Houq-keh, thoun-daun-ba be.","houq-keh, thoun-daun-ba be","Alright, 3000 then."]
  ]},
  [["သွားတယ်","thwa-deh","to go"],["ကား","ka","car"],["တက္ကစီ","teq-ka-si","taxi"],
   ["-ကို","-go","to (a place — direction marker)"],["ဘယ်လောက်ကျလဲ","beh-lauq ca-lé","how much does it cost?"],
   ["ကျတယ်","ca-deh","to cost"],["လျှော့","shaw","(a) discount"],["နေရာ","né-ya","place"]],
  [{"title":"-go — marking where you're going","explain":"Attach -go to a place name to mark it as your destination: [place]-go thwa-jin-ba-deh, \"I want to go to [place].\" This is the same -ko/-go you'll meet again in Unit 15 marking direct objects.",
    "examples":[["ဈေးကိုသွားချင်ပါတယ်။","Zé-go thwa-jin-ba-deh.","I want to go to the market."]]},
   {"title":"Négotiating a price","explain":"Théiq cí-ba-deh (\"that's a lot\") plus né-né shaw-pé-ba (\"a little discount, please\") is the standard two-line haggling exchange, using théiq from Unit 2 and pé-ba from Unit 8.",
    "examples":[["သိပ်ကြီးပါတယ်။","Théiq cí-ba-deh.","That's too much."],["နည်းနည်းလျှော့ပေးပါ။","Né-né shaw-pé-ba.","A little discount, please."]]}],
  "A rounded loop with a hook trailing to the right — write the loop first, then let the hook flick out lightly."
)

U(14, "ဎ", "da", "First Needs", "Directions inside a taxi",
  "Guide a driver in real time — left, right, straight, and stop.",
  {"type":"dialogue","lines":[
    ["A","Teh-teh thwa-ba.","teh-teh thwa-ba","Go straight."],
    ["B","Houq-keh.","houq-keh","Okay."],
    ["A","Beh-beq-ko lé-ba.","beh-beq-ko lé-ba","Turn left."],
    ["A","Di-hma ya-q-pa.","di-hma yaq-pa","Stop here."]
  ]},
  [["တည့်တည့်","teh-teh","straight ahead"],["ဘယ်ဘက်","beh-beq","left (side)"],["ညာဘက်","nya-beq","right (side)"],
   ["ကွေ့တယ်","kwé-deh","to turn"],["ရပ်တယ်","yaq-teh","to stop"],["ဒီမှာ","di-hma","here"],
   ["ဟိုမှာ","ho-hma","there"],["ရှေ့မှာ","shé-hma","up ahead"]],
  [{"title":"Direction + -ko + verb","explain":"Beh-beq-ko lé-ba is literally \"left-side-to turn-please\" — the same -ko direction marker from Unit 13's -go (they're the same marker; -ko after most syllables, -go after a nasal).",
    "examples":[["ဘယ်ဘက်ကိုလှည့်ပါ။","Beh-beq-ko lé-ba.","Turn left."],["ညာဘက်ကိုလှည့်ပါ။","Nya-beq-ko lé-ba.","Turn right."]]},
   {"title":"Short, urgent imperatives","explain":"In fast real-time situations like a moving taxi, Burmese drops down to bare verb + -ba, without the full -deh sentence — teh-teh thwa-ba, not the longer teh-teh thwa-ba-deh. Short and immediate.",
    "examples":[["ရပ်ပါ။","Yaq-pa.","Stop."],["ဆက်သွားပါ။","Seq-thwa-ba.","Keep going."]]}],
  "A rarer letter today, close cousin of ဍ. Recognize it in older texts more than you'll need to write it."
)

U(15, "ဏ", "na", "First Needs", "Shopping: this and that",
  "Point at things and ask what they are and what they cost.",
  {"type":"dialogue","lines":[
    ["A","Da ba-lé?","da ba-lé","What's this?"],
    ["B","Da longyi ba.","da longyi ba","This is a longyi."],
    ["A","Ho-da-go cí-lo ya-ma-la?","ho-da-go cí-lo ya-ma-la","May I look at that one?"],
    ["B","Ya-ba-deh, cí-ba.","ya-ba-deh, cí-ba","Sure, go ahead and look."]
  ]},
  [["ဒါ","da","this (thing)"],["ဟိုဒါ","ho-da","that (thing) over there"],["ဒီဟာ","di-ha","this one"],
   ["ဘယ်ဟာ","beh-ha","which one"],["-ကို","-ko","(object marker)"],["ကြည့်တယ်","cí-deh","to look"],
   ["လက်စွပ်","leq-suq","ring (jewelry)"],["ပုဆိုး/လုံချည်","longyi","longyi (sarong)"]],
  [{"title":"da / ho-da / di-ha — three ways to point","explain":"Da is the all-purpose \"this,\" ho-da specifically marks something farther away (\"that, over there\"), and di-ha adds emphasis (\"this one right here\"). All three work as the subject of a sentence exactly like any noun.",
    "examples":[["ဒါဘာလဲ။","Da ba-lé?","What's this?"],["ဟိုဒါဘာလဲ။","Ho-da ba-lé?","What's that (over there)?"]]},
   {"title":"-ko marking an object","explain":"When a verb acts on a specific, identified thing (\"look at that one,\" not just \"look\"), the object takes -ko. It's optional with vague objects but expected with specific ones like ho-da.",
    "examples":[["ဟိုဒါကိုကြည့်ပါ။","Ho-da-ko cí-ba.","Look at that one."]]}],
  "This letter is Pali-only today — you'll recognize it in loanwords far more often than write it yourself."
)

U(16, "တ", "ta", "First Needs", "Bargaining",
  "Push back gently on a price and reach a number you're both happy with.",
  {"type":"dialogue","lines":[
    ["A","Zé né-né shaw-pé-ba.","zé né-né shaw-pé-ba","A little discount on the price, please."],
    ["B","Ma-ya-ba-bú, zé di-lauq-béh ba.","ma-ya-ba-bú, zé di-lauq-béh ba","Can't do it, the price is only this much."],
    ["A","Houq-keh, weh-meh.","houq-keh, weh-meh","Alright, I'll take it."]
  ]},
  [["ဈေးနှုန်း","zé-hnoun","price"],["ဝယ်တယ်","weh-deh","to buy"],["ရောင်းတယ်","yaun-deh","to sell"],
   ["အရွယ်","a-ywéh","size"],["အရောင်","a-yaun","color"],["အသစ်","a-thiq","new"],
   ["အဟောင်း","a-haun","old (used)"],["အနည်းငယ်","a-né-ngeh","just a little"]],
  [{"title":"-meh — the future/intention ending","explain":"Weh-meh (\"I'll buy it\") uses -meh, the future counterpart to -deh: -deh states what is, -meh states what will be or what you intend. It follows the same politeness and negative patterns.",
    "examples":[["ဝယ်မယ်။","Weh-meh.","I'll buy it."],["မဝယ်ဘူး။","Ma-weh-ba-bú.","I won't buy it."]]},
   {"title":"di-lauq-béh — \"only this much\"","explain":"-béh (\"only\") attached to a quantity draws a firm line — a shopkeeper using it is signaling the price won't move further, politely but clearly.",
    "examples":[["ဒီလောက်ပဲ။","Di-lauq-béh.","Only this much."]]}],
  "One of the most common letters in the whole script: a flat top, a downstroke, a small foot. Worth drilling on its own before anything else."
)

U(17, "ထ", "hta", "First Needs", "Asking to take a photo",
  "Politely ask if you can take someone's photo.",
  {"type":"dialogue","lines":[
    ["A","Daq-poun yaiq-c'in-ba-deh.","daq-poun yaiq-c'in-ba-deh","I'd like to take a photo."],
    ["B","Yaiq-lo ya-ma-la?","yaiq-lo ya-ma-la","May I?"],
    ["A","Ya-ba-deh, yaiq-pa.","ya-ba-deh, yaiq-pa","Sure, go ahead."],
    ["B","Cé-zú-tin-ba-deh.","cé-zú-tin-ba-deh","Thank you."]
  ]},
  [["ဓာတ်ပုံ","daq-poun","photograph"],["ရိုက်တယ်","yaiq-teh","to take (a photo) / to hit"],
   ["ကင်မရာ","kin-ma-ya","camera"],["ဖုန်း","p'oun","phone"],["ပြုံးတယ်","pyoun-deh","to smile"],
   ["အတူတူ","a-tu-tu","together"],["ခွင့်ပြု","k'win-pyú","permission"],["ဗီဒီယို","bi-di-yo","video"]],
  [{"title":"Chaining -jin-deh and -lo ya-ma-la","explain":"You can state your intention (Unit 8's -jin-deh: \"I'd like to...\") and then formally ask permission (Unit 11's -lo ya-ma-la: \"may I?\") back to back — very natural, very polite Burmese.",
    "examples":[["ဓာတ်ပုံရိုက်ချင်ပါတယ်။ ရိုက်လို့ရမလား။","Daq-poun yaiq-jin-ba-deh. Yaiq-lo ya-ma-la?","I'd like to take a photo. May I?"]]},
   {"title":"yaiq-pa — a short, warm \"go ahead\"","explain":"The bare imperative yaiq-pa (\"[go ahead and] take it\") is friendlier and more immediate than a full -deh sentence — appropriate once permission is basically already given.",
    "examples":[["ရိုက်ပါ။","Yaiq-pa.","Go ahead, take it."]]}],
  "ထ is တ with a loop added on top. Write တ first, then curl the top stroke into a small loop."
)

U(18, "ဒ", "da", "First Needs", "Asking the way",
  "Ask for and follow directions to a place.",
  {"type":"dialogue","lines":[
    ["A","Zé beh-hma-lé?","zé beh-hma-lé","Where is the market?"],
    ["B","Teh-teh thwa-ba. Beh-beq-ko lé-ba.","teh-teh thwa-ba. beh-beq-ko lé-ba","Go straight. Turn left."],
    ["A","Ca-la-tha-la?","ca-la-tha-la","Is it far?"],
    ["B","Ma-ca-ba-bú, ni-ba-deh.","ma-ca-ba-bú, ni-ba-deh","No, it's close."]
  ]},
  [["ဘယ်မှာလဲ","beh-hma-lé","where is it?"],["ကြာတယ်","ca-deh","to be far / to take long"],
   ["နီးတယ်","ni-deh","to be close"],["ကားလမ်း","ka-lan","road"],["လမ်းဆုံ","lan-zoun","junction"],
   ["တံတား","ta-da","bridge"],["ရပ်ကွက်","yaq-kweq","neighborhood"],["အနီးဆုံး","a-ni-zoun","nearest"]],
  [{"title":"-hma — marking location","explain":"-hma attaches to a place or object to mark \"at/in/on\": Zé-hma = \"at the market.\" It's also how you ask where something is: place-word + beh-hma-lé, \"where is [place]?\"",
    "examples":[["ဈေးဘယ်မှာလဲ။","Zé beh-hma-lé?","Where's the market?"],["ဒီမှာရှိတယ်။","Di-hma shi-deh.","It's right here."]]},
   {"title":"ca-deh doing double duty","explain":"Ca-deh means both \"to be far\" and \"to take a long time\" — the same word covers physical and time distance, the way English sometimes overlaps \"far\" and \"long.\"",
    "examples":[["ကြာသလား။","Ca-tha-la?","Is it far? / Will it take long?"]]}],
  "A rounded loop with a flat base — a softer-edged cousin of တ."
)

U(19, "ဓ", "da", "First Needs", "Near, far, and landmarks",
  "Describe how close something is, using a nearby landmark.",
  {"type":"dialogue","lines":[
    ["A","S'ain-beq-hma shi-deh.","s'ain-beq-hma shi-deh","It's next to the shop."],
    ["B","Ta-da-naunh-hma-la?","ta-da-naunh-hma-la","Behind the bridge?"],
    ["A","Ma-houq-pa-bú, shé-hma ba.","ma-houq-pa-bú, shé-hma ba","No, it's in front."]
  ]},
  [["ဆိုင်","s'ain","shop"],["ဘေးမှာ","beq-hma","next to"],["ရှေ့မှာ","shé-hma","in front of"],
   ["နောက်မှာ","nauq-hma","behind"],["အထဲမှာ","a-t'eh-hma","inside"],["အပြင်မှာ","a-pyin-hma","outside"],
   ["အောက်မှာ","auq-hma","below / under"],["အပေါ်မှာ","apaw-hma","above / on top of"]],
  [{"title":"Landmark + -hma builds any location phrase","explain":"The same -hma from Unit 18 turns any noun into a location word by combining with position words: s'ain-beq-hma (\"next to the shop\"), ta-da-nauq-hma (\"behind the bridge\"). Landmark first, position word, then -hma.",
    "examples":[["ဆိုင်ဘေးမှာ","S'ain-beq-hma","next to the shop"],["တံတားနောက်မှာ","Ta-da-nauq-hma","behind the bridge"]]}],
  "Takes ဒ and adds a small hook at the top-right corner — same base loop, one extra flick."
)

U(20, "န", "na", "First Needs", "Getting around by bus, car, or train",
  "Talk about how you're traveling and catch the right transport.",
  {"type":"dialogue","lines":[
    ["A","Baq-sa-ka beh-hma si-ya-lé?","baq-sa-ka beh-hma si-ya-lé","Where do I catch the bus?"],
    ["B","Di-hma si-ya-deh.","di-hma si-ya-deh","You catch it right here."],
    ["A","Bu-da beh-lauq ca-la?","bu-da beh-lauq ca-la","How far is the station?"],
    ["B","Ma-ca-ba-bú.","ma-ca-ba-bú","Not far."]
  ]},
  [["ဘတ်စ်ကား","baq-sa-ka","bus"],["ကား","ka","car"],["ရထား","ya-ta","train"],
   ["တက္ကစီ","teq-ka-si","taxi"],["စီးတယ်","si-deh","to ride"],["ဘူတာ","bu-da","station"],
   ["အငှား","a-hnga","rental / for hire"],["ယာဉ်","yin","vehicle (general)"]],
  [{"title":"si-deh — the one verb for riding anything","explain":"Si-deh covers riding a bus, car, train, bike, boat, or elephant — one all-purpose verb, unlike English's drive/ride/take. What changes is the noun in front of it, not the verb.",
    "examples":[["ဘတ်စ်ကားစီးတယ်","Baq-sa-ka si-deh.","to ride the bus"],["ရထားစီးတယ်","Ya-ta si-deh.","to ride the train"]]},
   {"title":"si-ya-deh — \"you catch it (there)\"","explain":"Adding -ya- before -deh signals possibility/necessity — roughly \"[you] get to / need to [verb].\" Si-ya-deh, \"that's where you catch it,\" is subtly different from plain si-deh, \"to ride.\"",
    "examples":[["ဒီမှာစီးရတယ်။","Di-hma si-ya-deh.","You catch it right here."]]}],
  "One of the most frequent letters in the script — a loop with a straight tail down the right side."
)

# ============== PART 3 — FIRST CONVERSATIONS ==============

U(21, "ပ", "pa", "First Conversations", "Where are you from",
  "Answer the question every traveler gets asked first.",
  {"type":"dialogue","lines":[
    ["A","Beh-ga la-dha-lé?","beh-ga la-dha-lé","Where do you come from?"],
    ["B","Ameiq-ka-ga la-ba-deh.","ameiq-ka-ga la-ba-deh","I come from America."],
    ["A","Myan-ma-go beh-dawh la-thala?","myan-ma-go beh-dawh la-dha-la","When did you come to Myanmar?"],
    ["B","Ya-dhiq-pyi-ga la-ba-deh.","ya-dhiq-pyi-ga la-ba-deh","I came this year."]
  ]},
  [["ပြည်","pyi","country"],["နိုင်ငံ","nain-ngan","nation"],["နိုင်ငံခြား","nain-ngan-c'a","foreign"],
   ["-ကနေ / -ကလာတယ်","-ga / -ga la-deh","from / to come from"],["အမေရိကန်","ameiq-ka","America"],
   ["ခရီးသည်","k'a-yi-thé","traveler"],["ပထမဆုံး","pa-t'a-ma-zoun","the first time"],["ခရီးစဉ်","k'a-yi-zin","journey"]],
  [{"title":"-ga — marking where from","explain":"-ga attached to a place marks it as a source or starting point: Ameiq-ka-ga la-ba-deh, \"I come from America.\" It pairs with beh-ga la-dha-lé? to ask and answer the same question.",
    "examples":[["ဘယ်ကလာသလဲ။","Beh-ga la-dha-lé?","Where do you come from?"],["အမေရိကန်ကလာပါတယ်။","Ameiq-ka-ga la-ba-deh.","I'm from America."]]}],
  "A closed loop, flat-bottomed — this is the ပ from the very first example in the Basic Scripts Cheatsheet: ပ + ူ = ပူ."
)

U(22, "ဖ", "hpa", "First Conversations", "How long, and first impressions",
  "Talk about how long you're staying and what you think of the place.",
  {"type":"dialogue","lines":[
    ["A","Beh-lauq ca-ca né-me-lé?","beh-lauq ca-ca né-me-lé","How long will you stay?"],
    ["B","Ta-la-béh né-meh.","ta-la-béh né-meh","Just one month."],
    ["A","Myan-ma-go beh-lo t'in-lé?","myan-ma-go beh-lo t'in-lé","What do you think of Myanmar?"],
    ["B","Théiq hla-ba-deh!","théiq hla-ba-deh","It's really beautiful!"]
  ]},
  [["နေတယ်","né-deh","to stay / to live"],["လ","la","month"],["ရက်","yeq","day"],
   ["ထင်တယ်","t'in-deh","to think / to guess"],["လှတယ်","hla-deh","to be beautiful"],
   ["စိတ်ဝင်စားတယ်","seiq-win-sa-deh","to be interesting"],["ပထမဆုံးအကြိမ်","pa-t'a-ma-zoun a-cein","the first time"],
   ["ပြန်လာချင်တယ်","pyan-la-jin-deh","to want to come back"]],
  [{"title":"beh-lauq ca-ca — \"for how long\"","explain":"Ca-ca (doubling ca-deh, \"to take time\") after beh-lauq asks specifically about duration, distinct from beh-lauq-lé (price, Unit 6) — same question word, different follow-up shapes the meaning.",
    "examples":[["ဘယ်လောက်ကြာကြာနေမလဲ။","Beh-lauq ca-ca né-me-lé?","How long will you stay?"]]},
   {"title":"t'in-deh — sharing an opinion","explain":"Beh-lo t'in-lé? (\"what do you think?\") is the natural opener for small talk about impressions — answer it with any adjective-verb you already know: hla-ba-deh, seiq-win-sa-ba-deh, kaun-ba-deh.",
    "examples":[["ဘယ်လိုထင်လဲ။","Beh-lo t'in-lé?","What do you think?"],["လှပါတယ်။","Hla-ba-deh.","It's beautiful."]]}],
  "ဖ is ပ with the top broken open into a loop. Write ပ, then let the top curl outward instead of closing."
)

U(23, "ဗ", "ba", "First Conversations", "What's your name",
  "Introduce yourself and ask for someone else's name — properly, the Okell way.",
  {"type":"dialogue","lines":[
    ["A","Nan-meh beh-lo k'aw-dha-lé?","nan-meh beh-lo k'aw-dha-lé","What is your name?"],
    ["B","Ca-na-w nan-meh-ga Aun-ba.","ca-na-w nan-meh-ga aun-ba","My name is Aung. (man speaking)"],
    ["A","Twé-ya-da wun-tha-ba-deh.","twé-ya-da wun-tha-ba-deh","Nice to meet you."],
    ["B","Ca-ma nan-meh-ga Su ba.","ca-ma nan-meh-ga su ba","My name is Su. (woman speaking)"]
  ]},
  [["နာမည်","nan-meh","name"],["ခေါ်တယ်","k'aw-deh","to be called / to call"],
   ["ကျွန်တော်","ca-na-w","I (man speaking)"],["ကျွန်မ","ca-ma","I (woman speaking)"],
   ["တွေ့တယ်","twé-deh","to meet"],["ဝမ်းသာတယ်","wun-tha-deh","to be glad"],
   ["-က","-ga","(topic marker — \"as for...\")"],["ခင်ဗျား/ရှင်","khin-bya / shin","you (to a man / to a woman, polite)"]],
  [{"title":"ca-na-w / ca-ma — \"I\", by speaker gender","explain":"This is BAMA's own letter, and it starts the most personal sentence you'll learn: \"I\" has two words depending on who's speaking — ca-na-w for a man, ca-ma for a woman. Not a choice; it's fixed by the speaker's own gender.",
    "examples":[["ကျွန်တော်ကြိုက်ပါတယ်။","Ca-na-w caiq-pa-deh.","I like it. (man)"],["ကျွန်မကြိုက်ပါတယ်။","Ca-ma caiq-pa-deh.","I like it. (woman)"]]},
   {"title":"Nan-meh beh-lo k'aw-dha-lé — asking a name properly","explain":"Literally \"name — how — is called?\" This is Okell's own phrasing for \"what is your name?\" — note k'aw-dha-lé uses the -tha-la/-dha-la question ending from Unit 4, closed by -lé because beh-lo is a question word (Unit 7's rule).",
    "examples":[["နာမည်ဘယ်လိုခေါ်သလဲ။","Nan-meh beh-lo k'aw-dha-lé?","What is your name?"]]}],
  "ဗ — this is BAMA's own mark, and the first sound in ဗမာ, \"Bama.\" A rounded top over a small loop underneath."
)

U(24, "ဘ", "ba", "First Conversations", "How old are you",
  "Ask and answer questions about age.",
  {"type":"dialogue","lines":[
    ["A","A-t'eq beh-lauq shi-bi-lé?","a-t'eq beh-lauq shi-bi-lé","How old are you?"],
    ["B","Thoun-zeh-hniq shi-ba-bi.","thoun-zeh-hniq shi-ba-bi","I'm thirty-two."],
    ["A","Khin-bya-ga-cho beh-lauq shi-bi-lé?","khin-bya-ga-cho beh-lauq shi-bi-lé","And you (older, polite)?"],
    ["B","Ngá-zeh shi-ba-bi.","ngá-zeh shi-ba-bi","I'm fifty."]
  ]},
  [["အသက်","a-t'eq","age"],["နှစ်","hniq","year(s)"],["ရှိတယ်","shi-deh","there is / to have / to be [age]"],
   ["အကြီး","a-cí","older / senior"],["အငယ်","a-ngeh","younger / junior"],
   ["-ပြီ","-bi","already (change-of-state ending)"],["အသက်ကြီးတယ်","a-t'eq cí-deh","to be old (in years)"],
   ["ငယ်ရွယ်တယ်","ngeh-ywéh-deh","to be young"]],
  [{"title":"shi-deh — \"there is,\" \"to have,\" and age all at once","explain":"Shi-deh is the general existence verb — \"there is,\" \"to have\" — and Burmese states age with it: a-t'eq thoun-zeh-hniq shi-deh, literally \"age thirty exists.\" It behaves like any other -deh verb for negatives and questions.",
    "examples":[["အသက်ဘယ်လောက်ရှိပြီလဲ။","A-t'eq beh-lauq shi-bi-lé?","How old are you?"],["အသက်နှစ်ဆယ်ရှိပါတယ်။","A-t'eq hna-zeh shi-ba-deh.","I'm twenty."]]},
   {"title":"-bi — a change that's already happened","explain":"-bi replaces -deh when something has newly become true — shi-ba-bi (\"[I] am now...\") signals your age as an already-settled fact, not a general statement, subtly different from plain shi-ba-deh.",
    "examples":[["နှစ်ဆယ်ရှိပါပြီ။","Hna-zeh shi-ba-bi.","I've turned twenty."]]}],
  "ဘ is a large open loop — one of the roomiest letters on the page. Give it space; don't let it collapse into a tight circle."
)

U(25, "မ", "ma", "First Conversations", "Asking about work",
  "Talk about what you do for a living.",
  {"type":"dialogue","lines":[
    ["A","Ba a-louq louq-dha-lé?","ba a-louq louq-dha-lé","What work do you do?"],
    ["B","Ca-ma hsa-ya-ma louq-ba-deh.","ca-ma hsa-ya-ma louq-ba-deh","I'm a teacher. (woman)"],
    ["A","Beh-hma-lé?","beh-hma-lé","Where (do you work)?"],
    ["B","Kyaun-hma-ba.","kyaun-hma-ba","At a school."]
  ]},
  [["အလုပ်","a-louq","work / job"],["လုပ်တယ်","louq-teh","to do / to make"],["ကျောင်း","kyaun","school"],
   ["ကုမ္ပဏီ","koun-pa-ni","company"],["ဆရာ","hsa-ya","teacher (male)"],["ဆရာမ","hsa-ya-ma","teacher (female)"],
   ["အလုပ်ရှင်","a-louq-shin","employer / boss"],["အားလပ်ရက်","a-laq-yeq","day off"]],
  [{"title":"louq-teh — the general verb \"to do\"","explain":"Louq-teh (\"to do, to make\") is the workhorse for describing any job: a-louq louq-teh (\"to do work\"), or noun + louq-teh (\"to work as [noun]\") — hsa-ya-ma louq-ba-deh, \"I work as a teacher.\"",
    "examples":[["ဆရာမလုပ်ပါတယ်။","Hsa-ya-ma louq-ba-deh.","I work as a teacher."]]}],
  "Three humps in a row — a wave shape, evenly spaced. One of the easier letters to keep consistent at speed."
)

U(26, "ယ", "ya", "First Conversations", "Asking about family — married?",
  "Ask politely whether someone is married and reply about your own situation.",
  {"type":"dialogue","lines":[
    ["A","Ein-daun shi-bi-la?","ein-daun shi-bi-la","Are you married?"],
    ["B","Shi-ba-bi.","shi-ba-bi","Yes, I am."],
    ["A","Tha-tha-mi shi-tha-la?","tha-tha-mi shi-tha-la","Do you have children?"],
    ["B","Hna-yauq shi-ba-deh.","hna-yauq shi-ba-deh","I have two."]
  ]},
  [["အိမ်ထောင်","ein-daun","marriage / household"],["ဇနီး","za-ni","wife"],["ခင်ပွန်း","khin-poun","husband"],
   ["သားသမီး","tha-tha-mi","children (son/daughter, general)"],["တစ်ယောက်","ta-yauq","one (person)"],
   ["အပျို","a-pyo","unmarried woman"],["လူပျို","lu-pyo","unmarried man"],["မိသားစု","mi-tha-su","family"]],
  [{"title":"shi-tha-la vs shi-bi-la","explain":"Shi-tha-la (Unit 4's neutral question) simply asks \"do you have?\" Shi-bi-la adds -bi (Unit 24's change-of-state marker) — \"are you [now, already]?\" — the natural form for asking about marriage or age, since both describe a settled state.",
    "examples":[["အိမ်ထောင်ရှိပြီလား။","Ein-daun shi-bi-la?","Are you (already) married?"]]}],
  "A tall stroke with a loop at the base. Draw top to bottom first, then close the loop at the foot."
)

U(27, "ရ", "ya (ra)", "First Conversations", "Parents and siblings",
  "Talk about your parents and brothers and sisters, using the real kinship words.",
  {"type":"dialogue","lines":[
    ["A","မောင်နှမရှိသလား။","Maun-hna-ma shi-tha-la?","Do you have siblings?"],
    ["B","သုံးယောက်ရှိပါတယ်။","Thoun-yauq shi-ba-deh.","I have three."],
    ["A","အဖေအမေရှိသေးသလား။","A-p'é-a-mé shi-dhé-dha-la?","Are your parents still alive?"],
    ["B","ရှိသေးပါတယ်။","Shi-dhé-ba-deh.","Yes, still living."]
  ]},
  [["အဖေ","a-p'é","father"],["အမေ","a-mé","mother"],["အကို","a-ko","older brother"],
   ["အမ","a-ma","older sister"],["ညီ","nyi","younger brother"],["ညီမ","nyi-ma","younger sister"],
   ["မောင်","maun","younger brother (of a woman)"],["ရှိသေးတယ်","shi-dhé-deh","to still be alive / still there"]],
  [{"title":"-dhé — \"still\"","explain":"Attach -dhé (voiced from -thé) before -deh to mean \"still\": shi-dhé-deh, \"[they are] still there / still alive.\" A gentle, important suffix for asking about elderly relatives respectfully.",
    "examples":[["ရှိသေးတယ်။","Shi-dhé-deh.","Still living."],["အလုပ်လုပ်နေသေးတယ်။","A-louq louq-né-dhé-deh.","Still working."]]}],
  "ရ curls in the opposite direction from ယ — same fluid energy, mirrored."
)

U(28, "လ", "la", "First Conversations", "Feelings and small talk",
  "Say how you're feeling and keep a casual conversation moving.",
  {"type":"dialogue","lines":[
    ["A","Pyaw-né-la?","pyaw-né-la","Are you happy?"],
    ["B","Houq-keh, pyaw-ba-deh.","houq-keh, pyaw-ba-deh","Yes, I'm happy."],
    ["A","Pin-ban-né-dha-la?","pin-ban-né-dha-la","Are you tired?"],
    ["B","A-né-ngeh pin-ban-ba-deh.","a-né-ngeh pin-ban-ba-deh","A little tired."]
  ]},
  [["ပျော်တယ်","pyaw-deh","to be happy"],["ပင်ပန်းတယ်","pin-ban-deh","to be tired"],
   ["စိတ်ညစ်တယ်","seiq-nyiq-teh","to be upset"],["စိတ်လှုပ်ရှားတယ်","seiq-hlouq-sha-deh","to be excited"],
   ["-နေတယ်","-né-deh","(continuous / right now)"],["အနည်းငယ်","a-né-ngeh","a little"],
   ["ပူပန်တယ်","pu-ban-deh","to worry"],["အေးဆေးတယ်","é-zé-deh","to be calm / relaxed"]],
  [{"title":"-né-deh — happening right now","explain":"Insert -né- before -deh to mark an action or state as continuous, in progress right now: pin-ban-né-deh, \"[I] am tired [right now],\" versus the timeless pin-ban-deh, \"to be a tiring sort of thing.\"",
    "examples":[["ပင်ပန်းနေတယ်။","Pin-ban-né-deh.","I'm tired (right now)."],["အလုပ်လုပ်နေတယ်။","A-louq louq-né-deh.","I'm working (right now)."]]}],
  "A single wide loop, low and rounded — one of the more forgiving letters to write at speed."
)

U(29, "ဝ", "wa", "First Conversations", "Making plans",
  "Suggest meeting up and check whether someone's free.",
  {"type":"dialogue","lines":[
    ["A","Ma-neq-p'yan a-la?","ma-neq-p'yan a-la","Are you free tomorrow?"],
    ["B","A-ba-deh.","a-ba-deh","Yes, I'm free."],
    ["A","Nya-né-hma twé-ca-ya-aun.","nya-né-hma twé-ca-ya-aun","Let's meet in the evening."],
    ["B","Houq-keh, twé-meh.","houq-keh, twé-meh","Okay, let's meet."]
  ]},
  [["မနက်ဖြန်","ma-neq-p'yan","tomorrow"],["ဒီနေ့","di-né","today"],["မနေ့က","ma-né-ga","yesterday"],
   ["အားတယ်","a-deh","to be free (available)"],["ညနေ","nya-né","evening"],["-ရအောင်","-ya-aun","let's..."],
   ["ဖုန်းခေါ်ပါ့မယ်","p'oun k'aw-ba-meh","I'll call you"],["ချိန်းတယ်","c'ein-deh","to make an appointment"]],
  [{"title":"-ya-aun — a soft \"let's\"","explain":"Twé-ca-ya-aun (\"let's meet\") uses -ya-aun on the verb — a gentle suggestion, not a command. It invites agreement the way -naw invites agreement on a statement, but on an action instead.",
    "examples":[["သွားရအောင်။","Thwa-ya-aun.","Let's go."],["စားရအောင်။","Sa-ya-aun.","Let's eat."]]}],
  "A simple, near-perfect circle — one continuous stroke, no corners."
)

U(30, "သ", "tha (sa)", "First Conversations", "Weather and time",
  "Talk about the weather and what time it is.",
  {"type":"dialogue","lines":[
    ["A","Di-né mo ywa-ma-la?","di-né mo ywa-ma-la","Will it rain today?"],
    ["B","Ywa-lein-ba-deh.","ywa-lein-ba-deh","Looks like it might."],
    ["A","A-k'u beh-hna-na-yi shi-bi-lé?","a-k'u beh-hna-na-yi shi-bi-lé","What time is it now?"],
    ["B","Ngá-na-yi shi-ba-bi.","ngá-na-yi shi-ba-bi","It's five o'clock."]
  ]},
  [["မိုး","mo","rain"],["နေ","né","sun"],["လေ","lé","wind"],["နာရီ","na-yi","o'clock"],
   ["ရာသီဥတု","ya-thi-u-du","weather / season"],["ရွာတယ်","ywa-deh","to rain"],
   ["ပူအိုက်တယ်","pu-aiq-teh","to be muggy"],["အေးစက်တယ်","é-seq-teh","to be freezing cold"]],
  [{"title":"Number + na-yi — telling time","explain":"Just like counting people (Unit 5) or money (Unit 6), time uses a classifier: number + na-yi means \"o'clock.\" Ngá-na-yi = \"five o'clock,\" following the exact same number-classifier pattern you've used all book.",
    "examples":[["ငါးနာရီရှိပြီ။","Ngá-na-yi shi-bi.","It's five o'clock already."]]},
   {"title":"-lein — \"looks like / seems\"","explain":"Ywa-lein-ba-deh (\"looks like rain\") uses -lein to soften a prediction — you're guessing based on evidence, not stating a fact outright.",
    "examples":[["မိုးရွာလိမ့်မယ်။","Mo ywa-lein-meh.","It looks like it'll rain."]]}],
  "A large loop with a tail curling under — a very common, distinctive shape you'll see everywhere in running text."
)

U(31, "ဟ", "ha", "First Conversations", "Health and emergencies",
  "Get help fast when something goes wrong.",
  {"type":"dialogue","lines":[
    ["A","Ku-nyi-ba!","ku-nyi-ba","Help!"],
    ["B","Ba-p'yiq-lé?","ba-p'yiq-lé","What happened?"],
    ["A","Gaun kaiq-né-deh. Hsé-youn t'wa-pé-ba.","gaun kaiq-né-deh. hsé-youn t'wa-pé-ba","I have a headache. Please take me to the hospital."]
  ]},
  [["ကူညီပါ","ku-nyi-ba","help!"],["ဆေးရုံ","hsé-youn","hospital"],["ရဲ","yeh","police"],
   ["ကိုက်တယ်","kaiq-teh","to ache"],["ခေါင်း","gaun","head"],["အန္တရာယ်","an-da-yeh","danger"],
   ["အရေးပေါ်","a-yé-paw","emergency"],["နာတယ်","na-deh","to hurt / to be in pain"]],
  [{"title":"kaiq-teh — the go-to word for aches","explain":"Body part + kaiq-teh (\"to ache\") covers almost any everyday pain: gaun kaiq-teh (headache), wun kaiq-teh (stomachache). Simple, high-frequency, and exactly what you need in an emergency.",
    "examples":[["ခေါင်းကိုက်တယ်။","Gaun kaiq-teh.","I have a headache."],["ဗိုက်ကိုက်တယ်။","Wun kaiq-teh.","I have a stomachache."]]},
   {"title":"t'wa-pé-ba — \"please take (me)\"","explain":"T'wa-pé-ba (\"please take/lead me there\") combines with a place using -ko or -go: hsé-youn-go t'wa-pé-ba, or simply drop the marker in an urgent, clipped sentence, as above.",
    "examples":[["ဆေးရုံခေါ်သွားပေးပါ။","Hsé-youn k'aw-thwa-pé-ba.","Please take me to the hospital."]]}],
  "A tall loop with a straight leg down the right — write the loop first, then drop the leg without lifting the pen."
)

U(32, "ဠ", "la (great)", "First Conversations", "Apologies",
  "Apologize sincerely and accept an apology graciously.",
  {"type":"dialogue","lines":[
    ["A","Taun-ban-ba-deh.","taun-ban-ba-deh","I apologize."],
    ["B","Kiq-sa ma-shi-ba-bú.","kiq-sa ma-shi-ba-bú","No problem at all."],
    ["A","A-hma-ba, k'win-hlouq-pa.","a-hma-ba, k'win-hlouq-pa","My mistake — please forgive me."]
  ]},
  [["တောင်းပန်တယ်","taun-ban-deh","to apologize"],["အမှား","a-hma","mistake"],
   ["ခွင့်လွှတ်တယ်","k'win-hlouq-teh","to forgive"],["ကိစ္စမရှိပါဘူး","kiq-sa ma-shi-ba-bú","no problem / it's alright"],
   ["နောက်တစ်ခါ","nauq-ta-k'a","next time"],["တမင်မဟုတ်ပါဘူး","ta-min ma-houq-pa-bú","it wasn't on purpose"]],
  [{"title":"A rare letter, a common courtesy","explain":"ဠ appears in almost no modern words — it's kept mainly in Pali-derived spellings — but the phrase this unit teaches, taun-ban-ba-deh, is something you'll want ready in any language, any day.",
    "examples":[["တောင်းပန်ပါတယ်။","Taun-ban-ba-deh.","I'm sorry / I apologize."]]}],
  "Shares လ's loop with a small extra curl added. Write လ, then add the flourish without breaking stroke."
)

U(33, "အ", "a", "First Conversations", "Saying goodbye — and review",
  "Close a conversation warmly, and look back at everything Book 1 covered.",
  {"type":"dialogue","lines":[
    ["A","Thwa-daw-meh-naw.","thwa-daw-meh-naw","I'm heading off now."],
    ["B","Pyan-twé-ca-meh.","pyan-twé-ca-meh","See you again."],
    ["A","Cé-zú a-mya-cí pé-ba-deh.","cé-zú a-mya-cí pé-ba-deh","Thank you so much."],
    ["B","Thwa-la-ba-oun-meh.","thwa-la-ba-oun-meh","Take care — I'll be on my way too."]
  ]},
  [["နှုတ်ဆက်တယ်","hnouq-seq-teh","to say goodbye"],["ပြန်တွေ့မယ်","pyan-twé-meh","see you again"],
   ["ကျေးဇူးအများကြီး","cé-zú a-mya-cí","thank you so much"],["နှစ်ဆယ့်သုံး","hna-zeh-thoun","twenty-three (bonus number!)"],
   ["ဒါဆိုရင်","da-hso-yin","in that case / so then"],["တွေ့ရတာဝမ်းသာပါတယ်","twé-ya-da wun-tha-ba-deh","it was nice meeting you"]],
  [{"title":"The whole sentence engine, in one look back","explain":"You've now met every consonant, and every core sentence-ending you need: -deh (state it), -naw (invite agreement), -ba-/-pa- (say it politely), ma-...-bú (say no), -tha-la/-dha-la (ask plainly), -lé (ask with a question word), -meh (say what will happen), -bi (say it's already so), and -né- (say it's happening right now).",
    "examples":[["ပူတယ်။ ပူတယ်နော်။ ပူပါတယ်။ မပူပါဘူး။ ပူသလား။ ဘာလဲ။ ပူမယ်။ ပူပြီ။ ပူနေတယ်။","Pu-deh. Pu-deh-naw. Pu-ba-deh. Ma-pu-ba-bú. Pu-tha-la. Ba-lé. Pu-meh. Pu-bi. Pu-né-deh.","It's hot. Hot, isn't it? It's hot (polite). It's not hot. Is it hot? What is it? It'll be hot. It's (now) hot. It's (currently) hot."]]}],
  "အ stands alone — the only letter that's also a full vowel carrier by itself. A closed loop with a short tail, closing the set you opened in Unit 1."
)

if __name__ == "__main__":
    import json
    with open("data/book1-units.json", "w", encoding="utf-8") as f:
        json.dump(UNITS, f, ensure_ascii=False, indent=1)
    print(len(UNITS), "units written")
