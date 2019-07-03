stuff = {'rope': 1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
dragonloot= ['gold coin','dagger','gold coin','gold coin','ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        item_total +=v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory,addedItems):
    for Aitem in addedItems:
          inventory.setdefault(Aitem,0)
          inventory[Aitem] +=1


displayInventory(stuff)
addToInventory(stuff,dragonloot)
displayInventory(stuff)
print(stuff)