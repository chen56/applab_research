# create_vm.py
import streamlit as st

st.set_page_config(page_title="Create CVM (Mock)", layout="centered")

if(st.session_state.get("count") == None):
  st.session_state.count = 0
st.session_state.count += 1

from xx import cache
cache["count"] = cache.get("count", 0) + 1
print(cache)

# ----------------------------
# Mock data (模拟云厂商能力表)
# ----------------------------
REGIONS = {
    "ap-guangzhou": {
        "name": "广州",
        "zones": {
            "ap-guangzhou-1": {
                "instance_types": ["SA2.MEDIUM4", "SA2.LARGE8"],
            },
            "ap-guangzhou-2": {
                "instance_types": ["SA2.MEDIUM4"],
            },
        },
    },
    "ap-shanghai": {
        "name": "上海",
        "zones": {
            "ap-shanghai-1": {
                "instance_types": ["S5.MEDIUM4", "S5.LARGE8"],
            }
        },
    },
}

IMAGES = {
    "SA2.MEDIUM4": ["Ubuntu 22.04", "CentOS 7"],
    "SA2.LARGE8": ["Ubuntu 22.04"],
    "S5.MEDIUM4": ["Ubuntu 20.04", "Debian 12"],
    "S5.LARGE8": ["Ubuntu 22.04"],
}

DISK_TYPES = {
    "SA2.MEDIUM4": ["Cloud SSD", "Premium Cloud Storage"],
    "SA2.LARGE8": ["Cloud SSD"],
    "S5.MEDIUM4": ["Cloud SSD"],
    "S5.LARGE8": ["Cloud SSD"],
}

# ----------------------------
# Step 1: Region
# ----------------------------

region = st.selectbox(
    "Region",
    options=list(REGIONS.keys()),
    format_func=lambda r: f"{REGIONS[r]['name']} ({r})",
)
print("sdsd")

from time import sleep

# ----------------------------
# Step 2: Zone (depends on region)
# ----------------------------

zones = REGIONS[region]["zones"]
zone = st.selectbox(
    "Availability Zone",
    options=list(zones.keys()),
)

# ----------------------------
# Step 3: Instance Type (depends on zone)
# ----------------------------

instance_types = zones[zone]["instance_types"]
instance_type = st.selectbox(
    "Instance Type",
    options=instance_types,
)

# ----------------------------
# Step 4: Image (depends on instance type)
# ----------------------------

image = st.selectbox(
    "System Image",
    options=IMAGES.get(instance_type, []),
)

# ----------------------------
# Step 5: Disk
# ----------------------------

disk_type = st.selectbox(
    "System Disk Type",
    options=DISK_TYPES.get(instance_type, []),
)

disk_size = st.slider(
    "System Disk Size (GB)",
    min_value=50,
    max_value=500,
    step=10,
    value=100,
)

# ----------------------------
# Step 6: Network
# ----------------------------

vpc = st.selectbox(
    "VPC",
    options=["vpc-default", "vpc-prod", "vpc-dev"],
)

subnet = st.selectbox(
    "Subnet",
    options=[
        f"{vpc}-subnet-a",
        f"{vpc}-subnet-b",
    ],
)

public_ip = st.checkbox("Assign Public IP", value=True)

# ----------------------------
# Summary
# ----------------------------

st.divider()
st.subheader("Summary")

spec = {
    "region": region,
    "zone": zone,
    "instance_type": instance_type,
    "image": image,
    "disk": {
        "type": disk_type,
        "size_gb": disk_size,
    },
    "network": {
        "vpc": vpc,
        "subnet": subnet,
        "public_ip": public_ip,
    },
}

st.json(spec)

if st.button("Create VM"):
    st.success("VM creation request submitted (mock)")
