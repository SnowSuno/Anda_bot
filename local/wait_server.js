function response(room, msg, sender, isGroupChat, replier, ImageDB, packageName) {
if (msg.substr(0,2)=="안다") {
    var message = msg.replace(/[?]/gi, "$qs$")
            .replace(/\n/g, "$$$")
            .replace(/\//g, "$slash$")
            .replace(/#/g, "$sharp$");

    var data = org.jsoup.Jsoup
            .connect("serveraddress/api/"+room+"@2@"+message+"@2@"+sender+"@2@"+isGroupChat)
            .get()
            .select("body")
            .text ()+"";

    var text = data.replace(/\$\$\$/g, "\n").split('@nm@');
    for(var i = 0; i < text.length; i++) {
        replier.reply(text[i]);
    }
    }
}