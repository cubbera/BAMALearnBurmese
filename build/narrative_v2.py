# -*- coding: utf-8 -*-
# Overrides the "main" field of every unit with a single continuous narrative:
# a traveler arrives in Yangon, meets Ko Aung (a local who becomes their guide),
# then Ko Aung's friend Su. Length grows unit by unit — 4 lines early on, up to
# 8-9 lines plus a short narrated paragraph by the end of the book — instead of
# each unit being an isolated, disconnected vignette.
#
# Speaker key used throughout: "H" = hotel staff (units 1-3 only),
# "K" = Ko Aung, "S" = Su, "Y" = You (the learner/traveler).

import json

DIALOGUES = {}

def D(n, kind, lines, narration=None):
    DIALOGUES[n] = {"type": kind, "lines": lines}
    if narration:
        DIALOGUES[n]["narration"] = narration

# ---------------- FOUNDATIONS ----------------

D(1, "dialogue", [
  ["H","မင်္ဂလာပါ။","Mingalar-ba.","Hello."],
  ["Y","မင်္ဂလာပါ။ ပူတယ်နော်။","Mingalar-ba. Pu-deh-naw.","Hello. Hot today, isn't it."],
  ["H","ဟုတ်ကဲ့၊ ပူပါတယ်။","Houq-keh, pu-ba-deh.","Yeah, it is."],
  ["Y","ရပါတယ်။","Ya-ba-deh.","That's alright."]
])

D(2, "dialogue", [
  ["H","ရေအေးသောက်ပါ။","Yé-é thauq-pa.","Have some cold water."],
  ["Y","ကျေးဇူးတင်ပါတယ်။","Cé-zú-tin-ba-deh.","Thank you."],
  ["H","ဒီဟိုတယ်ကောင်းပါတယ်နော်။","Di ho-teh kaun-ba-deh-naw.","This hotel is nice, isn't it."],
  ["Y","ဟုတ်ကဲ့၊ သိပ်ကောင်းပါတယ်။","Houq-keh, théiq kaun-ba-deh.","Yeah, it's really nice."]
])

D(3, "dialogue", [
  ["H","ကော်ဖီသောက်မလား။","Kaw-p'i thauq-mala.","Would you like coffee?"],
  ["Y","မသောက်ချင်ပါဘူး၊ ကျေးဇူးပဲ။","Ma-thauq-jin-ba-bú, cé-zú-béh.","I don't want any, thanks."],
  ["H","လက်ဖက်ရည်ရော။","Leq-p'eq-yé yaw.","How about tea?"],
  ["Y","ဟုတ်ကဲ့၊ သောက်ချင်ပါတယ်။","Houq-keh, thauq-jin-ba-deh.","Yes, I'd like that."]
])

D(4, "dialogue", [
  ["H","ထမင်းစားပြီးပြီလား။","Hta-min sa-pí-bi-la.","Have you eaten yet?"],
  ["Y","မစားရသေးပါဘူး။","Ma-sa-ya-dhé-ba-bú.","Not yet."],
  ["H","ဒါဆို ဒီဟာစားသလား။","Da-hso di-ha sa-tha-la.","Then — do you eat this?"],
  ["Y","ဟုတ်ကဲ့၊ စားပါတယ်။","Houq-keh, sa-ba-deh.","Yes, I do."]
])

D(5, "dialogue", [
  ["H","မနက်စာဘယ်နှစ်ယောက်စားမလဲ။","Ma-net-sa beh-hna-yauq sa-ma-lé.","How many people for breakfast?"],
  ["Y","နှစ်ယောက်ပါ။","Hna-yauq ba.","Two people."],
  ["H","ဟုတ်ကဲ့၊ ခဏလောက်စောင့်ပါ။","Houq-keh, k'a-na-lauq saun-pa.","Okay, please wait a moment."],
  ["Y","ကျေးဇူးတင်ပါတယ်။","Cé-zú-tin-ba-deh.","Thank you."]
])

D(6, "dialogue", [
  ["Y","ဒါဘယ်လောက်လဲ။","Da beh-lauq-lé.","How much is this?"],
  ["H","ငါးရာကျပ်ပါ။","Ngá-ya caq ba.","Five hundred kyats."],
  ["Y","သိပ်ဈေးကြီးတယ်နော်။","Théiq zé-cí-deh-naw.","That's quite expensive, isn't it."],
  ["H","ဈေးမကြီးပါဘူး၊ ဈေးချိုပါတယ်။","Zé-ma-cí-ba-bú, zé-cho-ba-deh.","It's not expensive, it's cheap."]
])

