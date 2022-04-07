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


class AdminTexts():
    def order(username:str, full_name: str, phone_number: str, product: str, lang='ru'):
        return {
            'ru': f'<b>Новый заказ от {username}</b>\nИмя: {full_name}\nТелефон: {phone_number}\nТовар: {product}',
            'en': f'<b>New order from {username}</b>\nName: {full_name}\nPhone Number: {phone_number}\nProduct: {product}',
            'kg': f'<b>New Заказ {username}</b>\nАты: {full_name}\nТелефону: {phone_number}\nТовар: {product}',
        }[lang]
    
    def upload_product_name(lang='ru'):
        return {
            'ru': 'Как называется матрас(аксессуар)?',
            'en': 'What is the name of the product?',
            'kg': 'Товардын атын жазыңыз',
        }[lang]
    
    def upload_product_photo(lang='ru'):
        return {
            'ru': 'Теперь загрузите фотографию товара!',
            'en': 'Upload the picture of the product!',
            'kg': 'Эми товардын сүрөтүн жүктөнүз!',
        }[lang]
    
    def upload_product_description(lang='ru'):
        return {
            'ru': 'Теперь напишите описание!',
            'en': 'Write down a description!',
            'kg': 'Сурөттөмө жазыныз!',
        }[lang]

    def upload_product_price(lang='ru'):
        return {
            'ru': 'Теперь укажите цену без скидки!',
            'en': 'What is the price of this product!',
            'kg': 'Баасы канча?'
        }[lang]

    def upload_product_discount(lang='ru'):
        return {
            'ru': 'Теперь укажите скидку!',
            'en': 'Set the discount now!',
            'kg': 'Арзандатуусу канча?'
        }[lang]

    def upload_product_category(lang='ru'):
        return {
            'ru': '''
<b>Выберите категорию</b>
<code>'all' - Все матрасы</code>
<code>'dsc' - Матрасы со скидками</code>
<code>'chp' - Недорогие матрасы</code>
<code>'hvy' - Для тяжёлых людей</code>
<code>'hrd' - Жёсткие матрасы</code>
<code>'sft' - Мягкие матрасы</code>
<code>'kid' - Детские матрасы</code>
<code>'acs' - Аксессуары</code>
<b>Перечислите все категории через запятую 'dsc, sft, acs'</b>
        ''',
        'en': '''
<b>Choose categories</b>
<code>'all' - All the mattresses</code>
<code>'dsc' - Discounted mattresses</code>
<code>'chp' - Inexpensive mattresses</code>
<code>'hvy' - For heavy people</code>
<code>'hrd' - Hard mattresses</code>
<code>'sft' - Soft mattresses</code>
<code>'kid' - Kid mattresses</code>
<code>'acs' - Accessories</code>
<b>List all the categories separated by commas 'dsc, sft, acs'</b>
        ''',
        'kg': '''
<b>Категория танданыз</b>
<code>'all' - Бардык матрацтар</code>
<code>'dsc' - Арзандатуулар менен матрацтар</code>
<code>'chp' - Арзан матрацтар</code>
<code>'hvy' - Оор адамдар үчүн</code>
<code>'hrd' - Катуу матрацтар</code>
<code>'sft' - Жумшак матрацтар</code>
<code>'kid' - Балдар үчүн матрацтар</code>
<code>'acs' - Аксессуарлар</code>
<b>Утур менен болуп жазыныз 'dsc, sft, acs'</b>
        ''',
        }[lang]

    def upload_product_success(lang='ru'):
        return {
            'ru': 'Продукт успешно добавлен в базу данных!',
            'en': 'The product is added to the database!',
            'kg': 'Базага кошулду!'
        }[lang]
    
    def upload_product_cancel(lang='ru'):
        return {
            'ru': 'Загрузка успешно отменена!',
            'en': 'Upload is canceled!',
            'kg': 'Жокко чыкты!'
        }[lang]

    def delete_product(product_name, product_category, lang='ru'):
        return {
            'ru': f'{product_name}\nКатегории: {product_category}',
            'en': f'{product_name}\nCategories: {product_category}',
            'kg': f'{product_name}\nКатегорялар: {product_category}',
        }[lang]
    
    def delete_product_callback(product_name, lang='ru'):
        return {
            'ru': f"Вы успешно удалили {product_name}",
            'en': f'You successfuly deleted {product_name}',
            'kg': f'{product_name} өчүрдүнүз',
        }[lang]


    def change_language(lang='ru'):
        return {
            'ru': 'Язык поменялся на Русский!',
            'en': 'The language is English now!',
            'kg': 'Кыргыз тилине которулду!',
        }[lang]


