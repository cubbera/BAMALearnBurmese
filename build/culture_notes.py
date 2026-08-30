# -*- coding: utf-8 -*-
# Adds a "culture" field to every unit: what's actually happening
# pragmatically/socially in that unit's conversation, not just what
# the words mean. This is the difference between translating Burmese
# and teaching how to actually navigate a conversation as a Burmese
# speaker would read it.

import json

CULTURE = {

1: "Notice the receptionist opens with Mingalar-ba — that's genuine, but it's not what two Burmese friends say passing each other on the street. Mingalar-ba is a 20th-century coinage, popularized through schools and radio, and today it lives mainly in formal, service, or foreigner-facing settings — exactly this one. On the street, people mostly skip \"hello\" entirely and ask a real question instead: Beh thwa-mha-lé? (\"Where are you headed?\") or Hta-min sa-pi-bi-la? (\"Have you eaten yet?\") — the same way \"how's it going\" in English isn't really asking about your wellbeing. Nobody expects a detailed answer to either; \"just around\" or \"not yet\" closes the loop fine.",

2: "Being offered a drink the moment you arrive somewhere isn't a special gesture — it's the default. Turning it down flat can read as more distant than intended. If you don't want anything, a soft ma-thauq-jin-ba-bú (Unit 3) plus a reason lands better than silence or a bare no, and it's completely normal to accept a small amount just to be polite even if you don't finish it.",

3: "A flat \"no\" is rarer in Burmese than the dictionary form suggests. Ma-...-bú is grammatically correct and genuinely used, but a lot of everyday refusal happens more softly — a reason instead of a refusal (\"I'm full\" rather than \"I don't want it\"), a hesitant laugh, or simply not answering directly. If someone seems to be dodging a clear yes/no from you, that hesitation often is the no.",

4: "Pointing at food and asking \"do you eat this?\" is a genuinely common, welcome question from a visitor — it signals curiosity, not suspicion. If you're offered a taste of something unfamiliar, trying at least a small amount is read as warmth on your part, even if you don't finish it.",

5: "Burmese hosts routinely over-cater — more food than the headcount needs is a quiet sign of generosity, not poor planning. If you're asked how many people are coming and you're unsure, rounding up is safer than rounding down.",

6: "Bargaining is expected at a street market and basically absent at a fixed-price shop or supermarket — reading which kind of place you're in matters more than the specific words. A good-natured, smiling tone throughout the exchange is doing as much work as the numbers; treating it as a fight rather than a friendly back-and-forth is the actual foreign-tourist tell.",

7: "Asking what a dish is, and where it's from, is genuinely appreciated rather than seen as ignorant — Burmese cuisine varies a lot by region, and locals are often happy to explain. Complimenting a specific dish by name lands better than a generic \"it's good.\"",

8: "You'll often be offered more of something right after you finish it, sometimes more than once, even after you've said you're full — it's closer to a ritual than a real question. A polite, firm ma-lo-ba-bú (\"I don't need it\") once or twice is normal and not rude; the offer isn't a test.",

9: "Struggling with fast, natural Burmese and asking someone to slow down is completely normal, not embarrassing — most people react with warmth or amusement, not impatience. A visitor making a genuine effort, mistakes included, is generally received far better than one who doesn't try at all.",

10: "Two things worth noticing here. First, addressing a stranger by a kinship term (a-ma for an older woman, a-ko for a man near your age — Unit 10's vocabulary) rather than a neutral \"excuse me\" is the actual norm, not an exception. Second, when you need to slip past someone in a crowded space, a slightly lowered head or shoulders while saying kwin-pyu-ba (\"allow me\") is a common physical gesture of respect, especially near elders or monks — making yourself briefly \"smaller\" as you pass is doing as much of the politeness as the words are.",

11: "When a group of Burmese friends goes out to eat, there's often an unspoken understanding about who pays — frequently whoever is older, more established, or hosting. Ko Aung offering to cover the bill next unit isn't generosity out of nowhere; it's closer to a default expectation for him as the local, older friend.",

12: "Watch for the friendly \"fight\" over the bill — both people reaching for it, one insisting, the other protesting — it's a real, common social ritual, not awkwardness. Losing that fight gracefully (as Ko Aung does here, agreeing to \"next time\") is itself part of the etiquette.",

13: "Most street taxis don't run on a meter — the fare is agreed before the ride starts, which is why Ko Aung states a price up front rather than waiting until arrival. Negotiating it isn't rude; not negotiating at all is what marks someone as unfamiliar with how it works.",

14: "Giving directions from inside a moving vehicle is typically short and immediate — teh-teh thwa-ba (\"go straight\"), not a fuller polite sentence. The short imperative form isn't brusqueness, it's just what real-time, in-motion Burmese sounds like.",

15: "You're welcome to pick up and examine items at most stalls without any obligation to buy — handling goods is normal shopping behavior, not a commitment. A shopkeeper re-folding or replacing an item you looked at isn't a signal of annoyance.",

16: "Bargaining among Burmese people is often closer to a friendly game than a confrontation — both sides know roughly where it'll land, and getting there with good humor matters as much as the final number. Having a local friend along, like Ko Aung here, commonly gets a better price than a visitor alone would — not through anything underhanded, just the ordinary \"local rate.\"",

17: "Always ask before photographing monks, at religious sites, or people in general — it's taken seriously, not a formality. The reverse also happens often: don't be surprised if locals ask to take a photo with you instead of the other way around, especially outside major cities.",

18: "When you need to pass in front of someone — stepping past a seated group, cutting across someone's path — a small forward bow or lowered posture while moving through is the everyday version of \"excuse me,\" often doing more work than any phrase. It's especially expected in front of elders or monks, but common enough generally that you'll see locals do it for each other too.",

19: "Distance and time estimates in casual conversation are often more social than literal — \"just a bit further\" or \"five minutes\" can stretch a fair amount in practice. Treat these as reassurance more than precise measurement, the way you might in any language, just more so.",

20: "Strangers will often just point or physically walk a short distance with you to show the way, rather than give a verbal string of directions — showing is more common than telling. If someone starts walking alongside you after you ask directions, they're probably helping, not following you.",

21: "Personal questions that might feel forward elsewhere — where you're from, your age, whether you're married — are asked early and often in Myanmar, and answering them isn't an imposition, it's how people show interest in you. Expect this pattern to keep coming up through the rest of the book; it's not unique to Ko Aung.",

22: "Warm, general praise of the country (\"it's beautiful,\" \"the food is great\") is welcomed but sometimes lightly waved off, almost reflexively — a specific compliment about one place, dish, or person tends to land more genuinely than a broad one.",

23: "Burmese names don't work like Western ones — there's no inherited family surname passed down, and a name is usually chosen fresh for each child, often tied to their birth day of the week astrologically. The title before a name (Ko, U, Daw, Ma — which you'll meet properly in later books) carries as much social information as the name itself.",

24: "Asking someone's age directly, as Su does here, is completely ordinary — age often determines the kinship terms and level of formality used with someone (whether you're a \"Ko,\" older brother, or \"younger\" to them), so it's practical information, not a personal question the way it might read in English.",

25: "Descriptions of one's own job often undersell it a little — modesty in talking about your own status or achievements is the norm, so a humble-sounding answer may reflect politeness more than the actual scale of what someone does.",

26: "Like age, marital status is asked early and directly — again, out of genuine social interest and because it shapes how people relate to you, not because it's considered private the way it might be elsewhere.",

27: "Multi-generational households are common, and asking after someone's parents specifically is a real sign of respect and care, not small talk filler. Family is generally treated as the most stable, most important reference point in a conversation — you'll notice Ko Aung says as much outright in this unit.",

28: "Burmese conversation tends to keep an even, harmonious surface — genuine tiredness, stress, or worry is often understated (\"a little tired\" instead of \"exhausted\") rather than displayed openly. Reading past the understatement, and responding with the same gentle check-in Su does here, is more useful than taking the words at face value.",

29: "Two things worth knowing. On the phone, Burmese speakers commonly answer with Alo? (a loan from \"hello,\" used only for phone calls — never in person). And on invitations: a specific plan with a place and rough time, like this unit's, is a real invitation meant to happen. A vaguer \"come by sometime\" offered in passing is often closer to warmth than a commitment — the way \"we should get lunch sometime\" often works in English. If you're not sure which one you've been given, it's completely fine to ask directly, or suggest a specific time yourself and see what happens.",

30: "Plans and daily rhythms often bend around the weather and the lunar calendar more than the clock — many holidays and events are set by the Buddhist calendar rather than a fixed Gregorian date. Treat scheduled times as reasonably loose by default, in both directions.",

31: "What you're seeing in this unit — near-strangers dropping everything to help — isn't exaggerated for the story. A strong communal expectation to help someone in visible trouble, especially a guest, runs deep, and people will often go further than you'd think to ask for, or expect.",

32: "Direct correction or confrontation in front of others is generally avoided in favor of a private, gentle word — public apologies or callouts can cause more embarrassment than the original problem. A quiet, sincere taun-ban-ba-deh, like Unit 32 teaches, usually closes the matter completely; there's rarely a need to revisit it.",

33: "Burmese goodbyes tend to include a reciprocal blessing — kyan-ma-ba-zé (\"stay well/healthy\") rather than a bare \"bye\" — which is why Ko Aung closes with it here. And when a real friend says \"call me next time you're here,\" as he does, it's almost always meant sincerely, not as a farewell formality — which is the real answer to a question from early in the book: how do you tell a genuine invitation from a polite one? By the time you reach here, you'll likely already know the difference by ear.",
}

with open("data/book1-units.json", encoding="utf-8") as f:
    units = json.load(f)

for u in units:
    n = u["n"]
    if n in CULTURE:
        u["culture"] = CULTURE[n]

with open("data/book1-units.json", "w", encoding="utf-8") as f:
    json.dump(units, f, ensure_ascii=False, indent=1)

print("Added culture notes to", len(CULTURE), "of", len(units), "units")
