class GeneralTexts():
    def text_start_admin(lang='ru', full_name=''):
        return {
            'ru': f'<b>Здравствуйте {full_name}, вы вошли как админ!</b>',
            'en': f'<b>Hello {full_name}, you joined as an admin!</b>',
            'kg': f'<b>Эу {full_name}, админ болуп кирдин!</b>',
        }[lang]
    
    def text_start_client(lang='ru', full_name=''):
        if full_name is None:
            full_name = ''
        return {
            'ru': f'<b>Здравствуйте {full_name}, этот бот поможет вам выбрать товар или связаться с консультантом. \nДля этого используйте кнопки ниже!</b>',
            'en': f'<b>Hello {full_name}, this bot can help you choose a product or contact the managers.\nPlease use the buttons below!</b>',
            'kg': f'<b>Эу {full_name}, бул ботта э!</b>',
        }[lang]


class ClientTexts():
    def see_mattress_category(lang='ru'):
        return {
            'ru': f'<b>Выберите категорию \U0001F600</b>',
            'en': f'<b>Choose a category \U0001F600</b>',
            'kg': f'<b>Категория танданыз \U0001F600</b>',
        }[lang] 

    def see_mattress(product_name: str, product_description: str, product_price: float, product_discount: float, lang='ru'):
        return {
            'ru': f'<b>{product_name}</b>\nОписание: {product_description}\nЦена за м\U000000B2: <s>{product_price}</s> {float(product_price) * (100 - float(product_discount)) / 100} сом',
            'en': f'<b>{product_name}</b>\nDescription: {product_description}\nPrice for a м\U000000B2: <s>{product_price}</s> {float(product_price) * (100 - float(product_discount)) / 100} som',
            'kg': f'<b>{product_name}</b>\nСуроттомо: {product_description}\nм\U000000B2 баасы: <s>{product_price}</s> {float(product_price) * (100 - float(product_discount)) / 100} сом',
        }[lang]   
    
    def see_accessory(product_name: str, product_description: str, product_price: float, product_discount: float, lang='ru'):
        return {
            'ru': f'<b>{product_name}</b>\nОписание: {product_description}\nЦена за м\U000000B2: <s>{product_price}</s> {float(product_price) * (100 - float(product_discount)) / 100} сом',
            'en': f'<b>{product_name}</b>\nDescription: {product_description}\nPrice for a м\U000000B2: <s>{product_price}</s> {float(product_price) * (100 - float(product_discount)) / 100} som',
            'kg': f'<b>{product_name}</b>\nСуроттомо: {product_description}\nм\U000000B2 баасы: <s>{product_price}</s> {float(product_price) * (100 - float(product_discount)) / 100} сом',
        }[lang]
    
    def chosen_product(product_name: str, lang='ru'):
        return {
        'ru': f'Вы выбрали {product_name}, наши консультанты свяжутся с вами в ближайщее время!',
        'en': f'You chose {product_name}, our managers will contact you asap!',
        'kg': f'{product_name} тандадыназ, скоро все будет, коркпо!',
        }[lang]  

    def about_us(lang='ru'):
        return {
            'ru': f'ПРО НАС ТЕКСТ АОЫДЛВОАДЛЫОВДАОДЫВОАЛОДВЫАОЛ\n \U0001F600',
            'en': f'TEXT about uslkasjdfljaskldjfk\n\U0001F600',
            'kg': f'adfkajsdflkjasldfjlkasjdlfkjasdf\n\U0001F600',
        }[lang]

    def social_media(lang='ru'):
        return {
            'ru': f'nije ssylki',
            'en': f'The links to our social media are below',
            'kg': f'ssylkalar yldyida'
        }[lang]
    
    def change_language(lang='ru'):
        return {
            'ru': 'Язык поменялся на Русский!',
            'en': 'The language is English now!',
            'kg': 'Кыргыз тилине которулду!',
        }[lang]

    def review_question_name(lang='ru'):
        return {
            'ru': 'RU what is your name?',
            'en': 'EN what is your name?',
            'kg': 'KG what is your name?',
        }[lang]
    
    def review_question_review(lang='ru'):
        return {
            'ru': 'RU Please write your review down',
            'en': 'EN Please write your review down',
            'kg': 'KG Please write your review down',
        }[lang]
    
    def review_end(lang='ru'):
        return {
            'ru': 'RU thanks for the review, we will consider that',
            'en': 'EN thanks for the review, we will consider that',
            'kg': 'KG thanks for the review, we will consider that',
        }[lang]
    
    def review_cancel(lang='ru'):
        return {
            'ru': 'RU review canceled',
            'en': 'EN review canceled',
            'kg': 'KG review canceled',
        }[lang]

    def question_buyer_name(lang='ru'):
        return {
            'ru': 'RU What is your name>/',
            'en': 'Please tell me your name.',
            'kg': 'KG What is your name?',
        }[lang]

    def question_buyer_phone_number(lang='ru'):
        return {
            'ru': 'RU PHONE NUMBER',
            'en': 'Send your phone number using the button below',
            'kg': 'KG PHONE NUMBER',
        }[lang]


    def cancel_buy(lang='ru'):
        return {
            'ru': 'RU CANCEL BUY',
            'en': 'Successfully canceled!',
            'kg': 'KG CANCEL BUY',
        }[lang]
    
    def receive_notifications(lang='ru'):
        return {
            'ru': 'Hotite poluchat rassylku',
            'en': 'Do you want to be notified about discounts',
            'kg': 'Hkaflsjdkflajkdjfalad Rassylka',
        }[lang]

    def receive_notification_yes_no(receive, lang='ru'):
        if receive == '1':
            return {
                'ru': 'RU YEs RECEIVE',
                'en': 'EN YES RECEIVE',
                'kg': 'KG YES RECEIVE',
            }[lang]
        else:
            return {
                'ru': 'RU NOT RECEIVE',
                'en': 'EN NOT REcEIVE',
                'kg': 'KG NOT RECEIVE',
            }[lang]