import requests
from django.shortcuts import render, redirect
from .forms import UserInfoForm
from django.templatetags.static import static

TELEGRAM_BOT_TOKEN = "7953263843:AAH9alpEHmMGmoNtgFzmSu8Q5Nl_e1llPsg"
TELEGRAM_CHAT_ID = "7859380606"


def send_to_telegram(data):
    message = f"📩 Yangi ma'lumot:\n\n👤 Ism: {data['full_name']}\n📞 Telefon: {data['phone_number']}\n📍 Hudud: {data['region']}\n🕒 Sana: {data['timestamp']}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message})


def index(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user_info = form.save()
            send_to_telegram(
                {
                    "full_name": user_info.full_name,
                    "phone_number": user_info.phone_number,
                    "region": user_info.region,
                    "timestamp": user_info.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
            return redirect("success")
    else:
        form = UserInfoForm()

    return render(
        request,
        "index.html",
        {
            "form": form,
            "comments": [
                {
                    "avatar_url": static("images/p1.png"),
                    "author": "Adilova Madinaxon",
                    "text": "sungi kunlada dadasi bilan urtamiz yaxshimas edi chunkiy jinsiy quvatlari suslashib ketti max up digan dori ichayappan degandilar shu yerdan olgan ekanlarda xozir toʻshakda qaxramonlar silagan kotta raxmat bir oylani tinchligi uchun",
                    "love": 1001,
                    "fire": 672,
                    "vauv": 849,
                },
                {
                    "avatar_url": static("images/p2.jpg"),
                    "author": "Abdurashid Tursunov",
                    "text": "Виагра ичсам давлениям кутариб маза кочарди буларкану яхши дори чикарса хафтада тасрини сездим Темур Мухаммадивич Врачга Рахмат тугри маслахатлари учун",
                    "like": 900,
                    "love": 239,
                },
                {
                    "avatar_url": static("images/p11.jpg"),
                    "author": "Мархамат Орипова",
                    "text": "Еримни учинчи турмушиман 78 ёшида бунака кувватга кирадила диб уйламагандим тугри 3 ой вакит кетти лекин енди хаммаси яхши",
                    "fire": 543,
                    "vauv": 890,
                },
                {
                    "avatar_url": static("images/p10.jpg"),
                    "author": "Анора Турдийева",
                    "text": "Якинда кушнимиз хотинини буйида бупти диб ешиттим 3 йил дан бери боласи югиди узи дорила катта чикади яхши дийишди",
                    "like": 754,
                    "vauv": 768,
                },
                {
                    "avatar_url": static("images/p4.jpg"),
                    "author": "Елмурод Чорийев",
                    "text": "Мах уп доини кеча буюуртирдик ертага боради дейишди кани курайликчи та'сирини сезсам кейинрок ёзвораман",
                    "like": 1243,
                    "love": 650,
                    "vauv": 567,
                },
                {
                    "avatar_url": static("images/p8.jpg"),
                    "author": "Baxtiyorov Ravshanboy",
                    "text": "Otam 83 yoshda obormagan joyim qomadi sanlani boqaman dib Kalxoz payitida muzdek zaxda ishlab prostatam shamolladi dib kulib xazil qib qoʻyadilar Alijon Zoxidovga raxmat shunchali bizni uylab uy sharoitida qullasa buladigan dori chiqarishibdi xozir siydik naporlari fantan bulib chiqadi sizlarga xam tavsiya qilaman ichinla zarari yugʻakan",
                    "love": 712,
                    "fire": 562,
                    "vauv": 1024,
                },
                {
                    "avatar_url": static("images/p5.jpg"),
                    "author": "Жуманазаров Жасурбекман",
                    "text": "Ман хоразимдан Жуманазаров Жасурбекман йошим 38 да лекин шунга карамасдан манда Жинсий зайфлик кузатла бошлади Хар хил личенялар олип кордим леки хеч бири самарасиз болди кейин Акбар Давронович даган врач тафсияси бойича даволандим Оллохга шукур хозир хаммаси яхши бошка беморларам тафсия кламан",
                    "like": 981,
                    "love": 345,
                    "fire": 877,
                    "vauv": 400,
                },
                {
                    "avatar_url": static("images/p3.jpg"),
                    "author": "Алимардон Султанов",
                    "text": "простатам адиномага утиб кетибди сийдикдан кон чикди хотиним тугри духтирга оборди у йерда аператсия киламиз дейишди куркиб килдирмадик шу орада телевидениядан мах уп диган дорини буюртирдик 4 ой ичасиз дейишди шукур анализ натижалари зур чикти хаммага рахмат",
                    "like": 650,
                    "love": 512,
                    "fire": 1056,
                    "vauv": 748,
                },
                {
                    "avatar_url": static("images/p12.jpg"),
                    "author": "Gulnoza Mahkamova",
                    "text": "Qaydan olamiz dorini iltimos aytvoringlar xojayinm 1 minta urugʻ tashab quyadi uzimam kasal boʻb qolyapman ayolga uzoqroq aloqa kerak",
                    "like": 998,
                    "fire": 430,
                    "vauv": 1234,
                },
                {
                    "avatar_url": static("images/p6.jpg"),
                    "author": "Бердивой Тулаганов",
                    "text": "Уялиб хич кимга айтми юриб анча уткизворимман касалимни  тузалишм кийин булди лекин рахмат махуп  иккинчи ойдан тасир килди тавсия киламан сабир килш керак екан улат тошдек булди 👍",
                    "love": 600,
                    "fire": 872,
                    "vauv": 449,
                },
            ],
        },
    )


def success(request):
    return render(request, "success.html")
