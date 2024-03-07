st = "xsdlafqpcmjytoikojsecamgdkehrqqgfknlhoudqygkbxftivfbpxhxtqgpkvsrfflpgrlhkbfnyftwkdebwfidmpauoteahyh"
point = 0
ch = st[point]
cnt = st.count(ch)
while cnt > 1:
    st = st.replace(ch, chr(ord(ch) + 1) if ch != 'z' else 'a', 1).replace(ch, '', 1)
    point = 0
    cnt = st.count(st[point])
    while cnt==1:
        point += 1
        cnt = st.count(st[point])
    ch = st[point]
print(st)
