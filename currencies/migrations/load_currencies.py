# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

def load_currency_data(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Currency = apps.get_model("currencies", "Currency")
    db_alias = schema_editor.connection.alias
    Currency.objects.using(db_alias).bulk_create([
        Currency(name='Albania Lek',code='ALL',symbol='Lek'),
        Currency(name='Afghanistan Afghani',code='AFN',symbol='؋'),
        Currency(name='Argentina Peso',code='ARS',symbol='$'),
        Currency(name='Aruba Guilder',code='AWG',symbol='ƒ'),
        Currency(name='Australia Dollar',code='AUD',symbol='$'),
        Currency(name='Azerbaijan New Manat',code='AZN',symbol='ман'),
        Currency(name='Bahamas Dollar',code='BSD',symbol='$'),
        Currency(name='Barbados Dollar',code='BBD',symbol='$'),
        Currency(name='Belarus Ruble',code='BYN',symbol='Br'),
        Currency(name='Belize Dollar',code='BZD',symbol='BZ$'),
        Currency(name='Bermuda Dollar',code='BMD',symbol='$'),
        Currency(name='Bolivia Bolíviano',code='BOB',symbol='$b'),
        Currency(name='Bosnia and Herzegovina Convertible Marka',code='BAM',symbol='KM'),
        Currency(name='Botswana Pula',code='BWP',symbol='P'),
        Currency(name='Bulgaria Lev',code='BGN',symbol='лв'),
        Currency(name='Brazil Real',code='BRL',symbol='R$'),
        Currency(name='Brunei Darussalam Dollar',code='BND',symbol='$'),
        Currency(name='Cambodia Riel',code='KHR',symbol='៛'),
        Currency(name='Canada Dollar',code='CAD',symbol='$'),
        Currency(name='Cayman Islands Dollar',code='KYD',symbol='$'),
        Currency(name='Chile Peso',code='CLP',symbol='$'),
        Currency(name='China Yuan Renminbi',code='CNY',symbol='¥'),
        Currency(name='Colombia Peso',code='COP',symbol='$'),
        Currency(name='Costa Rica Colon',code='CRC',symbol='₡'),
        Currency(name='Croatia Kuna',code='HRK',symbol='kn'),
        Currency(name='Cuba Peso',code='CUP',symbol='₱'),
        Currency(name='Czech Republic Koruna',code='CZK',symbol='Kč'),
        Currency(name='Denmark Krone',code='DKK',symbol='kr'),
        Currency(name='Dominican Republic Peso',code='DOP',symbol='RD$'),
        Currency(name='East Caribbean Dollar',code='XCD',symbol='$'),
        Currency(name='Egypt Pound',code='EGP',symbol='£'),
        Currency(name='El Salvador Colon',code='SVC',symbol='$'),
        Currency(name='Euro Member Countries',code='EUR',symbol='€'),
        Currency(name='Falkland Islands (Malvinas) Pound',code='FKP',symbol='£'),
        Currency(name='Fiji Dollar',code='FJD',symbol='$'),
        Currency(name='Ghana Cedi',code='GHS',symbol='¢'),
        Currency(name='Gibraltar Pound',code='GIP',symbol='£'),
        Currency(name='Guatemala Quetzal',code='GTQ',symbol='Q'),
        Currency(name='Guernsey Pound',code='GGP',symbol='£'),
        Currency(name='Guyana Dollar',code='GYD',symbol='$'),
        Currency(name='Honduras Lempira',code='HNL',symbol='L'),
        Currency(name='Hong Kong Dollar',code='HKD',symbol='$'),
        Currency(name='Hungary Forint',code='HUF',symbol='Ft'),
        Currency(name='Iceland Krona',code='ISK',symbol='kr'),
        Currency(name='India Rupee',code='INR',symbol=''),
        Currency(name='Indonesia Rupiah',code='IDR',symbol='Rp'),
        Currency(name='Iran Rial',code='IRR',symbol='﷼'),
        Currency(name='Isle of Man Pound',code='IMP',symbol='£'),
        Currency(name='Israel Shekel',code='ILS',symbol='₪'),
        Currency(name='Jamaica Dollar',code='JMD',symbol='J$'),
        Currency(name='Japan Yen',code='JPY',symbol='¥'),
        Currency(name='Jersey Pound',code='JEP',symbol='£'),
        Currency(name='Kazakhstan Tenge',code='KZT',symbol='лв'),
        Currency(name='Korea (North) Won',code='KPW',symbol='₩'),
        Currency(name='Korea (South) Won',code='KRW',symbol='₩'),
        Currency(name='Kyrgyzstan Som',code='KGS',symbol='лв'),
        Currency(name='Laos Kip',code='LAK',symbol='₭'),
        Currency(name='Lebanon Pound',code='LBP',symbol='£'),
        Currency(name='Liberia Dollar',code='LRD',symbol='$'),
        Currency(name='Macedonia Denar',code='MKD',symbol='ден'),
        Currency(name='Malaysia Ringgit',code='MYR',symbol='RM'),
        Currency(name='Mauritius Rupee',code='MUR',symbol='₨'),
        Currency(name='Mexico Peso',code='MXN',symbol='$'),
        Currency(name='Mongolia Tughrik',code='MNT',symbol='₮'),
        Currency(name='Mozambique Metical',code='MZN',symbol='MT'),
        Currency(name='Namibia Dollar',code='NAD',symbol='$'),
        Currency(name='Nepal Rupee',code='NPR',symbol='₨'),
        Currency(name='Netherlands Antilles Guilder',code='ANG',symbol='ƒ'),
        Currency(name='New Zealand Dollar',code='NZD',symbol='$'),
        Currency(name='Nicaragua Cordoba',code='NIO',symbol='C$'),
        Currency(name='Nigeria Naira',code='NGN',symbol='₦'),
        Currency(name='Norway Krone',code='NOK',symbol='kr'),
        Currency(name='Oman Rial',code='OMR',symbol='﷼'),
        Currency(name='Pakistan Rupee',code='PKR',symbol='₨'),
        Currency(name='Panama Balboa',code='PAB',symbol='B/.'),
        Currency(name='Paraguay Guarani',code='PYG',symbol='Gs'),
        Currency(name='Peru Sol',code='PEN',symbol='S/.'),
        Currency(name='Philippines Peso',code='PHP',symbol='₱'),
        Currency(name='Poland Zloty',code='PLN',symbol='zł'),
        Currency(name='Qatar Riyal',code='QAR',symbol='﷼'),
        Currency(name='Romania New Leu',code='RON',symbol='lei'),
        Currency(name='Russia Ruble',code='RUB',symbol='₽'),
        Currency(name='Saint Helena Pound',code='SHP',symbol='£'),
        Currency(name='Saudi Arabia Riyal',code='SAR',symbol='﷼'),
        Currency(name='Serbia Dinar',code='RSD',symbol='Дин.'),
        Currency(name='Seychelles Rupee',code='SCR',symbol='₨'),
        Currency(name='Singapore Dollar',code='SGD',symbol='$'),
        Currency(name='Solomon Islands Dollar',code='SBD',symbol='$'),
        Currency(name='Somalia Shilling',code='SOS',symbol='S'),
        Currency(name='South Africa Rand',code='ZAR',symbol='R'),
        Currency(name='Sri Lanka Rupee',code='LKR',symbol='₨'),
        Currency(name='Sweden Krona',code='SEK',symbol='kr'),
        Currency(name='Switzerland Franc',code='CHF',symbol='CHF'),
        Currency(name='Suriname Dollar',code='SRD',symbol='$'),
        Currency(name='Syria Pound',code='SYP',symbol='£'),
        Currency(name='Taiwan New Dollar',code='TWD',symbol='NT$'),
        Currency(name='Thailand Baht',code='THB',symbol='฿'),
        Currency(name='Trinidad and Tobago Dollar',code='TTD',symbol='TT$'),
        Currency(name='Turkey Lira',code='TRY',symbol=''),
        Currency(name='Tuvalu Dollar',code='TVD',symbol='$'),
        Currency(name='Ukraine Hryvnia',code='UAH',symbol='₴'),
        Currency(name='United Kingdom Pound',code='GBP',symbol='£'),
        Currency(name='United States Dollar',code='USD',symbol='$'),
        Currency(name='Uruguay Peso',code='UYU',symbol='$U'),
        Currency(name='Uzbekistan Som',code='UZS',symbol='лв'),
        Currency(name='Venezuela Bolivar',code='VEF',symbol='Bs'),
        Currency(name='Viet Nam Dong',code='VND',symbol='₫'),
        Currency(name='Yemen Rial',code='YER',symbol='﷼'),
        Currency(name='Zimbabwe Dollar',code='ZWD',symbol='Z$'),
    ])

def unload_currency_data(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Currency = apps.get_model("currencies", "Currency")
    db_alias = schema_editor.connection.alias
    Currency.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
    ]
    
    operations = [
        migrations.RunPython(load_currency_data,unload_currency_data),
    ]