D(7, "dialogue", [
  ["Y","ဒါဘာလဲ။","Da ba-lé.","What is this?"],
  ["H","ဒါထမင်းပါ။","Da hta-min ba.","This is rice."],
  ["Y","ဟိုဟာရော ဘာလဲ။","Ho-ha yaw ba-lé.","And what about that one?"],
  ["H","ဟိုဟာက ဟင်းချိုပါ။","Ho-ha-ga hin-cho ba.","That's soup."]
])

D(8, "dialogue", [
  ["Y","ဘာလိုချင်သလဲ။","Ba lo-jin-dha-lé.","What would you like?"],
  ["H","ရေလိုချင်ပါတယ်။","Yé lo-jin-ba-deh.","I'd like water."],
  ["Y","ရေပေးပါ။","Yé pé-ba.","Water, please."],
  ["H","ဟုတ်ကဲ့၊ ရပါတယ်။","Houq-keh, ya-ba-deh.","Sure, no problem."]
])

# ---------------- FIRST NEEDS ----------------
# You leave the hotel and try the street market — and get lost in fast Burmese.

D(9, "dialogue", [
  ["H","(မြန်မြန်ပြောသံ)","(fast, natural-speed Burmese)",""],
  ["Y","ဆောရီး၊ နားမလည်ပါဘူး။","Sáw-rí, ná-ma-leh-ba-bú.","Sorry, I don't understand."],
  ["Y","ပြန်ပြောပေးပါ။","P'yan-pyaw-pé-ba.","Please say that again."],
  ["H","နှေးနှေးပြောပေးပါ့မယ်။","Hné-hné pyaw-pé-ba-meh.","I'll speak slowly."],
  ["Y","ကျေးဇူးတင်ပါတယ်။","Cé-zú-tin-ba-deh.","Thank you."]
])

# Ko Aung, standing nearby, steps in and helps.

D(10, "dialogue", [
  ["K","ကို အောင် ပါ။ ကူညီပေးရမလား။","Ko Aun ba. Ku-nyi-pé-ya-ma-la.","I'm Ko Aung. Should I help you?"],
  ["Y","ဟုတ်ကဲ့၊ ကျေးဇူးတင်ပါတယ်။","Houq-keh, cé-zú-tin-ba-deh.","Yes please, thank you."],
  ["K","ဒီဟာဘယ်လောက်လဲလို့ မေးနေတာလား။","Di-ha beh-lauq-lé-lo mé-né-da-la.","Were you asking how much this is?"],
  ["Y","ဟုတ်ကဲ့။ ဒီဟာဘယ်လောက်လဲ။","Houq-keh. Di-ha beh-lauq-lé.","Yes. How much is this?"],
  ["K","ငါးရာကျပ်တဲ့။","Ngá-ya caq-teh.","She says five hundred kyats."],
  ["Y","ကျေးဇူးပဲ၊ ကို အောင်။","Cé-zú-béh, Ko Aun.","Thanks, Ko Aung."]
])

# Ko Aung suggests a café.

D(11, "dialogue", [
  ["K","ဒီအနီးမှာကော်ဖီဆိုင်ရှိတယ်။ သွားမလား။","Di a-ni-hma kaw-p'i-s'ain shi-deh. Thwa-mala.","There's a café nearby. Shall we go?"],
  ["Y","သွားရအောင်။","Thwa-ya-aun.","Let's go."],
  ["K","မီနူးကြည့်လို့ရမလား။","Mi-nú cí-lo ya-ma-la.","May we see the menu?"],
  ["H","ရပါတယ်။","Ya-ba-deh.","Of course."],
  ["Y","ဟင်းချိုတစ်ခွက်ပေးပါ။","Hin-cho ta-k'weq pé-ba.","One bowl of soup, please."],
  ["H","ဟုတ်ကဲ့၊ ခဏလောက်စောင့်ပါ။","Houq-keh, k'a-na-lauq saun-pa.","Sure, one moment please."]
])

D(12, "dialogue", [
  ["Y","ဘေလ်ပေးပါ။","Beil pé-ba.","The bill, please."],
  ["H","ငါးရာငါးဆယ်ပါ။","Ngá-ya-ngá-zeh ba.","It's 550."],
  ["K","ကျွန်တော်ရှင်းမယ်။","Ca-na-w shin-meh.","I'll settle it."],
  ["Y","မလိုပါဘူး၊ ကျွန်တော်ရှင်းမယ်။","Ma-lo-ba-bú, ca-na-w shin-meh.","No need, I'll pay."],
  ["K","ဟုတ်ကဲ့၊ ဒါဆိုနောက်တစ်ခါ။","Houq-keh, da-hso nauq-ta-k'a.","Alright, next time then."],
  ["Y","ကျေးဇူးတင်ပါတယ်။","Cé-zú-tin-ba-deh.","Thank you."]
])

