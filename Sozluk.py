meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "MİNECRAFT": "Maden üret",
            'KODLAND':'Kod dümyası'
            }
kelime= input("kelime gir")
            
if kelime in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[kelime])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print('kelime listede yok')
