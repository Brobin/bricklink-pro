from bs4 import BeautifulSoup as soup
from copy import copy
from collections import Counter
import requests
import json
import sys

from models import Set, Part, Listing
from setlist import create_setlist


def get_part_listings(qty, part_id, element_id):
    if element_id == -1:
        return [Listing(part_id, element_id, qty, 0, '', '')]
    listings = []
    url = 'http://www.bricklink.com/search.asp'
    params = {
        'viewFrom': 'sa',
        'qMin': qty,
        'shipCountryID': 'US',
        'sellerCountryID': 'US',
        'moneyTypeID': 1,
        'q': element_id,
        'sellerLoc': 'C',
        'searchSort': 'P',
        'sz': 10
    }
    html = requests.get(url, params=params).text
    results = soup(html, 'html.parser').findAll('td', {'valign' : 'TOP'})
    if len(results) == 0:
        listings.append(Listing(part_id, element_id, qty, 0, '', ''))
    for r in results:
        link = r.find('a')
        price = r.findAll('b')[1].text
        price = float(price.replace('US $', ''))
        listing = Listing(part_id, element_id, qty, price,
                        link.text, link['href'])
        listings.append(listing)
    return listings


def optimize_bricklink(lego_set):
    stores = []
    pieces = []
    purchase = []
    for part in lego_set.parts:
        listings = get_part_listings(int(part.qty), part.part_id,
                                   part.element_id)
        if len(listings) > 0:
            print(part.element_id)
            stores = stores + [o.name for o in listings]
            pieces.append(listings)
    best_stores = Counter(stores)
    for store, val in best_stores.most_common():
        temp_pieces = copy(pieces)
        for piece in temp_pieces:
            listing = [x for x in piece if x.name == store]
            if len(listing) > 0:
                purchase.append(listing[0])
                pieces.remove(piece)
    return purchase


def output_purchase_to_csv(lego_set, purchase, set_id):
    with open(lego_set.bricklink_file, 'w+') as f:
        f.write('part_id,element_id,qty,price,name,link\n')
        def part_id(p):
            return p.part_id
        for p in sorted(purchase, key=part_id):
            f.write(str(p))


if __name__ == '__main__':
    try:
        set_id = sys.argv[1]
    except:
        set_id = '75102-1'
    lego_set = create_setlist(set_id)
    to_buy = optimize_bricklink(lego_set)
    output_purchase_to_csv(lego_set, to_buy, set_id)
    