D(13, "dialogue", [
  ["K","ကျွန်တော်တက္ကစီယာဉ်မောင်းတယ်။ ဘယ်ကိုသွားချင်လဲ။","Ca-na-w teq-ka-si yin-maun-deh. Beh-go thwa-jin-lé.","I drive a taxi. Where do you want to go?"],
  ["Y","ရွှေတိဂုံဘုရားကိုသွားချင်ပါတယ်။","Shwé-da-goun p'a-ya-go thwa-jin-ba-deh.","I want to go to Shwedagon Pagoda."],
  ["K","ဟုတ်ကဲ့။ လေးထောင်ကျပါတယ်။","Houq-keh. Lé-daun ca-ba-deh.","Alright. It costs 4000."],
  ["Y","သိပ်ကြီးပါတယ်။ နည်းနည်းလျှော့ပေးပါ။","Théiq cí-ba-deh. Né-né shaw-pé-ba.","That's a lot. A little discount, please?"],
  ["K","ဟုတ်ကဲ့၊ သုံးထောင်ပါပဲ။","Houq-keh, thoun-daun-ba-béh.","Alright, 3000 then."],
  ["Y","ကျေးဇူးတင်ပါတယ်။","Cé-zú-tin-ba-deh.","Thank you."]
])

D(14, "dialogue", [
  ["K","တည့်တည့်သွားရမလား။","Teh-teh thwa-ya-ma-la.","Should I go straight?"],
  ["Y","ဟုတ်ကဲ့၊ တည့်တည့်သွားပါ။","Houq-keh, teh-teh thwa-ba.","Yes, go straight."],
  ["Y","ရှေ့မှာဘယ်ဘက်ကိုလှည့်ပါ။","Shé-hma beh-beq-ko lé-ba.","Turn left up ahead."],
  ["K","ဟုတ်ကဲ့။","Houq-keh.","Okay."],
  ["Y","ဒီမှာရပ်ပါ။","Di-hma yaq-pa.","Stop here."],
  ["K","ဟုတ်ကဲ့၊ ရောက်ပါပြီ။","Houq-keh, yauq-pa-bi.","Alright, we've arrived."]
])

D(15, "dialogue", [
  ["K","ဘုရားဖူးပြီးရင် ဈေးလေးဝင်ကြည့်မလား။","P'a-ya-p'u-pyí-yin zé-lé win-cí-mala.","After the pagoda, want to look at a little market?"],
  ["Y","ဟုတ်ကဲ့၊ ဝင်ကြည့်ရအောင်။","Houq-keh, win-cí-ya-aun.","Sure, let's go look."],
  ["Y","ဒါဘာလဲ။","Da ba-lé.","What's this?"],
  ["K","ဒါလုံချည်ပါ။","Da longyi ba.","This is a longyi."],
  ["Y","ဟိုဒါကိုကြည့်လို့ရမလား။","Ho-da-ko cí-lo ya-ma-la.","May I look at that one?"],
  ["H","ရပါတယ်၊ ကြည့်ပါ။","Ya-ba-deh, cí-ba.","Sure, go ahead and look."],
  ["Y","ကျေးဇူးတင်ပါတယ်။","Cé-zú-tin-ba-deh.","Thank you."]
])

D(16, "dialogue", [
  ["Y","ဒါဘယ်လောက်လဲ။","Da beh-lauq-lé.","How much is this?"],
  ["H","တစ်သောင်းပါ။","Ta-thaun ba.","Ten thousand."],
  ["Y","ဈေးနည်းနည်းလျှော့ပေးပါ။","Zé né-né shaw-pé-ba.","A little discount on the price, please."],
  ["H","မရပါဘူး၊ ဈေးဒီလောက်ပဲပါ။","Ma-ya-ba-bú, zé di-lauq-béh ba.","Can't do it, the price is only this much."],
  ["K","ကို့ကို ဈေးသင့်အောင်ပြောပေးပါ။","Ko-go zé thin-aun pyaw-pé-ba.","Help him get a fair price."],
  ["H","ဒါဆို ရှစ်ထောင်ပါ။","Da-hso shiq-htaun ba.","Alright then, eight thousand."],
  ["Y","ဟုတ်ကဲ့၊ ဝယ်မယ်။","Houq-keh, weh-meh.","Alright, I'll take it."]
])

D(17, "dialogue", [
  ["Y","ဓာတ်ပုံရိုက်ချင်ပါတယ်။","Daq-poun yaiq-jin-ba-deh.","I'd like to take a photo."],
  ["Y","ရိုက်လို့ရမလား။","Yaiq-lo ya-ma-la.","May I?"],
  ["H","ရပါတယ်၊ ရိုက်ပါ။","Ya-ba-deh, yaiq-pa.","Sure, go ahead."],
  ["K","ကျွန်တော် အတူတူရိုက်ပေးမယ်။","Ca-na-w a-tu-tu yaiq-pé-meh.","I'll take one of us together."],
  ["Y","ကျေးဇူးတင်ပါတယ်၊ ကို အောင်။","Cé-zú-tin-ba-deh, Ko Aun.","Thank you, Ko Aung."],
  ["K","ပြုံးပါ။","Pyoun-ba.","Smile."],
  ["Y","ဟုတ်ကဲ့။","Houq-keh.","Okay."]
])

