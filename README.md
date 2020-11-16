# promoscrapper.py

Criei este programa para procurar promoções em páginas específicas. Ótimo para utilizar em fóruns com seções de promoções ou qualquer site que agregue itens em promoção em uma página.
Foi feito para ser utilizado em um cronjob no Linux, por isso o subprocesso invoca o caminho absoluto para o notify-send.

Uso: promoscrapper.py -i (items separados por espaço) -u (endereço do site)

Small program to search for intens on sale on a specific page. Good for sites or boards who compile itens on sale in one page.
It was made for use as a cronjob on Linux. That's the reason it uses absolute path to call notify-send.

Usage: promoscrapper.py -i (items separated by space) -u (url)
