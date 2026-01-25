from deepdiff import DeepDiff
from deepdiff.helper import COLORED_VIEW


def get_all_paths(d, current_path="root"):
    """get all paths from a nested dict or list"""
    paths = []
    if isinstance(d, dict):
        for k, v in d.items():
            new_path = f"{current_path}['{k}']"
            paths.extend(get_all_paths(v, new_path))
    elif isinstance(d, list):
        for i, v in enumerate(d):
            new_path = f"{current_path}[{i}]"
            paths.extend(get_all_paths(v, new_path))
    else:
        # leaf node（int, str, float...）
        paths.append(current_path)
    return paths


subset = {"params": {"gpu": "A100", "memory": {"size": "64G"}}}
full_set = {"params": {"gpu": "A100", "memory": {"size": "64G", "type": "HBM2"}}, "other": 1}

print(f"get all leaf paths: {get_all_paths(subset)}")


# get all leaf paths: ["root['params']['gpu']", "root['params']['memory']['size']"]

def only_diff_subset(full_set: dict, subset_: dict):
    return DeepDiff(full_set, subset_, include_paths=get_all_paths(subset_), view=COLORED_VIEW)


diff = only_diff_subset(full_set, subset)
assert {} == diff, diff
# ok

diff = only_diff_subset(full_set, {"params": {"gpu": "XXX", "memory": {"size": "64G"}}})
assert {} == diff, diff
# Traceback (most recent call last):
#   File "/Users/chen/git/chen56/applab_research/features/validation/diff/test_pycheck.py", line 39, in <module>
#     assert {} == diff, diff
#            ^^^^^^^^^^
# AssertionError: {
#   "params": {
#     "gpu": "A100" -> "XXX",
#     "memory": {
#       "size": "64G"
#     }
#   }
# }