D(18, "dialogue", [
  ["Y","နောက်တစ်နေရာ ဘယ်မှာလဲ။","Nauq-ta-nay-ya beh-hma-lé.","Where's the next place?"],
  ["K","တည့်တည့်သွားပါ။ ဘယ်ဘက်ကိုလှည့်ပါ။","Teh-teh thwa-ba. Beh-beq-ko lé-ba.","Go straight. Turn left."],
  ["Y","ဒီလမ်းလား။","Di-lan-la.","This road?"],
  ["K","ဟုတ်ကဲ့၊ ဒီလမ်းပါ။","Houq-keh, di-lan ba.","Yes, this road."],
  ["Y","ကျွန်တော်ကိုယ်တိုင်လမ်းလျှောက်ချင်ပါတယ်။","Ca-na-w ko-dain lan-shauq-jin-ba-deh.","I'd like to walk there myself."],
  ["K","ဟုတ်ကဲ့၊ ကျွန်တော်လမ်းညွှန်ပေးမယ်။","Houq-keh, ca-na-w lan-hnyun-pé-meh.","Sure, I'll show you the way."],
  ["Y","ကျေးဇူးတင်ပါတယ်။","Cé-zú-tin-ba-deh.","Thank you."]
])

D(19, "dialogue", [
  ["Y","ဒီကနေ ဘယ်လောက်ကြာမလဲ။","Di-ga-né beh-lauq ca-ma-lé.","How long from here?"],
  ["K","ဆိုင်ဘေးမှာရှိတယ်။ ငါးမိနစ်ပဲ။","S'ain-beq-hma shi-deh. Ngá-mi-niq-béh.","It's next to the shop. Just five minutes."],
  ["Y","ကြာသလား။","Ca-tha-la.","Is it far?"],
  ["K","မကြာပါဘူး၊ နီးပါတယ်။","Ma-ca-ba-bú, ni-ba-deh.","Not far, it's close."],
  ["Y","တံတားနောက်မှာလား။","Ta-da-nauq-hma-la.","Behind the bridge?"],
  ["K","မဟုတ်ပါဘူး၊ ရှေ့မှာပါ။","Ma-houq-pa-bú, shé-hma ba.","No, it's in front."],
  ["Y","ဟုတ်ကဲ့၊ သွားရအောင်။","Houq-keh, thwa-ya-aun.","Okay, let's go."]
])

D(20, "dialogue", [
  ["Y","ညနေဆို ဘယ်လိုပြန်ရမလဲ။","Nya-né-hso beh-lo pyan-ya-ma-lé.","In the evening, how do I get back?"],
  ["K","ဘတ်စ်ကားစီးလို့ရတယ်။ ဒါမှမဟုတ် တက္ကစီခေါ်လို့ရတယ်။","Baq-sa-ka si-lo ya-deh. Da-hma-ma-houq teq-ka-si k'aw-lo ya-deh.","You can take a bus, or call a taxi."],
  ["Y","ဘူတာဘယ်လောက်ကြာလဲ။","Bu-da beh-lauq ca-lé.","How far is the station?"],
  ["K","ဒီကနေ ဆယ်မိနစ်ပဲ။","Di-ga-né sé-mi-niq-béh.","Just ten minutes from here."],
  ["Y","ဒါဆို ဘတ်စ်ကားစီးမယ်။","Da-hso baq-sa-ka si-meh.","Then I'll take the bus."],
  ["K","ဟုတ်ကဲ့၊ ကျွန်တော်ဖုန်းခေါ်ထားမယ်။","Houq-keh, ca-na-w p'oun k'aw-hta-meh.","Okay, I'll be a phone call away."],
  ["Y","ကျေးဇူးတင်ပါတယ်၊ ကို အောင်။","Cé-zú-tin-ba-deh, Ko Aun.","Thank you, Ko Aung."]
])

# ---------------- FIRST CONVERSATIONS ----------------
# The sightseeing is done. Now Ko Aung gets to know you properly.

