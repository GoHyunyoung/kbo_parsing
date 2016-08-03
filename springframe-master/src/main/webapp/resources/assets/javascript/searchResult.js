/**
 * Created by gohyunyoung98 on 16. 7. 25.
 */

$(document).ready(function() {
    var win = $(window);
    // Each time the user scrolls
    win.scroll(function() {
        // End of the document reached?
        if ($(document).height() - win.height() <= win.scrollTop()){
            $.ajax({
                url: '/',
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