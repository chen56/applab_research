import gradio as gr

REGIONS = {
    "ap-guangzhou4": {
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

def update_zones(region):
    zones = list(REGIONS[region]["zones"].keys())
    return gr.update(choices=zones, value=zones[0])

def update_instance_types(region, zone):
    flavors = REGIONS[region]["zones"][zone]
    return gr.update(choices=flavors, value=flavors[0])

def create_vm(region, zone, flavor, image):
    return f"""
    创建虚拟机参数：
    Region: {region}
    Zone: {zone}
    Flavor: {flavor}
    Image: {image}
    """

with gr.Blocks() as demo:
    print("with gr.Blocks() as demo:")

    gr.Markdown("## 创建腾讯云虚拟机")

    region = gr.Dropdown(
        label="Region",
        choices=list(REGIONS.keys()),
        value="ap-guangzhou",
    )

    zone = gr.Dropdown(label="Availability Zone")
    instance_type = gr.Dropdown(label="Instance Type")
    image = gr.Dropdown(
        label="Image",
        choices=list(IMAGES.keys()),
        value="Ubuntu 22.04",
    )

    output = gr.Textbox(label="Result")
    btn = gr.Button("Create VM")

    region.change(update_zones, region, zone)
    zone.change(lambda r, z: update_instance_types(r, z), [region, zone], instance_type)
    btn.click(create_vm, [region, zone, instance_type, image], output)

print("创建腾讯云虚拟机region_select")

demo.launch()