D(21, "dialogue", [
  ["K","ခဏနားရအောင်။ ဘယ်ကလာတာလဲ။","K'a-na na-ya-aun. Beh-ga la-da-lé.","Let's rest a moment. Where do you come from?"],
  ["Y","အမေရိကန်ကလာပါတယ်။","Ameiq-ka-ga la-ba-deh.","I come from America."],
  ["K","မြန်မာကို ဘယ်တော့လာတာလဲ။","Myan-ma-go beh-dawh la-da-lé.","When did you come to Myanmar?"],
  ["Y","ဒီနှစ်ကလာပါတယ်။","Ya-dhiq-pyi-ga la-ba-deh.","I came this year."],
  ["K","ဒါဆို ပထမဆုံးလာတာပေါ့။","Da-hso pa-t'a-ma-zoun la-da-paw.","So this is your first time, then."],
  ["Y","ဟုတ်ကဲ့၊ ပထမဆုံးပါ။","Houq-keh, pa-t'a-ma-zoun ba.","Yes, my first time."],
  ["K","ကျေနပ်လား။","Cé-naq-la.","Are you enjoying it?"],
  ["Y","ဟုတ်ကဲ့၊ သိပ်ကျေနပ်ပါတယ်။","Houq-keh, théiq cé-naq-ba-deh.","Yes, very much."]
])

D(22, "dialogue", [
  ["K","ဘယ်လောက်ကြာကြာနေမလဲ။","Beh-lauq ca-ca né-me-lé.","How long will you stay?"],
  ["Y","တစ်လပဲနေမယ်။","Ta-la-béh né-meh.","Just one month."],
  ["K","မြန်မာကို ဘယ်လိုထင်လဲ။","Myan-ma-go beh-lo t'in-lé.","What do you think of Myanmar?"],
  ["Y","သိပ်လှပါတယ်။ လူတွေလည်း စိတ်ကောင်းကြတယ်။","Théiq hla-ba-deh. Lu-dwé-léh seiq-kaun-ca-deh.","It's really beautiful. And the people are kind, too."],
  ["K","ရွှေတိဂုံကို ဘယ်လိုထင်လဲ။","Shwé-da-goun-go beh-lo t'in-lé.","What did you think of Shwedagon?"],
  ["Y","အံ့သြစရာကောင်းတယ်။","An-o-za-ya-kaun-deh.","It was amazing."],
  ["K","ပြန်လာချင်သေးလား။","Pyan-la-jin-dhé-la.","Do you want to come back again?"],
  ["Y","ဟုတ်ကဲ့၊ ပြန်လာချင်ပါတယ်။","Houq-keh, pyan-la-jin-ba-deh.","Yes, I'd like to."]
])

D(23, "dialogue", [
  ["K","ဒါက ကျွန်တော့်သူငယ်ချင်း စု ပါ။","Da-ga ca-nawt thu-ngeh-jin Su ba.","This is my friend Su."],
  ["S","မင်္ဂလာပါ။ နာမည်ဘယ်လိုခေါ်သလဲ။","Mingalar-ba. Nan-meh beh-lo k'aw-dha-lé.","Hello. What is your name?"],
  ["Y","ကျွန်တော့်နာမည်က [name] ပါ။","Ca-nawt nan-meh-ga [name] ba.","My name is [name]."],
  ["S","တွေ့ရတာဝမ်းသာပါတယ်။","Twé-ya-da wun-tha-ba-deh.","Nice to meet you."],
  ["Y","ကျွန်တော်လည်း တွေ့ရတာဝမ်းသာပါတယ်။","Ca-na-w-léh twé-ya-da wun-tha-ba-deh.","I'm glad to meet you too."],
  ["K","စုက ဒီမှာနေတဲ့ ကျွန်တော့်သူငယ်ချင်းပါ။","Su-ga di-hma né-deh ca-nawt thu-ngeh-jin ba.","Su's my friend who lives here."],
  ["S","ကို အောင်ရော ဘယ်လိုသိကြသလဲ။","Ko Aun yaw beh-lo thi-ca-dha-lé.","And how do you two know each other?"],
  ["Y","ဈေးထဲမှာတွေ့တာပါ။","Zé-t'eh-hma twé-da ba.","We met at the market."]
])

D(24, "dialogue", [
  ["S","အသက်ဘယ်လောက်ရှိပြီလဲ။","A-t'eq beh-lauq shi-bi-lé.","How old are you?"],
  ["Y","သုံးဆယ့်နှစ်ရှိပါပြီ။","Thoun-zeh-hniq shi-ba-bi.","I'm thirty-two."],
  ["S","ကို အောင်ကရော ဘယ်လောက်ရှိပြီလဲ။","Ko Aun-ga-yaw beh-lauq shi-bi-lé.","And how old is Ko Aung?"],
  ["K","ငါးဆယ်ရှိပါပြီ။","Ngá-zeh shi-ba-bi.","I'm fifty."],
  ["S","ငါကတော့ သုံးဆယ်ပဲ ရှိသေးတယ်။","Nga-ga-daw thoun-zeh-béh shi-dhé-deh.","I'm still only thirty."],
  ["K","စုက ငါ့ထက်အများကြီးငယ်တယ်။","Su-ga ngat'eq a-mya-cí ngeh-deh.","Su's a lot younger than me."],
  ["Y","သုံးယောက်လုံး အသက်မတူဘူးနော်။","Thoun-yauq-loun a-t'eq ma-tu-bu-naw.","None of us are the same age, huh."],
  ["S","ဟုတ်တယ်၊ ဒါပေမဲ့ သူငယ်ချင်းတွေပါ။","Houq-teh, da-bé-méh thu-ngeh-jin-dwé ba.","True, but we're friends all the same."]
])

