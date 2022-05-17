CURRENT_YEAR = 2021


def get_inductees(nms, bth_yrs, gen):
    unknown_list = []
    inductees_list = []
    for n, b, g in zip(nms, bth_yrs, gen):
        if g is None or b is None:
            unknown_list.append(n)
        elif 18 <= CURRENT_YEAR - b < 30 and g == 'Male':
            inductees_list.append(n)

    # In two lines
    # inductees_list = [n for n, b, g in zip(nms, bth_yrs, gen) if (g is not None and b is not None) and 18 <= CURRENT_YEAR - b < 30 and g == 'Male']
    # unknown_list = [n for n, b, g in zip(nms, bth_yrs, gen) if g is None or b is None]
    return inductees_list, unknown_list


if __name__ == "__main__":
    names = ["Vasya","Alice","Petya","Jenny","Fedya","Viola","Mark","Chris","Margo"]
    birthday_years = [1962,1995,2000,None,None,None,None,1998,2001]
    genders = ["Male","Female","Male","Female","Male",None,None,None,None]
    print(get_inductees(names, birthday_years, genders))

