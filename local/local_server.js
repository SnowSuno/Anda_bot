function response(room, msg, sender, isGroupChat, replier, ImageDB, packageName) {
if (msg.substr(0,2)=="안다") {
    var data = org.jsoup.Jsoup
            .connect("internal_ip_address")
            .data("room", room)
            .data("msg", msg)
            .data("sender", sender)
            .data("isGroupChat", isGroupChat)
            .post()
            .select("body")
            .text ()+"";


    var text = data.replace(/\$\$\$/g, "\n").split('@nm@');
    for(var i = 0; i < text.length; i++) {
        replier.reply(text[i]);
    }
    }
}