D(25, "dialogue", [
  ["S","ဘာအလုပ်လုပ်သလဲ။","Ba a-louq louq-dha-lé.","What work do you do?"],
  ["Y","ကျွန်တော် အင်ဂျင်နီယာလုပ်ပါတယ်။","Ca-na-w in-ji-ni-ya louq-ba-deh.","I work as an engineer."],
  ["S","ကျွန်မကတော့ ဆရာမလုပ်ပါတယ်။","Ca-ma-ga-daw hsa-ya-ma louq-ba-deh.","I work as a teacher."],
  ["Y","ဘယ်မှာလဲ။","Beh-hma-lé.","Where (do you work)?"],
  ["S","ကျောင်းမှာပါ၊ ဒီအနီးမှာပဲ။","Kyaun-hma ba, di-a-ni-hma-béh.","At a school, right nearby."],
  ["K","ကျွန်တော်ကတော့ တက္ကစီယာဉ်မောင်းတယ်ဆိုတာ သိပြီးသားနော်။","Ca-na-w-ga-daw teq-ka-si yin-maun-deh-hso-da thi-pyí-dha-naw.","You already know I drive a taxi, right."],
  ["Y","ဟုတ်ကဲ့၊ သိပါပြီ။","Houq-keh, thi-ba-bi.","Yes, I know already."],
  ["S","အလုပ်ကြိုက်လား။","A-louq caiq-la.","Do you like your job?"]
])

D(26, "dialogue", [
  ["S","အိမ်ထောင်ရှိပြီလား။","Ein-daun shi-bi-la.","Are you married?"],
  ["Y","မရှိသေးပါဘူး။","Ma-shi-dhé-ba-bú.","Not yet."],
  ["S","ကို အောင်ကတော့ အိမ်ထောင်ရှိပြီ။","Ko Aun-ga-daw ein-daun shi-bi.","Ko Aung is married already."],
  ["K","ဟုတ်တယ်၊ ဇနီးရှိတယ်။","Houq-teh, za-ni shi-deh.","Right, I have a wife."],
  ["Y","သားသမီးရှိသလား။","Tha-tha-mi shi-tha-la.","Do you have children?"],
  ["K","နှစ်ယောက်ရှိပါတယ်။","Hna-yauq shi-ba-deh.","I have two."],
  ["S","ငါ့ကျတော့ လူပျိုပဲ။","Nga-ga-daw lu-pyo-béh.","As for me, still single."],
  ["Y","အားလုံးအခြေအနေမတူဘူးနော်။","A-loun a-jé-a-né ma-tu-bú-naw.","Everyone's situation is different, huh."]
])

D(27, "dialogue", [
  ["Y","မောင်နှမရှိသလား။","Maun-hna-ma shi-tha-la.","Do you have siblings?"],
  ["K","သုံးယောက်ရှိပါတယ်။","Thoun-yauq shi-ba-deh.","I have three."],
  ["Y","အဖေအမေရှိသေးသလား။","A-p'é-a-mé shi-dhé-dha-la.","Are your parents still alive?"],
  ["K","ရှိသေးပါတယ်၊ ရွာမှာနေတယ်။","Shi-dhé-ba-deh, ywa-hma né-deh.","Still living, they live in the village."],
  ["S","ငါ့ကျတော့ အစ်ကိုတစ်ယောက်ပဲရှိတယ်။","Nga-ga-daw a-ko-ta-yauq-béh shi-deh.","I only have one older brother."],
  ["Y","ရန်ကုန်မှာနေလား။","Yan-goun-hma né-la.","Does he live in Yangon?"],
  ["S","မဟုတ်ပါဘူး၊ မန္တလေးမှာနေတယ်။","Ma-houq-pa-bú, Man-da-lé-hma né-deh.","No, he lives in Mandalay."],
  ["K","မိသားစုက အရေးကြီးဆုံးပဲနော်။","Mi-tha-su-ga a-yé-cí-zoun-béh-naw.","Family's the most important thing, huh."]
])

