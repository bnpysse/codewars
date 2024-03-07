text = "A wise old owl lived in an oak"
text = "The more he saw the less he spoke"
text = "The less he spoke the more he heard"
text = '99zdSpGGvaeWeKSNO 110RjvhNmQDcJXitVjhh 75LPYahLsbQl 121DyiWVZPFrHGLdSqiy 81cWxoF 112KWGDVNUZLJmxQrJPju 82eOlkVK 110zwFhyhMqtAZoiCt 83UhjeyCuXMFgObzGTQ 122TRDCQxSmwUnnSc 65Nfs 122ZtRiAfEwvwqo 79JBhZ 104 116mOPseauUcdRdqU 106k 113isDzvPJIrx 122RGfNZHTFFrd 7878 78nfFGklbkcKpaxBGvn 106pzxMiNagakgVHih 75GbPnwxMBWN 79TpadaPxzd'
text = '99zdSpGGvaeWeKSNO 110RjvhNmQDcJXitVjhh 75LPYahLsbQl 121DyiWVZPFrHGLdSqiy 81cWxoF 112KWGDVNUZLJmxQrJPju 82eOlkVK 110zwFhyhMqtAZoiCt 83UhjeyCuXMFgObzGTQ 122TRDCQxSmwUnnSc 65Nfs 122ZtRiAfEwvwqo 79JBhZ 104 116mOPseauUcdRdqU 106k 113isDzvPJIrx 122RGfNZHTFFrd 78N  78nfFGklbkcKpaxBGvn 106pzxMiNagakgVHih 75GbPnwxMBWN 79TpadaPxzd'
result = []
for sub_str in text.split():
    item=sub_str
    if len(item)<=2:
        item = item.replace(item[0], str(ord(item[0])))
    else:
        # item = item.translate(str.maketrans(sub_str[1]+sub_str[-1],sub_str[-1]+sub_str[1]))
        item=str(ord(item[0]))+ sub_str[-1] + sub_str[2:len(sub_str)-1] +sub_str[1]

    result.append(item)
print(' '.join(result))
