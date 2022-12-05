import requests
try:
    ur1 ="https://www.google.com.hk/search?tbm=isch&as_q=%E5%86%B0%E5%B2%9B%20(site:www.pexels.com%20OR%20site:pixabay.com%20OR%20site:unsplash.com)"
    ur2 ="https://www.google.com.hk/imgres?imgurl=https%3A%2F%2Fcdn.pixabay.com%2Fphoto%2F2016%2F02%2F19%2F20%2F57%2Ficeland-1211171__340.jpg&imgrefurl=https%3A%2F%2Fpixabay.com%2Fzh%2Fimages%2Fsearch%2F%25E5%2586%25B0%25E5%25B2%259B%2F&tbnid=rY9CtaDRkcLfKM&vet=12ahUKEwj7qoPP2c_7AhVVjNgFHftlDDkQMygBegUIARDZAQ..i&docid=ZyWfaUJnMLGLmM&w=509&h=340&ved=2ahUKEwj7qoPP2c_7AhVVjNgFHftlDDkQMygBegUIARDZAQ"
    ur3 ="https://m.baidu.com/from=0/bd_page_type=1/ssid=0/uid=0/pu=usm%409%2Csz%40224_220%2Cta%40iphone___24_107.0/baiduid=451C32E422BEA55BEB8DBB1A3960BDCD/w=0_10_/t=iphone/l=1/tc?ref=www_iphone&lid=12034641408700970835&order=1&fm=alop&isAtom=1&clk_info=%7B%22tplname%22%3A%22image_strong_normal%22%2C%22srcid%22%3A%224%22%7D&is_baidu=1&tj=image_strong_normal_1_0_10_l1&wd=&eqid=a703a29954d3f7531000000563840d36&w_qd=IlPT2AEptyoA_yk5tx9awgO&bdver=2&tcplug=1&dict=-1&sec=25777&di=3d6670a9edfb6e71&bdenc=1&nsrc=o34BjaVBU0LDE8gL0XDj3wL8HUMRAKiImXO7nGAzrRBaBqa%2Bkzu9iCyKVD%2F5JvpF9A3maTHePdTLS07ulAubRiKpBEpCLDFGbhJyPi1F%2FJ%2BFvK%2BfLvnOR9kKhdpNY8wwgo8rtXvbQWW8N%2BOJgEqoaADU9GDfb8WRGifUWemADs2t%2BYyIXxpB6bOWbpbu4T3rs8mfR20EFlsRypqGAhfwO5JeHlwmg1LJxNEqfHcY53P0cuNrGxAqele8%2BrZwKiFeg1E5CApdFb8JQoqIi%2Bg5e2zRg%2BfFuKu32iWVQWsg1UyVzD8ijZs9glq33Gq6t%2FAkean5QEKbPIK%2FgxyAiJoFak%2Fsj6YqrRPCad%2Be1OPvZgVkPDwwd%2FVCNAIZbMzwrkWm0HXtRFB5r73YDqYuYY9m%2FYNHvU7u60bKHZW%2Bs9w4KjChw3%2Bm%2BUvPltX5F6el0Y04WL9SePgXLF5vW4uXL1q%2BUYg64jwyBD9QDprP1CTlwa5EZtnBkxMRVfaXKnkSmDlLB6hT%2FtTL8iBCX%2BsHZ4dacL9t8icylp3rJvvXaE3%2BhWZX%2FlAboOCLapUA9E5ibmOhq9rsP%2FCQ%2Bir0xJahtrwUp2glIjMwq0Rt%2Fg3FnrWGCvuQM9UbJ6PgthDRr7F3F%2FF6Ma2H7MO%2BVOLatcFtqR1Bn4YQkWuA8KjRofHr8LmVDguFbiwnHwuLS47nKaMY1aQKpeMMwsg5E56Z%2BuZ2OmKnDg9zp0Fjnegk%2B5DMpuE90KI3dTTRaYza6Gik960MfQhi"
    hd = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    r = requests.get(ur3,headers = hd)
    r.raise_for_status()
    r.encoding="utf-8"
    rb = (r.content)
except:
    print("异常")
with open("D:\\temp\\pc\\hu.jpg" ,"wb+") as f:
    f.write(rb)
    print("图片保存成功")