D(28, "dialogue", [
  ["S","ဒီခရီးစဉ် ပျော်နေလား။","Di k'a-yi-zin pyaw-né-la.","Are you enjoying this trip?"],
  ["Y","ဟုတ်ကဲ့၊ သိပ်ပျော်ပါတယ်။","Houq-keh, théiq pyaw-ba-deh.","Yes, I'm really enjoying it."],
  ["S","ပင်ပန်းနေသလား။","Pin-ban-né-dha-la.","Are you tired?"],
  ["Y","အနည်းငယ်ပင်ပန်းပါတယ်၊ ဒါပေမဲ့ ပျော်ပါတယ်။","A-né-ngeh pin-ban-ba-deh, da-bé-méh pyaw-ba-deh.","A little tired, but I'm happy."],
  ["K","စိတ်ညစ်စရာရှိလား။","Seiq-nyiq-za-ya shi-la.","Anything bothering you?"],
  ["Y","မရှိပါဘူး၊ အားလုံးကောင်းပါတယ်။","Ma-shi-ba-bú, a-loun-kaun-ba-deh.","No, everything's good."],
  ["S","ဒါဆို အေးဆေးနေပါ။","Da-hso é-zé-né-ba.","Then just relax."],
  ["Y","ကျေးဇူးတင်ပါတယ်၊ နှစ်ယောက်လုံး။","Cé-zú-tin-ba-deh, hna-yauq-loun.","Thank you, both of you."]
])

D(29, "dialogue", [
  ["S","မနက်ဖြန်အားလား။","Ma-neq-p'yan a-la.","Are you free tomorrow?"],
  ["Y","ဟုတ်ကဲ့၊ အားပါတယ်။","Houq-keh, a-ba-deh.","Yes, I'm free."],
  ["K","ဒါဆို ညနေမှာတွေ့ကြရအောင်။","Da-hso nya-né-hma twé-ca-ya-aun.","Then let's meet in the evening."],
  ["Y","ဘယ်မှာတွေ့မလဲ။","Beh-hma twé-ma-lé.","Where should we meet?"],
  ["S","ဒီကော်ဖီဆိုင်မှာပဲ တွေ့ကြရအောင်။","Di kaw-p'i-s'ain-hma-béh twé-ca-ya-aun.","Let's just meet at this café."],
  ["Y","ဟုတ်ကဲ့၊ ရပါတယ်။","Houq-keh, ya-ba-deh.","Okay, that works."],
  ["K","ငါဖုန်းခေါ်ပါ့မယ်။","Nga p'oun k'aw-ba-meh.","I'll call."],
  ["S","ဟုတ်ကဲ့၊ မနက်ဖြန်တွေ့မယ်။","Houq-keh, ma-neq-p'yan twé-meh.","Alright, see you tomorrow."],
  ["Y","မနက်ဖြန်တွေ့မယ်။","Ma-neq-p'yan twé-meh.","See you tomorrow."]
])

D(30, "dialogue", [
  ["Y","ဒီနေ့မိုးရွာမလား။","Di-né mo ywa-ma-la.","Will it rain today?"],
  ["K","ရွာလိမ့်ပါတယ်၊ ညနေဆို။","Ywa-lein-ba-deh, nya-né-hso.","Looks like it, come evening."],
  ["S","အခုဘယ်နှစ်နာရီရှိပြီလဲ။","A-k'u beh-hna-na-yi shi-bi-lé.","What time is it now?"],
  ["K","ငါးနာရီရှိပါပြီ။","Ngá-na-yi shi-ba-bi.","It's five o'clock."],
  ["Y","ဒါဆို မိုးမရွာခင် ပြန်ကြရအောင်။","Da-hso mo-ma-ywa-gin pyan-ca-ya-aun.","Then let's head back before it rains."],
  ["S","ဟုတ်ကဲ့၊ လိုက်ပို့ပေးမယ်။","Houq-keh, laiq-po-pé-meh.","Okay, I'll walk you back."],
  ["K","ခုနက ပူတာနဲ့ အခုအေးသွားပြီနော်။","K'u-na-ga pu-da-néh a-k'u é-thwa-bi-naw.","It was hot earlier, and now it's gotten cool, huh."],
  ["Y","ဟုတ်တယ်၊ ရာသီဥတု အမြန်ပြောင်းတာပဲ။","Houq-teh, ya-thi-u-du a-myan pyaun-da-béh.","True, the weather changes fast here."],
  ["S","မြန်မာမှာ ဒီလိုပါပဲ။","Myan-ma-hma di-lo ba-béh.","That's just how it is in Myanmar."]
])

