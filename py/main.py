from onepasswordconnectsdk.client import (
    new_client_from_environment
)
from onepasswordconnectsdk.models import (
    Item, ItemVault, Field
)
import string
import secrets
import os
from time import sleep

def pass_gen(size=64):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    # if you want to add special characters
    # chars += '!@^*-_=+?/.>,<"\\:;|]}[{\'`~%&$#()'
    return ''.join(secrets.choice(chars) for x in range(size))

# creating client using OP_CONNECT_TOKEN environment variable
client = new_client_from_environment("http://op-connect-api:8080")


# creating Item
item = Item(vault=ItemVault(id=os.environ["VAULT_ID"]),
            title=pass_gen(5),
            category="LOGIN",
            tags=["1password-connect"],
            fields=[Field(
                value="new_user",
                purpose="USERNAME"
            ),
                Field(
                value=pass_gen(),
                purpose="PASSWORD"
            )],
        )
created_item = client.create_item(os.environ["VAULT_ID"], item)
print('created', created_item)
item_id = created_item.id
sleep(2)

# get Item

get_item = client.get_item(item_id, os.environ["VAULT_ID"])
print('got', get_item)
sleep(2)

# update item

update_item = get_item
update_item.fields[1].value = pass_gen()

updated_item = client.update_item(item_id, os.environ["VAULT_ID"], update_item)
print('updated', updated_item)
sleep(2)

# delete item
client.delete_item(item_id, os.environ["VAULT_ID"])

vaults = client.get_vaults()
for vault in vaults:
    print(vault)
