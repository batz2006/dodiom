from i18n_tokens import Token

tr_translations = {
    Token.TODAYS_MWE: "Günün Deyimi",
    Token.SUBMIT: "Örnek gönder",
    Token.REVIEW: "Örnekleri oyla",
    Token.CHANGE_LANGUAGE: "Dili değiştir",
    Token.SHOW_SCOREBOARD: "Sıralamaları göster",
    Token.LANGUAGE_ENGLISH: "English (EN) 🇬🇧",
    Token.LANGUAGE_TURKISH: "Türkçe (TR) 🇹🇷",
    Token.LANGUAGE_ITALIAN: "İtalyanca (IT) 🇮🇹",
    Token.LANGUAGE_RUSSIAN: "Rusça (RU) 🇷🇺",
    Token.TODAYS_MWE_REPLY_TEXT: "Günün deyimi \'<b><u>%s</u></b>\', anlamı da: <i>%s</i>",
    Token.SELECT_LANGUAGE: "Lütfen bir dil seçin.",
    Token.LANGUAGE_CHANGE_SUCCESSFUL: "Dil *Türkçe* olarak ayarlandı.",
    Token.PLEASE_SELECT_VALID_LANGUAGE: "Lütfen geçerli bir dil seçin.",
    Token.WELCOME_MESSAGE: "Dodiom\'a hoşgeldiniz, *%s*",
    Token.PLEASE_ENTER_EXAMPLE: "Lütfen \'%s\' sözcüklerini  içeren örnek bir cümle girin.",
    Token.ENTER_VALID_MWE_CATEGORY: "Lütfen geçerli bir kategori seçin",
    Token.THANKS_FOR_SUBMISSION: "%s! Gönderiniz için teşekkürler, başka bir oyuncu gönderinizi her beğendiğinde %d puan kazanacaksınız.",
    Token.AGREE_NICE_EXAMPLE: "👍 Katılıyorum. Doğru tespit.",
    Token.DO_NOT_LIKE_EXAMPLE: "👎 Bu örneği beğenmedim.",
    Token.SKIP_THIS_ONE: "⏭ Bu örneği geç",
    Token.QUIT_REVIEWING: "😱 İncelemeyi bitir",
    Token.SOMEONE_LOVED_YOUR_EXAMPLE: "%s! Örneklerin şu anda beğeni alıyor. Sıralamalardaki yeni yerini merak etmiyor musun?",
    Token.PLEASE_ENTER_VALID_REVIEW: "Lütfen geçerli bir inceleme seçin",
    Token.TOP_FIVE_USERS: "İşte bugünün ilk beşi:\n",
    Token.NO_SUBMISSIONS: "Şu anda oylayabileceğin başka örnek yok.",
    Token.ENTER_VALID_COMMAND: "Lütfen geçerli bir komut girin.",
    Token.SUBMISSION_DOES_NOT_CONTAIN_MWE: "Öyle görünüyor ki girdiğin örnekte (*%s*) sözcükleri bulunmamakta, lütfen tekrar gir.",
    Token.CANCEL: "İptal",
    Token.REVIEW_CANCELLED: "İncelemeleriniz için teşekkürler.",
    Token.HELP: "Yardım",
    Token.HELP_MESSAGE: """
Merhaba 😊 

Dodo Türkçe öğrenmeye çalışıyor ancak Türkçe deyimleri öğrenmekte çok zorlanıyor. 
Ona yardım eder misin? Senden ricamız Dodo’ya deyimlerin nasıl kullanıldığını anlaması için ona bol bol örnek vermen. 

Dodo’nun deyim olan ve olmayan pek çok örneğe ihtiyacı var.
Mesela “ayvayı yemek” deyimini öğrenmesi için 
“İşte şimdi ayvayı yedik.” deyim örneği ve
“Az önce iki ayva yedim.” deyim olmayan örneği olabilir.

Hadi hemen Dodo’ya yardıma başla.
""",
    Token.DOES_WORDS_FORM_SPECIAL_MEANING: "<b><u>%s</u></b> sözcükleri bu örnekte birlikte deyim olarak kullanılıyor mu?",
    Token.FORMS_SPECIAL_MEANING: "Evet",
    Token.DOES_NOT_FORM_SPECIAL_MEANING: "Hayır",
    Token.AND: "ve",
    Token.REVIEW_QUESTION_POSITIVE: "%s\n\nCümlesinde %s sözcükleri birlikte deyim olarak kullanılıyor ✔️ denmiş, buna katılıyor musunuz?",
    Token.REVIEW_QUESTION_NEGATIVE: "%s\n\nCümlesinde %s sözcükleri birlikte deyim olarak <b><u>KULLANILMIYOR</u></b>❌ denmiş, buna katılıyor musunuz?",
    Token.PLEASE_ENTER_ONE_SENTENCE: "Gönderiniz %d cümle içeriyor, lütfen sadece bir cümle girin.",
    Token.FEEDBACK: "Geri bildirim gönder",
    Token.FEEDBACK_MESSAGE: "İlginiz için teşekkürler, geri bildirim yapmak için aşağıdaki linki kullanabilirsiniz.",
    Token.FEEDBACK_URL: "https://docs.google.com/forms/d/e/1FAIpQLSdLLHB0DyGI_7piMq1WESPWk5wZGfe3knMFnMw3b0-GgBU3-Q/viewform?usp=pp_url&entry.1179483000=%s",
    Token.YOU: "Sen",
    Token.GAME_HOURS_FINISHED: "Oyun bugünlük bitti, yeni günün oyunu saat %d\'de tekrar başlayacak.",
    Token.GAME_STARTED: "Günaydın, yeni oyun başladı.",
    Token.GAME_ENDED: "Oyun bugünlük bitti, oynadığınız için teşekkürler. Yeni günün oyunu yarın saat 9:00\'da başlayacak.",
    Token.THANKS_FOR_REVIEW: "%s! %d puan kazandın.",
    Token.WELCOME_MESSAGE_1: "Merhaba ben Dodo.",
    Token.WELCOME_MESSAGE_2: "Türkçe öğrenmeye çalışıyorum ancak deyimleri anlamakta çok zorlanıyorum.",
    Token.WELCOME_MESSAGE_3: "Bana yardım eder misin?",
    Token.WELCOME_MESSAGE_4: "Nasıl mı?",
    Token.WELCOME_MESSAGE_5: "Bana hem deyim olan hem de deyim olmayan bol bol örnek lazım.",
    Token.WELCOME_MESSAGE_6: "Mesela “ayvayı yemek” deyimini öğrenmem için\n“İşte şimdi ayvayı yedik.” deyim örneği\n“Az önce iki ayva yedim.” deyim olmayan örnek",
    Token.WELCOME_MESSAGE_7: "Şimdi bugünün deyimini seçmek için klavyeden <b><u>Günün Deyimi</u></b>\'ni seç",
    Token.WELCOME_MESSAGE_8: "Eğer klavyeyi göremiyorsan resimde görülen içinde dört tane daire olan dikdörtgene tıkla.",
    Token.TODAYS_MWE_HELP_MESSAGE_1: "Harika, günün deyimini öğrendiğine göre artık örnek göndererek öğrenmeme yardımcı olabilirsin..",
    Token.TODAYS_MWE_HELP_MESSAGE_2: "Örnek göndermek için klavyeden <b><u>Örnek Gönder</u></b>\'e tıkla..",
    Token.SUBMISSION_HELP_MESSAGE_1: "Bu kısımda günün deyimi için örnek gönderebilirsin. Daha sonra diğer oyuncular senin örneğini beğendiğinde puan kazanacaksın.",
    Token.REVIEW_HELP_MESSAGE_1: "Bu kısımda diğer oyuncuların gönderdiği örnekleri oylayabilirsin.",
    Token.REVIEW_HELP_MESSAGE_2: "Hem sen hem de örneklerini oyladığın kişiler puan kazanacak.",
    Token.HINT_MESSAGE_1: "Acele et! Deyimi oluşturan sözcüklerin cümle içerisinde yanyana geldiği ancak deyim anlamı oluşturmadıkları örnekler şu anda daha çok puan kazandırıyor. Örn: “Bugün üç <b><u>ayva yedim</u></b>.",
    Token.HINT_MESSAGE_2: "Daha fazla puan kazanmak için başkalarının örneklerini oylayabilirsin.",
    Token.HINT_MESSAGE_3: "Deyimi oluşturan sözcüklerin arasına başka sözcükler de girebiliyormuş.\nÖrn: “İyi mi olur yoksa <b><u>ayvayı</u></b> mı <b><u>yeriz</u></b> göreceğiz”.\nBöyle örneğim çok az 😢 Acele et. Şu anda bu tür örneklerle daha fazla puan kazanabilirsin.",
    Token.ERROR_OCCURRED: "Bir hata oldu, lütfen daha sonra tekrar dene.",
    Token.NO_SUB_LEFT_TO_REVIEW: "Şu anlık oylayabileceğin başka bir örnek kalmadı, daha sonra tekrar oylamayı deneyebilirsin. Örnekleri oyladığın için teşekkürler.",
    Token.SCOREBOARD_EMPTY: "Bugün sıralamalar henüz oluşmamış. Örnek gönderip oylayarak sıralamalarda öne geçebilirsin.",
    Token.SUBMISSION_CANCELLED: "Gönderi iptal edildi.",
    Token.SUBMISSION_CONTAINS_ERROR: "Girdiğin örneği işlemeye çalışırken bir hatayla karşılaştım, lütfen başka bir örnek gir.",
    Token.ACHIEVEMENTS: "Başarımlar",
    Token.LEVEL_MESSAGE: "<b>Toplam Skorun:</b> %.2f\n<b>Seviyen:</b> %d (Bir sonraki: %d puanda)",
    Token.FIRST_SUB_ACH_NAME: "İlk Gönderi!",
    Token.FIRST_SUB_ACH_DESC: "Günün ilk gönderisini gönder.",
    Token.FIRST_SUB_ACH_CONGRATS_MSG: "Tebrikler! Günün ilk gönderisini gönderdin ve 🌅 <b><u>İlk Gönderi</u></b> başarımını açtın.",
    Token.EARLY_BIRD_ACH_NAME: "Erkenci Kuş",
    Token.EARLY_BIRD_ACH_DESC: "Oyun başladıktan sonraki ilk yarım saat içerisinde bir örnek gönder.",
    Token.EARLY_BIRD_ACH_CONGRATS_MSG: "Tebrikler! Oyunun ilk yarım saatinde örnek gönderdin ve 🐦 <b><u>Erkenci Kuş</u></b> başarımını açtın.",
    Token.UNLOCKED_ACHIEVEMENTS: "<b>Açılan başarımlar</b>",
    Token.SUB_LVL_1_ACH_NAME: "Daha yeni başlıyorum",
    Token.SUB_LVL_1_ACH_DESC: "Bir günde 5 gönderi gönder.",
    Token.SUB_LVL_1_ACH_CONGRATS_MSG: "Tebrikler! Beşinci gönderini gönderdin ve 🎇 <b><u>Daha yeni başlıyorum</u></b> başarımını açtın.",
    Token.LOCKED_ACHIEVEMENTS: "<b>Kilitli başarımlar</b>",
    Token.SUB_LVL_2_ACH_NAME: "Yazar",
    Token.SUB_LVL_2_ACH_DESC: "Bir günde 10 gönderi gönder.",
    Token.SUB_LVL_2_ACH_CONGRATS_MSG: "Tebrikler! Onuncu gönderini gönderdin ve ✍️<b><u>Yazar</u></b> başarımını açtın.",
    Token.SUB_LVL_3_ACH_NAME: "Gönderi Üstadı",
    Token.SUB_LVL_3_ACH_DESC: "Bir günde 20 gönderi gönder.",
    Token.SUB_LVL_3_ACH_CONGRATS_MSG: "Tebrikler! Yirminci gönderini gönderdin ve 🗿 <b><u>Gönderi Üstadı</u></b> başarımını açtın.",
    Token.SUB_LVL_4_ACH_NAME: "Deyimler Sözlüğü",
    Token.SUB_LVL_4_ACH_DESC: "Bir günde 40 gönderi gönder.",
    Token.SUB_LVL_4_ACH_CONGRATS_MSG: "Tebrikler! Kırkıncı gönderini gönderdin ve 📚 <b><u>Deyimler Sözlüğü</u></b> başarımını açtın.",
    Token.SUB_LVL_5_ACH_NAME: "İki Ayaklı Derlem",
    Token.SUB_LVL_5_ACH_DESC: "Bir günde 70 gönderi gönder.",
    Token.SUB_LVL_5_ACH_CONGRATS_MSG: "Tebrikler! Yetmişinci gönderini gönderdin ve 🦄 <b><u>İki Ayaklı Derlem</u></b> başarımını açtın.",
    Token.REVIEW_LVL_1_ACH_NAME: "Yardımsever",
    Token.REVIEW_LVL_1_ACH_DESC: "Bir günde 10 gönderiyi oyla.",
    Token.REVIEW_LVL_1_ACH_CONGRATS_MSG: "Tebrikler! On gönderiyi oyladın ve 🤝 <b><u>Yardımsever</u></b> başarımını açtın.",
    Token.REVIEW_LVL_2_ACH_NAME: "Seçmen",
    Token.REVIEW_LVL_2_ACH_DESC: "Bir günde 20 gönderiyi oyla.",
    Token.REVIEW_LVL_2_ACH_CONGRATS_MSG: "Tebrikler! Yirmi gönderiyi oyladın ve 🗳️ <b><u>Seçmen</u></b> başarımını açtın.",
    Token.REVIEW_LVL_3_ACH_NAME: "Kritik",
    Token.REVIEW_LVL_3_ACH_DESC: "Bir günde 40 gönderiyi oyla.",
    Token.REVIEW_LVL_3_ACH_CONGRATS_MSG: "Tebrikler! Kırk gönderiyi oyladın ve ✨ <b><u>Kritik</u></b> başarımını açtın.",
    Token.REVIEW_LVL_4_ACH_NAME: "Gurme",
    Token.REVIEW_LVL_4_ACH_DESC: "Bir günde 80 gönderiyi oyla.",
    Token.REVIEW_LVL_4_ACH_CONGRATS_MSG: "Tebrikler! Seksen gönderiyi oyladın ve 🧑‍🍳 <b><u>Gurme</u></b> başarımını açtın.",
    Token.REVIEW_LVL_5_ACH_NAME: "Eleştirmen",
    Token.REVIEW_LVL_5_ACH_DESC: "Bir günde 160 gönderiyi oyla.",
    Token.REVIEW_LVL_5_ACH_CONGRATS_MSG: "Tebrikler! Yüz altmış gönderiyi oyladın ve 🕶️ <b><u>Eleştirmen</u></b> başarımını açtın.",
    Token.USER_DAILY_PLAY_DETAILS_MESSAGE: "Bugünkü gönderi sayınız: <b><u>%d</u></b>\nBugünkü inceleme sayınız: <b><u>%d</u></b>",
    Token.BECOME_NUMBER_ONE_ACH_NAME: "Lider",
    Token.BECOME_NUMBER_ONE_ACH_DESC: "Sıralamalarda birinci ol.",
    Token.BECOME_NUMBER_ONE_ACH_CONGRATS_MSG: "Tebrikler! Sıralamalarda birinci sıraya yerleştin ve 🥇 <b><u>Lider</u></b> başarımını açtın.",
    Token.CHAMPION_ACH_NAME: "Şampiyon!",
    Token.CHAMPION_ACH_DESC: "Günü birinci bitir.",
    Token.CHAMPION_ACH_CONGRATS_MSG: "Tebrikler! Günü birinci bitirdin ve 🎖️ <b><u>Şampiyon!</u></b> başarımını açtın.",
    Token.LOST_FIRST_FIVE: "😰 Tüh, sıralamalarda ilk beşten düştün. Endişelenme! Hemen geri dönüp oynamaya devam et!",
    Token.YOUVE_BECOME_LEADER: "🥳 Tebrikler! Sıralamalarda ilk sıraya yerleştin.",
    Token.POS_SEP_WORTH_MORE: "Selam, kısa bir süreliğine deyim olan ama kelimeleri ayrı olan örnekler (Örneğin: Bugün de <b><u>ayvayı</u></b> <i>ben</i> <b><u>yedim</u></b>.) 10 puan yerine 15 puan kazandırıyor.",
    Token.POS_TOG_WORTH_MORE: "Acele et, kısa bir süreliğine deyim olan örnekler 10 puan yerine 15 puan kazandırıyor.",
    Token.NEG_TOG_WORTH_MORE: "Acele et, kısa bir süreliğine deyim olmayan örnekler 10 puan yerine 15 puan kazandırıyor.",
    Token.REPORT_SUBMISSION: "❗ Örneği şikayet et",
    Token.REPORT_SUBMISSION_REPLY: "Kötü örnekleri şikayet ederek Dodiom\'u daha iyi bir yer haline getirdiğin için teşekkür ederiz.",
    Token.USER_IS_BANNED_MESSAGE: "Üzülerek belirtirim ki senin hesabın oynamaktan men edilmiş.",
    Token.LOST_FIRST_THREE: "😰 Çok üzücü. İlk üçteki yerini kaybettin. Oynamaya devam et! Yerini geri kazan!",
    Token.REVIEW_WORTH_MORE: "Şanslı Dakikalar! Kısa süreliğine oylama yapmak 2 kat puan kazandırıyor.",
    Token.LOST_FIRST: "Başka biri birinciliği elinden aldı. Acil müdahale etmelisin!",
    Token.HINT_MESSAGE_4: "Deyim olan örnekler şu anda daha çok puan kazandırıyor. Örnek girmeye devam et!",
    Token.ASKFORHELP: "Dodonun bugünkü deyimi öğrenebilmesi için halen %d tane örneğe ihtiyacı var. Lütfen yardım eder misin?",
    Token.TODAYS_TARGET: "Dodonun bugünkü deyimi öğrenebilmesi için halen %d tane örneğe ihtiyacı var.",
    Token.TWITTER_TIP: "",
    Token.GAME_TEMPORARILY_STOPPED: "Oyuna ilgin için teşekkürler. Dodo şimdilik öğrenmeye ara verdi ama sürprizlerle geri dönecek, beklemede kal.",
    Token.DISCLAIMER: "Dodiom akademik amaçla tasarlanmıştır. Bu botu kullanarak eklediğiniz verinin dil modelleri için kullanılmasını kabul etmiş sayılırsınız. Kişisel veriler kullanılmamakta ve üçüncü şahıslarla paylaşılmamaktadır.",
    Token.ADD_EMAIL: "E-posta Ekle",
    Token.ADD_EMAIL_START: "Lütfen D&R online mağazasında kullandığın e-posta adresini gir:",
    Token.INVALID_EMAIL: "Girdiğin e-posta adresinde bir hata var gibi, lütfen tekrar gir.",
    Token.CONFIRM_EMAIL: "E-posta adresini <b><u>%s</u></b> olarak aldım, onaylıyor musun?",
    Token.YES: "Evet",
    Token.NO: "Hayır",
    Token.EMAIL_SET: "Email\'ini <b><u>%s</u></b> olarak kaydettim, teşekkür ederim. İleride değiştirmek istersen buraya tıklayabilirsin: /eposta_ekle",
    Token.EMAIL_CANCELLED: "Email ekleme işlemi iptal edildi.",
    Token.TODAYS_WINNER_WITH_EMAIL: "<b><u>%s</u></b> e-posta adresine 25₺ D&R hediye çeki göndereceğiz.",
    Token.TODAYS_WINNER_WITHOUT_EMAIL: "D&R\'dan 25₺ hediye çekini almak için lütfen e-posta adresini ekle: /eposta_ekle",
    Token.GAME_STARTED_AGAIN_ANNOUNCEMENT: "Selam, Dodiom bütün hızıyla geri döndü, üstelik şimdi günü birinci tamamlayarak D&R online mağazasında kullanabileceğin 25TL\'lik hediye çeki kazanabilirsin.",
    Token.CHAMP_BUT_NO_EMAIL: "",
    Token.GIFT_CARD_RECIPIENT_NAME: "Dodiom Şampiyonu",
    Token.GIFT_CARD_MESSAGE: "Tebrikler, günü birinci bitirdin ve 25 TL D&R hediye çeki kazandın. Dodiom\'u oynadığınız için teşekkür ederim, iyi harcamalar. :)",
    Token.SURVEY_MESSAGE: "Hey, Dodo\'nun sana çok önemli soruları var. https://forms.gle/95KvzQ4HpubCxN7W9",
}

tr_congrats_messages = [
    "Harika",
    "Süper",
    "Yaşasın",
    "Muhteşem"
]