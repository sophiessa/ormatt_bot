class GeneralTexts():
    def text_start_admin(lang='ru', full_name=''):
        return {
            'ru': f'<b>Здравствуйте {full_name}, вы вошли как админ!</b>',
            'en': f'<b>Hello {full_name}, you joined as an admin!</b>',
            'kg': f'<b>Арыбаңыз {full_name}, админ болуп кирдиңиз!</b>',
        }[lang]
    
    def text_start_client(lang='ru', full_name=''):
        if full_name is None:
            full_name = ''
        return {
            'ru': f'<b>Здравствуйте {full_name}, этот бот поможет вам выбрать товар или связаться с консультантом. \nДля этого используйте кнопки ниже!</b>',
            'en': f'<b>Hello {full_name}, this bot can help you choose a product or contact the managers.\nPlease use the buttons below!</b>',
            'kg': f'<b>Арыбаңыз {full_name}, бул бот менен заказ берсеңиз же менеджер менен суйлөшсөңуз болот!</b>',
        }[lang]


class ClientTexts():
    def see_mattress_category(lang='ru'):
        return {
            'ru': f'<b>Выберите категорию \U0001F600</b>',
            'en': f'<b>Choose a category \U0001F600</b>',
            'kg': f'<b>Категория тандаңыз \U0001F600</b>',
        }[lang] 

    def see_mattress(product_name: str, product_description: str, product_price: float, product_discount: float, lang='ru'):
        return {
            'ru': f'<b>{product_name}</b>\nОписание: {product_description}\nЦена за м\U000000B2: <s>{product_price}</s> {float(product_price) * (100 - float(product_discount)) / 100} сом',
            'en': f'<b>{product_name}</b>\nDescription: {product_description}\nPrice for a м\U000000B2: <s>{product_price}</s> {float(product_price) * (100 - float(product_discount)) / 100} som',
            'kg': f'<b>{product_name}</b>\nСурөттөмө: {product_description}\nм\U000000B2 баасы: <s>{product_price}</s> {float(product_price) * (100 - float(product_discount)) / 100} сом',
        }[lang]   
    
    def see_accessory(product_name: str, product_description: str, product_price: float, product_discount: float, lang='ru'):
        return {
            'ru': f'<b>{product_name}</b>\nОписание: {product_description}\nЦена за м\U000000B2: <s>{product_price}</s> {float(product_price) * (100 - float(product_discount)) / 100} сом',
            'en': f'<b>{product_name}</b>\nDescription: {product_description}\nPrice for a м\U000000B2: <s>{product_price}</s> {float(product_price) * (100 - float(product_discount)) / 100} som',
            'kg': f'<b>{product_name}</b>\nСурөттөмө: {product_description}\nм\U000000B2 баасы: <s>{product_price}</s> {float(product_price) * (100 - float(product_discount)) / 100} сом',
        }[lang]
    
    def chosen_product(product_name: str, lang='ru'):
        return {
        'ru': f'Вы выбрали {product_name}, наши консультанты свяжутся с вами в ближайщее время!',
        'en': f'You chose {product_name}, our managers will contact you asap!',
        'kg': f'{product_name} тандадыңаз, жакын арада сиз менен байланышабыз!',
        }[lang]  

    def about_us(lang='ru'):
        return {
            'ru': f'Мы относительно недавно начинали практически не зная ничего про матрасы. Не знали практически ничего, и возможно поэтому были открыты для нового. Не знали места, где «клевала рыба», поэтому искали своё место под солнцем. И вот сейчас, спустя три года, мы начали привносить новое, небывалое для рынка Кыргызстана. Сегодня с уверенностью можем сказать, что являемся одной из самых современных и инновационных производителей.\n\U0001F600',
            'en': f'We relatively recently started almost without knowing anything about mattresses. We knew almost nothing, and perhaps that\'s why we were open to new things. We did not know the place where the “fish pecked”, so we were looking for our place under the sun. And now, three years later, we have begun to introduce something new, unprecedented for the Kyrgyz market. Today we can say with confidence that we are one of the most modern and innovative manufacturers.\n\U0001F600',
            'kg': f'Жакында эле матрацтар жөнүндө эч нерсе билбечик. Биз дээрлик эле эч нерсе билбегендиктен жаңы ачылыштарга ачык болчук. Биз күн астында өз ордун издедик. Эми үч жылдан кийин, биз Кыргызстан рыногуна болуп көрбөгөн жаңылыктарды алып келе баштадык. Бүгүн биз эң алдыңкы жана инновациялык өндүрүүчүлөрдүн бири экенибизди ишеним менен айта алабыз\n\U0001F600',
        }[lang]

    def social_media(lang='ru'):
        return {
            'ru': f'Ниже ссылки на наши социяльные сети',
            'en': f'The links to our social media are below',
            'kg': f'Биздин социалдык тармактарга шилтемелер'
        }[lang]
    
    def change_language(lang='ru'):
        return {
            'ru': 'Язык поменялся на Русский!',
            'en': 'The language is English now!',
            'kg': 'Кыргыз тилине которулду!',
        }[lang]

    def review_question_name(lang='ru'):
        return {
            'ru': 'Как вас зовут?',
            'en': 'What is your name?',
            'kg': 'Атыңыз ким?',
        }[lang]
    
    def review_question_review(lang='ru'):
        return {
            'ru': 'Напишите ваш отзыв',
            'en': 'Please write your review down',
            'kg': 'Ылдыйга өз оюунузду жазыңыз',
        }[lang]
    
    def review_end(lang='ru'):
        return {
            'ru': 'Спасибо за отзыв, мы обязательно учтём ваше мнение',
            'en': 'Thanks for the review, we will consider your opinion',
            'kg': 'Оюунуз учун рахмат, биз оюнузду карап чыгабыз',
        }[lang]
    
    def review_cancel(lang='ru'):
        return {
            'ru': 'Отзыв отменён',
            'en': 'The review in canceled',
            'kg': 'Оюнуз жокко чыкты',
        }[lang]

    def question_buyer_name(lang='ru'):
        return {
            'ru': 'Напишите ваше имя?',
            'en': 'What is your name?',
            'kg': 'Атыңыз ким?',
        }[lang]

    def question_buyer_phone_number(lang='ru'):
        return {
            'ru': 'Напишите номер телефона',
            'en': 'Send your phone number',
            'kg': 'Телефон номериңизди жазыңыз',
        }[lang]


    def cancel_buy(lang='ru'):
        return {
            'ru': 'Покупка отменена',
            'en': 'Purchase canceled',
            'kg': 'Жокко чыкты',
        }[lang]
    
    def receive_notifications(lang='ru'):
        return {
            'ru': 'Хотите получать иформацию про скидки?',
            'en': 'Do you want to be notified about discounts?',
            'kg': 'Арзандатуулар жөнүндө информация билип тургуңуз келеби?',
        }[lang]

    def receive_notification_yes_no(receive, lang='ru'):
        if receive == '1':
            return {
                'ru': 'Вы будете получать рассылки про скидки',
                'en': 'You will receive notifications about discounts',
                'kg': 'Арзандатуулар жөнүндө информация билип турасыз',
            }[lang]
        else:
            return {
                'ru': 'Вы не будете получать рассылки про скидки',
                'en': 'You won\'t receive notifications about discounts',
                'kg': 'Арзандатуулар жөнүндө информация билип турбайсыз',
            }[lang]



            