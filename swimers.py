def find_athletes(knw_en, sts_men, mre_thn_20):
    lists = [knw_en, sts_men, mre_thn_20]
    lens = [(len(l), i) for i, l in enumerate(lists)]

    min_list = min(lens)
    athletes = []
    for name in lists[min_list[1]]:
        if name in knw_en and name in sts_men and name in mre_thn_20:
            athletes.append(name)

    # In one line
    # athletes = [name for name in lists[min_list[1]] if name in knw_en and name in sts_men and name in mre_thn_20]

    return athletes


if __name__ == "__main__":
    know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
    sportsmen = ["Don","Peter","Eric","Jimmy","Mark"]
    more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]

    print(find_athletes(know_english, sportsmen, more_than_20_years))
