#!/usr/bin/env python3
#
# Populate db

from app import *
from model import *
from datetime import datetime

with app.app_context():
    db.create_all()

    # Banks
    BRD = Banks(
        bank_name='BRD GSG',
        long_name='Banca Romana pentru Dezvoltare',
        country='RO'
    )
    BT = Banks(
        bank_name='BT',
        long_name='Banca Transilvania',
        country='RO'
    )
    ING = Banks(
        bank_name='ING',
        country='RO'
    )
    RAIF = Banks(
        bank_name='Raiffeisen',
        country='RO'
    )

    Mastercard = CardTypes(
        type_name='Mastercard'
        # digits = 16
    )

    Visa = CardTypes(
        type_name='Visa'
        # digits = 16
    )

    AMEX = CardTypes(
        type_name='AMEX',
        digits = 15
    )


    # Cards
    brd_cvt = Cards(
        bank=BRD,
        card_name='Cum Vrei Tu',
        type=Mastercard,
        currency='RON',
        interest_rate=14.72,
        interest_free_days=60,
        minimum_repayment_percent=2,
        max_credit_limit=22000,
        opening_fee=50,
        yearly_fee=50,
        eligibility_employment_months=3,
        promotion='15% cashback la magazinele partenere: Emag, Decathlon, Casa Rusu, Praktiker, etc.',
        internet_banking='MyBRD Net, MyBRD Mobile',
        is_contactless=True,
        offer_url='https://www.brd.ro/persoane-fizice/carduri/carduri-de-credit/cardul-de-credit-cumvreitu',
        renew_years=3,
        allows_additional_cards=True,
        last_update=datetime.utcnow(),
    )

    brd_dcc = Cards(
        bank=BRD,
        card_name='Dusi cu cardul',
        type=Mastercard,
        currency='RON',
        interest_rate=23.00,
        interest_free_days=55,
        minimum_repayment_percent=3.5,
        max_credit_limit=25000,
        opening_fee=0,
        yearly_fee=50,
        eligibility_employment_months=3,
        promotion='Reduceri de până la 50% în peste 500 de locații partenere - Sport, Telecom, ElectroIT, Copii, Hobby, Medical, Modă, Turism',
        interest_free_installments=18,
        internet_banking='MyBRD Net, MyBRD Mobile',
        is_contactless=True,
        offer_url='https://campanii.brd.ro/cardcredit/',
        renew_years=3,
        allows_additional_cards=True,
        balance_transfer='REFINANTARE IN 36 DE RATE CU DOBANDA ZERO',
        balance_transfer_interest_rate=0,
        last_update=datetime.utcnow(),
    )

    bt_star_forte = Cards(
        bank=BT,
        card_name='Star Forte',
        type=Mastercard,
        currency='RON',
        interest_rate=24.00,
        interest_free_days=56,
        credit_limit_comment='De pana la 5 ori venitul lunar, maximum echivalentul a 5000 EUR in RON',
        minimum_repayment_percent=10,
        minimum_repayment='10%, intre 1 si 25 a lunii',
        opening_fee = 0,
        yearly_fee = 25,
        eligibility_employment_months=12,
        offer_url='http://www.starbt.ro/',
        rewards='Puncte Star - 1 punct = 1 leu, 8500 magazine partenere',
        interest_free_installments=12,
        renew_years=5,
        is_contactless=True,
        allows_additional_cards=True,
        other_fees='http://www.starbt.ro/files/star-forte/comisioane_star_forte.pdf',
        last_update=datetime.utcnow(),
    )

    ing_cc = Cards(
        bank=ING,
        card_name='Credit Card',
        type=Visa,
        currency='RON',
        max_credit_limit=35000,
        renew_years=5,
        eligibility_employment_months=3,
        eligibility_min_salary=1500,
        eligibility='Venit minim 1500 RON, Minim un an vechime in munca si minim 3 luni vechime la ultimul angajator, fara intreruperi mai mari de o luna in ultimul an',
        interest_rate=20.83,
        interest_free_days=45,
        rewards='12 rate fara dobanda, 24 sau 36 rate cu 12% dobanda',
        interest_free_installments=3,
        minimum_repayment_percent=5,
        minimum_repayment_sum=50,
        minimum_repayment='5%, 10% sau 15%, minim 50 RON, pe data de 5, 15 sau 25 ale lunii',
        is_contactless=True,
        allows_additional_cards=False,
        offer_url='https://www.ing.ro/ingb/persoane-fizice/credite/credit-card.html',
        sms_notif='Plati peste 300 RON',
        last_update=datetime.utcnow(),
    )

    raif_cc = Cards(
        bank=RAIF,
        card_name='Cardul Standard',
        type=Mastercard,
        currency='RON',
        min_credit_limit=700,
        max_credit_limit=20000,
        interest_rate=20.28,
        eligibility_employment_months=3,
        eligibility='Minim 3 luni vechime la ultimul loc de munca, 1 an vechime in piata muncii, Venit minim de 150 EUR pe familie',
        interest_free_days=56,
        is_contactless=True,
        allows_additional_cards=True,
        minimum_repayment_percent=5,
        minimum_repayment='5%, pe data de 7, 15, 22 ale lunii',
        rewards='puncte Multishop - 1 punct = 1 leu',
        interest_free_installments=12,
        offer_url='https://www.raiffeisen.ro/persoane-fizice/produsele-noastre/credite/carduri-de-cumparaturi/cardul-de-cumparaturi-standard/',
        opening_fee=0,
        yearly_fee=40,
        default_charges='Plata intarziata: 20 RON',
        additional_charges='Interogare ATM propriu: 0.75 RON, Interogare ATM alte banci: 2.5 RON',
        travel_insurance='Travel insurance',
        purchase_protection=45,
        last_update=datetime.utcnow(),
    )


    # Add and commit
    db.session.add(Visa)
    db.session.add(Mastercard)
    db.session.add(AMEX)

    db.session.add(BRD)
    db.session.add(brd_cvt)

    # db.session.add(BT)
    # db.session.add(bt_star_forte)

    db.session.commit()