D(31, "dialogue", [
  ["Y","ခေါင်းကိုက်နေတယ်။","Gaun kaiq-né-deh.","I have a headache."],
  ["S","ဘာဖြစ်လဲ။ နေမကောင်းဘူးလား။","Ba-p'yiq-lé. Né-ma-kaun-bu-la.","What's wrong? Are you not feeling well?"],
  ["Y","ဟုတ်ကဲ့၊ နည်းနည်းမကောင်းဘူး။","Houq-keh, né-né ma-kaun-bu.","Yeah, a little unwell."],
  ["K","ကျွန်တော် ဆေးရုံခေါ်သွားပေးမယ်။","Ca-na-w hsé-youn k'aw-thwa-pé-meh.","I'll take you to the hospital."],
  ["Y","ကျေးဇူးတင်ပါတယ်။","Cé-zú-tin-ba-deh.","Thank you."],
  ["S","စိတ်မပူပါနဲ့၊ ကျွန်မတို့ ရှိတယ်။","Seiq-ma-pu-ba-néh, ca-ma-dó shi-deh.","Don't worry, we're here."],
  ["K","ကားပေါ်တက်ပါ။","Ka-paw teq-pa.","Get in the car."],
  ["Y","ဟုတ်ကဲ့၊ ကျေးဇူးအများကြီး။","Houq-keh, cé-zú a-mya-cí.","Okay, thank you so much."]
], narration=["A short scare — a headache turns out to be nothing serious, but it's the moment you realize how far Ko Aung and Su are willing to go for a friend they've known less than a week."])

D(32, "dialogue", [
  ["Y","အနှောင့်အယှက်ဖြစ်စေလို့ တောင်းပန်ပါတယ်။","A-hnaung-a-sheq p'yiq-sé-lo taun-ban-ba-deh.","I'm sorry for the trouble I caused."],
  ["S","ကိစ္စမရှိပါဘူး။","Kiq-sa ma-shi-ba-bú.","No problem at all."],
  ["K","သူငယ်ချင်းအချင်းချင်း ဒါလောက်တော့ လုပ်ရမှာပေါ့။","Thu-ngeh-jin a-chin-jin da-lauq-daw louq-ya-hma-paw.","That's what friends do."],
  ["Y","ကျွန်တော်တမင်မဟုတ်ပါဘူး။","Ca-na-w ta-min ma-houq-pa-bú.","It wasn't on purpose, of course."],
  ["S","သိပါတယ်၊ စိတ်မညစ်ပါနဲ့။","Thi-ba-deh, seiq-ma-nyiq-pa-néh.","We know, don't worry about it."],
  ["K","အခု ပိုကောင်းလားဗျ။","A-k'u po-kaun-la-bya.","Feeling better now?"],
  ["Y","ဟုတ်ကဲ့၊ သိပ်ကောင်းသွားပါပြီ။","Houq-keh, théiq kaun-thwa-ba-bi.","Yes, much better now."]
])

D(33, "dialogue", [
  ["Y","သွားတော့မယ်နော်။","Thwa-daw-meh-naw.","I'm heading off now."],
  ["S","ပြန်တွေ့ကြမယ်။","Pyan-twé-ca-meh.","See you again."],
  ["K","တစ်ခါလာရင် ငါ့ဆီဆက်ခေါ်ပါ။","Ta-k'a la-yin ngat-si seq-k'aw-pa.","Whenever you come again, call me up."],
  ["Y","ကျေးဇူးအများကြီး၊ နှစ်ယောက်လုံး။","Cé-zú a-mya-cí, hna-yauq-loun.","Thank you so much, both of you."],
  ["S","မြန်မာစာ တော်တော်တိုးတက်သွားပြီနော်။","Myan-ma-sa taw-taw to-teq-thwa-bi-naw.","Your Burmese has really improved, hasn't it."],
  ["K","ပထမနေ့ကနေ အခုထိ ကြည့်ပါ။","Pa-t'a-ma-né-ga-né a-k'u-t'i cí-ba.","Look how far you've come since day one."],
  ["Y","ကျေးဇူးတင်ပါတယ်၊ နှစ်ယောက်လုံးကြောင့်ပါ။","Cé-zú-tin-ba-deh, hna-yauq-loun-caun-ba.","Thank you — it's thanks to both of you."],
  ["S","သွားလာပါဦးမယ်။","Thwa-la-ba-oun-meh.","Take care — I'll be on my way too."],
  ["K","ကျန်းမာပါစေ။","Kyan-ma-ba-zé.","Stay well."]
], narration=["A month ago you landed in Yangon knowing four words. Today you're saying goodbye to two friends, in their language, without translating a single sentence in your head first."])

# ---------------- apply ----------------

with open("data/book1-units.json", encoding="utf-8") as f:
    units = json.load(f)

for u in units:
    n = u["n"]
    if n in DIALOGUES:
        u["main"] = DIALOGUES[n]

with open("data/book1-units.json", "w", encoding="utf-8") as f:
    json.dump(units, f, ensure_ascii=False, indent=1)

print("Replaced main dialogue for", len(DIALOGUES), "of", len(units), "units")
