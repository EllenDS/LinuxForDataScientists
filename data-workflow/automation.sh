#! /bin/bash

# Voor het automatiseren vermoed ik dat we het laatste hoofdstuk dienen te gebruiken,
# maar zo ver ben ik nog niet geraakt in de cursus.
# Om deze opdracht te automatiseren zou ik gebruik maken van de crontab.

# Het eerste script kan, net zoals er gebeurd is voor de verzameling van de data,
# continue doorlopen en elke minuut of 2 minuten data binnenhalen.

# Het tweede script kan aangepast worden om enkel data te verwerken van een bepaalde datum
# en kan steeds enkele minuten na middernacht de data van de corige dag verwerken.
# De datum kan dan verwerkt worden in de bestandsnaam.

# Het derde script kan vervolgens deze data omzetten in een rapport.
# Dit kan dagelijks of wekelijks gebeuren, zoals gewenst.
# Ook hier kan de bestandsnaam verwijzen naar de periode waarin de data verzameld werd.

# Het resultaat in de crontab:
# */2 * * * * get_data.sh
# 5 0 * * * transform_data.sh
# 0 2 * * * analyse.py

# Maar om er toch een script van te maken:
# Om dit script te laten werken zou het toegevoegd worden aan de crontab als volgt:
# */2 * * * * automation.sh
# De andere scripts zouden wel aangepast moeten worden om enkel de relevante bestanden te # verwerken.


./get_data.sh

day=$(date +"%u")
hour=$(date +"%H")
minute=$(date +"%M")

if [ "$hour" == 0 ]; then
    if [ "$minute" == 05 ]; then 
            ./transform_data.sh
    fi
fi

if [ "$day" == 7 ]; then
    if [ "$hour" == 2 ]; then
        if [ "$minute" == 00 ]; then 
            ./analyse.py
        fi
    fi
fi




