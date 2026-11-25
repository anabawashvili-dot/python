# ამოცანა 1: პიცერიის შეკვეთა 🍕

def make_order(customer, size, *toppings, **extras):
    size_prices = {'small': 10, 'medium': 15, 'large': 20}
    topping_price = 2
    delivery_price = 5

    total = size_prices.get(size, 0)
    total += len(toppings) * topping_price
    if extras.get('delivery', False):
        total += delivery_price

    print("=" * 30)
    print(f"მომხმარებელი: {customer}")
    print(f"ზომა: {size} ({size_prices.get(size, 0)}₾)")

    print("დანამატები:")
    if toppings:
        for topping in toppings:
            print(f"  - {topping} ({topping_price}₾)")
    else:
        print("  (არ არის)")

    print("დამატებითი პარამეტრები:")
    if extras:
        for key, value in extras.items():
            print(f"  - {key}: {value}")
    else:
        print("  (არ არის)")

    print("-" * 30)
    print(f"ჯამი: {total}₾")
    print("=" * 30)

    return total


# გზა 1: პირდაპირი გამოძახება
price1 = make_order('Nino', 'large', 'cheese', 'olives', delivery=True, drink='Cola')

# გზა 2: სიისა და ლექსიკონის დაშლით
toppings = ['cheese', 'mushrooms', 'ham']
extras = {'delivery': False, 'note': 'No onions'}
price2 = make_order('Luka', 'medium', *toppings, **extras)


# ამოცანა 2: თამაშის ლიდერბორდი 🎮

players = [
    {"nick": "ShadowWolf", "level": 42, "wins": 120, "losses": 30},
    {"nick": "PixelQueen", "level": 42, "wins": 95, "losses": 10},
    {"nick": "NoobMaster", "level": 7, "wins": 3, "losses": 40},
    {"nick": "DragonFly", "level": 58, "wins": 200, "losses": 100},
    {"nick": "CatLord", "level": 58, "wins": 150, "losses": 25},
]

# 1. ლიდერბორდი: level კლებადობით, შემდეგ wins კლებადობით
leaderboard = sorted(players, key=lambda p: (-p["level"], -p["wins"]))
print("ლიდერბორდი:")
for p in leaderboard:
    print(f"  {p['nick']}: level {p['level']}, wins {p['wins']}")

# 2. ყველაზე სტაბილურები: win rate კლებადობით
by_winrate = sorted(
    players,
    key=lambda p: p["wins"] / (p["wins"] + p["losses"]),
    reverse=True,
)
print("\nყველაზე სტაბილური მოთამაშეები:")
for p in by_winrate:
    rate = p["wins"] / (p["wins"] + p["losses"])
    print(f"  {p['nick']}: {rate:.1%}")

# 3. ნიკების ტოპი: სიგრძით, ტოლობისას ანბანით
nicks = sorted((p["nick"] for p in players), key=lambda n: (len(n), n))
print("\nნიკების ტოპი:")
for nick in nicks:
    print(f"  {nick} ({len(nick)})")


# ამოცანა 3: მუსიკალური პლეილისტი 🎵

songs = [
    {"title": "Sunrise", "artist": "Luna", "duration": 215, "plays": 5400},
    {"title": "Midnight Drive", "artist": "Neon Pulse", "duration": 187, "plays": 12800},
    {"title": "Ocean Eyes", "artist": "Luna", "duration": 243, "plays": 9100},
    {"title": "Thunder", "artist": "Neon Pulse", "duration": 201, "plays": 7600},
    {"title": "Quiet Rain", "artist": "Mira", "duration": 156, "plays": 3200},
]


# ნაბიჯი 1
def show_playlist(name, *songs):
    print(name)
    number = 1
    for song in songs:
        print(f"{number}. {song['title']} - {song['artist']} ({song['duration']} წმ)")
        number += 1
    print()


show_playlist('My Playlist', *songs)

# ნაბიჯი 2: Short First
short_first = sorted(songs, key=lambda song: song["duration"])
show_playlist('Short First', *short_first)

# ნაბიჯი 3: Top 3 მოსმენების მიხედვით
top3 = sorted(songs, key=lambda song: song["plays"], reverse=True)[:3]
show_playlist('Top 3', *top3)