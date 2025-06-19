from aiogram import F,Router,types,Bot
from aiogram.filters import Command
from aiogram.types import LoginUrl
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile
from aiogram.enums import ParseMode



router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Пауэрлифтинг 🏋️‍♂️",callback_data="powerlifting")
    builder.button(text="Бодибилдинг 🦾",callback_data="bodybuilding")
    builder.button(text="Авторы 📖",callback_data="author")
    builder.button(text="Жимовые раскладки 📕", callback_data="bench_press")
    builder.button(text="Гайды 📚",callback_data="gaids")
    builder.adjust(2,1)
    await message.answer(f"Привет! {message.from_user.first_name} Я тренировочный бот,\tБот в котором вы можете получить тренировку для себя и не платить ни копейки! 🚀",reply_markup=builder.as_markup())
    

def powerlifting_menu():
    builder1 = InlineKeyboardBuilder()
    builder1.button(text="Высокий", callback_data="highlevel")
    builder1.button(text="Лёгкий",callback_data="lowlevel")
    builder1.button(text="Назад ◀️", callback_data="back_to_main")
    builder1.adjust(2)
    return builder1.as_markup()

def Genderbodybuilding_menu():
    builder1 = InlineKeyboardBuilder()
    builder1.button(text="Мужчина 🤵‍♂️", callback_data="manlevel")
    builder1.button(text="Женщина 👩‍🦰",callback_data="womanlevel")
    builder1.button(text="Назад ◀️", callback_data="back_to_main")
    builder1.adjust(2)
    return builder1.as_markup()

def bodybuilding_menu():
        builder1 = InlineKeyboardBuilder()
        builder1.button(text="Больше 3-4 лет", callback_data="highlevelbody")
        builder1.button(text="Меньше трёх лет",callback_data="lowlevelbody")
        builder1.button(text="Назад ◀️", callback_data="back_to_main")
        builder1.adjust(2)
        return builder1.as_markup()

def womanbodybuilding_menu():
    builder1 = InlineKeyboardBuilder()
    builder1.button(text="Больше 3-4 лет", callback_data="womanhighlevelbody")
    builder1.button(text="Меньше трёх лет",callback_data="womanlowlevelbody")
    builder1.button(text="Назад ◀️", callback_data="back_to_main")
    builder1.adjust(2)
    return builder1.as_markup()


def author_menu():
    buildermenu = InlineKeyboardBuilder()
    buildermenu.button(text="Telegram", url="https://t.me/ne1romediator")
    buildermenu.button(text="VK", url="https://vk.com/is_ma5")
    buildermenu.button(text="Назад ◀️", callback_data="back_to_main")
    buildermenu.adjust(3)
    return buildermenu.as_markup()

def gaids():
    buildergaids = InlineKeyboardBuilder()
    buildergaids.button(text="📕 Гайд - набор мышечной массы",url="https://telegra.ph/Rekompoziciya-sushka-12-09")
    buildergaids.button(text="📗 Гайд - профицит, дефицит каллорий(набор, сушка)",url="https://telegra.ph/Hh-06-01-10")
    buildergaids.button(text="📘 Гайд - увеличение силовых показателей",url="https://telegra.ph/Progress---ehto-ne-skuchno-s-07-09")
    buildergaids.button(text="📙 Гайд - как уберечься от травм",url="https://telegra.ph/Testovyj-dokument-07-09")
    buildergaids.adjust(1)
    return buildergaids.as_markup()

@router.callback_query(F.data=="highlevel")
async def highlevelgeneral(callback:types.CallbackQuery):
    document = FSInputFile("Линейный цикл для продвинутых.xlsx")
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    await callback.message.answer_document(document,caption="Уровень Высокий 🔴 - Пауэрлифтинг",reply_markup=builder3.as_markup())
    try:
        await callback.message.delete()
    except:
        pass

@router.callback_query(F.data=="lowlevel")
async def highlevelgeneral(callback:types.CallbackQuery):
    document = FSInputFile("Цикл начального уровня.xlsx")
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    await callback.message.answer_document(document,caption="Уровень Низкий 🟢 - Пауэрлифтинг",reply_markup=builder3.as_markup())
    try:
        await callback.message.delete()
    except:
        pass

@router.callback_query(F.data=="manlevel")
async def manlevel(callback:types.CallbackQuery):
    await callback.message.edit_text(
        "Выберите уровень стажа:",
        reply_markup=bodybuilding_menu()
    )
    await callback.answer()

@router.callback_query(F.data=="womanlevel")
async def manlevel(callback:types.CallbackQuery):
    await callback.message.edit_text(
        "Выберите уровень стажа:",
        reply_markup=womanbodybuilding_menu()
    )
    await callback.answer()


