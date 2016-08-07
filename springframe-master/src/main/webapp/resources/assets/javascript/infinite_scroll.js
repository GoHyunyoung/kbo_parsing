/**
 * Created by gohyunyoung98 on 16. 7. 25.
 */

$(document).ready(function() {
    var win = $(window);
    var begin=10;

    // Each time the user scrolls
    win.scroll(function() {
        // End of the document reached?
        if ($(document).height() - win.height() <= win.scrollTop()){
            // console.log("Activate");
            $.ajax({
                url: '/scroll',
                type: 'get',
                data:'articleId='+begin,
                success: function (data) {
                    begin+=10;
                    $('li#getMoreArticle').before(data);
                }
            });
        }
    });
});