from nicegui import ui

REGIONS = {
    "ap-guangzhou": {
        "zones": {
            "ap-guangzhou-1": ["S5.MEDIUM4", "S6.LARGE8"],
            "ap-guangzhou-2": ["S6.LARGE8"],
        }
    },
    "ap-shanghai": {
        "zones": {
            "ap-shanghai-1": ["S5.MEDIUM4"],
        }
    }
}

IMAGES = {
    "Ubuntu 22.04": "img-ubuntu",
    "CentOS 7": "img-centos",
}

state = {
    "region": "ap-guangzhou",
    "zone": None,
    "flavor": None,
    "image": "Ubuntu 22.04",
}

def update_zones():
    zones = list(REGIONS[state["region"]]["zones"].keys())
    zone_select.options = zones
    zone_select.value = zones[0]
    update_flavors()

def update_flavors():
    flavors = REGIONS[state["region"]]["zones"][state["zone"]]
    flavor_select.options = flavors
    flavor_select.value = flavors[0]

def create_vm():
    ui.notify(
        f"""
        创建虚拟机：
        Region={state['region']}
        Zone={state['zone']}
        Flavor={state['flavor']}
        Image={state['image']}
        """
    )

ui.label("创建腾讯云虚拟机")
print("创建腾讯云虚拟机region_select")
region_select = ui.select(
    list(REGIONS.keys()),
    value=state["region"],
    label="Region",
    on_change=lambda e: (
        state.update(region=e.value),
        update_zones(),
    ),
)

zone_select = ui.select([], label="Availability Zone",
    on_change=lambda e: state.update(zone=e.value)
)

flavor_select = ui.select([], label="Instance Type",
    on_change=lambda e: state.update(flavor=e.value)
)

image_select = ui.select(
    list(IMAGES.keys()),
    value=state["image"],
    label="Image",
    on_change=lambda e: state.update(image=e.value),
)

ui.button("Create VM", on_click=create_vm)

update_zones()
ui.run()
