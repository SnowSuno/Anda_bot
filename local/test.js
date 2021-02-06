function response(room, msg, sender, isGroupChat, replier, ImageDB, packageName) {
if (msg.charAt(0)=="/") {
    var message = msg.replace("/", "$");
    var data = org.jsoup.Jsoup
            .connect("server_address/api/"+room+"@2@"+message+"@2@"+sender+"@2@"+isGroupChat)
            .get()
            .select("body")
            .text ()+"";

    var text = data.split('@nm@');
    for(var i = 0; i < text.length; i++) {
        var rep = text[i].replace(/\$\$\$/g, "\n")
        replier.reply(rep);
    }
    }
}