@router.callback_query(F.data == "powerlifting")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(
        
        "⚠️ Обращаем внимание - программы начального и среднего уровней подходят и мужчинам и женщинам,\n" \
        " так же внутри файла каждой программы есть инструкция с уточнениями или ответами на возможно возникшие вопросы.\n" \
        "\nВыберите уровень стажа:",
        reply_markup=powerlifting_menu()
    )
    try:
        await callback.message.delete()
    except:
        pass
    await callback.answer()

@router.callback_query(F.data == "bodybuilding")
async def send_random_value(callback: types.CallbackQuery):
    hidden_link = 'https://telegra.ph/Instrukciya-k-programmam-bb-11-01'
    answerquestion = ("<b>🦾Бодибилдинг</b> перед выбором пола, ознакомься со <a href='{}'>статьей</a>\t").format(hidden_link)
    await callback.message.answer(
        answerquestion,reply_markup=Genderbodybuilding_menu(),parse_mode="HTML")
    try:
        await callback.message.delete()
    except:
        pass
    await callback.answer()


@router.callback_query(F.data == "back_to_main")
async def backtomain(callback:types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="Пауэрлифтинг 🏋️‍♂️", callback_data="powerlifting")
    builder.button(text="Бодибилдинг 🦾",callback_data="bodybuilding")
    builder.button(text="Авторы 📖",callback_data="author")
    builder.button(text="Жимовые раскладки 📕", callback_data="bench_press")
    builder.button(text="Гайды 📚",callback_data="gaids")
    builder.adjust(2,1)
    await callback.message.answer(
            f"Привет! Я тренировочный бот на aiogram 3.x!. Бот в котором вы можете получить тренировку для себя и не платить ни копейки! 🚀",
            reply_markup=builder.as_markup()
        )
    try:
        await callback.message.delete()
    except:
        pass
    
    await callback.answer()

@router.callback_query(F.data == "gaids")
async def gaids12(callback:types.CallbackQuery):
    gaidsimage = FSInputFile("zias-bench.gif")
    await callback.message.answer_photo(gaidsimage,caption="В данном разделе вы можете найти гайды по питанию/тренировкам и другие.",reply_markup=gaids())


@router.callback_query(F.data == "author")
async def author(callback:types.CallbackQuery):
    photoimage = FSInputFile("photoimageismail.jpg")
    await callback.message.answer_photo(photoimage,caption="<strong>Исмаил Мендгалиев</strong> - FullStack-Developer\n" \
    "\n✍️<b>Ниже представлены Соц-сети</b> автора данного телеграм бота, с которыми вы "
    "можете ознакомиться",parse_mode="HTML",reply_markup=author_menu())
    try:
        await callback.message.delete()
    except:
        pass
    await callback.answer()
        

@router.callback_query(F.data == "highlevelbody")
async def highlevelbody(callback:types.CallbackQuery):
    document = FSInputFile("Муж высокий 3дневный.xlsx")
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    await callback.message.answer_document(document,caption="Уровень Высокий 🔴 - Бодибилдинг",reply_markup=builder3.as_markup())
    try:
        await callback.message.delete()
    except:
        pass

@router.callback_query(F.data == "lowlevelbody")
async def highlevelbody(callback:types.CallbackQuery):
    document = FSInputFile("Мужской начальный 3х дневный.xlsx")
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    await callback.message.answer_document(document,caption="Уровень Низкий 🟢 - Бодибилдинг",reply_markup=builder3.as_markup())
    try:
        await callback.message.delete()
    except:
        pass

@router.callback_query(F.data == "womanhighlevelbody")
async def highlevelbody(callback:types.CallbackQuery):
    document = FSInputFile("Жен средний 3дневный.xlsx")
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    await callback.message.answer_document(document,caption="Уровень Высокий 🔴 - Бодибилдинг",reply_markup=builder3.as_markup())
    try:
        await callback.message.delete()
    except:
        pass

@router.callback_query(F.data == "womanlowlevelbody")
async def highlevelbody(callback:types.CallbackQuery):
    document = FSInputFile("Жен начальный 3дневный.xlsx")
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    await callback.message.answer_document(document,caption="Уровень Низкий 🟢 - Бодибилдинг",reply_markup=builder3.as_markup())
    try:
        await callback.message.delete()
    except:
        pass




@router.callback_query(F.data == "bench_press")
async def bench(callback:types.CallbackQuery):
    docx = FSInputFile("bench_presses_article.docx")
    builder32 = InlineKeyboardBuilder()
    builder32.button(text="Назад",callback_data="back_to_main")
    await callback.message.answer_document(document=docx,reply_markup=builder32.as_markup())
    try:
        await callback.message.delete()
    except:
        pass


@router.message()
async def echo(message: types.Message):
    await message.answer("Ты чё написал,чепуха?!")