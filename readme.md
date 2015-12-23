# Bricklink Pro

After spending countless hours managing an enormous spreadsheet and trying to figure out how to get all of the pieces for my bricklinked UCS Millneium Falcon, I decided that it would be way simpler to run a script to see how much a bricklinked set would cost. That's when I decided to create Bricklink Pro.

Bricklink Pro contians 2 scripts that automate the process of creating set lists and figuring out where to get all the pieces from.

### Setlist.py

The first is `setlist.py`. It takes in a set number and will create a csv with the parts and quantities required for building that set.

Example usage:

```bash
$ python setlist.py 10179-1
```

Example output csv:

```csv
part_id,element_id, qty
3004,300426,20
3009,300926,4
2357,235726,4
...
```

### Bricklink.py

The bricklink script is where the magic happens. Like setlist, it takes the number of the set, but will search bricklink for all of the required pieces and try to get the best bang for your buck.

It searches for the 10 cheapest lots of each piece and bundles orders together from the same store. The output is a csv file containing all the part information as well as the name and link to the store so you can make the purchases. This is really similar to the spreadsheet that I manually created while building my UCS Falcon.

Right now the algorithm is pretty naive (well, very naive). Efforts might be put forth in the future to optimize it, but first it would be nice to have a decent API (looking at you bricklink.com).

Example usage:

```bash
$ python bricklink.py 10179-1
```

Example output csv:

```csv
part_id,element_id,qty,price,name,link
2357,235726,4,0.04,"The Bricky",http://bricklink.com/store.asp?p=landers&itemID=84891667
6134,4124096,2,0.02,"The Bricky",http://bricklink.com/store.asp?p=landers&itemID=82460878
4079,407926,4,0.05,"The Bricky",http://bricklink.com/store.asp?p=landers&itemID=85428707
...
```

Note: This script uses web scraping and requests (one for each piece) so it can take a few minutes for sets with a lot of pieces.

