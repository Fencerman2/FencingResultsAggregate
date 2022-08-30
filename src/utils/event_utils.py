from bs4 import BeautifulSoup


def event_name_standardizer(event_name: str):
    trimmed_name = event_name
    if "D & Under" in event_name:
        trimmed_name = event_name.replace("D & Under", "Div3")
    if "C & Under" in event_name:
        trimmed_name = event_name.replace("C & Under", "Div2")
    if "Junior (U20)" in event_name:
        trimmed_name = event_name.replace("Junior (U20)", "Junior")
    if "Cadet (U17)" in event_name:
        trimmed_name = event_name.replace("Cadet (U17)", "Cadet")
    if "VetCombined" in event_name:
        trimmed_name = event_name.replace("VetCombined", "Vet Combined")
    if "Div 1A" in event_name:
        trimmed_name = event_name.replace("Div 1A", "Div1A")
    if "EUnder" in event_name:
        trimmed_name = event_name.replace("EUnder", "E & Under")

    return trimmed_name


def build_pool_results(pool_html, first_name, last_name):
    soup = BeautifulSoup(pool_html, 'html.parser')

    raise "unimplemented"
