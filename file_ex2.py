with open(r"files\ex2_read.html","r") as fr:
    with open(r"files\ex2_write.txt","w") as fw:
        content = fr.read()
        links_exist = "<a href" in content
        while(links_exist):
            link_line = content.find("<a href")
            start = content.find('"',link_line)
            end = content.find("\"",start+1)
            fw.write(content[start+1:end] + "\n")
            content = content[end:]
            links_exist = "<a href" in content
            