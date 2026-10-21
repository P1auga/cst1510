from math import tan, pi


# length
def m_to_ft(m):
    return m * 3.28084


def ft_to_m(ft):
    return ft / 3.28084


def in_to_cm(inch):
    return inch * 2.54


def cm_to_in(cm):
    return cm / 2.54


def mi_to_km(mi):
    return mi * 1.60934


def km_to_mi(km):
    return km / 1.60934


# temperature
def c_to_f(c):
    return c * 9 / 5 + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


def c_to_k(c):
    return c + 273.15


def k_to_c(k):
    return k - 273.15


# mass
def kg_to_lb(kg):
    return kg * 2.20462


def lb_to_kg(lb):
    return lb / 2.20462


def g_to_oz(g):
    return g / 28.3495


def oz_to_g(oz):
    return oz * 28.3495


# volume
def l_to_gal(l):
    return l * 0.264172


def gal_to_l(gal):
    return gal / 0.264172


def l_to_qt(l):
    return l * 1.05669


def qt_to_l(qt):
    return qt / 1.05669


# pressure
def bar_to_psi(bar):
    return bar * 14.5038


def psi_to_bar(psi):
    return psi / 14.5038


def atm_to_kpa(atm):
    return atm * 101.325


def kpa_to_atm(kpa):
    return kpa / 101.325


# energy
def j_to_cal(j):
    return j / 4.184


def cal_to_j(cal):
    return cal * 4.184


def kwh_to_mj(kwh):
    return kwh * 3.6


def mj_to_kwh(mj):
    return mj / 3.6


CONVERSIONS = {
    "length": {
        "1": ("m -> ft", m_to_ft),
        "2": ("ft -> m", ft_to_m),
        "3": ("in -> cm", in_to_cm),
        "4": ("cm -> in", cm_to_in),
        "5": ("mi -> km", mi_to_km),
        "6": ("km -> mi", km_to_mi),
    },
    "temperature": {
        "1": ("C -> F", c_to_f),
        "2": ("F -> C", f_to_c),
        "3": ("C -> K", c_to_k),
        "4": ("K -> C", k_to_c),
    },
    "mass": {
        "1": ("kg -> lb", kg_to_lb),
        "2": ("lb -> kg", lb_to_kg),
        "3": ("g -> oz", g_to_oz),
        "4": ("oz -> g", oz_to_g),
    },
    "volume": {
        "1": ("L -> gal", l_to_gal),
        "2": ("gal -> L", gal_to_l),
        "3": ("L -> qt", l_to_qt),
        "4": ("qt -> L", qt_to_l),
    },
    "pressure": {
        "1": ("bar -> psi", bar_to_psi),
        "2": ("psi -> bar", psi_to_bar),
        "3": ("atm -> kPa", atm_to_kpa),
        "4": ("kPa -> atm", kpa_to_atm),
    },
    "energy": {
        "1": ("J -> cal", j_to_cal),
        "2": ("cal -> J", cal_to_j),
        "3": ("kWh -> MJ", kwh_to_mj),
        "4": ("MJ -> kWh", mj_to_kwh),
    },
}


def choose(prompt, options):
    print(prompt)
    for key, (label, _) in sorted(options.items()):
        print(f"  {key}. {label}")
    return input("> ").strip()


def main():
    while True:
        print("\nTypes: " + ", ".join(CONVERSIONS))
        kind = input("Type (or q to quit): ").strip().lower()
        if kind == "q":
            break
        if kind not in CONVERSIONS:
            print("Unknown type.")
            continue

        options = CONVERSIONS[kind]
        key = choose(f"{kind.capitalize()} conversions:", options)
        if key not in options:
            print("Unknown conversion.")
            continue

        label, func = options[key]
        try:
            value = float(input("Value: "))
        except ValueError:
            print("Not a number.")
            continue
        print(f"{label}: {func(value):.4f}")


if __name__ == "__main__":
    main()
