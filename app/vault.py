from app.models import Vault
import json


def get_default_vault() -> Vault:
    with open(".data/vaults.json", "r", encoding="utf-8") as f:
        vaults: list[dict[str, str]] = json.load(f)

    vault = None

    for v in vaults:
        if vault:
            break

        if v.get("is_default") == True:
            vault = Vault(v["path"], v["id"], True)

    if vault == None:
        raise ValueError("No default vault was set.")

    return vault
